---
name: sysml-v2
description: >-
  Model-based systems engineering with SysML v2.0 only (KerML-based language).
  Never SysML v1, UML profiles, blocks, BDD/IBD, or v1 stereotypes. Use when
  creating or interpreting SysML v2 textual/graphical models — not as a
  substitute for full systems engineering judgment or domain detailed design.
---
# SysML v2.0 (not SysML v1)

**This skill is SysML v2 only.** The language, metamodel, textual syntax, graphical
views, and vocabulary are SysML v2 (KerML foundation). They are not SysML v1,
not UML 2, and not a SysML v1 profile.

If a source, tool, or training example uses SysML v1, **do not copy it**. Translate
to SysML v2 before writing any model. If asked for “SysML” without a version, that
means **SysML v2**. If asked for SysML v1, refuse the v1 form and give the SysML v2
equivalent instead.

See [reference.md](reference.md) for the v1→v2 term map, forbidden constructs, and
canonical textual examples.

Use this skill when the project uses (or should use) SysML v2 models for system
truth, traceability, and collaboration across hardware and software.

## SysML v2 only — hard rules

- **Language:** SysML v2.0 as specified by OMG, built on **KerML**. Not UML, not
  SysML v1, not a UML profile.
- **Canonical form:** Text-serialized SysML v2 (`.sysml`). Graphical views are
  projections of that model, not UML diagrams.
- **Definition vs usage:** Model with `part def` / `part`, `requirement def` /
  `requirement`, `port def` / `port`, `action def` / `action`, and the rest of the
  SysML v2 definition/usage pattern. Never `block`, part properties, or v1
  stereotypes.
- **No v1 diagrams as the model:** Do not produce BDD, IBD, parametric diagrams,
  SysML v1 activity/state-machine diagrams, or stereotype-decorated UML as system
  truth.
- **No v1 serialization or tooling conventions:** No XMI-as-source, no UML
  profiles, no MagicDraw/Cameo v1 project idioms (`«block»`, flow ports, proxy
  ports, value properties, constraint blocks).
- **Unqualified “SysML” in this skill = SysML v2.** Do not mix v1 keywords,
  relationships, or diagram types into a v2 model.

## Scope

**Owns:**
- SysML v2 model structure (packages, definitions, usages)
- Requirements as SysML v2 model elements with trace links
- Structural decomposition (parts, ports, connections)
- Behavior modeling where appropriate (actions, states, flows)
- Viewpoints and views for audiences (operators, firmware, safety)
- Model versioning and export for tooling pipelines
- Mapping model elements to verification items (with `systems-engineering`)

**Does NOT own:**
- SysML v1 / UML-profile modeling (out of scope; convert to SysML v2)
- CAD or ECAD geometry → engineering skills
- PLC code → `industrial-automation`
- Legal requirements interpretation → `legal-advice`, `product-compliance`
- Replacing ADRs/decisions — models complement `docs/decisions/`

## Core principles

- **SysML v2 is the language:** Every artifact this skill produces is SysML v2
  (KerML-based). v1 syntax, definitions, and diagram types are defects, not
  alternatives.
- **Model is not bureaucracy:** Model elements must earn their keep in
  traceability or analysis.
- **Single source of truth:** Avoid duplicating requirements in issues and models
  without sync discipline.
- **Open artifacts:** Prefer text-serialized SysML v2 in git for diff/review in
  cooperative projects.
- **Tool-agnostic mindset:** SysML v2 standard over vendor lock-in; document
  toolchain pins. Do not treat a v1 tool’s dialect as the language.
- **Co-evolve with hardware/software:** Model revision aligns with system
  baseline (`systems-engineering`).

## Key workflows

### Model bootstrap

1. Define SysML v2 package hierarchy (context, requirements, architecture, V&V)
2. Import stakeholder needs as `requirement def` / `requirement` usages
3. Decompose the system with `part def` / `part`, ports, and connections (ICDs)
4. Link verification cases to requirements with SysML v2 `verify` / `satisfy`

### Change impact

When a requirement or interface changes:

1. Query trace links (dependents)
2. Notify owning skills via issues/log
3. Update views and regenerate docs if automated

### Review checklist

- [ ] Language is SysML v2 only (no v1 keywords, stereotypes, or diagram types)
- [ ] Definitions and usages used correctly (`def` vs usage)
- [ ] IDs stable and meaningful
- [ ] No orphan requirements
- [ ] Interfaces have units and constraints
- [ ] Safety-related reqs tagged for `product-compliance`
- [ ] Export readable for non-modelers (HTML/PDF/SysML v2 views)

## Terminology and standards

- **SysML v2.0 (OMG)** on **KerML** — this is the only SysML this skill uses
- SysML v2 constructs: `package`, `part def`/`part`, `item def`/`item`,
  `port def`/`port`, `connection`, `attribute`, `requirement def`/`requirement`,
  `action`, `state`, `constraint`, `view`/`viewpoint`
- Relationships in SysML v2 form: specialization `:>`, redefinition `:>>`,
  typing `:`, `satisfy`, `verify`, `allocate`, `connect`, `flow`
- INCOSE MBSE patterns expressed in SysML v2, not SysML v1

Do not use SysML v1 terms as if they were SysML v2: `block`, BDD, IBD, flow port,
proxy port, full port, value property, constraint block, `«stereotype»`, XMI,
UML profile. Map them via [reference.md](reference.md).

## Cross-links

| Need | Skill |
| --- | --- |
| SE process | `systems-engineering` |
| Implementation | domain engineering skills |
| Agile backlog sync | `agile` |
| Compliance evidence | `product-compliance` |

## Practical constraints

- SysML v2 tooling is still maturing — document known limitations. Do not fall
  back to SysML v1 because a v2 tool is incomplete; subset the v2 model instead.
- Small teams may model only critical subsystems; don't mandate full-V model day one.
- Community contributors need generated views; raw KerML alone may be insufficient.
