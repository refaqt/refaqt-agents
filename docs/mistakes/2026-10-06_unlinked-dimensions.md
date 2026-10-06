# 2026-10-06 — CAD models had typed numbers and sketches that could still move

## What happened

Agents built FreeCAD models that looked right but could not be changed safely.

- Some sketches were not fully constrained. A point or a line could still move.
- Many dimensions were typed numbers. They were not linked to the parameter
  spreadsheet, to another dimension, or to any reason.
- A row of 8 holes got 7 typed spacings. To change the pitch, someone had to
  change 7 numbers, and nothing showed that the 7 belonged together.

## Why it went wrong

- The skill only said to prefer spreadsheets and master sketches. Typing a
  number was shorter, so agents did that.
- Nobody asked where a value comes from: a requirement, a bought part, a
  standard, a simulation, or a design choice.
- The model was called done when it looked right, not when every sketch was
  fully constrained and every size was linked.

## Prevention rule

- Before you draw, write the parameter table. Mark each value as independent,
  with its reason, or derived, as a formula. Ask the user before you invent a
  design value.
- Fully constrain every sketch. Link every dimension and every feature size to
  the parameter spreadsheet.
- Draw a repeated feature once and pattern it from a count and a pitch.
- Before you say done, check for free sketches and typed sizes, and report what
  is left.

## Related

- [FreeCAD skill, Think parametric](../../skills/freecad/SKILL.md#think-parametric-every-dimension-has-a-reason)
- doqs decision `docs/decisions/2026-10-06_every-dimension-has-a-source.md`
