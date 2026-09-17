# refaqt-agents

Rules and skills for AI agents that work on Refaqt repositories. Any agent tool can use this kit.

Add this repository as a git submodule at `.agents/` in each project repo (Cursor, Claude Code, and anything that reads `AGENTS.md`).

Write every reply and every file in B2 English. Follow [`rules/communication.md`](rules/communication.md). Keep official names, file paths, and numbers exact.
Write pull requests, commit messages, GitHub comments, issues, and log entries for a manager, not for a
developer. Follow [`rules/reporting.md`](rules/reporting.md).

## Layout

| Path              | Purpose                                                                              |
| ----------------- | ------------------------------------------------------------------------------------ |
| `rules/`          | Lasting guidance (markdown). Project repos load these through small adapters and root `AGENTS.md`. |
| `skills/`         | Process skills (`SKILL.md`).                                                         |
| `templates/`      | Starter `AGENTS.md`, pull request template, decision template, Cursor rule stubs, and living-doc stubs for new repos. |
| `bootstrap/docs/` | Same stubs, kept for kits that still point at `.cursor/bootstrap`.                  |

## Install into a project repo

```bash
# From the project repo root (after any existing .agents/ content is moved out)
git submodule add https://github.com/refaqt/refaqt-agents.git .agents
```

Set `branch = main` on tooling submodules in `.gitmodules` (`doqs` and/or `.agents`). Copy helpers from [`doqs/templates/setup-tooling/`](https://github.com/refaqt/doqs/tree/main/templates/setup-tooling) to the **repo root** (never run them from that templates folder). After clone, agents run `bash setup-tooling.sh`.

Then:

1. Copy or adapt [`templates/AGENTS.md`](templates/AGENTS.md) to the **repo root** as `AGENTS.md` (keep the **First step (required)** block; add a "This repository" section).
2. Keep root `CLAUDE.md` as a one-liner pointing at `AGENTS.md`.
3. Add small Cursor adapters under `.cursor/rules/*.mdc` that point at `.agents/rules/*.md` (see project examples in aqtuator).
4. Put skills that belong only to this repo under `.agents-local/skills/` (not inside the submodule).
5. Put coding patterns that belong only to this repo in `.agents-local/skills/patterns/SKILL.md` and point agents at them from `AGENTS.md`.
6. Copy [`templates/pull-request.md`](templates/pull-request.md) to `.github/pull_request_template.md`.

Windows note: do not symlink root `AGENTS.md` into the submodule — use a small stub file.

## Branching

Every task that changes the repo must start on a **new git branch** off `main`, unless the user says otherwise. Do not put task work as commits directly on `main`.

## Pull requests

A pull request is read by a manager, not only by a developer. Use these four headings, in this
order, and keep everything above the closed block under 200 words:

```markdown
## What changed

## Why it matters

## What you need to do

## How it was checked

<details>
<summary>Notes for reviewers</summary>

</details>
```

The rule, with a worked example, is [`rules/reporting.md`](rules/reporting.md). Copy
[`templates/pull-request.md`](templates/pull-request.md) to `.github/pull_request_template.md` in
each project repo.

## Skills in this kit

### Process (any role)

| Skill               | When                                                           |
| ------------------- | -------------------------------------------------------------- |
| `log`               | Add or edit `docs/log/` activity entries (any role)            |
| `mistake-log`       | Read/write `docs/mistakes/`; turn repeats into prevention rules |
| `maintain-patterns` | Update the project's `.agents-local/skills/patterns/SKILL.md` |
| `doqs-naming`       | DOQS module/BOM/OKH naming and checks (needs `doqs/` submodule) |
| `freecad`           | FreeCAD debugging, workbench issues, assembly/Binder problems   |

### Role skills

Files live under `skills/{category}/{skill-name}/SKILL.md` for cooperative open-hardware ventures.

| Category | Skills |
| --- | --- |
| `business/` | `business-development`, `finance`, `marketing`, `purchasing`, `sales` |
| `engineering/` | `software-development`, `mechanical-engineering`, `electrical-engineering`, `industrial-automation`, `mechatronic-engineering`, `optical-engineering`, `systems-engineering`, `production-engineering`, `sysml-v2` |
| `supply-chain/` | `supply-chain-management` |
| `compliance/` | `product-compliance` (CE marking, machinery safety, conformity checks) |
| `legal/` | `legal-advice`, `belgian-law`, `european-law`, `us-law`, `belgian-fiscal-tax`, `belgian-corporate-law` |
| `governance/` | `open-source-community`, `sociocracy`, `agile` |
| `web3/` | `web3-blockchain`, `token-engineering` |

## License

GPL-3.0 (see [LICENSE](LICENSE)).
