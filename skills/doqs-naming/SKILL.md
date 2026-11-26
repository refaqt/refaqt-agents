---
name: doqs-naming
description: >-
  Use when you create or rename DOQS modules, bill of materials (BOM) rows, parts, adapters, okh.toml versions or release tags. Gives the naming rules and the check command.
---

# DOQS naming and validation

## When to use

- New or renamed folders under `modules/`
- Bill of materials (BOM) `id` / `name` rows or `bom/bom.csv` headers
- `[[part]]`, `[[model]]`, or adapter paths
- Release tagging and Open Know-How (`okh.toml`) `version` bumps
- Exported drawings (title block revision)

## Rules (summary)

Read the official spec:

- `doqs/docs/naming.md`
- `doqs/docs/naming-lexicon.md`

Quick reference (kebab-case means lowercase words with hyphens; semver means semantic versioning, major.minor.patch):

| Item | Rule |
|------|------|
| Module folder | kebab-case function: `x-axis`, `drive-belt` |
| Adapter | `modules/adapters/<from>-to-<to>/` |
| BOM `id` | `PREFIX-NNN` per module (e.g. `MEC-001`) |
| `okh.toml` version | semver without `v`: `1.2.0` |
| Git tag | `v1.2.0` |
| FreeCAD `Comment` | `Module: <slug> — see okh.toml` (no per-release bump) |
| Drawing export | Title block `Rev: <semver>` at export time |

## Mandatory validation

From the **machine repository root** after Open Know-How (OKH), bill of materials (BOM), or path changes:

```bash
./doqs.sh check
```

On Windows, use `doqs.bat check`.

Before tagging:

```bash
./doqs.sh check --expected-version X.Y.Z
```

On existing machines, adopt the names step by step. `./doqs.sh check` reports names that do not follow the rules yet.

## Do not

- Put dimensions or materials in module folder names
- Use `v` prefix in `okh.toml` `version`
- Bump FreeCAD file metadata on every patch release
- Duplicate BOM `id` within one module BOM file

See [reference.md](reference.md) for examples.
