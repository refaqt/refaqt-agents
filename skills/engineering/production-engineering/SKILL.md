---
name: production-engineering
description: >-
  Manufacturing process design, work instructions, fixtures, quality
  control, and scale-up from prototype to repeatable production. Use for
  design-for-manufacture (DfM) checks, assembly lines, test jigs, and yield.
  Do not use this skill as the main owner of initial research and design.
---
# Production Engineering

Use this skill to make hardware reproducible at volume with known quality and cost.

## Scope

**Owns:**
- Process planning (station sequence (routing), stations, cycle time estimates)
- Work instructions and visual aids for assembly
- Fixtures, jigs, and test equipment specification
- Pilot runs and yield analysis
- Incoming inspection criteria coordination with `purchasing`
- Packaging for shipment (electrostatic discharge (ESD), shock, environmental)
- Continuous improvement (scrap, rework, slow stations)
- Manufacturing parts list (mBOM) alignment with the engineering parts list (BOM)

**Does NOT own:**
- Original mechanical and electrical design → engineering skills (DfM feedback loop)
- Strategic sourcing → `supply-chain-management`
- European product conformity (CE) production conformity ongoing audits → `product-compliance`
- Operator human resources (HR) and payroll → organization (legal/finance boundaries)
- Marketing of "made in" claims → `marketing`, `legal-advice`

## Core principles

- **A prototype is not a product:** Use a clear gate before you promote an engineering release to a production release.
- **Mistake-proofing (poka-yoke):** Design the process so people cannot fit the wrong part, use the wrong orientation, or miss a torque.
- **Open manufacturing docs:** Assembly guides can be community assets. Protect only supplier-specific pricing and terms.
- **Measure yield:** Track first-pass yield (FPY), defects per million opportunities (DPMO), and a ranked top-defect list (Pareto).
- **Cooperative production:** Record the skills the floor needs. Training reduces risk that only one person can do the work.

## Key workflows

### NPI (new product introduction) gate

- [ ] Engineering BOM (EBOM) frozen at promotion revision
- [ ] mBOM and routing drafted
- [ ] Fixtures quoted/built
- [ ] Pilot quantity build with recorded issues
- [ ] Quality-control (QC) checklist and traceability (serial/lot)
- [ ] Packaging validated with `supply-chain-management` ship tests
- [ ] Handoff docs to `sales` for lead time promises

### Work instruction template

1. Safety personal protective equipment (PPE) and hazards
2. Tools and torque specs
3. Step-by-step with photos
4. QC checkpoints
5. Rework and what-to-do-with-bad-parts (disposition) rules

### Test station design

Coordinate with `electrical-engineering` and `software-development` for flashing, in-circuit test (ICT), and functional circuit test (FCT). Log limits and known-good reference units (golden units).

## Terminology and standards

- FPY, overall equipment effectiveness (OEE), required production pace (takt time), cycle time
- IPC-A-610 accept/reject rules for electronics assembly
- International Organization for Standardization (ISO) 9001 concepts (quality management system (QMS) — full certification is organizational)

## Cross-links

| Need | Skill |
| --- | --- |
| DfM changes | `mechanical-engineering`, `electrical-engineering` |
| Automation on line | `industrial-automation` |
| Optical alignment QC | `optical-engineering` |
| Cost | `finance` |
| CE serial records | `product-compliance` |

## Practical constraints

- Low-volume cooperative production may use small team work cells (cell assembly). Still document stations.
- Open hardware kits shift assembly work to the customer. Liability and instructions → `legal-advice`, `product-compliance`.
- Spreading tooling cost over produced units belongs in `finance` models.
