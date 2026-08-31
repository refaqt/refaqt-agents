---
name: systems-engineering
description: >-
  End-to-end requirements, architecture, verification, and integration for
  hardware-software machines and processes. Use when decomposing problems,
  defining interfaces, V&V strategy, or resolving cross-domain trade-offs.
---
# Systems Engineering

Use this skill to hold the whole system: requirements flow down, evidence flows up, interfaces stay coherent across domains.

## Scope

**Owns:**
- Stakeholder needs and system requirements (functional, performance, constraints)
- Architecture and interface control (ICDs, budgets: mass, power, thermal, cost)
- Trade studies and decision records
- Verification and validation planning (what evidence proves what)
- Integration sequencing and system test plans
- Configuration management across HW/SW/firmware revisions
- Risk register (technical) with mitigations

**Does NOT own:**
- Detailed domain design → respective engineering skills
- CE technical file authorship execution → `product-compliance` (close collaboration)
- Contractual requirements → `legal-advice`, `sales`
- Financial approval → `finance`, `sociocracy`
- Detailed SysML modeling mechanics → `sysml-v2` (this skill consumes/produces those artifacts)

## Core principles

- **Requirements are testable:** Every shall-statement maps to a verification method.
- **Interfaces are contracts:** Changing an ICD triggers impact analysis across teams.
- **Open system documentation:** System architecture descriptions and ICDs published where policy allows accelerate community contribution.
- **Safety integrated:** Hazard analysis inputs from ISO 12100 mindset early; hand off evidence to `product-compliance`.
- **Lifecycle thinking:** Manufacture, deploy, maintain, decommission — involve `production-engineering` and `supply-chain-management`.

## Key workflows

### Requirements flow

1. Capture need → analyze → allocate to subsystem
2. Non-functional: safety, EMC, environment, maintainability, security
3. Baseline with version; change control via ADRs or formal CRs

### V&V matrix (template)

| Req ID | Method (Test/Analysis/Inspection/Demo) | Owner skill | Evidence artifact |
| --- | --- | --- | --- |
| | | | |

### Integration milestones

- [ ] Interface mock-ups or bench rigs
- [ ] Subsystem qualification
- [ ] Full system FAT/SAT criteria defined with customer if applicable (`sales`)
- [ ] Regression suite for releases (`software-development`)

### Trade study

Document options, criteria weights, scores, sensitivity, recommendation — store in `docs/decisions/`.

## Terminology and standards

- INCOSE SE Handbook concepts
- ISO/IEC/IEEE 15288 lifecycle
- ISO 12100 risk assessment (input to safety)
- MBSE relationship → `sysml-v2`

## Cross-links

| Need | Skill |
| --- | --- |
| MBSE models | `sysml-v2` |
| Domain design | all engineering skills |
| CE evidence | `product-compliance` |
| Agile delivery cadence | `agile` |
| Business scope | `business-development` |

## Practical constraints

- Open hardware cooperatives still need a **system baseline** — chaos is not openness.
- Over-documenting slows small teams; right-size artifacts to risk and stage.
- Configuration drift between forked community designs and official releases must be visible in naming and docs.
