# DOQS naming examples

These examples show exact names. Copy the pattern. Do not change the spelling.

## Module paths

Use these folder names as written.

```
modules/x-axis/
modules/x-axis/modules/drive-belt/
modules/x-axis-belt/
modules/adapters/spindle-mount-v1-to-v2/
```

## BOM row

This bill of materials (BOM) row shows a valid `id` of `SW-001`.

```csv
SW-001,Limit Switch,"SPDT 5A lever",electrical,4,pc,3.20,18,SPDT-5A-LEVER,Omron,X20-1,,,,
```

## OKH fragment

Open Know-How (`okh.toml`) uses a version with no `v` prefix. The git tag in the release URL does use `v`.

```toml
version = "1.2.0"
release = "https://github.com/org/qarve/releases/tag/v1.2.0"

[[model]]
name = "500mm"

[[part]]
name = "Carriage Plate"
```

## Interface

Interface names and versions look like this.

```toml
[[provides-interface]]
name = "XAxisOutputInterface"
version = "1.0"
```

## Lockfile pin

The lockfile pin uses `v` on the version. That is different from `okh.toml`.

```toml
[[module]]
path = "modules/x-axis"
version = "v1.2.0"
```
