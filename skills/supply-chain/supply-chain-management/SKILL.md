---
name: supply-chain-management
description: >-
  End-to-end supply network design, inventory strategy, logistics, risk, and
  continuity for hardware ventures. Use for multi-tier sourcing, lead-time
  risk, customs flow, and demand-supply planning — not single PO placement.
---
# Supply Chain Management

Use this skill for strategic and operational flow of materials from suppliers to customers — beyond individual purchase orders.

## Scope

**Owns:**
- Supply network design (single/dual source, regional strategy)
- Inventory policy (safety stock, reorder points, consignment)
- Demand planning input and S&OP light process
- Logistics (freight mode, 3PL, warehousing)
- Risk management (geo, single-source, obsolescence, counterfeits)
- Incoterms and ship route optimization (with `finance`)
- Returns/RMA logistics coordination
- Supplier scorecards and continuity plans

**Does NOT own:**
- Individual RFQ/PO execution → `purchasing`
- Detailed customs legal classification → `belgian-fiscal-tax`, `legal-advice`
- Product design alternates → engineering skills (request changes)
- Sales promises → `sales` (provide feasible dates)
- CE importer of record duties → `product-compliance`, `legal-advice`

## Core principles

- **Visibility beats heroics:** Know where parts are and when they arrive.
- **Design for supply chain:** Engineering choices drive 80% of risk — escalate EOL and NRND early.
- **Cooperative resilience:** Avoid opaque sole-source dependencies that threaten member jobs and customers.
- **Counterfeit awareness:** Authorized distributors, incoming inspection for critical parts.
- **Open BOM aids community sourcing:** Document approved alternates publicly when safe.

## Key workflows

### Risk register (supply)

| Part/system | Risk | Mitigation | Owner | Review date |
| --- | --- | --- | --- | --- |
| | sole source | qualify 2nd source | `purchasing` | |

### Inventory policy

- Classify ABC by value and criticality
- Set safety stock from lead time variance and service target
- Align with `finance` cash constraints

### Obsolescence watch

- Monitor PCN/EOL notices
- Trigger redesign or last-time buy with `engineering` and `finance`

### Shipment checklist

- [ ] Commercial invoice accurate
- [ ] Export compliance screened → `legal-advice`, `us-law`, `european-law` if US content
- [ ] HS codes consistent with `belgian-fiscal-tax` guidance
- [ ] Insurance and incoterms match quote (`sales`)

## Terminology

- LT, MOQ, S&OP, ATP, safety stock, LTB (last time buy)
- 3PL, cross-dock, bonded warehouse

## Cross-links

| Need | Skill |
| --- | --- |
| PO execution | `purchasing` |
| Cost | `finance` |
| Design changes | engineering skills |
| Customer dates | `sales` |
| Production ramp | `production-engineering` |

## Practical constraints

- Hardware cooperatives often run lean inventory — document stockout risk explicitly to `sales`.
- Global disruptions require scenario plans, not single LT numbers.
- Kit shipping vs. assembled product changes logistics and `product-compliance` responsibilities.
