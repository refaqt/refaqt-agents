#!/usr/bin/env bash
# SPDX-FileCopyrightText: 2025-2026 Refaqt (BE 0804.145.539) and contributors
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Sync the shared files in one repository. The workflow
# .github/workflows/sync-root.yml calls this for every repository that mounts
# the kit at .agents.
#
#   bash scripts/sync_one_repo.sh ORG REPO BRANCH KIT_SHA [DRY_RUN]
#
# Needs GH_TOKEN with write access to the repository. The kit and doqs are taken
# at their latest main, the same versions that agent sessions use.
#
# - Something changed: commit on BRANCH and open a pull request, or update the
#   one that is open.
# - Nothing changed: close an old sync pull request, if one is open.
# - DRY_RUN=true: only list what would change.

set -euo pipefail
org="$1"; repo="$2"; branch="$3"; kit_sha="${4:-main}"; dry_run="${5:-false}"
summary="${GITHUB_STEP_SUMMARY:-/dev/null}"

work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT

gh repo clone "$org/$repo" "$work/repo" -- --quiet --depth 1
cd "$work/repo"
base="$(git rev-parse --abbrev-ref HEAD)"

# Fill only the tooling folders. Other submodules, such as private modules,
# are not needed for these files.
tooling=(.agents)
if grep -Eq '^\s*path\s*=\s*doqs\s*$' .gitmodules; then
  tooling+=(doqs)
fi
# --checkout overrides "update = none", which doqs sets on its own .agents.
git submodule update --init --remote --checkout --depth 1 -- "${tooling[@]}"

if [ -f doqs/scripts/install_root_tools.py ]; then
  # Writes the launchers, setup-tooling.*, the session hook and the settings,
  # then runs the kit's sync_root.py.
  python3 doqs/scripts/install_root_tools.py --root .
else
  python3 .agents/scripts/sync_root.py --root .
fi
python3 .agents/scripts/mistakes_index.py --root .

# The tooling folders move ahead of their pins on purpose. Never commit them.
git add -A -- . ':!.agents' ':!doqs'
open_pr="$(gh pr list --repo "$org/$repo" --head "$branch" --state open --json number --jq '.[0].number // empty')"

if git diff --cached --quiet; then
  echo "$repo: the shared files are already up to date."
  echo "- $repo: up to date" >> "$summary"
  if [ -n "$open_pr" ] && [ "$dry_run" != "true" ]; then
    gh pr close "$open_pr" --repo "$org/$repo" --delete-branch \
      --comment "The shared files on the default branch already match the kit. This pull request is no longer needed."
    echo "- $repo: closed the old sync pull request" >> "$summary"
  fi
  exit 0
fi

changed="$(git diff --cached --name-only | sed 's/^/  /')"
echo "$repo: these files would change:"
echo "$changed"
{
  echo "- $repo: $(git diff --cached --name-only | wc -l) files"
  git diff --cached --name-only | sed 's/^/  - `/; s/$/`/'
} >> "$summary"
[ "$dry_run" = "true" ] && exit 0

git checkout -q -B "$branch"
git commit -q -m "chore(agents): sync the shared files with the kit

Written by the kit's sync job from refaqt-agents ${kit_sha:0:7}.
Do not edit these files by hand: change the kit, or .agents-local/."
git push -q --force origin "$branch"

if [ -n "$open_pr" ]; then
  echo "$repo: updated pull request #$open_pr."
  exit 0
fi

gh pr create --repo "$org/$repo" --base "$base" --head "$branch" \
  --title "Update the shared agent files from the kit" \
  --body "## What changed

The shared files in this repository now match the latest kit. These are the files that tell AI agents how to work here, and the shared helper files.

## Why it matters

Every Refaqt repository shows its agents the same short rules and uses the same helpers. Without this update, this repository keeps an older version.

## What you need to do

Read the changes and merge. Do not edit these files by hand: change the kit, or \`.agents-local/\` in this repository.

## How it was checked

The kit's sync script wrote the files. No person and no AI edited them.

<details>
<summary>Notes for reviewers</summary>

- Kit version: refaqt-agents \`${kit_sha:0:7}\`.
- Made by the workflow \`sync-root.yml\` in refaqt/refaqt-agents.
- Changed files:
${changed}

</details>"
echo "$repo: opened a pull request."
