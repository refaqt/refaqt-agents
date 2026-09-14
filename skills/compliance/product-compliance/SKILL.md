---
name: product-compliance
description: >-
  Product rules for hardware — EU CE marking, Machinery Regulation, Low Voltage
  Directive (LVD), electromagnetic compatibility (EMC), Restriction of Hazardous
  Substances (RoHS), EU chemical rules (REACH), and a plan for conformity checks.
  Use when you decide which directives apply, what goes in the technical file,
  labeling, and a test plan — not for general legal advice or company law for a
  whole country.
---
# Product Compliance (CE Marking & Conformity)

Use this skill when you place hardware (and the software inside it) on markets that require conformity checks. This is especially EU CE marking for machinery and electrical products.

**Skill name rationale:** `product-compliance` covers CE marking, machinery safety, electromagnetic compatibility (EMC), the Low Voltage Directive (LVD), material rules, and related **product** regulations. It is narrower than all "regulatory compliance" (which includes the General Data Protection Regulation (GDPR), labor law, and more). It is broader than "CE marking" alone.

## Scope

**Owns:**
- Deciding which EU regulations and directives apply (Machinery Regulation / EU 2023/1230, electromagnetic compatibility (EMC), Low Voltage Directive (LVD), Radio Equipment Directive (RED), Restriction of Hazardous Substances (RoHS), EU chemical rules (REACH), and similar)
- Hazard and risk assessment inputs (ISO 12100, ISO 13849, IEC 62061 as applicable)
- Conformity assessment route (self-declaration vs a notified body)
- Technical file structure and the list of required evidence
- Declaration of Conformity (DoC) content checklist — legal signing → `legal-advice`, `belgian-law`
- Labeling, manuals, and market language requirements (high level)
- Test plan (electromagnetic compatibility (EMC), safety, functional) and work with a test lab
- Checks after the product is on the market (post-market surveillance) and how a change affects conformity

**Does NOT own:**
- Drafting contracts or corporate statutes → `legal-advice`, jurisdiction skills
- Tax or import Harmonized System (HS) code filings → `belgian-fiscal-tax`
- Detailed electrical or mechanical design → engineering skills (this skill sets requirements)
- US Federal Communications Commission (FCC) / UL strategy as the main path → coordinate `us-law` concepts; this skill focuses on the EU
- Guaranteeing legal outcomes — flag when a human notified body or a lawyer is required

## Core principles

- **Start early:** Adding compliance after design is expensive. Involve this skill at architecture time (`systems-engineering`).
- **Evidence, not stickers:** CE marking follows a technical file. Buying a CE sticker is not enough.
- **Open hardware still counts:** Publishing designs does not skip the rules for placing a product on the market.
- **Integrated systems:** Machinery plus control software plus optional Internet of Things (IoT) devices — map every in-scope component.
- **Cooperative duty of care:** Keep members and customers safe. That matches compliance. Document this with care.

## Key workflows

### Applicability assessment

1. Product description and intended use
2. Markets (EU, UK, US, and others) — leave non-EU detail to other skills
3. Directives and regulations list with reasons
4. Harmonized standards selection (presumption of conformity: you are presumed to meet the law if you follow the standard)
5. Is a notified body needed? (depends on the category)

### Technical file checklist (typical EU machinery or electrical product)

- [ ] Product description and drawings / bill of materials (BOM) revisions
- [ ] Risk assessment (ISO 12100)
- [ ] Safety and control concept (ISO 13849 / IEC 62061 if applicable)
- [ ] Electrical schematics and Low Voltage Directive (LVD) evidence
- [ ] Electromagnetic compatibility (EMC) test reports
- [ ] Manuals and warnings (languages)
- [ ] Declaration of Conformity (DoC) draft
- [ ] Process after the product is on the market (post-market)

### Change control

Any bill of materials (BOM), firmware, or safety-relevant change triggers an impact review before shipment.

## Terminology and references

- CE marking, Declaration of Conformity (DoC), Technical File, Notified Body
- EU Machinery Regulation (EU) 2023/1230 (transition from Machinery Directive 2006/42/EC — verify current applicability dates)
- Electromagnetic Compatibility (EMC) Directive 2014/30/EU, Low Voltage Directive (LVD) 2014/35/EU, Restriction of Hazardous Substances (RoHS), EU chemical rules (REACH)
- ISO 12100, ISO 13849-1, IEC 60204-1, IEC 61010 (depends on the product)

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

- Do-it-yourself (DIY) kits versus finished machines may have different duties. Document the intended sales channel (`sales`).
- Open documentation may help **maintenance** compliance. It does not replace the first conformity check.
- Subagents and agents **do not sign** Declarations of Conformity (DoCs). Hand this to a qualified human role.
