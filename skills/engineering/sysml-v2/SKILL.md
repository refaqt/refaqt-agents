---
name: sysml-v2
description: >-
  Model-based systems engineering with SysML v2.0 only (built on the Kernel
  Modeling Language, KerML). Never SysML v1, Unified Modeling Language (UML)
  profiles, blocks, block definition diagrams (BDD), internal block diagrams
  (IBD), or v1 UML tags (stereotypes). Use when you create or read SysML v2
  text or graphical models. Do not use this skill in place of full systems
  engineering judgment or detailed domain design.
---
# SysML v2.0 (not SysML v1)

**This skill is SysML v2 only.** The language is SysML v2. The language structure (metamodel), text form, graphical views, and vocabulary are SysML v2. SysML v2 is built on KerML (Kernel Modeling Language). They are not SysML v1. They are not Unified Modeling Language (UML) 2. They are not a SysML v1 profile.

If a source, tool, or training example uses SysML v1, **do not copy it**. Translate to SysML v2 before you write any model. If someone asks for “SysML” without a version, that means **SysML v2**. If someone asks for SysML v1, refuse the v1 form and give the SysML v2 equivalent instead.

See [reference.md](reference.md) for the v1→v2 term map, forbidden constructs, and standard textual examples.

Use this skill when the project uses (or should use) SysML v2 models as the official system description. Use them for trace links and for work across hardware and software.

## SysML v2 only — hard rules

- **Language:** SysML v2.0 as specified by the Object Management Group (OMG), built on **KerML** (Kernel Modeling Language). Not UML, not SysML v1, not a UML profile.
- **Required source form:** Text-serialized SysML v2 (`.sysml`). Graphical views are views of that model, not UML diagrams.
- **Definition vs usage:** Model with `part def` / `part`, `requirement def` / `requirement`, `port def` / `port`, `action def` / `action`, and the rest of the SysML v2 definition/usage pattern. Never `block`, part properties, or v1 stereotypes.
- **No v1 diagrams as the model:** Do not produce block definition diagrams (BDD), internal block diagrams (IBD), parametric diagrams, SysML v1 activity/state-machine diagrams, or UML with stereotypes as system truth.
- **No v1 file format or tooling conventions:** No XML Metadata Interchange (XMI) as the source of the model. No UML profiles. No MagicDraw/Cameo v1 project conventions (`«block»`, flow ports, proxy ports, value properties, constraint blocks).
- **When this skill says “SysML” with no version, it means SysML v2.** Do not mix v1 keywords, relationships, or diagram types into a v2 model.

## Scope

**Owns:**
- SysML v2 model structure (packages, definitions, usages)
- Requirements as SysML v2 model elements with trace links
- Breaking the system into parts, ports, and connections
- Behavior modeling where appropriate (actions, states, flows)
- Viewpoints and views for audiences (operators, firmware, safety)
- Model versioning and export for tooling pipelines
- Mapping model elements to verification items (with `systems-engineering`)

**Does NOT own:**
- SysML v1 / UML-profile modeling (out of scope; convert to SysML v2)
- Computer-aided design (CAD) or electronics CAD (ECAD) geometry → engineering skills
- Programmable logic controller (PLC) code → `industrial-automation`
- Legal requirements interpretation → `legal-advice`, `product-compliance`
- Replacing architecture decision records (ADRs) and decisions — models complement `docs/decisions/`

## Core principles

- **SysML v2 is the language:** Every artifact this skill produces is SysML v2 (KerML-based). v1 syntax, definitions, and diagram types are defects, not alternatives.
- **Model is not paperwork:** Each model element must help with traceability or analysis.
- **Single source of truth:** Do not copy requirements into issues and models unless you keep them in sync.
- **Open artifacts:** Prefer text-serialized SysML v2 in git so cooperative projects can compare changes (diff) and review.
- **Do not depend on one tool:** Follow the SysML v2 standard. Do not lock the project to one vendor. Record toolchain versions. Do not treat a v1 tool’s local variant as the language.
- **Change with hardware and software:** Model revision aligns with the system baseline (`systems-engineering`).

## Key workflows

### Start the model

1. Define SysML v2 package hierarchy (context, requirements, architecture, verification and validation (V&V))
2. Import needs of the people involved (stakeholders) as `requirement def` / `requirement` usages
3. Split the system with `part def` / `part`, ports, and connections (interface control documents (ICDs))
4. Link verification cases to requirements with SysML v2 `verify` / `satisfy`

### Change impact

When a requirement or interface changes:

1. Query trace links (elements that depend on the change)
2. Notify owning skills via issues/log
3. Update views and regenerate docs if automated

### Review checklist

- [ ] Language is SysML v2 only (no v1 keywords, stereotypes, or diagram types)
- [ ] Definitions and usages used correctly (`def` vs usage)
- [ ] IDs stable and meaningful
- [ ] No requirements with no links (orphan requirements)
- [ ] Interfaces have units and constraints
- [ ] Safety-related requirements tagged for `product-compliance`
- [ ] Export readable for people who do not use the modeling tool (HTML/PDF/SysML v2 views)

## Terminology and standards

- **SysML v2.0 (OMG)** on **KerML** — this is the only SysML this skill uses
- SysML v2 constructs: `package`, `part def`/`part`, `item def`/`item`,
  `port def`/`port`, `connection`, `attribute`, `requirement def`/`requirement`,
  `action`, `state`, `constraint`, `view`/`viewpoint`
- Relationships in SysML v2 form: specialization `:>`, redefinition `:>>`,
  typing `:`, `satisfy`, `verify`, `allocate`, `connect`, `flow`
- International Council on Systems Engineering (INCOSE) model-based systems engineering (MBSE) patterns expressed in SysML v2, not SysML v1

Do not use SysML v1 terms as if they were SysML v2: `block`, BDD, IBD, flow port,
proxy port, full port, value property, constraint block, `«stereotype»`, XMI,
UML profile. Map them via [reference.md](reference.md).

## Cross-links

| Need | Skill |
| --- | --- |
| Systems engineering process | `systems-engineering` |
| Implementation | domain engineering skills |
| Agile backlog sync | `agile` |
| Compliance evidence | `product-compliance` |

## Practical constraints

- SysML v2 tooling is still new and incomplete. Record known limits. Do not switch to SysML v1 because a v2 tool is incomplete. Use a smaller SysML v2 model instead.
- Small teams may model only critical subsystems. Do not require a full model on the first day.
- Community contributors need generated views. Raw KerML alone may not be enough.
