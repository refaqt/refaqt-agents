---
name: product-compliance
description: >-
  Product regulatory compliance — EU CE marking, Machinery Regulation, LVD, EMC,
  RoHS, REACH, and conformity assessment planning. Use when determining applicable
  directives, technical files, labeling, and testing strategy — not general legal
  advice or jurisdiction-wide corporate law.
---
# Product Compliance (CE Marking & Conformity)

Use this skill when placing hardware (and integrated software) on markets that require conformity assessment — especially EU CE marking for machinery and electrical products.

**Skill name rationale:** `product-compliance` covers CE marking, machinery safety, EMC/LVD, material compliance, and related **product** regulations. It is narrower than all "regulatory compliance" (which includes GDPR, labor, etc.) and broader than "CE marking" alone.

## Scope

**Owns:**
- Determining applicable EU regulations/directives (Machinery Regulation/EU 2023/1230, EMC, LVD, RED, RoHS, REACH, etc.)
- Hazard and risk assessment inputs coordination (ISO 12100, ISO 13849, IEC 62061 as applicable)
- Conformity assessment route (self-declaration vs. notified body)
- Technical file structure and required evidence list
- Declaration of Conformity (DoC) content checklist — legal signing → `legal-advice`, `belgian-law`
- Labeling, manuals, and market language requirements (high level)
- Test plan (EMC, safety, functional) and lab engagement
- Post-market surveillance and change impact on conformity

**Does NOT own:**
- Drafting contracts or corporate statutes → `legal-advice`, jurisdiction skills
- Tax/import HS code filings → `belgian-fiscal-tax`
- Detailed electrical/mechanical design → engineering skills (this skill sets requirements)
- US FCC/UL strategy primary → coordinate `us-law` concepts; EU focus here
- Guaranteeing legal outcomes — flag when human notified body or counsel required

## Core principles

- **Start early:** Retrofit compliance is expensive; involve this skill at architecture phase (`systems-engineering`).
- **Evidence, not stickers:** CE marking follows a technical file, not a checklist sticker purchase.
- **Open hardware nuance:** Publishing designs does not exempt from placing product on market rules.
- **Integrated systems:** Machinery + control software + optional IoT — map all components in scope.
- **Cooperative duty of care:** Member and customer safety aligns with compliance; document seriously.

## Key workflows

### Applicability assessment

1. Product description and intended use
2. Markets (EU, UK, US, etc.) — defer non-EU detail to other skills
3. Directives/regulations list with rationale
4. Harmonized standards selection (presumption of conformity)
5. Notified body needed? (category dependent)

### Technical file checklist (EU machinery/electrical typical)

- [ ] Product description and drawings/BOM revisions
- [ ] Risk assessment (ISO 12100)
- [ ] Safety/control concept (ISO 13849 / IEC 62061 if applicable)
- [ ] Electrical schematics and LVD evidence
- [ ] EMC test reports
- [ ] Manuals and warnings (languages)
- [ ] DoC draft
- [ ] Post-market process

### Change control

Any BOM, firmware, or safety-relevant change triggers impact review before shipment.

## Terminology and references

- CE, DoC, Technical File, Notified Body
- EU Machinery Regulation (EU) 2023/1230 (transition from Machinery Directive 2006/42/EC — verify current applicability dates)
- EMC Directive 2014/30/EU, LVD 2014/35/EU, RoHS, REACH
- ISO 12100, ISO 13849-1, IEC 60204-1, IEC 61010 (product dependent)

## Cross-links

| Need | Skill |
| --- | --- |
| Design implementation | engineering skills |
| System hazards | `systems-engineering` |
| Contractual warranty vs. regulatory | `legal-advice` |
| EU regulatory context | `european-law` |
| Belgium-specific market surveillance | `belgian-law` |
| Sales/marketing claims | `sales`, `marketing` |
| Test budgeting | `finance` |

## Practical constraints

- DIY kits vs. finished machines may differ in obligations — document intended channel (`sales`).
- Open documentation may help **maintenance** compliance but not replace initial conformity.
- Subagents and agents **do not sign** DoCs — escalate to qualified human roles.
