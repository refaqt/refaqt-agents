# Agent guide

Start here if you are an agent (Cursor, Claude Code, or similar) working in this repository.

## First step (required)

Before you read `.agents/` rules or skills, update tooling submodules to the latest `main`:

- **All agents, any OS:** `bash setup-tooling.sh`
- **People on Windows** may double-click `setup-tooling.bat` (`pause` is OK there only). Agents must not run the `.bat`.

## Shared kit

This repo mounts [refaqt/refaqt-agents](https://github.com/refaqt/refaqt-agents) at [`.agents/`](.agents/).

1. Read [`.agents/rules/core.md`](.agents/rules/core.md), [`.agents/rules/communication.md`](.agents/rules/communication.md), [`.agents/rules/reporting.md`](.agents/rules/reporting.md), and [`.agents/rules/living-docs.md`](.agents/rules/living-docs.md).
2. Read [`docs/mistakes/`](docs/mistakes/) and say which prevention rules apply.
3. Read [`docs/architecture.md`](docs/architecture.md) before larger work.
4. Before new coding solutions, check [`.agents-local/skills/patterns/SKILL.md`](.agents-local/skills/patterns/SKILL.md) if it is there.

Write every reply and every file in B2 English. Follow `.agents/rules/communication.md`.
Write pull requests, commit messages, GitHub comments, issues, and log entries for a manager, not
for a developer. Follow `.agents/rules/reporting.md`.
Copy [`.agents/templates/pull-request.md`](.agents/templates/pull-request.md) to
`.github/pull_request_template.md` so the pull request box starts with the right headings.

## This repository

<!-- Customize: stack, Windows/PowerShell notes, measurement archives, local skills, validate command. -->

| You are adding | It goes in |
| --- | --- |
| A day's work write-up | `docs/log/YYYY-MM-DD_topic.md` |
| Why a choice was made | `docs/decisions/YYYY-MM-DD_topic.md` |
| Something that went wrong | `docs/mistakes/YYYY-MM-DD_topic.md` |

Skills that belong only to this repo: [`.agents-local/skills/`](.agents-local/skills/).

## Skills

| Skill | Path |
| --- | --- |
| Activity log | `.agents/skills/log/SKILL.md` |
| Mistake log | `.agents/skills/mistake-log/SKILL.md` |
| Maintain patterns | `.agents/skills/maintain-patterns/SKILL.md` |

## DOQS machine repos (when `doqs/` submodule is present)

1. Read `doqs/docs/architecture.md` for module layout, OKH, builds, and simulation.
2. After structural changes: `python doqs/scripts/validate_all.py` from the repo root.
3. Extra skills from this kit:

| Skill | Path |
| --- | --- |
| DOQS naming | `.agents/skills/doqs-naming/SKILL.md` |
| FreeCAD debugging | `.agents/skills/freecad/SKILL.md` |

4. Workflow rules for this repo go in `.agents-local/rules/` (for example `doqs-workflow.md`).
5. Copy [`templates/cursor-rule-doqs-naming.mdc`](templates/cursor-rule-doqs-naming.mdc) and [`templates/cursor-rule-freecad.mdc`](templates/cursor-rule-freecad.mdc) to `.cursor/rules/` when you use Cursor.
