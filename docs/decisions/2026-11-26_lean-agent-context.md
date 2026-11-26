# Agents load short rules first, and the rest only when a task needs it

- **Date:** 2026-11-26
- **Status:** Accepted

## Context

Agents spent many tokens before they started any work. In aqtuator, a normal start meant about
82 KB of text (about 20,000 tokens). In doqs, larger work meant about 257 KB. The main causes:

- The rules said to read whole folders: every mistake note at every task, every decision before
  larger work.
- Every rule loaded in every session, also rules for one task only, such as pull requests.
- Claude Code could not find the kit skills. It looks only in `.claude/skills/<name>/`, and the kit
  kept them in nested category folders. Agents found them only through tables in `AGENTS.md`.
- About 25 of the 39 skills repeated general knowledge that Claude already has.
- Root files (`CLAUDE.md`, `AGENTS.md`, Cursor rules) drifted apart between repositories. Nothing
  kept them in step.

## Decision

1. **Three levels.** Always: `CLAUDE.md`, `AGENTS.md`, `rules/core.md` and the repository's own
   `repo.md`, under 6 KB in total. Per task: skills, one mistake note, one decision. Deep reference:
   long docs, read by section only.
2. **Indexes, not folders.** Agents read `docs/mistakes/README.md` at the start of a task. A script
   writes its table, with one prevention rule per line.
3. **Task rules became skills:** `reporting`, `copyright`, `coding`, `source-documents`,
   `delegate`, `advice`. The old files in `rules/` only point to the new place.
4. **Sixteen skills, one folder each.** Generic skills were deleted. Five legal and token skills
   became `belgian-cooperative-legal-tax`.
5. **Skills reach agents three ways from one source.** The organization turns on the `refaqt`
   plugin in claude.ai, so every session gets the skills. Other people get links that the session
   hook makes in `.claude/skills/`. Cursor reads the table in `AGENTS.md`.
6. **Anthropic plugins are not copied.** Claude for Manufacturing and other Anthropic plugins are
   turned on for the organization in claude.ai. Each repository can turn one off in
   `.agents-local/profile.toml`, to save the space their skill list takes. Copying them would break
   updates, and their licence does not allow it in this GPL repository.
7. **Root files are generated.** `scripts/sync_root.py` writes them from `templates/root/`. A
   GitHub Action in this kit (`.github/workflows/sync-root.yml`) runs it in every repository
   that has `.agents-local/profile.toml`, and opens a pull request. It uses
   no AI, so the result is the same every time.

## Consequences

- A start in aqtuator drops from about 82 KB to about 20 KB, most of it the skill list and the mistakes index. `scripts/context_budget.py` measures
  it, and CI can fail when it grows back.
- Agents must open a skill or an index entry when the task needs it. The table in `AGENTS.md` says
  which.
- People change shared text in this kit, never in a repository's `CLAUDE.md` or `AGENTS.md`.
- Outside contributors do not get Anthropic's plugins. They do get every Refaqt skill.
- Repositories need `.agents-local/profile.toml` before the sync can run.
