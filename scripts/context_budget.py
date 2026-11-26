#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025-2026 Refaqt (BE 0804.145.539) and contributors
# SPDX-License-Identifier: GPL-3.0-or-later
"""Show how much text an agent loads before it starts a task.

    python3 .agents/scripts/context_budget.py [--root DIR] [--budget BYTES]

It counts three things, the way Claude Code loads them:

1. CLAUDE.md (or AGENTS.md when there is no CLAUDE.md), with every @import
   expanded, up to four levels deep.
2. The skill list: the name and description of each skill an agent can see.
3. Files the rules tell an agent to read at the start of every task. Today that
   is the mistakes index, docs/mistakes/README.md.

About 4 bytes of English make one token. --budget makes the script exit 1 when
the total is above the limit, so a check in CI stops the start-up text from
growing back.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

IMPORT_RE = re.compile(r"(?<![\w`])@([\w./-]+\.md)\b")
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
CODE_SPAN_RE = re.compile(r"`[^`\n]*`")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
DEFAULT_BUDGET = 20000


def expand(path: Path, depth: int, seen: set[Path], rows: list[tuple[str, int]], root: Path) -> None:
    resolved = path.resolve()
    if depth > 4 or resolved in seen or not path.is_file():
        if not path.is_file():
            rows.append((f"{_rel(path, root)} (missing, not loaded)", 0))
        return
    seen.add(resolved)
    text = path.read_text(encoding="utf-8")
    rows.append((_rel(path, root), len(text.encode("utf-8"))))
    scan = CODE_SPAN_RE.sub("", FENCE_RE.sub("", text))
    for name in IMPORT_RE.findall(scan):
        expand((path.parent / name), depth + 1, seen, rows, root)


def _rel(path: Path, root: Path) -> str:
    for candidate, base in ((path, root), (path.resolve(), root.resolve())):
        try:
            return str(candidate.relative_to(base))
        except ValueError:
            continue
    return str(path)


def skill_listing(root: Path) -> list[tuple[str, int]]:
    rows = []
    folder = root / ".claude" / "skills"
    if not folder.is_dir():
        return rows
    for skill in sorted(folder.iterdir()):
        file = skill / "SKILL.md"
        if not file.is_file():
            continue
        match = FRONTMATTER_RE.match(file.read_text(encoding="utf-8"))
        size = len(match.group(1).encode("utf-8")) if match else 0
        rows.append((f"skill list: {skill.name}", size))
    return rows


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", default=".", help="repository root (default: current folder)")
    parser.add_argument("--budget", type=int, default=None,
                        help=f"exit 1 above this many bytes (suggested: {DEFAULT_BUDGET})")
    args = parser.parse_args(argv)
    root = Path(args.root)

    rows: list[tuple[str, int]] = []
    entry = root / "CLAUDE.md"
    if not entry.is_file():
        entry = root / "AGENTS.md"
    expand(entry, 0, set(), rows, root)

    skills = skill_listing(root)
    skills_total = sum(size for _, size in skills)
    if skills:
        rows.append((f"skill list ({len(skills)} skills in .claude/skills/)", skills_total))

    index = root / "docs" / "mistakes" / "README.md"
    if index.is_file():
        rows.append((f"{_rel(index, root)} (read at task start)", len(index.read_bytes())))

    total = sum(size for _, size in rows)
    width = max(len(name) for name, _ in rows) if rows else 10
    for name, size in rows:
        print(f"{name:<{width}}  {size:>7,} bytes")
    print(f"{'Total':<{width}}  {total:>7,} bytes  (about {total // 4:,} tokens)")
    print("Skills synced from claude.ai plugins are not counted here.")

    if args.budget is not None and total > args.budget:
        print(f"Over budget: {total:,} bytes is more than {args.budget:,}.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
