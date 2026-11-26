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

Write `.agents-local/rules/repo.md` with what is true only for this repository: what it is, its
folders, its stack, and its special rules. Keep it under 3 KB. Every session loads it. Put
everything that is true for all Refaqt repositories in this kit instead. When the file is
missing, Step 3 writes it once. If the old `AGENTS.md` was written by hand, its part from "## This
repository" on moves there unchanged; shorten it later. Otherwise you get a file with the headings to
fill in.

Repository-only skills go in `.agents-local/skills/<name>/SKILL.md`.

The script finds the rest itself. The name is the first `# ` heading of `README.md`. The profile
is `doqs` when the repository has a `doqs` submodule, and `base` otherwise. Only when you need to
change one of these, create `.agents-local/profile.toml`:

```toml
name = "Your project name"   # instead of the README heading
profile = "base"             # instead of the automatic choice
setup = "..."                # a different setup command for the first step
own_hook = true              # keep the repository's own session hook

[plugins]                    # claude.ai plugins to switch off or on in this repository
off = ["claude-for-manufacturing@synced"]
on = []
```

## Step 3: write the shared files

```bash
python3 .agents/scripts/sync_root.py
```

This writes `CLAUDE.md`, `AGENTS.md`, the Cursor rule files, the pull request template and the
contributor agreement check, and merges the session hook into `.claude/settings.json`. In a `base` repository it also writes
`setup-agents.sh` and `.claude/hooks/session-start.sh`. In a `doqs` repository, doqs installs
those. Commit the result.

Do not edit the generated files by hand. The weekly sync below writes them again.

## Step 4: check it

```bash
python3 .agents/scripts/sync_root.py --check
python3 .agents/scripts/context_budget.py --budget 20000
```

The first says whether the shared files match the kit. The second prints how much text an agent
loads before it starts, and fails above 20 KB.

## The weekly sync

The job `.github/workflows/sync-root.yml` in this kit keeps the shared files the same in every
Refaqt repository that mounts the kit at `.agents/`. It runs when the templates change on `main`,
every Monday, and when you start it by hand.

- In every repository it runs `sync_root.py` and the mistakes index.
- In a machine repository it also runs doqs' installer. That writes `doqs.sh`, `doqs.bat`,
  `syson.*`, `setup-tooling.sh`, `setup-tooling.bat`, the session hook and the doqs settings.
- When something changed, it opens one pull request from the branch `refaqt-agent-files`. A
  person merges it. When nothing changed, it closes an old sync pull request.
- It uses no AI, and an agent can change it from a cloud session.

It uses the GitHub App "Refaqt file sync", which is installed on every Refaqt repository. One
setting is needed once: give this repository access to the App's key.

1. In GitHub, open the `refaqt` organization, then **Settings**.
2. In the menu on the left, open **Secrets and variables**, then **Actions**.
3. On the **Secrets** tab, click the pencil next to `SYNC_APP_PRIVATE_KEY`. Under **Repository
   access**, add `refaqt-agents`, and save.
4. On the **Variables** tab, open `SYNC_APP_ID`. If it is limited to some repositories, add
   `refaqt-agents` there too.

To try it: open **Actions** in this repository, choose "Sync shared agent files", then **Run
workflow**. Tick "Only report what would change" the first time. The run's summary lists each
repository and its files.

## How it works in each tool

| Tool | What happens |
| --- | --- |
| Claude Code, one repository | The session hook fills `.agents/` and links the skills into `.claude/skills/`. `CLAUDE.md` imports `AGENTS.md`, which imports `core.md` and `repo.md`. |
| Claude Code, several repositories, or a thread in a Claude project | The hook does not run. `CLAUDE.md` tells the agent to run the check and the setup file. |
| Claude, for your team | Add the marketplace `refaqt/refaqt-agents` in claude.ai under Organization settings, Plugins & skills, and turn the plugin `refaqt` on for all members. The skills then reach every session, also Cowork, chat, and sessions where the hook does not run. Marking it "required" only stops members from switching it off. The hook sees the plugin and does not link the kit skills a second time. |
| Cursor | Reads `AGENTS.md` and the generated `.cursor/rules/refaqt-*.mdc`. `.cursor/environment.json` runs the same hook in Cursor cloud agents. |
| GitHub Actions | Add `submodules: recursive` to the checkout step of every workflow that needs the kit. |

## When something goes wrong

| What you see | What to do |
| --- | --- |
| `.agents/` is empty | Run `bash setup-agents.sh`, or `bash setup-tooling.sh` in a doqs repository |
| The session says nothing at start | The hook did not run. Check the `SessionStart` entry in `.claude/settings.json`, or see the second row above |
| A sync pull request changes a file you edited | Generated files come from the kit. Make the change in the kit, or in `.agents-local/` |
| `bad interpreter` or `\r: command not found` | Add `*.sh text eol=lf` to `.gitattributes` (the sync adds it) and check the file out again |
| Each skill shows up twice | The plugin is on, and an old link is left in `.claude/skills/`. Delete that folder; the hook makes it again |
| `.agents` shows as modified in `git status` | That is the update working. Leave it uncommitted unless you mean to fix a version |
