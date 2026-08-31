---
name: agile
description: >-
  Agile delivery for hardware-software teams — iterations, backlogs, discovery,
  and Done definitions that respect physical lead times. Use for sprint planning,
  retros, and cross-functional delivery — not statutory cooperative governance.
---
# Agile

Use this skill to deliver incrementally in environments where hardware lead times and certification constrain pure software agility.

## Scope

**Owns:**
- Backlog refinement and prioritization frameworks
- Sprint/iteration planning and reviews
- Definition of Ready / Definition of Done (cross-discipline)
- Retrospectives and continuous improvement
- Kanban/Scrumban flow for mixed HW/SW teams
- Discovery cadence with `business-development` and customers (`sales`)
- Risk buffers for long-lead items in roadmaps

**Does NOT own:**
- Circle policy and consent → `sociocracy`
- System requirements baseline → `systems-engineering`
- Legal release gates → `product-compliance`
- Financial budgeting → `finance`
- Detailed MBSE → `sysml-v2`

## Core principles

- **Hardware-aware agility:** Stories account for fab, assembly, and test time; avoid fantasy sprints.
- **Vertical slices when possible:** Prefer end-to-end thin slices (prototype subsystem) over siloed finishes.
- **Open work visible:** Issues and milestones public where cooperative policy allows.
- **Done means releasable:** Include docs, tests, compliance hooks in DoD.
- **WIP limits:** Especially costly for physical WIP inventory.

## Key workflows

### Definition of Done (cooperative hardware example)

- [ ] Code reviewed, CI green (`software-development`)
- [ ] HW rev documented and BOM updated
- [ ] User/docs updated
- [ ] Safety/regression checklist if applicable (`product-compliance` trigger)
- [ ] Log or release note entry (`log`)
- [ ] Known limitations communicated to `sales`/`marketing`

### Sprint planning checklist

- [ ] Capacity accounts for holidays and lab time
- [ ] Long-lead orders triggered (`purchasing`, `supply-chain-management`)
- [ ] Dependencies across circles acknowledged (`sociocracy`)
- [ ] Single sprint goal stated

### Retro prompts (hardware)

- What blocked us waiting on parts or tests?
- Where did open documentation help/hurt velocity?
- Are estimates improving for physical tasks?

## Terminology

- INVEST stories, spike, epic, increment
- Lead time vs cycle time (critical in HW)
- CFD (cumulative flow diagram) for Kanban

## Cross-links

| Need | Skill |
| --- | --- |
| Requirements | `systems-engineering` |
| Governance | `sociocracy` |
| Community contributors | `open-source-community` |
| Production handoff | `production-engineering` |

## Practical constraints

- Cannot "deploy" hardware daily — align release trains with inventory and CE baselines.
- Regulatory changes may freeze backlog items — communicate externally via `marketing`.
- Avoid agile jargon with shop floor; use visual boards and `production-engineering` language where needed.
