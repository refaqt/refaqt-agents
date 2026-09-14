---
name: supply-chain-management
description: >-
  Full supply-network design, stock strategy, logistics, risk, and continuity
  for hardware ventures. Use for multi-tier sourcing, wait-time (lead-time)
  risk, customs flow, and demand-supply planning — not for a single purchase
  order (PO).
---
# Supply Chain Management

Use this skill for the flow of materials from suppliers to customers. This is more than a single purchase order (PO).

## Scope

**Owns:**
- Supply network design (one source or two sources, regional strategy)
- Stock policy (safety stock, reorder points, consignment)
- Demand planning input and a light sales and operations planning (S&OP) process
- Logistics (freight mode, third-party logistics (3PL), warehousing)
- Risk management (geography, single source, parts going obsolete, counterfeits)
- International delivery terms (Incoterms) and ship-route optimization (with `finance`)
- Returns and return-merchandise authorization (RMA) logistics coordination
- Supplier scorecards and continuity plans

**Does NOT own:**
- Individual request for quote (RFQ) or purchase order (PO) execution → `purchasing`
- Detailed customs legal classification → `belgian-fiscal-tax`, `legal-advice`
- Product design alternates → engineering skills (request changes)
- Sales promises → `sales` (provide dates that you can meet)
- CE marking duties of the company that imports the product (importer of record) → `product-compliance`, `legal-advice`

## Core principles

- **Know where parts are:** Track location and arrival time. Do not rely on last-minute rescue.
- **Design with supply in mind:** Engineering choices drive most of the risk (about 80%). Flag end-of-life (EOL) and not-recommended-for-new-designs (NRND) parts early.
- **Cooperative resilience:** Do not depend on one hidden supplier in a way that threatens member jobs and customers.
- **Watch for counterfeits:** Use authorized distributors. Inspect incoming critical parts.
- **A public bill of materials (BOM) helps community sourcing:** Publish approved alternates when that is safe.

## Key workflows

### Risk register (supply)

| Part/system | Risk | Mitigation | Owner | Review date |
| --- | --- | --- | --- | --- |
| | sole source | approve a second source | `purchasing` | |

### Inventory policy

- Classify ABC by value and criticality (A = highest value or risk)
- Set safety stock from wait-time (lead-time) variance and the service target
- Align with `finance` cash limits

### Obsolescence watch

- Monitor product change notices (PCN) and end-of-life (EOL) notices
- Trigger a redesign or a last-time buy (LTB) with `engineering` and `finance`

### Shipment checklist

- [ ] Commercial invoice accurate
- [ ] Export compliance screened → `legal-advice`, `us-law`, `european-law` if the goods have US content
- [ ] Harmonized System (HS) codes consistent with `belgian-fiscal-tax` guidance
- [ ] Insurance and international delivery terms (Incoterms) match the quote (`sales`)

## Terminology

- Wait time (lead time, LT), minimum order quantity (MOQ), sales and operations planning (S&OP), available to promise (ATP), safety stock, last-time buy (LTB)
- Third-party logistics (3PL), cross-dock (unload and reload without storing), bonded warehouse (customs warehouse)

## Cross-links

| Need | Skill |
| --- | --- |
| Purchase order (PO) execution | `purchasing` |
| Cost | `finance` |
| Design changes | engineering skills |
| Customer dates | `sales` |
| Production ramp | `production-engineering` |

## Practical constraints

- Hardware cooperatives often keep little stock. State stockout risk clearly to `sales`.
- Global disruptions need scenario plans. One wait-time (lead-time) number is not enough.
- Shipping a kit versus an assembled product changes logistics and `product-compliance` duties.
