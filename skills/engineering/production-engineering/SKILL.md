---
name: production-engineering
description: >-
  Manufacturing process design, work instructions, fixtures, quality control,
  and scale-up from prototype to repeatable production. Use for DfM validation,
  assembly lines, test jigs, and yield — not initial R&D design primary ownership.
---
# Production Engineering

Use this skill to make hardware reproducible at volume with known quality and cost.

## Scope

**Owns:**
- Process planning (routing, stations, cycle time estimates)
- Work instructions and visual aids for assembly
- Fixtures, jigs, and test equipment specification
- Pilot runs and yield analysis
- Incoming inspection criteria coordination with `purchasing`
- Packaging for shipment (ESD, shock, environmental)
- Continuous improvement (scrap, rework, bottlenecks)
- Manufacturing BOM (mBOM) alignment with engineering BOM

**Does NOT own:**
- Original mechanical/electrical design → engineering skills (DfM feedback loop)
- Strategic sourcing → `supply-chain-management`
- CE production conformity ongoing audits → `product-compliance`
- Operator HR and payroll → organization (legal/finance boundaries)
- Marketing of "made in" claims → `marketing`, `legal-advice`

## Core principles

- **Prototype ≠ product:** Explicit promotion gate from engineering release to production release.
- **Poka-yoke:** Design process to prevent wrong part, wrong orientation, missed torque.
- **Open manufacturing docs:** Assembly guides can be community assets; protect only supplier-specific pricing/terms.
- **Measure yield:** Track FPY, DPMO, top defect Pareto.
- **Cooperative production:** Document skills needed on floor; training reduces key-person risk.

## Key workflows

### NPI (new product introduction) gate

- [ ] EBOM frozen at promotion revision
- [ ] mBOM and routing drafted
- [ ] Fixtures quoted/built
- [ ] Pilot qty build with recorded issues
- [ ] QC checklist and traceability (serial/lot)
- [ ] Packaging validated with `supply-chain-management` ship tests
- [ ] Handoff docs to `sales` for lead time promises

### Work instruction template

1. Safety PPE and hazards
2. Tools and torque specs
3. Step-by-step with photos
4. QC checkpoints
5. Rework/disposition rules

### Test station design

Coordinate with `electrical-engineering`, `software-development` for flashing/ICT/FCT; log limits and golden units.

## Terminology and standards

- FPY, OEE, takt time, cycle time
- IPC-A-610 accept/reject (electronics assembly)
- ISO 9001 concepts (QMS — full certification is organizational)

## Cross-links

| Need | Skill |
| --- | --- |
| DfM changes | `mechanical-engineering`, `electrical-engineering` |
| Automation on line | `industrial-automation` |
| Optical alignment QC | `optical-engineering` |
| Cost | `finance` |
| CE serial records | `product-compliance` |

## Practical constraints

- Low-volume cooperative production may use cell assembly — still document stations.
- Open hardware kits shift burden to customer assembly; liability and instructions → `legal-advice`, `product-compliance`.
- Tooling amortization belongs in `finance` models.
