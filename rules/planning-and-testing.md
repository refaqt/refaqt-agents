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
- Done means checked against reality, not against your own input. If you build something from a
  source (a datasheet, a drawing, a specification), check the result against the real thing or a
  trusted reference. "The values come from the source" is not proof. For CAD models, see the
  FreeCAD skill.
- A test must not change the files it checks. Work on a copy, or check before you commit that
  nothing changed that you did not mean to change.

## Working from a source document

- First list everything in the source: every value and every feature. Show the list to the user.
  Then do each item, or write why you leave it out. Do not drop what you do not understand. Ask.
- Know which values are exact and which are estimates. Mark every estimate as an estimate, and ask
  the user how to confirm it.
