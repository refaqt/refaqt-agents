#!/usr/bin/env bash
# SPDX-FileCopyrightText: 2025-2026 Refaqt (BE 0804.145.539) and contributors
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Sync the shared agent files in one repository, and open a pull request when
# something changed. The workflow .github/workflows/sync-root.yml calls this.
#
#   bash scripts/sync_one_repo.sh ORG REPO BRANCH KIT_SHA
#
# Needs GH_TOKEN with write access to the repository. The kit is taken from
# its latest main, the same version agent sessions use.

set -euo pipefail
org="$1"; repo="$2"; branch="$3"; kit_sha="${4:-main}"

work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT

gh repo clone "$org/$repo" "$work/repo" -- --quiet --depth 1
cd "$work/repo"
base="$(git rev-parse --abbrev-ref HEAD)"

# Fill the kit folder at the latest main. Only .agents: other submodules,
# such as doqs or private modules, are not needed for these files.
git submodule update --init --remote --depth 1 -- .agents

python3 .agents/scripts/sync_root.py --root .
python3 .agents/scripts/mistakes_index.py --root .

# The kit folder moves ahead of its pin on purpose. Never commit it here.
git add -A -- . ':!.agents' ':!doqs'
if git diff --cached --quiet; then
  echo "$repo: the shared agent files are already up to date."
  exit 0
fi

git checkout -q -B "$branch"
git commit -q -m "chore(agents): sync the shared agent files with the kit

Written by the kit's sync job from refaqt-agents ${kit_sha:0:7}.
Do not edit these files by hand: change the kit, or .agents-local/."
git push -q --force origin "$branch"

if [ -n "$(gh pr list --repo "$org/$repo" --head "$branch" --state open --json number --jq '.[].number')" ]; then
  echo "$repo: updated the open pull request."
  exit 0
fi

gh pr create --repo "$org/$repo" --base "$base" --head "$branch" \
  --title "Update the shared agent files from the kit" \
  --body "## What changed

The shared agent files in this repository now match the latest kit: \`CLAUDE.md\`, \`AGENTS.md\`, the Cursor rules, the pull request template, and the mistakes index.

## Why it matters

Every Refaqt repository shows its agents the same short rules. Without this update, this repository would keep older rules.

## What you need to do

Read the changes and merge. Do not edit these files by hand: change the kit, or \`.agents-local/\` in this repository.

## How it was checked

The kit's sync script wrote the files. No person or AI edited them.

<details>
<summary>Notes for reviewers</summary>

- Kit version: refaqt-agents \`${kit_sha:0:7}\`.
- Made by the workflow \`sync-root.yml\` in refaqt/refaqt-agents.

</details>"
echo "$repo: opened a pull request."
