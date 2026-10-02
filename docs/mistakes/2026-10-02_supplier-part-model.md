# 2026-10-02 — A supplier part model was called done, but it did not match the real part

## What happened

An agent built CAD models of a bought part from a supplier catalogue and said they were done. They
did not match the real part.

- It modelled only the table values it understood. It left out the rest without saying so. Some of
  the missing features stick out of the main shape: a grease nipple, a plug, screw heads, and a
  reference edge. Without them, the assembly cannot show collisions.
- It read sizes from a figure that the catalogue drew for another size of the same part.
- A helper agent said "pass". The main agent accepted it without asking how the helper measured.
- A helper kept supplier values in the main agent's folder, where the main agent must not see them.
- A test opened a model file and saved it again, so the model changed without anyone wanting it.
- Files were removed from git but stayed on disk. The report did not say so.

## Why it went wrong

- There was no list of what the drawing contains, so nobody could see what was missing.
- Exact table values and rough figure estimates were treated the same way.
- "Done" meant "the values come from the datasheet", not "the model matches the part".
- A helper's result was trusted without its method.
- The report described the branch, not the real state of the project.

## Prevention rule

- Before you model from a drawing, list every dimension and feature, and show the list to the user.
  Model each one, or write why you leave it out. Never leave out a feature that sticks out.
- Mark every value read from a figure as an estimate. First check that the figure is to scale for
  this size. Ask the user to measure the real part.
- Done means rebuilt, measured, compared with the real part or a reference model, and shown to the
  user as a picture.
- Ask every helper how it measured. Keep helpers that see restricted data in their own temporary
  folder.
- Tests must not save model files. Check fingerprints before you commit.
- Say whether removed files are still on disk, and say that the main branch is unchanged until the
  pull request is merged.

## Related

- [`skills/freecad/SKILL.md`](../../skills/freecad/SKILL.md), section "Modelling a part from a
  supplier drawing"
- [`rules/subagents.md`](../../rules/subagents.md)
- [`rules/planning-and-testing.md`](../../rules/planning-and-testing.md)
- [`rules/reporting.md`](../../rules/reporting.md), section "Report the real state"
