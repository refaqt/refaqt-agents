# refaqt-agents

Rules and skills for AI agents that work on Refaqt repositories. Any agent tool can use this kit:
Claude Code, Cursor, and tools that read `AGENTS.md`.

Write every reply and every file in B2 English. The rules are in [`rules/core.md`](rules/core.md).

## How agents use it

The kit keeps start-up text small. An agent loads only what every task needs, and loads the rest
when a task asks for it.

| Level | What | When it loads |
| --- | --- | --- |
| Always | `CLAUDE.md` and `AGENTS.md` in the repository, which import [`rules/core.md`](rules/core.md) and the repository's `.agents-local/rules/repo.md` | Every session, about 6 KB |
| Always | The name and one-line description of each skill | Every session, about 2 KB |
| Per task | A skill's full text, such as [`reporting`](skills/reporting/SKILL.md) for pull requests | When the task matches the description |
| Per task | One mistake note, one decision, one doc page | When its line in an index matches the task |

`AGENTS.md` and `CLAUDE.md` are generated. Do not edit them in a repository: change
[`templates/root/`](templates/root/) here, or the repository's own `.agents-local/`.

## Layout

| Path | What it holds |
| --- | --- |
| `rules/core.md` | The rules for every task. Keep it under 2.5 KB. The other files in `rules/` only point to where their text moved. |
| `skills/<name>/SKILL.md` | Skills, one folder each, in the open Agent Skills format |
| `scripts/` | `sync_root.py` (writes the shared root files), `sync_one_repo.sh` (used by the weekly sync job), `link_skills.sh`, `mistakes_index.py`, `context_budget.py` |
| `templates/root/` | Templates for `CLAUDE.md`, `AGENTS.md` and the Cursor rule files |
| `templates/` | The session hook and setup file for repositories without doqs, the pull request and decision templates |
| `bootstrap/docs/` | Starting files for `docs/log/`, `docs/decisions/`, `docs/mistakes/` and `docs/architecture.md` |
| `.claude-plugin/` | Makes this repository a Claude plugin called `refaqt` |

## Install

See [INSTALL.md](INSTALL.md). Short version: add the kit as a submodule at `.agents/`, write
`.agents-local/rules/repo.md`, and run `python3 .agents/scripts/sync_root.py`. A weekly job then
keeps the shared files current in every repository.

To use the skills in Claude Code without the submodule, install the plugin:

```
/plugin install refaqt --marketplace refaqt/refaqt-agents
```

## Skills

| Skill | Use when |
| --- | --- |
| `reporting` | Writing a pull request, commit, issue, GitHub comment or log entry |
| `copyright` | Creating files, adding material from others, setting up a repository |
| `coding` | Writing or changing code and tests |
| `source-documents` | Working from a data sheet, drawing or standard; calling pass or fail |
| `delegate` | Handing work to subagents |
| `advice` | Giving people legal, money, safety or compliance advice |
| `log` | Recording work in `docs/log/` |
| `mistake-log` | Recording a mistake and its prevention rule |
| `maintain-patterns` | Keeping the repository's coding patterns current |
| `doqs-naming` | Naming DOQS modules, BOM rows, versions and tags |
| `freecad` | Creating, changing or debugging FreeCAD models |
| `sysml-v2` | Writing or reviewing SysML v2 system models |
| `design-quality` | Judging whether a design is done, with gates and measuring scripts |
| `machine-hmi-design` | Operator screens and alarms on machines |
| `product-compliance` | CE marking and the machinery rules for selling a machine in the EU |
| `belgian-cooperative-legal-tax` | Belgian company, cooperative, tax and token questions |
| `github-actions` | Adding or changing a GitHub Actions workflow |

General knowledge that Claude already has (marketing, sales, agile, general engineering) is not
repeated here. Anthropic's own plugins, such as Claude for Manufacturing, are turned on for the
organization in claude.ai and are not copied into this kit. See
[the decision record](docs/decisions/2026-11-26_lean-agent-context.md).

## Pull requests

Use the four headings in the [`reporting`](skills/reporting/SKILL.md) skill. The template is
[`templates/pull-request.md`](templates/pull-request.md).

## License

Copyright © 2025–2026 Refaqt (BE 0804.145.539) and contributors. Contributions are accepted under the [Refaqt Contributor Licence Agreement](https://github.com/refaqt/.github/blob/main/CLA.md).

GPL-3.0 (see [LICENSE](LICENSE)).
