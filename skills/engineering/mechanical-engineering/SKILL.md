---
name: mechanical-engineering
description: >-
  Mechanical design, computer-aided design (CAD), design for manufacture
  (DfM), structures, mechanisms, and thermal design for open hardware
  machines and parts. Use for parts, assemblies, tolerances, materials, and
  manufacturing drawings. Do not use this skill for electrical work or
  control logic.
---
# Mechanical Engineering

Use this skill for physical structure, motion, and how easy the mechanical system is to manufacture.

## Scope

**Owns:**
- Concept and detailed mechanical design
- Computer-aided design (CAD) models, drawings, and mechanical lines in the parts list (BOM)
- Tolerance analysis and fit definitions
- Material selection (strength, environment, and food or medical limits if any)
- Design for manufacture (DfM) and design for assembly (DfA) for the chosen processes (machining, sheet metal, printing, molding)
- Packaging and mechanical safety guards (with `product-compliance`)
- Maintenance access and ease of service

**Does NOT own:**
- Electrical routing and electromagnetic compatibility (EMC) → `electrical-engineering`
- Sensor and actuator selection integration → `mechatronic-engineering`
- Production line layout → `production-engineering`
- Optical bench design → `optical-engineering`
- Full system requirements → `systems-engineering`

## Core principles

- **Open hardware documentation:** Publish editable source (STEP plus native CAD where policy allows), drawings, and a BOM with a clear license.
- **DfM early:** Cost and lead time come from the process choice. Involve `production-engineering` and `purchasing` before you lock the shape.
- **Safety by design:** Treat places that can pinch fingers (pinch points), emergency-stop (e-stop) reach, stability, and sharp edges as design inputs to `product-compliance` (Machinery Regulation / International Organization for Standardization (ISO) 12100 approach). This feeds European product conformity (CE) evidence.
- **Revision discipline:** Use part numbers, revision tables, and a change log. Align with `doqs-naming` in consumer repos.
- **Modularity:** Keep interfaces (mounting, space envelopes, couplings) stable across product variants.

## Key workflows

### Design review checklist

- [ ] Loads and boundary conditions documented
- [ ] Tolerances achievable at target process and volume
- [ ] Standard parts preferred over custom
- [ ] Service and assembly sequence (`production-engineering`)
- [ ] Mass, center of gravity (CG), and mounting loads
- [ ] Corrosion and environment rating
- [ ] Export control screening if applicable → `legal-advice`

### Release package

- Native CAD + STEP/STL as policy defines
- PDF drawings with title block, revision, material, finish
- BOM lines with manufacturer part number (MPN) or drawing number
- Assembly instructions outline

### DfM questions

| Process | Ask |
| --- | --- |
| Computer numerical control (CNC) | Setup count, tool access, thin walls |
| Sheet metal | Bend radius, hole edge distance |
| 3D print | Orientation, supports, strength that depends on print direction (anisotropy) |
| Injection mold | Draft angles, undercuts, tooling cost |

## Terminology and standards

- Geometric dimensioning and tolerancing (GD&T) per ISO 1101 / American Society of Mechanical Engineers (ASME) Y14.5 as the project standard
- ISO 12100 risk assessment inputs (not full compliance — `product-compliance`)
- Restriction of Hazardous Substances (RoHS) and Registration, Evaluation, Authorisation and Restriction of Chemicals (REACH) material declarations for purchased parts

## Cross-links

| Need | Skill |
| --- | --- |
| CAD tooling issues | `freecad` (consumer repos) |
| Motors, bearings integration | `mechatronic-engineering` |
| CE guards and fixtures | `product-compliance` |
| Costing | `finance`, `purchasing` |
| System envelopes | `systems-engineering` |

## Practical constraints

- Open CAD files let other people copy and change the design. Design clear, stable interfaces.
- A tolerance stack with optics or precision motion may need a joint review with `optical-engineering` / `mechatronic-engineering`.
- Weight and shipping affect `supply-chain-management` and `sales` quotes.
