#!/usr/bin/env bash
# SPDX-License-Identifier: GPL-3.0-or-later
# Fill .agents/ at the start of every session.
#
# Copy this file to .claude/hooks/session-start.sh in your repository root and
# make it executable. The file on its own does nothing: .claude/settings.json is
# what starts it. .cursor/environment.json can run the same file, so Cursor
# cloud agents get the same result from one copy.
#
# Use this file only in a repository that does NOT have a doqs submodule. doqs
# installs its own hook at this exact path and overwrites whatever is there.
#
# Why this exists: a cloud session copies a repository without the contents of
# its submodules, so .agents/ arrives empty. The agent then reads no rules and
# no skills. The folder is there, so nothing looks wrong: the failure is silent,
# which is the worst kind.
#
# The two git calls must stay in this order:
#
#   1. --init -- .agents checks the kit out at the commit this repository
#      records. Naming .agents keeps every other submodule untouched.
#   2. --remote -- .agents moves the kit to the latest main.
#
# This hook never stops a session. With no network it says so and exits 0.

set -uo pipefail

root="${CLAUDE_PROJECT_DIR:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
cd "$root" || exit 0

# A session start has no keyboard, so git must never wait for a password.
export GIT_TERMINAL_PROMPT=0

# timeout keeps a dead network from holding the session open.
run_git() {
  if command -v timeout >/dev/null 2>&1; then
    timeout "$1" git "${@:2}" 2>&1
  else
    git "${@:2}" 2>&1
  fi
}

output="$(run_git 180 submodule update --init -- .agents)"
status=$?

output="${output}
$(run_git 120 submodule update --remote -- .agents)"
remote_status=$?

# The marker file is the real test. Both commands above can exit 0 and still
# leave the folder empty: git prints "Skipping submodule" and succeeds. An exit
# code on its own proves nothing.
if [ -f ".agents/rules/core.md" ]; then
  kit="$(git -C .agents rev-parse --short HEAD 2>/dev/null || echo unknown)"
  echo "The agent kit is ready: .agents/ (${kit})."
  # The folder is usable even when only the first call worked, but then it holds
  # the recorded commit rather than the latest main. Say so, rather than let an
  # old kit pass for a fresh one.
  if [ $remote_status -ne 0 ]; then
    echo "Could not reach the remote, so the kit sits at its recorded commit, not the latest main."
    echo "Run 'bash setup-agents.sh' once you have a network again."
  fi
  echo "Read .agents/rules/core.md first, then AGENTS.md."
  echo "Write every reply and every file in B2 English: .agents/rules/communication.md."
  exit 0
fi

echo "Could not check out .agents (git exit codes ${status} and ${remote_status})."

# A failing clone repeats itself once per retry, so the raw output runs to dozens
# of lines. A session start is not the place for that: keep the lines that name
# the cause, and cap them.
reason="$(printf '%s\n' "$output" | grep -E '^(fatal|error):' | sort -u | head -4)"
if [ -n "$reason" ]; then
  echo "git said:"
  printf '%s\n' "$reason" | sed 's/^/  /'
fi
echo "The session continues, but the shared rules and skills are missing."
echo "Write every reply and every file in B2 English anyway: short sentences, common words."
echo "Once you have a network again, run:"
echo "  bash setup-agents.sh"
exit 0
