# Install the agent kit in your repository

This guide adds the shared rules and skills to one project repository. After that, every AI agent
that works in that repository reads the same rules, on a laptop and in the cloud.

You do not need to be a software developer to follow this. You do need to be able to run commands in
a terminal and push to the repository.

Write every file and every reply in B2 English. Follow [`rules/communication.md`](rules/communication.md).

## What you get

The kit is a folder of shared rules and skills. It arrives in your repository as a folder called
`.agents/`. You do not copy the files. You link to them, so every repository uses one shared copy and
gets improvements automatically.

The link is a **git submodule**: a second repository that lives in a folder inside yours and keeps
its own history. Your repository records which version of the kit it uses.

## Before you start

You need three things.

- A project repository on GitHub, and permission to push to it.
- `git` installed on your computer.
- A terminal open in your repository folder.

Nothing else. [refaqt/refaqt-agents](https://github.com/refaqt/refaqt-agents) is a public repository,
so no password or access token is needed to read it.

## Which case are you in

Look in your repository for a folder called `doqs`. Your answer decides which version of Step 2
you follow, and which command you run in Step 3.

| Your repository | Follow | Why |
| --- | --- | --- |
| Has a `doqs` folder (machine and hardware projects) | **Route A** | `doqs` already ships a setup helper that handles both folders. |
| Has no `doqs` folder (business, legal, web, and other projects) | **Route B** | You install the kit on its own, with the files in `templates/`. |

Do not mix the two routes. Route A and Route B both install a start-up file at the same place, and
`doqs` overwrites whatever it finds there.

## Step 1 — Add the kit (both routes)

Run this from the top folder of your repository.

```bash
git submodule add -b main https://github.com/refaqt/refaqt-agents.git .agents
git commit -m "chore: add the shared agent kit at .agents"
```

`-b main` matters. It writes `branch = main` into your `.gitmodules` file, which is what lets the kit
move forward later. Without it, your repository stays on today's version of the kit and never gets a
newer one.

Open `.gitmodules` and check that it now holds this entry:

```
[submodule ".agents"]
	path = .agents
	url = https://github.com/refaqt/refaqt-agents.git
	branch = main
```

If the folder `.agents/` already exists in your repository with older copied files in it, move those
files somewhere else first. Git refuses to add a submodule on top of an existing folder.

## Step 2 — Add the start-up files

### Route A — your repository has `doqs`

The `doqs` repository owns the helpers. Take them from
[`doqs/templates/setup-tooling/`](https://github.com/refaqt/doqs/tree/main/templates/setup-tooling).

1. Copy `setup-tooling.sh` and `setup-tooling.bat` to the top folder of your repository. Commit them.
   Do not put them in `.gitignore`. Do not run them from inside the templates folder: they would look
   in the wrong place.
2. Add the line `*.sh text eol=lf` to your `.gitattributes` file. This stops Windows from saving the
   helper with line endings that Linux cannot read.
3. Run `bash setup-tooling.sh` once, from the top folder.

That one run does the rest. It fills both folders, installs the start-up file at
`.claude/hooks/session-start.sh`, and adds the entry to `.claude/settings.json` that starts it.

If you use Cursor cloud agents, add one more file by hand. Create `.cursor/environment.json` with
your own project name, so Cursor runs the same start-up file:

```json
{
  "name": "<your repository name>",
  "install": "bash .claude/hooks/session-start.sh"
}
```

**Do not copy `.agents/templates/setup-agents.sh` or `.agents/templates/session-start.sh` into a
repository that has `doqs`.** Both routes use the same file name, and the `doqs` helper replaces that
file every time it runs. You would lose your copy without a warning.

Now go to Step 3.

### Route B — the kit on its own

Copy four files out of the kit. The paths below start from the top folder of your repository.

| Copy this file | To here | What it does |
| --- | --- | --- |
| `.agents/templates/setup-agents.sh` | `setup-agents.sh` | Fills and updates `.agents/` when you run it by hand |
| `.agents/templates/session-start.sh` | `.claude/hooks/session-start.sh` | Fills `.agents/` at the start of every session |
| `.agents/templates/claude-settings.json` | `.claude/settings.json` | Starts the file above |
| `.agents/templates/cursor-environment.json` | `.cursor/environment.json` | Starts the same file in Cursor cloud agents |

These commands do all four copies.

```bash
mkdir -p .claude/hooks .cursor
cp .agents/templates/setup-agents.sh setup-agents.sh
cp .agents/templates/session-start.sh .claude/hooks/session-start.sh
cp .agents/templates/cursor-environment.json .cursor/environment.json
chmod +x setup-agents.sh .claude/hooks/session-start.sh
```

Then finish three small things by hand.

1. **The settings file.** If you have no `.claude/settings.json` yet, copy the template:
   `cp .agents/templates/claude-settings.json .claude/settings.json`. If you already have one, open
   both files and add the `hooks` block from the template into your file. Do not replace your file:
   you would throw away your own settings.
2. **The name in `.cursor/environment.json`.** Replace `<your repository name>` with the name of your
   project.
3. **Line endings.** Add this line to your `.gitattributes` file, so Windows cannot save the scripts
   in a form that Linux refuses to run:

   ```
   *.sh text eol=lf
   ```

Last, give agents a starting page. Copy [`templates/AGENTS.md`](templates/AGENTS.md) to the top folder
as `AGENTS.md` and fill in the "This repository" section. Copy
[`templates/CLAUDE.md`](templates/CLAUDE.md) to the top folder as `CLAUDE.md`. On Windows, do not link
`AGENTS.md` into the submodule. Use the small copy, as the template does.

Commit everything.

```bash
git add -A
git commit -m "chore: run agents from the shared kit in every session"
```

## Step 3 — Agents on your own computer

This covers Claude Code in a terminal or in the desktop app, and Cursor on a laptop.

**If you are cloning the repository for the first time**, ask for the kit in the same command:

```bash
git clone --recurse-submodules <the address of your repository>
```

**If you already have the repository on your computer**, run the setup file once from the top folder:

| Route | Command |
| --- | --- |
| Route A | `bash setup-tooling.sh` |
| Route B | `bash setup-agents.sh` |

On Windows, people may double-click `setup-tooling.bat` instead. Agents must not use the `.bat` file:
it waits for a key press and nobody is there to press one. Agents run the `.sh` file in Git Bash.

You should see a line that says the kit is ready, with a short code for the version.

## Step 4 — Agents in the cloud

A cloud session copies your repository **without** the contents of the kit folder. The folder
`.agents/` arrives empty. Nothing warns you about it. The agent reads no rules, finds no skills, and
keeps working as if everything were normal.

That is why the start-up file from Step 2 exists. It fills the folder before the agent reads
anything.

### Claude Code on the web

Nothing more to do. Step 2 already installed `.claude/hooks/session-start.sh` and the entry in
`.claude/settings.json` that starts it. Your next cloud session begins with a line like this:

```
The agent kit is ready: .agents/ (d42d850).
Read .agents/rules/core.md first, then AGENTS.md.
```

If you see nothing at all, the file is on disk but nothing starts it. Check `.claude/settings.json`.

### Cursor cloud agents

Cursor reads `.cursor/environment.json` and runs the same file. Step 2 created it. Check that it
holds this, with your own project name:

```json
{
  "name": "<your repository name>",
  "install": "bash .claude/hooks/session-start.sh"
}
```

### GitHub Actions

Automated checks need the same thing, and they ask for it in the checkout step. Add the `submodules`
line to that step in every workflow that needs the rules or the skills:

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      submodules: recursive
```

Use `submodules: recursive`, not the update command with `--remote`. A check should run against the
version of the kit your repository records, so that the same commit always gives the same result.

### Any other agent tool

The rule is the same for every tool. Before the agent reads anything, the tool must run one of these
from the top folder of the repository:

| Route | Command |
| --- | --- |
| Route A | `bash setup-tooling.sh` |
| Route B | `bash setup-agents.sh` |

Most tools have a setting for a command that runs when a session or a container starts. Put the
command there.

## Step 5 — Check that it worked

Run this from the top folder:

```bash
head -3 .agents/rules/core.md
```

You should see the first lines of the shared rules. If the command says the file does not exist, the
kit is not installed. Go to the table at the end of this guide.

Then check the list below.

- [ ] `.gitmodules` holds a `.agents` entry with `branch = main`.
- [ ] `.agents/rules/core.md` opens and has text in it.
- [ ] Route B only: `setup-agents.sh` is in the top folder.
- [ ] `.claude/hooks/session-start.sh` is there and is executable.
- [ ] `.claude/settings.json` names that file under `SessionStart`.
- [ ] `.cursor/environment.json` names that file under `install`.
- [ ] `AGENTS.md` and `CLAUDE.md` are in the top folder.

## Step 6 — Files that belong only to your repository

The kit holds what every Refaqt repository shares. Four more things are yours alone. Add them when
you need them.

| What you want | Where it goes |
| --- | --- |
| The four headings in the pull request box on GitHub | Copy [`templates/pull-request.md`](templates/pull-request.md) to `.github/pull_request_template.md` |
| A skill only this repository needs | `.agents-local/skills/<name>/SKILL.md` |
| Coding patterns only this repository uses | `.agents-local/skills/patterns/SKILL.md`, named from `AGENTS.md` |
| Cursor rules that point at the shared rules | Small files under `.cursor/rules/*.mdc` that link to `.agents/rules/*.md` |

Keep all of these **outside** `.agents/`. That folder belongs to the kit, and anything you write
inside it is lost the next time the kit updates. Two ready-made Cursor files are in the kit:
[`templates/cursor-rule-doqs-naming.mdc`](templates/cursor-rule-doqs-naming.mdc) and
[`templates/cursor-rule-freecad.mdc`](templates/cursor-rule-freecad.mdc).

## Keeping the kit up to date

The setup file and the start-up file both move `.agents/` to the latest `main` every time they run.
So you get new rules and skills without doing anything.

When the kit has moved on since your repository last recorded it, `git status` then shows `.agents` as
modified. That is normal, and it is the update doing its job. **Leave it uncommitted.** Only commit it
when you mean to fix your repository to one version of the kit on purpose, for example just before a
release. When the kit had not moved, nothing shows up, and that is normal too.

## When something goes wrong

| What you see | What it means | What to do |
| --- | --- | --- |
| `.agents/` is empty | The session copied your repository without the kit | Run `bash setup-agents.sh`, or `bash setup-tooling.sh` in Route A |
| Git said `Skipping submodule` | Git skipped the folder and still reported success | Check that `.gitmodules` has the `.agents` entry, then run the setup file again |
| The session says nothing at start-up | The start-up file is on disk, but nothing runs it | Check the `SessionStart` entry in `.claude/settings.json` |
| `bad interpreter` or `\r: command not found` | Windows saved the script with the wrong line endings | Add `*.sh text eol=lf` to `.gitattributes`, then re-checkout the file |
| `Permission denied` when the start-up file runs | The file is not marked as a program | Run `chmod +x .claude/hooks/session-start.sh` and commit that change |
| `could not read Username for 'https://github.com'` | The session has no network, or the repository is private | The kit is public, so this is almost always the network. Run the setup file again when you are online |
| Your start-up file keeps changing back | The repository has `doqs`, and `doqs` owns that file | Follow Route A only. Delete the copies you made from `templates/` |
| The folder `.agents/` already existed | Git will not add a submodule on top of a folder | Move the old files somewhere else, then run Step 1 again |

## Where to read next

| File | What is in it |
| --- | --- |
| [`README.md`](README.md) | What the kit holds, and the list of skills |
| [`rules/core.md`](rules/core.md) | The rules every agent follows |
| [`rules/communication.md`](rules/communication.md) | How to write, in B2 English |
| [`rules/reporting.md`](rules/reporting.md) | How to write pull requests, commits, and log entries |
| [`templates/AGENTS.md`](templates/AGENTS.md) | The starting page you copy into your repository |
