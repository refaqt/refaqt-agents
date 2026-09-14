---
name: agile
description: >-
  Step-by-step delivery for hardware and software teams. Covers work lists
  (backlogs), short cycles (sprints), learning from customers, and a clear
  meaning of Done that respects real wait times for physical parts. Use for
  planning a work cycle, looking back on what happened (retro), and delivering
  across roles — not for legal cooperative governance.
---
# Agile

Use this skill to deliver work in small steps. Hardware wait times and certification limit how fast you can move. This is not the same as software-only speed.

Talk to the shop floor in plain words. Use visual boards and `production-engineering` language there. Do not use agile jargon with people on the floor.

## Scope

**Owns:**
- Keeping the work list (backlog) clear and putting the most important items first
- Planning and reviewing each work cycle (sprint or iteration)
- A shared "ready to start" list and a shared "done" list across roles (Definition of Ready / Definition of Done)
- Look-back meetings (retrospectives) and ongoing improvement
- A visual flow board for mixed hardware and software teams (Kanban or Scrumban)
- A regular discovery rhythm (cadence) with `business-development` and customers (`sales`)
- Extra time in the plan (risk buffers) for parts that take a long time to arrive

**Does NOT own:**
- Circle policy and consent → `sociocracy`
- The baseline of system requirements → `systems-engineering`
- Legal release gates → `product-compliance`
- Money budgets → `finance`
- Detailed model-based systems engineering (MBSE) → `sysml-v2`

## Core principles

- **Hardware-aware agility:** Work items must include fabrication (fab), assembly, and test time. Do not plan a cycle that ignores physical wait times.
- **Thin end-to-end slices when possible (vertical slices):** Prefer a thin slice that works from start to finish (for example a prototype subsystem). Do not finish one team's work while other teams wait.
- **Open work visible:** Keep issues and milestones public where cooperative policy allows.
- **Done means we can release:** Include docs, tests, and compliance checks in the shared "done" list.
- **Limit unfinished work:** Limit work in progress (WIP). Unfinished physical stock is especially expensive.

## Key workflows

### Definition of Done (cooperative hardware example)

- [ ] Code reviewed, automated checks pass (`software-development`)
- [ ] Hardware revision documented and bill of materials (BOM) updated
- [ ] User docs updated
- [ ] Safety and regression checklist if it applies (`product-compliance` trigger)
- [ ] Log or release note entry (`log`)
- [ ] Known limitations sent to `sales` / `marketing`

### Sprint planning checklist

- [ ] Capacity includes holidays and lab time
- [ ] Long-wait orders started (`purchasing`, `supply-chain-management`)
- [ ] Dependencies across circles noted (`sociocracy`)
- [ ] One goal for the cycle written down

### Retro prompts (hardware)

- What blocked us while we waited on parts or tests?
- Where did open documentation help or slow the work?
- Are estimates getting better for physical tasks?

## Terminology

Use these names with the team that already knows them. On the shop floor, use the everyday words.

- Work items that are independent, negotiable, valuable, estimable, small, and testable (INVEST). A short investigation (spike). A large theme (epic). A finished slice (increment).
- Wait time from order to arrival (lead time) versus time we spend working on an item (cycle time). Both matter in hardware.
- A chart of work in each stage over time (cumulative flow diagram, CFD) for a visual board (Kanban).

Work-list and cycle names you may see: backlog, sprint, iteration, Definition of Ready, Definition of Done, retrospective, Kanban, Scrumban.

## Cross-links

| Need | Skill |
| --- | --- |
| Requirements | `systems-engineering` |
| Governance | `sociocracy` |
| Community contributors | `open-source-community` |
| Production handoff | `production-engineering` |

## Practical constraints

- You cannot ship hardware every day. Line up each release batch with stock and the CE version you certified.
- A regulatory change can freeze work items. Tell the outside world through `marketing`.
- Do not use agile jargon with the shop floor. Use visual boards and `production-engineering` language there.
