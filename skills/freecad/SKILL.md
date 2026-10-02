---
name: freecad
description: >-
  Debug FreeCAD designs and answer modeling and workbench questions for
  intermediate users. Search the official wiki, forum, and GitHub issues,
  discussions, and pull requests (PRs) before you answer. Use when the user
  mentions FreeCAD, .FCStd, PartDesign, Assembly, workbenches, macros,
  Binder or Link errors, or FreeCAD troubleshooting.
---

# FreeCAD

Stay current with the latest FreeCAD version and its documentation. Help debug FreeCAD designs. Search the FreeCAD forum and GitHub issues, discussions, and pull requests (PRs) so you understand why something fails. Give clear answers for a FreeCAD user at an intermediate level, not a FreeCAD core developer. When you give advice, always point to the exact online sources.

## When to use

- FreeCAD modeling, assembly, or workbench questions
- `.FCStd` design failures, recompute errors, or broken links or Binders
- PartDesign, Assembly, TechDraw, FEM (finite element analysis), or addon/workbench issues
- Macros, spreadsheets, or top-down design with master sketches (one sketch drives many parts)
- The user asks why a FreeCAD feature or workflow is not working
- You model a bought part from a supplier catalogue, datasheet, or drawing

## Audience

Target a **FreeCAD intermediate** user:

- Explain graphical user interface (GUI) steps, workbench context, and model-tree fixes
- Use FreeCAD terms (Body, Tip, Binder, Link, recompute). Do not over-explain basics
- Prefer workbench menus and property panels over the Python console unless the user already uses macros
- Do **not** go into C++ source, patch proposals, or compiler flags unless the user asks for that

## Research-first workflow

Do **not** answer from memory alone. Before you give advice:

