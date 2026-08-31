---
name: industrial-automation
description: >-
  PLCs, fieldbus, SCADA, safety PLCs, and industrial control integration for
  machines and processes. Use when designing ladder/ST logic, I/O maps, HMI,
  or factory connectivity — not general application software or mechanical design.
---
# Industrial Automation Engineering

Use this skill for industrial control systems on the plant floor: PLCs, safety controllers, fieldbuses, and operator interfaces.

## Scope

**Owns:**
- Control architecture (PLC, safety PLC, remote I/O)
- I/O mapping and signal conditioning requirements
- PLC programming (IEC 61131-3 languages), state machines, interlocks
- HMI/SCADA screens for operators (UX with operations input)
- Fieldbus selection (Profinet, EtherCAT, Modbus TCP, etc.)
- Commissioning procedures and backup/export of programs
- Integration with MES/ERP boundaries (document interfaces to `software-development`)

**Does NOT own:**
- Machine mechanical design → `mechanical-engineering`
- Custom PCB controllers → `electrical-engineering` (may overlap at embedded edge)
- Functional safety validation sign-off → `product-compliance`, `systems-engineering`
- IT cybersecurity policy → `software-development`, `legal-advice`
- Process chemistry or product formulation → domain experts / `systems-engineering`

## Core principles

- **Safety interlocks non-bypassable in production:** Development overrides clearly labeled and removed before shipment.
- **Deterministic behavior:** Document scan cycle assumptions, watchdogs, and fail-safe states.
- **Open documentation:** Export logic descriptions, I/O lists, and network diagrams suitable for community maintenance (respect safety secrets only where legally necessary).
- **Standardize tags:** Naming conventions aligned with `sysml-v2` or project standards for traceability.
- **Version control:** PLC projects in git where vendor allows; export artifacts for releases.

## Key workflows

### I/O and network design

1. Process I/O list (AI/AO/DI/DO, safety rated vs. standard)
2. Network topology and VLAN/separation if applicable
3. Power and grounding coordination with `electrical-engineering`
4. HMI alarm philosophy (priority, acknowledgement)

### Commissioning checklist

- [ ] Safe state on estop and communication loss verified
- [ ] Manual mode limits (speed, torque) enforced
- [ ] Simulation vs. field I/O documented
- [ ] Backup of PLC/HMI stored with release tag
- [ ] Operator training materials outline → `production-engineering`

### Safety integration

Coordinate with `product-compliance` for ISO 13849 / IEC 62061 performance levels; never claim PL/SIL without evidence.

## Terminology and standards

- IEC 61131-3, IEC 61131-2
- ISO 13849-1, IEC 62061 (functional safety)
- IEC 60204-1 machine electrical equipment

## Cross-links

| Need | Skill |
| --- | --- |
| Motion control detail | `mechatronic-engineering` |
| Embedded edge | `software-development`, `electrical-engineering` |
| System requirements | `systems-engineering` |
| Production rollout | `production-engineering` |
| CE machinery | `product-compliance` |

## Practical constraints

- Vendor lock-in is real — document migration paths for cooperative longevity.
- Legacy plants may forbid cloud egress; respect air-gap requirements.
- Open-sourcing ladder logic may expose process know-how — scope with `business-development` and `legal-advice`.
