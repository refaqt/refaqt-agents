---
name: software-development
description: >-
  Application, firmware, infrastructure, and tooling software for machines and
  processes. Use when designing, implementing, testing, or documenting code,
  CI/CD, APIs, or machine interfaces — defer mechanical/electrical design to
  engineering hardware skills.
---
# Software Development

Use this skill for code that runs on devices, servers, or developer machines in support of hardware and processes.

## Scope

**Owns:**
- Application and service architecture
- Firmware and embedded software (with `electrical-engineering` for MCU selection constraints)
- Machine interfaces (APIs, protocols, drivers, ROS/PLC bridges as applicable)
- Testing strategy (unit, integration, HIL where feasible)
- CI/CD, release tagging, changelogs
- Documentation for build, deploy, and API usage
- Open-source license compliance in software artifacts

**Does NOT own:**
- PCB design → `electrical-engineering`
- Motion/control PLC logic primary ownership → `industrial-automation`
- System-level requirements allocation → `systems-engineering`
- CE functional safety software evidence alone → coordinate `product-compliance`, `systems-engineering`
- Legal license interpretation → `legal-advice`

## Core principles

- **Reproducible builds:** Pin dependencies; document toolchain versions; CI matches local.
- **Hardware/software co-versioning:** Release artifacts reference compatible hardware revision (`mechanical-engineering`, `electrical-engineering`).
- **Open by default:** Prefer OSI-approved licenses aligned with cooperative policy; document third-party notices.
- **Safety-aware software:** Fail-safe defaults, interlocks, and explicit states for machine control; never bypass safety without `systems-engineering` and `product-compliance`.
- **Interoperability:** Prefer documented protocols and schemas; avoid gratuitous vendor lock-in.

## Key workflows

### Feature delivery

1. Requirement trace (link to `systems-engineering` or issue)
2. Design note or ADR for non-trivial changes
3. Implementation with tests
4. Update user/dev docs
5. Release notes with hardware compatibility matrix

### Machine interface checklist

- [ ] Protocol documented (bytes, timing, error handling)
- [ ] Simulation or mock for CI
- [ ] Timeouts and safe shutdown paths
- [ ] Version negotiation with firmware/hardware revision
- [ ] Logging suitable for field debug (no secrets in logs)

### Open-source release checklist

- [ ] LICENSE file and SPDX headers where used
- [ ] Third-party attribution (`NOTICE`)
- [ ] No committed secrets or customer data
- [ ] README: build, flash, test, supported platforms

## Terminology and standards

- Semantic versioning for software; coordinate with hardware rev naming (`doqs-naming` in consumer repos)
- MISRA / IEC 62304 — when medical or safety-related; scope with `product-compliance`
- OSHW stack: host tools + firmware + config repos

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

- Field updates on machines need rollback and compatibility gates.
- Cooperative contributors need good first issues and CONTRIBUTING.md — coordinate `open-source-community`.
- Long-running agents on factory floors: offline behavior and secure update channel.
