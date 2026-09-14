---
name: industrial-automation
description: >-
  Programmable logic controllers (PLCs), industrial networks (fieldbus),
  plant monitoring (SCADA), safety PLCs, and industrial control integration
  for machines and processes. Use when you design ladder or Structured Text
  (ST) logic, input/output (I/O) maps, operator screens (HMI), or factory
  connectivity. Do not use this skill for general application software or
  mechanical design.
---
# Industrial Automation Engineering

Use this skill for industrial control systems on the factory floor: programmable logic controllers (PLCs), safety controllers, industrial networks (fieldbuses), and operator interfaces.

## Scope

**Owns:**
- Control architecture (PLC, safety PLC, remote input/output (I/O))
- I/O mapping and signal conditioning requirements
- PLC programming (International Electrotechnical Commission (IEC) 61131-3 languages), state machines, interlocks
- Human-machine interface (HMI) and supervisory control and data acquisition (SCADA) screens for operators (operator experience with input from operations)
- Fieldbus selection (Profinet, EtherCAT, Modbus TCP, and similar)
- Commissioning procedures (first start-up on site) and backup/export of programs
- Integration with manufacturing execution (MES) and enterprise resource planning (ERP) boundaries (document interfaces to `software-development`)

**Does NOT own:**
- Machine mechanical design → `mechanical-engineering`
- Custom printed circuit board (PCB) controllers → `electrical-engineering` (may overlap at embedded machine controllers)
- Functional safety validation sign-off → `product-compliance`, `systems-engineering`
- IT cybersecurity policy → `software-development`, `legal-advice`
- Process chemistry or product formulation → domain experts / `systems-engineering`

## Core principles

- **Safety interlocks stay active in production:** Label development overrides clearly. Remove them before shipment.
- **Predictable timing:** Document scan cycle assumptions, watchdog timers, and fail-safe states.
- **Open documentation:** Export logic descriptions, I/O lists, and network diagrams that the community can maintain. Keep safety secrets only where the law requires it.
- **Standardize signal names (tags):** Align naming with `sysml-v2` or project standards so you can trace requirements.
- **Version control:** Keep PLC projects in git where the vendor allows it. Export artifacts for releases.

## Key workflows

### I/O and network design

1. Process I/O list (analog in/out and digital in/out (AI/AO/DI/DO), safety rated vs. standard)
2. Network topology and virtual local area network (VLAN) separation if it applies
3. Power and grounding coordination with `electrical-engineering`
4. HMI alarm rules (priority, acknowledgement)

### Commissioning checklist

- [ ] Safe state on emergency stop (estop) and communication loss verified
- [ ] Manual mode limits (speed, torque) enforced
- [ ] Simulation vs. field I/O documented
- [ ] Backup of PLC/HMI stored with release tag
- [ ] Operator training materials outline → `production-engineering`

### Safety integration

Coordinate with `product-compliance` for International Organization for Standardization (ISO) 13849 / IEC 62061 performance levels. Never claim a performance level (PL) or safety integrity level (SIL) without evidence.

## Terminology and standards

- IEC 61131-3, IEC 61131-2
- ISO 13849-1, IEC 62061 (functional safety)
- IEC 60204-1 machine electrical equipment

## Cross-links

| Need | Skill |
| --- | --- |
| Motion control detail | `mechatronic-engineering` |
| Embedded machine controllers | `software-development`, `electrical-engineering` |
| System requirements | `systems-engineering` |
| Production rollout | `production-engineering` |
| European product conformity (CE) machinery | `product-compliance` |

## Practical constraints

- Vendor lock-in is a real risk. Document migration paths so the cooperative can last.
- Older plants may forbid sending data to the cloud (egress). Respect air-gap requirements (no network path out).
- Publishing ladder logic as open source may expose secret process knowledge. Set scope with `business-development` and `legal-advice`.
