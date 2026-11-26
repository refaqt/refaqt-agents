#!/usr/bin/env bash
# SPDX-FileCopyrightText: 2025-2026 Refaqt (BE 0804.145.539) and contributors
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Make the kit skills and the repository's own skills visible to Claude Code.
#
#   bash .agents/scripts/link_skills.sh [REPO_ROOT]
#
# Claude Code finds a skill only at .claude/skills/<name>/SKILL.md. The kit keeps
# its skills at .agents/skills/<name>/, and a repository keeps its own at
# .agents-local/skills/<name>/. This script links each of them into
# .claude/skills/. The links are ignored by git (sync_root.py adds the line to
# .gitignore), so every session makes them again.
#
# Team members get the kit skills from the "refaqt" plugin that the
# organization turns on in claude.ai. When that plugin is already on this
# machine, the kit skills are not linked, so they do not show up twice. The
# repository's own skills are always linked.
#
# Claude Code reads the skill list when the session starts. A session hook runs
# before that, so links made by the hook count in the same session.
#
# This script never fails a session: it always exits 0.

set -u

root="${1:-$PWD}"
cd "$root" 2>/dev/null || exit 0

target=".claude/skills"

# The refaqt plugin, synced from claude.ai or installed from the marketplace.
plugin_present() {
  local dir
  for dir in "$HOME/.claude/plugins/synced" "$HOME/.claude/plugins/cache"; do
    [ -d "$dir" ] || continue
    if find "$dir" -maxdepth 6 -path '*/.claude-plugin/plugin.json' -print0 2>/dev/null |
      xargs -0 -r grep -l -E '"name"[[:space:]]*:[[:space:]]*"refaqt"' 2>/dev/null | grep -q .; then
      return 0
    fi
  done
  return 1
}

# Remove links that this script made earlier and that now point nowhere, for
# example after a skill was renamed in the kit. Real folders are never touched.
if [ -d "$target" ]; then
  for link in "$target"/*; do
    [ -L "$link" ] || continue
    [ -e "$link" ] || rm -f "$link"
  done
fi

linked=0
link_from() {
  local source_dir="$1" skill name dest
  [ -d "$source_dir" ] || return 0
  mkdir -p "$target"
  for skill in "$source_dir"/*/; do
    skill="${skill%/}"
    [ -f "$skill/SKILL.md" ] || continue
    name="$(basename "$skill")"
    dest="$target/$name"
    # Never replace a real folder that someone committed on purpose.
    if [ -e "$dest" ] && [ ! -L "$dest" ]; then
      continue
    fi
    ln -sfn "../../$skill" "$dest" && linked=$((linked + 1))
  done
}

if plugin_present; then
  kit_note="kit skills come from the refaqt plugin"
  # Drop kit links left from an earlier session, so nothing shows up twice.
  if [ -d "$target" ]; then
    for link in "$target"/*; do
      [ -L "$link" ] || continue
      case "$(readlink "$link")" in
        ../../.agents/skills/*) rm -f "$link" ;;
      esac
    done
  fi
else
  kit_note="kit skills linked from .agents/skills"
  link_from ".agents/skills"
fi
link_from ".agents-local/skills"

echo "Skills: ${linked} linked into ${target}/ (${kit_note})."
exit 0