1. **Confirm version** — Ask or infer the FreeCAD version and build (stable vs weekly). Check [releases](https://github.com/FreeCAD/FreeCAD/releases) and [release notes](https://wiki.freecad.org/Feature_list) for behavior that depends on the version.
2. **Search the wiki** — [wiki.freecad.org](https://wiki.freecad.org/Main_Page) for the workbench, tool, and error terms.
3. **Search the forum** — [forum.freecad.org](https://forum.freecad.org/) (Help, workbench forums, Issues). Many failures are usage questions or known workarounds.
4. **Search GitHub** — [issues](https://github.com/FreeCAD/FreeCAD/issues), [discussions](https://github.com/FreeCAD/FreeCAD/discussions), [pull requests (PRs)](https://github.com/FreeCAD/FreeCAD/pulls). For addon or workbench bugs, search the **addon repo**, not core FreeCAD.
5. **Put it together** — Note whether the problem is a bug, a version change, a modeling mistake, or an addon limit. Cite every source you used.

Use web search with `site:wiki.freecad.org`, `site:forum.freecad.org`, and `site:github.com/FreeCAD` plus the exact error text when possible.

See [reference.md](reference.md) for a URL catalog and search query templates.

## Debugging checklist

Work through these in order when you diagnose a design problem:

```
Task progress:
- [ ] FreeCAD version and workbench identified
- [ ] Report view checked for errors (View → Panels → Report view)
- [ ] File → Recompute (Ctrl+R) after changes
- [ ] External links and SubShapeBinders inspected (right-click → Link tools)
- [ ] Dependency cycles ruled out (assembly ↔ part ↔ assembly)
- [ ] Correct workbench active (PartDesign vs Part vs Assembly)
- [ ] Addon scope confirmed (core vs third-party workbench)
- [ ] Reproduced in Safe Mode if a bug is suspected (Help → Safe Mode)
```

### Common failure patterns

| Symptom | First checks |
|---------|----------------|
| Part missing from Assembly Insert | Binder/link cycles; part not in `App::Part`; unsaved external file |
| Recompute failed / red features | Sketch constraints, missing references, tip not set |
| Binder shows broken link | Target moved or renamed; document path changed; copy-paste broke the external reference |
| PartDesign "tip" errors | Body tip not on the last feature; feature order is wrong |
| TechDraw missing geometry | Body not visible; wrong view source; outdated projection |
| FEM mesh or solve failure | Version change; material or boundary setup; check the forum for solver-specific threads |

### When `doqs/` is present: part container, master sketches, and Assembly Insert

When the machine repo includes a DOQS submodule, also read:

- `doqs/docs/decisions/2026-06-24_freecad-master-sketches-body.md`
- `doqs/docs/decisions/2026-10-01_part-container-on-top.md`

Key rule: master sketches must live in a dedicated `PartDesign::Body` with their own origin planes — not constrained to Assembly origin planes. That avoids circular document dependencies that block Insert.

Part container rule: when you create a new part, put a Part container (`App::Part`) at the top of the document. Put every `PartDesign::Body` inside it. In a build script, use `body(doc)` from `cad_build`. It returns a Body that is already inside the Part. If a Body sits outside a Part, the build stops and `validate_cad.py` fails. Assembly documents do not follow this rule. These are files under `cad/assemblies/` or files that hold an `Assembly::AssemblyObject`. They keep master sketches in a `Body_master` inside a plain group. See [`doqs/docs/decisions/2026-10-01_part-container-on-top.md`](https://github.com/refaqt/doqs/blob/main/docs/decisions/2026-10-01_part-container-on-top.md).

Visibility rule: a new part or assembly must open visible. `run()` in `cad_build` does this for you. If you create objects another way, for example through the FreeCAD connection, set `Visibility = True` on each new `App::Part`, `PartDesign::Body`, `Assembly::AssemblyObject` and `App::Link`, and on the `Tip` of each new Body. Keep the coordinate system hidden: the `Origin` and its axes, planes and point stay `Visibility = False`.

## Modelling a part from a supplier drawing

A model of a bought part is only useful if it matches the real part. A missing grease nipple or
screw head can hide a collision in the assembly. Follow these rules every time you model a part
from a catalogue, a datasheet, or a drawing.

1. **Make an inventory first.** Before you model, list every labelled dimension and every drawn
   feature: holes, threads, plugs, grease nipples, screw heads, reference edges, chamfers. Show the
   list to the user. Then model each item, or write next to it why you leave it out. Never leave
   out a feature that sticks out of the main shape.
2. **Know which values are exact.** A value in a table is exact. A value you read from a figure is
   an estimate. Before you scale anything from a figure, check that the figure is drawn to scale
   for this size: compare several dimensions in the same view that the table gives. Catalogues
   often draw one size for a whole range. Mark every estimate as an estimate in the build script
   and in your report. Make estimates of features that stick out a little too large, not too
   small. Ask the user to measure the real part.
3. **Use the same reference frame.** A model that replaces another model uses the same axes and the
   same origin. That includes which side is the reference side. If you do not know, ask before
   you model.
4. **Options are not the base shape.** A feature that a part-number suffix adds (for example a
   seal, a plug, or a second grease nipple) is a parameter. Keep it out of the base shape until
   the drawing and the supplier agree that it belongs there.
5. **Done means checked against reality.** "The values come from the datasheet" is not proof. The
   model is done only when you have:
   - rebuilt it from the build script, not edited it by hand;
   - measured it: the fingerprint (a short record of volume, area, bounding box, and face count),
     the bounding box, and a few slices (cuts through the part at known heights);
   - checked symmetry where the real part is symmetric;
   - compared it with the reference model or the real part;
   - shown the user a picture of it.

### FreeCAD jobs and files

- Never run two FreeCAD jobs with a graphical window at the same time.
- Use `FreeCADCmd` (FreeCAD without a window) to measure and to rebuild.
- A test must not change a model file. Do not open a model with `openDocument` in a test and then
  let anything save it. Open a copy, or close the document without saving.
- Compare the fingerprints with the saved ones before you commit. If a model changed and you did
  not mean to change it, stop and find out why.

## Response format

Structure every answer as:

```markdown
## Summary
[One sentence: what is going wrong]

## Likely cause
[Plain-language explanation for an intermediate user]

## What to try
1. [GUI step or model-tree change]
2. [Next step]
3. [Verification step]

## References
- [Page title](full URL) — what this source confirms
- [Forum thread or GitHub issue](full URL) — workaround or known bug status
```

Rules:

- Every factual claim about FreeCAD behavior must have a **References** entry with a full URL
- If no official source exists, say so and label the advice as inference
- Mention the user's FreeCAD version when behavior differs between releases
- Link to wiki pages by their actual titles, not bare domain names

### Example (abbreviated)

**User:** Part won't show in Assembly Insert panel; Binder to master sketch in assembly file.

**Response skeleton:**

## Summary
The part likely creates a circular link. The assembly also depends on geometry inside that part.

## Likely cause
Insert adds assembly → part. Your Binder adds part → assembly document. FreeCAD rejects that cycle.

## What to try
1. Open the part file → inspect SubShapeBinder target (should point at sketches inside `Body_master`, not Assembly origin planes).
2. In the assembly file, ensure master sketches live in `Body_master` per the DOQS architecture decision record (ADR) when `doqs/` is present.
3. Recompute both files, save, retry Insert.

## References
- [Assembly workbench](https://wiki.freecad.org/Assembly_Workbench) — Insert workflow
- [SubShapeBinder](https://wiki.freecad.org/FeatureSubShapeBinder) — external geometry links
- `doqs/docs/decisions/2026-06-24_freecad-master-sketches-body.md` — Binder cycle fix for DOQS assemblies (when `doqs/` submodule is present)

## Version awareness

FreeCAD version numbers are changing:

- Stable releases use semantic versioning style labels (for example **1.0**, **1.1**)
- From 2026, [calendar versioning (CalVer)](https://blog.freecad.org/2026/06/26/new-freecad-versioning-scheme-and-development-cycle/) (for example **26.3**, **27.1**) applies to new major releases
- Weekly or development builds may report `X.Ydev`. Behavior can differ from stable

Always match advice to the user's stated version. When you are unsure, ask and check [GitHub releases](https://github.com/FreeCAD/FreeCAD/releases).

## Additional resources

- [reference.md](reference.md) — official URLs, forum sections, GitHub targets, search templates
- [FreeCAD Manual](https://wiki.freecad.org/Manual:Introduction) — a linear beginner-to-intermediate guide
- [Python API](https://www.freecadweb.org/api/) — only when the user works with macros or scripting
