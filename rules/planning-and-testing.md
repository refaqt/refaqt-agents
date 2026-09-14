# Planning and quality

## Before coding

- For work that touches several files, plan which files change, what is added, edge cases, and side effects before you edit.
- Split large features into small steps. Check each step before the next.
- Look for existing helpers before you add dependencies, patterns, or extra layers, unless the user asks.

## While coding

- Follow naming and structure from nearby files. Keep functions small and focused on one job.
- Handle errors in the open. Do not hide exceptions.
- Do not delete code unless you are sure it is unused. If you are not sure, comment with `// TODO: remove if confirmed unused`.
- Do not leave debug logs, prints, or commented-out test code in committed files.
- Add comments only when the why is not clear from the what. Write comments in B2 English. Follow [communication.md](communication.md).

## Testing

- Run existing tests when you can before you say the work is done.
- For new logic, add at least a small smoke test unless the user says not to.
- Say clearly when a change is untested and why.
