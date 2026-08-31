---
name: electrical-engineering
description: >-
  Schematics, PCB layout, power, signal integrity, EMC, and electrical safety
  design for open hardware. Use for circuits, BOM electrical lines, and test —
  not mechanical enclosures or PLC programming primary ownership.
---
# Electrical Engineering

Use this skill for electrons: power distribution, sensing, actuation electronics, and PCB design.

## Scope

**Owns:**
- Architecture (power budgets, domains, isolation)
- Schematic capture and PCB layout
- Component selection (derating, availability, lifecycle)
- Signal integrity and basic EMC design practices
- Electrical test plans (bring-up, functional, hi-pot where required)
- Design files for fabrication (Gerbers, pick-place, BOM)
- Electrical safety concepts (isolation, fusing, earthing) — evidence package with `product-compliance`

**Does NOT own:**
- Enclosure thermal/mechanical → `mechanical-engineering`
- Motor control algorithms and fieldbus → `industrial-automation`, `mechatronic-engineering`
- Firmware → `software-development`
- LVD/EMC certification testing execution → `product-compliance`
- Legal product liability → `legal-advice`

## Core principles

- **Design for supply chain:** Prefer multi-source passives; flag NRND parts to `purchasing` and `supply-chain-management`.
- **Open hardware releases:** Publish schematics, board files, and BOM under project license; document programming/debug interfaces.
- **Safety first:** Mains, isolation, and energy storage designs reviewed before prototype power-on; follow relevant IEC standards as design guides.
- **EMC awareness:** Grounding, filtering, and layout practices reduce retest cost.
- **Testability:** Test points, JTAG/SWD, boundary scan where justified.

## Key workflows

### Schematic review

- [ ] Power tree and sequencing
- [ ] Protection (fuse, TVS, reverse polarity)
- [ ] Isolation barriers rated for working voltage
- [ ] Connector pinout documented and keyed
- [ ] ESD on external interfaces
- [ ] Design rule checklist for target fab

### PCB release

- Gerbers, drill, stackup, impedance notes
- Pick-place and BOM with MPN and alternates
- Assembly drawing notes (reflow profile, no-wash, etc.)
- Revision matches firmware hardware ID

### Bring-up protocol

1. Visual inspection
2. Resistance checks before power
3. Current-limited first power
4. Rail verification
5. Program and smoke test with `software-development`

## Terminology and standards

- IEC 60204-1 (machinery electrical equipment — design input)
- IEC 61010 / 62368 (product category dependent — confirm with `product-compliance`)
- CISPR 32/11 EMC (design targets)
- IPC-2221, IPC-A-610 assembly quality

## Cross-links

| Need | Skill |
| --- | --- |
| CE/LVD/EMC | `product-compliance` |
| Cabling in machine | `mechanical-engineering`, `industrial-automation` |
| Sensors/actuators | `mechatronic-engineering` |
| Production test fixtures | `production-engineering` |
| Optoelectronics | `optical-engineering` |

## Practical constraints

- Chip shortages: design alternates in schematic, not only notes.
- Mains-connected open hardware increases compliance burden — early `product-compliance` engagement.
- Cooperative repos: clarify patent/grant clauses in hardware licenses with `legal-advice` when mixing GPL software and hardware docs.
