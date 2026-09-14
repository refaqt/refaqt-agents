---
name: software-development
description: >-
  Application, firmware, infrastructure, and tooling software for machines and
  processes. Use when you design, write, test, or document code, automated
  build and release (CI/CD), programming interfaces (APIs), or machine
  interfaces. Send mechanical and electrical design to the hardware
  engineering skills.
---
# Software Development

Use this skill for code that runs on devices, servers, or developer computers. The code supports hardware and processes.

## Scope

**Owns:**
- Application and service architecture
- Firmware and embedded software (with `electrical-engineering` for microcontroller chip (MCU) selection limits)
- Machine interfaces (application programming interfaces (APIs), protocols, drivers, and Robot Operating System (ROS) or programmable logic controller (PLC) bridges when they apply)
- Testing strategy (unit tests, integration tests, and hardware-in-the-loop (HIL) tests when they are practical)
- Continuous integration and delivery (CI/CD), release tags, and changelogs
- Documentation for build, deploy, and API use
- Open-source license checks on software files

**Does NOT own:**
- Printed circuit board (PCB) design → `electrical-engineering`
- Motion and control PLC logic as the main owner → `industrial-automation`
- System-level requirements allocation → `systems-engineering`
- European product conformity (CE) functional safety software evidence on its own → coordinate `product-compliance`, `systems-engineering`
- Legal license interpretation → `legal-advice`

## Core principles

- **Reproducible builds:** Lock dependency versions. Record toolchain versions. Make continuous integration (CI) match the local build.
- **Hardware and software version together:** Release files must name the compatible hardware revision (`mechanical-engineering`, `electrical-engineering`).
- **Prefer open licenses:** Use Open Source Initiative (OSI) approved licenses that match cooperative policy. Record third-party notices.
- **Safety-aware software:** Use safe defaults if something fails (fail-safe). Use interlocks and explicit states for machine control. Never skip safety without `systems-engineering` and `product-compliance`.
- **Work with other systems:** Prefer documented protocols and schemas. Do not lock the project to one vendor without a strong reason.

## Key workflows

### Feature delivery

1. Requirement trace (link to `systems-engineering` or an issue)
2. Design note or architecture decision record (ADR) for changes that are not small
3. Implementation with tests
4. Update user and developer docs
5. Release notes with a hardware compatibility matrix

### Machine interface checklist

- [ ] Protocol documented (bytes, timing, error handling)
- [ ] Simulation or mock for CI
- [ ] Timeouts and safe shutdown paths
- [ ] Version negotiation with firmware and hardware revision
- [ ] Logging suitable for field debug (no secrets in logs)

### Open-source release checklist

- [ ] LICENSE file and Software Package Data Exchange (SPDX) headers where used
- [ ] Third-party attribution (`NOTICE`)
- [ ] No committed secrets or customer data
- [ ] README: build, flash, test, supported platforms

## Terminology and standards

- Semantic versioning for software (version numbers like 1.2.3). Coordinate with hardware revision naming (`doqs-naming` in consumer repos).
- MISRA coding rules / International Electrotechnical Commission (IEC) 62304 — when the work is medical or safety-related. Set scope with `product-compliance`.
- Open-source hardware (OSHW) stack: host tools + firmware + config repos

## Cross-links

| Need | Skill |
| --- | --- |
| Requirements | `systems-engineering`, `sysml-v2` |
| Real-time control | `industrial-automation`, `mechatronic-engineering` |
| Optics pipelines | `optical-engineering` |
| Production flashing | `production-engineering` |
| Web3 interfaces | `web3-blockchain` |
| Patterns in repo | `maintain-patterns` |

## Practical constraints

- Field updates on machines need rollback and compatibility checks before you allow an update.
- Cooperative contributors need easy starter tasks and CONTRIBUTING.md — coordinate `open-source-community`.
- Long-running agents on factory floors need offline behavior and a secure update channel.
