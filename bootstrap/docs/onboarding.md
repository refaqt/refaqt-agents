# Onboarding

How to set up, run, and find your way around this repository.
Write this file in B2 English. Follow `.agents/rules/communication.md`.

## Prerequisites

- [List prerequisites.]

## Setup

1. Clone the repository (with submodules): `git clone --recurse-submodules …`
2. Copy helpers from `doqs/templates/setup-tooling/` to the **repo root** if this is a new repo (never run them from the templates folder). Agents: `bash setup-tooling.sh`. People on Windows may double-click `setup-tooling.bat`.
3. [Install dependencies and configure the environment.]

## Where to read next

| Doc | Use |
| --- | --- |
| `docs/architecture.md` | Module map and data flow |
| `.agents-local/skills/patterns/SKILL.md` | Project-specific reusable patterns |
| `docs/decisions/` | Why past technical choices were made |
| `docs/mistakes/` | What went wrong and how to avoid it |
| `docs/log/` | Date-ordered activity log |
| `.agents/` | Shared agent rules and skills (refaqt-agents) |

## Cursor / Agent

Root `AGENTS.md` is the start file. Shared rules and skills live in `.agents/`. Cursor adapters may live under `.cursor/rules/`. Prefer project files over the same text copied into User Rules in Settings.
