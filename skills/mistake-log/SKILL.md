---
name: mistake-log
description: >-
  Use after a bug, a failed approach, rejected output or a misunderstood convention, to write docs/mistakes/ and its prevention rule, and to turn a repeated mistake into a lasting rule.
---

# Mistake log

## What counts as a mistake

- A bug introduced and fixed in the same session.
- A wrong approach taken and then dropped.
- A misunderstanding of project conventions that caused rework.
- A test failure from an incorrect assumption.
- Any output the user rejected or asked to redo.

## Before starting work

1. Read the index `docs/mistakes/README.md`. Do not read every note.
2. Say which prevention rules apply to the current task. Open a note only when its rule matches.

## After a mistake

1. Add `docs/mistakes/YYYY-MM-DD_topic.md` (one file per incident), with a `## Prevention rule` section whose first line is the rule. Then update the index with `python3 .agents/scripts/mistakes_index.py` (in a doqs repository: `./doqs.sh mistakes`). Do not edit the index table by hand.
2. If the same mistake happens twice, add a bold warning on the relevant section and write a lasting rule: in `.agents-local/rules/repo.md` for this repository, or in the kit when every repository needs it.
3. Treat every mistake as a gap in the process, not a one-off.

Write every mistake entry in B2 English. Follow `.agents/rules/core.md`.
Keep file names, commands, and official names exact.

## Continuous improvement

- After a long session, review the mistakes index and `.agents-local/skills/patterns/SKILL.md` (if present) for rules or patterns to promote.
- Prefer making `docs/mistakes/` shorter over time by stopping repeat categories.

## Entry format

Use this format (see also [`templates/adr.md`](../../templates/adr.md) for decision records):

```markdown
# YYYY-MM-DD — Short title

## What happened

## Why it went wrong

## Prevention rule

## Related
```
