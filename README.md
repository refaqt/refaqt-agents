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
| `templates/`      | Starter `AGENTS.md` and `CLAUDE.md`, setup and session-start files, pull request template, decision template, Cursor rule stubs, and living-doc stubs for new repos. |
| `bootstrap/docs/` | Same stubs, kept for kits that still point at `.cursor/bootstrap`.                  |

## Install into a project repo

Step-by-step instructions, for agents on a laptop and for agents in the cloud:
**[INSTALL.md](INSTALL.md)**.

The short version, from the project repo root:

```bash
git submodule add -b main https://github.com/refaqt/refaqt-agents.git .agents
```

`-b main` records `branch = main` in `.gitmodules`, which is what lets the kit move forward later.

A cloud session copies a repository **without** the contents of its submodules, so `.agents/`
arrives empty and nothing warns about it. A start-up file has to fill the folder before an agent
reads anything. [INSTALL.md](INSTALL.md) covers that for repos with the `doqs` submodule and for
repos that install this kit on its own, and lists the extra files each project repo keeps outside
`.agents/`.

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
