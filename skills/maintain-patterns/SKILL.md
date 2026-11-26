---
name: maintain-patterns
description: >-
  Use before you build a new solution in code, after a fix that is specific to this codebase, or when the user mentions project patterns. Keeps .agents-local/skills/patterns/SKILL.md current.
---

# Project patterns (`.agents-local/skills/patterns/SKILL.md`)

Write pattern entries in B2 English. Follow `.agents/rules/core.md`.
Keep code, file paths, and official names exact.

## Before starting work

1. Read `.agents-local/skills/patterns/SKILL.md` if it exists.
2. If an entry matches the task, follow that pattern instead of inventing a new approach.
3. If nothing applies, proceed with normal implementation.

## After a novel, codebase-specific fix

When you solve something specific to this repository in a way worth repeating:

1. Add or update an entry in `.agents-local/skills/patterns/SKILL.md` using the format below.
2. Do not add generic programming knowledge; only patterns tied to this project.
3. If the pattern should become standing agent guidance for every Refaqt repo, propose adding it to `.agents/rules/` in refaqt-agents instead of duplicating long prose.

## When updating or deprecating

- Change or remove the entry in `.agents-local/skills/patterns/SKILL.md` in the same change as the code, or immediately after.
- If deprecated, mark clearly or remove after migration.

## Entry format

```markdown
## [Pattern name]
**When to use:** [One sentence]
**Pattern:**
```[language]
// minimal example
```
**Gotchas:** [Any known edge cases or pitfalls]
**Last used:** [Date or task reference]
```

## Quality bar

- **Name:** Short, unique, searchable. Use everyday words.
- **When to use:** One sentence so the agent can match tasks quickly.
- **Pattern:** Smallest example that still shows the project-specific hook.
- **Gotchas:** Real pitfalls for this repo, in plain sentences.
- **Last used:** ISO date or issue/PR reference.
