# Agent guide

Entry point for Cursor, Claude Code, and other agents working in this repository.

## Shared kit

This repo mounts [refaqt/refaqt-agents](https://github.com/refaqt/refaqt-agents) at [`.agents/`](.agents/).

1. Read [`.agents/rules/core.md`](.agents/rules/core.md) and [`.agents/rules/living-docs.md`](.agents/rules/living-docs.md).
2. Read [`docs/mistakes/`](docs/mistakes/) and state which prevention rules apply.
3. Read [`docs/architecture.md`](docs/architecture.md) before non-trivial work.
4. Before new coding solutions, check [`.agents-local/skills/patterns/SKILL.md`](.agents-local/skills/patterns/SKILL.md) if present.

If `.agents/` is empty: `git submodule update --init --recursive`.

## This repository

<!-- Customize: stack, Windows/PowerShell notes, measurement archives, local skills, validate command. -->

| You are adding | It goes in |
| --- | --- |
| A day's work write-up | `docs/log/YYYY-MM-DD_topic.md` |
| Why a choice was made | `docs/decisions/YYYY-MM-DD_topic.md` |
| Something that went wrong | `docs/mistakes/YYYY-MM-DD_topic.md` |

Repo-specific skills: [`.agents-local/skills/`](.agents-local/skills/).

## Skills

| Skill | Path |
| --- | --- |
| Activity log | `.agents/skills/log/SKILL.md` |
| Mistake log | `.agents/skills/mistake-log/SKILL.md` |
| Maintain patterns | `.agents/skills/maintain-patterns/SKILL.md` |

## DOQS machine repos (when `doqs/` submodule is present)

1. Read `doqs/docs/architecture.md` for module layout, OKH, builds, simulation.
2. After structural changes: `python doqs/scripts/validate_all.py` from repo root.
3. Additional skills from this kit:

| Skill | Path |
| --- | --- |
| DOQS naming | `.agents/skills/doqs-naming/SKILL.md` |
| FreeCAD debugging | `.agents/skills/freecad/SKILL.md` |

4. Repo-specific workflow rules → `.agents-local/rules/` (e.g. `doqs-workflow.md`).
5. Copy [`templates/cursor-rule-doqs-naming.mdc`](templates/cursor-rule-doqs-naming.mdc) and [`templates/cursor-rule-freecad.mdc`](templates/cursor-rule-freecad.mdc) to `.cursor/rules/` when using Cursor.
