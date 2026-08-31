---
name: mechanical-engineering
description: >-
  Mechanical design, CAD, DfM, structures, mechanisms, and thermal design for
  open hardware machines and components. Use for parts, assemblies, tolerancing,
  materials, and manufacturing drawings — not electrical or control logic.
---
# Mechanical Engineering

Use this skill for physical structure, motion, and manufacturability of mechanical systems.

## Scope

**Owns:**
- Concept and detailed mechanical design
- CAD models, drawings, BOM mechanical lines
- Tolerance analysis and fit definitions
- Material selection (strength, environment, food/medical constraints if any)
- DfM/DfA for chosen processes ( machining, sheet metal, printing, molding)
- Packaging and mechanical safety guards (with `product-compliance`)
- Maintenance access and serviceability

**Does NOT own:**
- Electrical routing and EMC → `electrical-engineering`
- Sensor/actuator selection integration → `mechatronic-engineering`
- Production line layout → `production-engineering`
- Optical bench design → `optical-engineering`
- Full system requirements → `systems-engineering`

## Core principles

- **Open hardware documentation:** Publish editable source (STEP + native CAD where policy allows), drawings, and BOM with clear license.
- **DfM early:** Cost and lead time driven by process choice; engage `production-engineering` and `purchasing` before locking geometry.
- **Safety by design:** Pinch points, e-stop reach, stability, sharp edges — input to `product-compliance` (Machinery Regulation / ISO 12100 mindset).
- **Revision discipline:** Part numbers, revision tables, change log; align with `doqs-naming` in consumer repos.
- **Modularity:** Interfaces (mounting, envelopes, couplings) stable across product variants.

## Key workflows

### Design review checklist

- [ ] Loads and boundary conditions documented
- [ ] Tolerances achievable at target process and volume
- [ ] Standard parts preferred over custom
- [ ] Service and assembly sequence (`production-engineering`)
- [ ] Mass, CG, and mounting loads
- [ ] Corrosion and environment rating
- [ ] Export control screening if applicable → `legal-advice`

### Release package

- Native CAD + STEP/STL as policy defines
- PDF drawings with title block, revision, material, finish
- BOM lines with MPN or drawing number
- Assembly instructions outline

### DfM questions

| Process | Ask |
| --- | --- |
| CNC | Setup count, tool access, thin walls |
| Sheet metal | Bend radius, hole edge distance |
| 3D print | Orientation, supports, anisotropy |
| Injection mold | Draft, undercuts, tooling cost |

## Terminology and standards

- GD&T per ISO 1101 / ASME Y14.5 as project standard
- ISO 12100 risk assessment inputs (not full compliance — `product-compliance`)
- RoHS/REACH material declarations for purchased parts

## Cross-links

| Need | Skill |
| --- | --- |
| CAD tooling issues | `freecad` (consumer repos) |
| Motors, bearings integration | `mechatronic-engineering` |
| CE guards/fixtures | `product-compliance` |
| Costing | `finance`, `purchasing` |
| System envelopes | `systems-engineering` |

## Practical constraints

- Open publication of CAD enables forks — design for clarity and robust interfaces.
- Tolerance stack with optics or precision motion may require `optical-engineering` / `mechatronic-engineering` joint review.
- Weight and shipping affect `supply-chain-management` and `sales` quotes.
