---
name: systems-engineering
description: >-
  End-to-end requirements, architecture, verification, and integration for
  hardware-software machines and processes. Use when you split problems,
  define interfaces, plan verification and validation (V&V), or resolve
  trade-offs across domains.
---
# Systems Engineering

Use this skill to manage the whole system. Requirements go from the system to the parts. Evidence goes from the parts back to the system. Interfaces stay consistent across domains.

## Scope

**Owns:**
- Needs of the people involved (stakeholders) and system requirements (functional, performance, constraints)
- Architecture and interface control (interface control documents (ICDs); budgets for mass, power, thermal, cost)
- Trade studies and decision records
- Verification and validation (V&V) planning (what evidence proves what)
- Integration sequencing and system test plans
- Configuration management across hardware (HW), software (SW), and firmware revisions
- Risk list (register) for technical risks, with actions that reduce risk

**Does NOT own:**
- Detailed domain design → respective engineering skills
- European product conformity (CE) technical file authorship execution → `product-compliance` (close collaboration)
- Contractual requirements → `legal-advice`, `sales`
- Financial approval → `finance`, `sociocracy`
- Detailed SysML v2 modeling mechanics → `sysml-v2` (this skill consumes and produces those artifacts; never SysML v1)

## Core principles

- **Requirements are testable:** Every requirement that says "shall" maps to a verification method.
- **Interfaces are contracts:** Changing an ICD triggers impact analysis across teams.
- **Open system documentation:** Publish system architecture descriptions and ICDs where policy allows. That speeds community contribution.
- **Safety integrated:** Bring hazard analysis inputs from an International Organization for Standardization (ISO) 12100 approach early. Hand off evidence to `product-compliance`.
- **Lifecycle thinking:** Cover manufacture, deploy, maintain, and taking the product out of service. Involve `production-engineering` and `supply-chain-management`.

## Key workflows

### Requirements flow

1. Capture need → analyze → allocate to subsystem
2. Quality and constraint requirements (non-functional): safety, electromagnetic compatibility (EMC), environment, maintainability, security
3. Baseline with version. Change control via architecture decision records (ADRs) or formal change requests (CRs)

### V&V matrix (template)

| Req ID | Method (Test/Analysis/Inspection/Demo) | Owner skill | Evidence artifact |
| --- | --- | --- | --- |
| | | | |

### Integration milestones

- [ ] Interface mock-ups or bench rigs
- [ ] Subsystem qualification
- [ ] Full system factory acceptance test (FAT) / site acceptance test (SAT) criteria defined with customer if applicable (`sales`)
- [ ] Repeat-test suite for releases (`software-development`)

### Trade study

Document options, criteria weights, scores, sensitivity, and recommendation. Store in `docs/decisions/`.

## Terminology and standards

- International Council on Systems Engineering (INCOSE) Systems Engineering Handbook concepts
- ISO / International Electrotechnical Commission (IEC) / Institute of Electrical and Electronics Engineers (IEEE) 15288 lifecycle
- ISO 12100 risk assessment (input to safety)
- Model-based systems engineering (MBSE) relationship → SysML v2 only (`sysml-v2`; not SysML v1)

## Cross-links

| Need | Skill |
| --- | --- |
| MBSE models | `sysml-v2` |
| Domain design | all engineering skills |
| CE evidence | `product-compliance` |
| Agile delivery cadence | `agile` |
| Business scope | `business-development` |

## Practical constraints

- Open hardware cooperatives still need a **system baseline**. Uncontrolled change is not openness.
- Too much documentation slows a small team. Match the artifacts to the risk and the project stage.
- When community copies (forks) differ from official releases, show that difference in names and docs.
