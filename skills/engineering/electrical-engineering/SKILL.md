---
name: electrical-engineering
description: >-
  Schematics, printed circuit board (PCB) layout, power, clean signals
  (signal integrity), electromagnetic compatibility (EMC), and electrical
  safety design for open hardware. Use for circuits, electrical lines in
  the parts list (BOM), and test. Do not use this skill as the main owner
  of mechanical enclosures or programmable logic controller (PLC)
  programming.
---
# Electrical Engineering

Use this skill for electrical work: power distribution, sensing, actuation electronics, and printed circuit board (PCB) design.

## Scope

**Owns:**
- Architecture (power budgets, domains, electrical isolation)
- Schematic capture and PCB layout
- Component selection (use parts below max rating (derating), availability, how long the part stays in production)
- Clean signals (signal integrity) and basic electromagnetic compatibility (EMC) design practices
- Electrical test plans (first power-on (bring-up), functional tests, and high-potential insulation tests (hi-pot) where required)
- Design files for fabrication (Gerber files, pick-and-place files, parts list (BOM))
- Electrical safety concepts (isolation, fusing, earthing) — evidence package with `product-compliance`

**Does NOT own:**
- Enclosure thermal and mechanical design → `mechanical-engineering`
- Motor control algorithms and industrial networks (fieldbus) → `industrial-automation`, `mechatronic-engineering`
- Firmware → `software-development`
- Low Voltage Directive (LVD) / EMC certification test execution → `product-compliance`
- Legal product liability → `legal-advice`

## Core principles

- **Design for supply chain:** Prefer resistors, capacitors, and other passives that more than one vendor can supply. Flag parts that are not recommended for new designs (NRND) to `purchasing` and `supply-chain-management`.
- **Open hardware releases:** Publish schematics, board files, and the BOM under the project license. Document programming and debug interfaces.
- **Safety first:** Review mains, isolation, and energy storage designs before you power a prototype. Follow relevant International Electrotechnical Commission (IEC) standards as design guides.
- **EMC awareness:** Grounding, filtering, and layout practices reduce retest cost.
- **Testability:** Add test points and Joint Test Action Group (JTAG) / Serial Wire Debug (SWD) access. Use boundary scan when it is justified.

## Key workflows

### Schematic review

- [ ] Power tree and sequencing
- [ ] Protection (fuse, transient voltage suppressor (TVS), reverse polarity)
- [ ] Isolation barriers rated for working voltage
- [ ] Connector pinout documented and keyed so it cannot plug in the wrong way
- [ ] Electrostatic discharge (ESD) on external interfaces
- [ ] Design rule checklist for the target fabrication shop (fab)

### PCB release

- Gerber files, drill, layer stackup, impedance notes
- Pick-and-place files and BOM with manufacturer part number (MPN) and alternate parts
- Assembly drawing notes (reflow profile, no-wash, and similar)
- Revision matches firmware hardware ID

### First power-on (bring-up) protocol

1. Visual inspection
2. Resistance checks before power
3. Current-limited first power
4. Voltage rail verification
5. Program and basic functional test with `software-development`

## Terminology and standards

- IEC 60204-1 (machinery electrical equipment — design input)
- IEC 61010 / 62368 (depends on product category — confirm with `product-compliance`)
- International Special Committee on Radio Interference (CISPR) 32/11 EMC (design targets)
- IPC-2221, IPC-A-610 electronics assembly quality

## Cross-links

| Need | Skill |
| --- | --- |
| European product conformity (CE) / LVD / EMC | `product-compliance` |
| Cabling in machine | `mechanical-engineering`, `industrial-automation` |
| Sensors/actuators | `mechatronic-engineering` |
| Production test fixtures | `production-engineering` |
| Optoelectronics | `optical-engineering` |

## Practical constraints

- Chip shortages: design alternate parts in the schematic, not only in notes.
- Mains-connected open hardware creates more compliance work. Involve `product-compliance` early.
- Cooperative repos: clarify patent and grant clauses in hardware licenses with `legal-advice` when you mix GNU General Public License (GPL) software and hardware docs.
