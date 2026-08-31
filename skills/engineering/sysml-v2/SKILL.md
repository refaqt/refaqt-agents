---
name: sysml-v2
description: >-
  Model-based systems engineering with SysML v2.0 — requirements, structure,
  behavior, and analysis in textual/kerml/sysml form. Use when creating or
  interpreting MBSE models, not as a substitute for full systems engineering
  judgment or domain detailed design.
---
# SysML v2.0

Use this skill when the project uses (or should use) SysML v2 models for system truth, traceability, and collaboration across hardware and software.

## Scope

**Owns:**
- SysML v2 model structure (packages, definitions, usages)
- Requirements as model elements with trace links
- Structural decomposition (parts, ports, connections)
- Behavior modeling where appropriate (actions, states, flows)
- Viewpoints and views for audiences (operators, firmware, safety)
- Model versioning and export for tooling pipelines
- Mapping model elements to verification items (with `systems-engineering`)

**Does NOT own:**
- CAD or ECAD geometry → engineering skills
- PLC code → `industrial-automation`
- Legal requirements interpretation → `legal-advice`, `product-compliance`
- Replacing ADRs/decisions — models complement `docs/decisions/`

## Core principles

- **Model is not bureaucracy:** Model elements must earn their keep in traceability or analysis.
- **Single source of truth:** Avoid duplicating requirements in issues and models without sync discipline.
- **Open artifacts:** Prefer text-serialized SysML v2 in git for diff/review in cooperative projects.
- **Tool-agnostic mindset:** SysML v2 standard over vendor lock-in; document toolchain pins.
- **Co-evolve with hardware/software:** Model revision aligns with system baseline (`systems-engineering`).

## Key workflows

### Model bootstrap

1. Define package hierarchy (context, requirements, architecture, V&V)
2. Import stakeholder needs as requirement definitions
3. Decompose system into parts with ports and ICDs
4. Link verification cases to requirements

### Change impact

When a requirement or interface changes:

1. Query trace links (dependents)
2. Notify owning skills via issues/log
3. Update views and regenerate docs if automated

### Review checklist

- [ ] IDs stable and meaningful
- [ ] No orphan requirements
- [ ] Interfaces have units and constraints
- [ ] Safety-related reqs tagged for `product-compliance`
- [ ] Export readable for non-modelers (HTML/PDF/diagrams)

## Terminology and standards

- SysML v2 (OMG), KerML foundation
- requirement def/usage, part def/usage, connection, action, state
- INCOSE MBSE patterns

## Cross-links

| Need | Skill |
| --- | --- |
| SE process | `systems-engineering` |
| Implementation | domain engineering skills |
| Agile backlog sync | `agile` |
| Compliance evidence | `product-compliance` |

## Practical constraints

- SysML v2 tooling is still maturing — document known limitations.
- Small teams may model only critical subsystems; don't mandate full-V model day one.
- Community contributors need generated views; raw KerML alone may be insufficient.
