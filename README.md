# refaqt-agents

Portable, tool-neutral rules and skills for AI agents working on Refaqt repositories.

Mount this repository as a git submodule at `.agents/` in each consumer repo (Cursor, Claude Code, and anything that reads `AGENTS.md`).

## Layout

| Path              | Purpose                                                                              |
| ----------------- | ------------------------------------------------------------------------------------ |
| `rules/`          | Standing guidance (markdown). Consumers load via thin adapters and root `AGENTS.md`. |
| `skills/`         | Process skills (`SKILL.md`).                                                         |
| `templates/`      | Starter `AGENTS.md`, ADR template, Cursor rule stubs, and living-doc stubs for new repos. |
| `bootstrap/docs/` | Same stubs, kept for kits that still reference `.cursor/bootstrap`.                  |

## Install into a consumer repo

```bash
# From the consumer repo root (after any existing .agents/ content is moved out)
git submodule add https://github.com/refaqt/refaqt-agents.git .agents
```

Set `branch = main` on tooling submodules in `.gitmodules` (`doqs` and/or `.agents`). Copy helpers from [`doqs/templates/setup-tooling/`](https://github.com/refaqt/doqs/tree/main/templates/setup-tooling) to the **repo root** (never run them from that templates folder). After clone, agents run `bash setup-tooling.sh`.

Then:

1. Copy or adapt [`templates/AGENTS.md`](templates/AGENTS.md) to the **repo root** as `AGENTS.md` (keep the **First step (required)** block; add a "This repository" section).
2. Keep root `CLAUDE.md` as a one-liner pointing at `AGENTS.md`.
3. Add thin Cursor adapters under `.cursor/rules/*.mdc` that point at `.agents/rules/*.md` (see consumer examples in aqtuator).
4. Put **repo-specific** skills under `.agents-local/skills/` (not inside the submodule).
5. Put **repo-specific** coding patterns in `.agents-local/skills/patterns/SKILL.md` and point agents at them from `AGENTS.md`.

Windows note: do not symlink root `AGENTS.md` into the submodule — use a thin stub file.

## Branching

Every task that changes the repo must start on a **new git branch** off `main`, unless the user explicitly says otherwise. Do not land task work as commits directly on `main`.

## Skills in this kit

### Process (any role)

| Skill               | When                                                           |
| ------------------- | -------------------------------------------------------------- |
| `log`               | Add or edit `docs/log/` activity entries (any role)            |
| `mistake-log`       | Read/write `docs/mistakes/`; promote prevention rules          |
| `maintain-patterns` | Update the consumer's `.agents-local/skills/patterns/SKILL.md` |
| `doqs-naming`       | DOQS module/BOM/OKH naming and validation (requires `doqs/` submodule) |
| `freecad`           | FreeCAD debugging, workbench issues, assembly/Binder problems   |

### Role skills

Organized under `skills/{category}/{skill-name}/SKILL.md` for cooperative open-hardware ventures.

| Category | Skills |
| --- | --- |
| `business/` | `business-development`, `finance`, `marketing`, `purchasing`, `sales` |
| `engineering/` | `software-development`, `mechanical-engineering`, `electrical-engineering`, `industrial-automation`, `mechatronic-engineering`, `optical-engineering`, `systems-engineering`, `production-engineering`, `sysml-v2` |
| `supply-chain/` | `supply-chain-management` |
| `compliance/` | `product-compliance` (CE marking, machinery safety, conformity assessment) |
| `legal/` | `legal-advice`, `belgian-law`, `european-law`, `us-law`, `belgian-fiscal-tax`, `belgian-corporate-law` |
| `governance/` | `open-source-community`, `sociocracy`, `agile` |
| `web3/` | `web3-blockchain`, `token-engineering` |

## License

GPL-3.0 (see [LICENSE](LICENSE)).
