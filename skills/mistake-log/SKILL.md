---
name: mistake-log
description: >-
  Logs incidents to docs/mistakes/, records repeated failures, and turns them
  into prevention rules. Use at task start, after bugs, failed approaches, rejected
  output, or convention misunderstandings in this repository.
---

# Mistake log

## What counts as a mistake

- A bug introduced and fixed in the same session.
- A wrong approach taken and then dropped.
- A misunderstanding of project conventions that caused rework.
- A test failure from an incorrect assumption.
- Any output the user rejected or asked to redo.

## Before starting work

1. Read `docs/mistakes/` (and its `README.md` index).
2. Say which prevention rules apply to the current task.

## After a mistake

1. Add `docs/mistakes/YYYY-MM-DD_topic.md` (one file per incident) and a row in `docs/mistakes/README.md`.
2. If the same mistake happens twice, add a bold warning on the relevant section and write a lasting rule (`.agents/rules/` in the kit, or a small adapter such as `.cursor/rules/`).
3. Treat every mistake as a gap in the process, not a one-off.

Write every mistake entry in B2 English. Follow `.agents/rules/communication.md`.
Keep file names, commands, and official names exact.

## Continuous improvement

- After a long session, review `docs/mistakes/` and `.agents-local/skills/patterns/SKILL.md` (if present) for rules or patterns to promote.
- Prefer making `docs/mistakes/` shorter over time by stopping repeat categories.

## Entry format

Use this format (see also [`templates/adr.md`](../templates/adr.md) for ADRs):

```markdown
# YYYY-MM-DD — Short title

## What happened

## Why it went wrong

## Prevention rule

## Related
```
