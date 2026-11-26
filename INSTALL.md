# Install the agent kit in your repository

After these steps, every AI agent that works in your repository reads the same short rules, on a
laptop and in the cloud. You need `git`, Python 3.11 or newer, and push rights to the repository.

## Step 1: add the kit

From the top folder of your repository:

```bash
git submodule add -b main https://github.com/refaqt/refaqt-agents.git .agents
```

`-b main` lets the kit move forward later. Without it, your repository stays on today's version.

A machine repository also adds doqs. Follow
[doqs `templates/setup-tooling/README.md`](https://github.com/refaqt/doqs/blob/main/templates/setup-tooling/README.md)
for that part. It copies `setup-tooling.sh`, which fills both folders.

## Step 2: describe your repository

Create `.agents-local/profile.toml`:

```toml
name = "Your project name"
profile = "base"      # "doqs" in a machine repository with a doqs/ submodule

[plugins]             # claude.ai plugins to switch off or on in this repository
off = []              # for example ["claude-for-manufacturing@synced"]
on = []
```

Create `.agents-local/rules/repo.md` with what is true only for this repository: what it is, its
folders, its stack, and its special rules. Keep it under 3 KB. Every session loads it. Put
everything that is true for all Refaqt repositories in this kit instead.

Repository-only skills go in `.agents-local/skills/<name>/SKILL.md`.

## Step 3: write the shared files

```bash
python3 .agents/scripts/sync_root.py
```

This writes `CLAUDE.md`, `AGENTS.md`, the Cursor rule files and the pull request template, and
merges the session hook into `.claude/settings.json`. In a `base` repository it also writes
`setup-agents.sh` and `.claude/hooks/session-start.sh`. In a `doqs` repository, doqs installs
those. Commit the result.

Do not edit the generated files by hand. A weekly job in `refaqt/.github` runs the same script in
every repository and opens a pull request when the templates change.

## Step 4: check it

```bash
python3 .agents/scripts/sync_root.py --check
python3 .agents/scripts/context_budget.py --budget 20000
```

The first says whether the shared files match the kit. The second prints how much text an agent
loads before it starts, and fails above 20 KB.

## How it works in each tool

| Tool | What happens |
| --- | --- |
| Claude Code, one repository | The session hook fills `.agents/` and links the skills into `.claude/skills/`. `CLAUDE.md` imports `AGENTS.md`, which imports `core.md` and `repo.md`. |
| Claude Code, several repositories, or a thread in a Claude project | The hook does not run. `CLAUDE.md` tells the agent to run the check and the setup file. |
| Claude, for your team | Add the marketplace `refaqt/refaqt-agents` in claude.ai under Organization settings, Plugins & skills, and mark the plugin `refaqt` as required. The skills then reach every session, also Cowork and chat. The hook sees the plugin and does not link the kit skills a second time. |
| Cursor | Reads `AGENTS.md` and the generated `.cursor/rules/refaqt-*.mdc`. `.cursor/environment.json` runs the same hook in Cursor cloud agents. |
| GitHub Actions | Add `submodules: recursive` to the checkout step of every workflow that needs the kit. |

## When something goes wrong

| What you see | What to do |
| --- | --- |
| `.agents/` is empty | Run `bash setup-agents.sh`, or `bash setup-tooling.sh` in a doqs repository |
| The session says nothing at start | The hook did not run. Check the `SessionStart` entry in `.claude/settings.json`, or see the second row above |
| `sync_root.py` says `profile.toml is missing` | Do Step 2 |
| `bad interpreter` or `\r: command not found` | Add `*.sh text eol=lf` to `.gitattributes` (the sync adds it) and check the file out again |
| Each skill shows up twice | The plugin is on, and an old link is left in `.claude/skills/`. Delete that folder; the hook makes it again |
| `.agents` shows as modified in `git status` | That is the update working. Leave it uncommitted unless you mean to fix a version |
