#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025-2026 Refaqt (BE 0804.145.539) and contributors
# SPDX-License-Identifier: GPL-3.0-or-later
"""Write the shared agent files at the root of a Refaqt repository.

    python3 .agents/scripts/sync_root.py [--root DIR] [--check]

Every Refaqt repository shows its agents the same entry files. This script
writes them from the templates in .agents/templates/root/, so they cannot drift
apart. What belongs to one repository lives in .agents-local/ only:

    .agents-local/profile.toml     name, profile, plugins (read by this script)
    .agents-local/rules/repo.md    the repository's own rules (imported by AGENTS.md)
    .agents-local/skills/<name>/   the repository's own skills

profile.toml looks like this:

    name = "AQTUATOR"
    profile = "doqs"            # "doqs" for machine repositories, else "base"
    [plugins]                   # claude.ai plugins: on or off in this repository
    off = ["claude-for-manufacturing@synced"]
    on = []

Files this script owns and rewrites:
    CLAUDE.md, AGENTS.md, .github/pull_request_template.md,
    .cursor/rules/refaqt-*.mdc
    base profile only: .claude/hooks/session-start.sh, setup-agents.sh
    (in a doqs repository, doqs installs those itself)

Files this script merges and never empties:
    .claude/settings.json   the SessionStart hook and the plugin switches
    .cursor/environment.json  the install command
    .gitignore              ignore .claude/skills/ (links made each session)
    .gitattributes          *.sh text eol=lf

--check changes nothing and exits 1 when a file differs from what the
templates give. A GitHub Action runs this script across all repositories and
opens a pull request when something changed.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import tomllib
from pathlib import Path

KIT = Path(__file__).resolve().parent.parent
TEMPLATES = KIT / "templates"
ROOT_TEMPLATES = TEMPLATES / "root"

PROFILES = {
    "base": {
        "check": "ls .agents/rules/core.md",
        "setup": "bash setup-agents.sh",
        "never_commit": "`.agents/`",
        "rows": [],
        "cursor": ["refaqt-core.mdc"],
    },
    "doqs": {
        "check": "ls .agents/rules/core.md doqs/scripts/validate_all.py",
        "setup": "bash setup-tooling.sh",
        "never_commit": "`.agents/` or `doqs/`",
        "rows": [
            "| change modules, parts, the BOM, CAD models or variants | `doqs/docs/using-doqs.md`; "
            "its table names the one page you need |",
            "| finish work before a pull request | run `./doqs.sh pre-pr` (generate, check, save the models) |",
        ],
        "cursor": ["refaqt-core.mdc", "refaqt-doqs-naming.mdc", "refaqt-freecad.mdc"],
    },
}

HOOK_COMMAND = "$CLAUDE_PROJECT_DIR/.claude/hooks/session-start.sh"
GITIGNORE_LINES = [
    "# Skill links made by .agents/scripts/link_skills.sh at the start of each session.",
    "/.claude/skills/",
]
GITATTRIBUTES_LINE = "*.sh text eol=lf"
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
WHEN_RE = re.compile(r"\bUse (?:it )?(?:when|for|at|before|after|to)\b", re.IGNORECASE)


class ProfileError(Exception):
    pass


def load_profile(root: Path) -> dict:
    path = root / ".agents-local" / "profile.toml"
    if not path.is_file():
        raise ProfileError(
            f"{path} is missing. Create it with at least: name = \"<repository name>\" and "
            "profile = \"base\" (or \"doqs\" in a machine repository)."
        )
    data = tomllib.loads(path.read_text(encoding="utf-8"))
    if "name" not in data:
        raise ProfileError(f"{path} has no name.")
    kind = data.get("profile", "base")
    if kind not in PROFILES:
        raise ProfileError(f"{path}: profile must be one of {', '.join(PROFILES)}, not {kind!r}.")
    plugins = data.get("plugins", {})
    return {
        "name": data["name"],
        "kind": kind,
        "on": list(plugins.get("on", [])),
        "off": list(plugins.get("off", [])),
    }


def _frontmatter(path: Path) -> dict[str, str]:
    match = FRONTMATTER_RE.match(path.read_text(encoding="utf-8"))
    if not match:
        return {}
    fields: dict[str, str] = {}
    key = None
    for line in match.group(1).splitlines():
        top = re.match(r"^([a-zA-Z_-]+):\s*(.*)$", line)
        if top:
            key = top.group(1)
            value = top.group(2).strip()
            fields[key] = "" if value in (">-", ">", "|", "|-") else value.strip("'\"")
        elif key:
            fields[key] = (fields[key] + " " + line.strip()).strip()
    return fields


def _when(description: str) -> str:
    """Turn a skill description into a short 'When you ...' cell."""
    text = description.strip()
    match = WHEN_RE.search(text)
    if match:
        text = text[match.start():]
    # Cut at the end of the first sentence or before a list after a colon.
    text = re.split(r"\.\s|:\s", text, maxsplit=1)[0].rstrip(".")
    text = re.sub(r"^Use (?:it )?", "", text, flags=re.IGNORECASE)
    text = re.sub(r"^(?:when you|when)\s+", "", text, flags=re.IGNORECASE)
    if len(text) > 80:
        text = text[:80].rsplit(" ", 1)[0] + " …"
    return text


def skill_rows(root: Path) -> list[str]:
    rows = []
    for base in (".agents/skills", ".agents-local/skills"):
        folder = root / base
        if not folder.is_dir():
            continue
        for skill in sorted(folder.iterdir()):
            file = skill / "SKILL.md"
            if not file.is_file():
                continue
            meta = _frontmatter(file)
            when = _when(meta.get("description", skill.name)).replace("|", "/")
            rows.append(f"| {when} | skill `{meta.get('name', skill.name)}`: `{base}/{skill.name}/SKILL.md` |")
    return rows


def render_root_files(root: Path, profile: dict) -> dict[str, str]:
    spec = PROFILES[profile["kind"]]
    values = {
        "{{NAME}}": profile["name"],
        "{{CHECK}}": spec["check"],
        "{{SETUP}}": spec["setup"],
        "{{NEVER_COMMIT}}": spec["never_commit"],
        "{{PROFILE_ROWS}}": "".join(row + "\n" for row in spec["rows"]),
        "{{SKILL_ROWS}}": "".join(row + "\n" for row in skill_rows(root)),
    }
    files = {}
    for name in ("CLAUDE.md", "AGENTS.md"):
        text = (ROOT_TEMPLATES / name).read_text(encoding="utf-8")
        for key, value in values.items():
            text = text.replace(key, value)
        files[name] = text.rstrip("\n") + "\n"
    for name in spec["cursor"]:
        files[f".cursor/rules/{name}"] = (ROOT_TEMPLATES / "cursor" / name).read_text(encoding="utf-8")

    pr = (TEMPLATES / "pull-request.md").read_text(encoding="utf-8")
    pr = "\n".join(line for line in pr.splitlines() if not line.startswith("Copy this file")) + "\n"
    files[".github/pull_request_template.md"] = pr

    if profile["kind"] == "base":
        files[".claude/hooks/session-start.sh"] = (TEMPLATES / "session-start.sh").read_text(encoding="utf-8")
        files["setup-agents.sh"] = (TEMPLATES / "setup-agents.sh").read_text(encoding="utf-8")
    return files


def merge_settings(text: str | None, profile: dict) -> str:
    data = json.loads(text) if text and text.strip() else {}
    hooks = data.setdefault("hooks", {})
    session = hooks.setdefault("SessionStart", [])
    present = any(
        hook.get("command") == HOOK_COMMAND
        for group in session
        for hook in group.get("hooks", [])
    )
    if not present:
        session.append({"hooks": [{"type": "command", "command": HOOK_COMMAND}]})
    if profile["on"] or profile["off"]:
        enabled = data.setdefault("enabledPlugins", {})
        for plugin in profile["on"]:
            enabled[plugin] = True
        for plugin in profile["off"]:
            enabled[plugin] = False
    return json.dumps(data, indent=2) + "\n"


def merge_cursor_env(text: str | None, profile: dict) -> str:
    data = json.loads(text) if text and text.strip() else {}
    data.setdefault("name", profile["name"].lower())
    data["install"] = "bash .claude/hooks/session-start.sh"
    return json.dumps(data, indent=2) + "\n"


def merge_lines(text: str | None, lines: list[str]) -> str:
    current = text or ""
    existing = {line.strip() for line in current.splitlines()}
    missing = [line for line in lines if line.strip() not in existing]
    if not missing:
        return current
    joined = current.rstrip("\n")
    return (joined + "\n\n" if joined else "") + "\n".join(missing) + "\n"


def desired_state(root: Path, profile: dict) -> dict[str, str]:
    def read(rel: str) -> str | None:
        path = root / rel
        return path.read_text(encoding="utf-8") if path.is_file() else None

    files = render_root_files(root, profile)
    files[".claude/settings.json"] = merge_settings(read(".claude/settings.json"), profile)
    files[".cursor/environment.json"] = merge_cursor_env(read(".cursor/environment.json"), profile)
    files[".gitignore"] = merge_lines(read(".gitignore"), GITIGNORE_LINES)
    files[".gitattributes"] = merge_lines(read(".gitattributes"), [GITATTRIBUTES_LINE])
    return files


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", default=".", help="repository root (default: current folder)")
    parser.add_argument("--check", action="store_true", help="change nothing; exit 1 on drift")
    args = parser.parse_args(argv)
    root = Path(args.root)

    try:
        profile = load_profile(root)
    except ProfileError as error:
        print(error)
        return 2

    changed = []
    for rel, content in desired_state(root, profile).items():
        path = root / rel
        old = path.read_text(encoding="utf-8") if path.is_file() else None
        if old == content:
            continue
        changed.append(rel)
        if not args.check:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            if rel.endswith(".sh"):
                path.chmod(0o755)

    if args.check:
        if changed:
            print("These shared agent files differ from the kit templates:")
            for rel in changed:
                print(f"  {rel}")
            print("Run: python3 .agents/scripts/sync_root.py   (do not edit them by hand)")
            return 1
        print("Shared agent files match the kit templates.")
        return 0
    if changed:
        print(f"Updated {len(changed)} shared agent files: {', '.join(changed)}")
    else:
        print("Shared agent files were already up to date.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
