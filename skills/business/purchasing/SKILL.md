---
name: purchasing
description: >-
  Finding suppliers, comparing quotes, purchase orders, and vendor management for
  hardware bills of materials (BOMs) and services. Use when you choose a
  supplier, compare quotes, place an order, or manage a vendor — not for
  long-term supply-chain design.
---
# Purchasing

Use this skill to buy parts and services in a way that is efficient and easy to trace. Long-term network design and risk programs belong in `supply-chain-management`.

## Scope

**Owns:**
- Request for quote (RFQ) and request for proposal (RFP) packs from engineering bills of materials (BOMs)
- Quote comparison (price, minimum order quantity (MOQ), wait time, terms, alternates)
- Creating purchase orders (POs) and tracking orders
- Vendor onboarding data (contacts, payment terms, international delivery terms (Incoterms))
- Matching incoming goods to inventory records
- One-off and prototype buying

**Does NOT own:**
- Long-term plan to buy from two suppliers (dual-sourcing) → `supply-chain-management`
- Budget approval and cost modeling → `finance`
- Contract negotiation and liability terms → `legal-advice`
- Technical accept or reject criteria → engineering skills
- Customs classification detail → `supply-chain-management`, `belgian-fiscal-tax` (value-added tax (VAT) and import)

## Core principles

- **Revision control:** Every purchase order (PO) names the drawing or bill of materials (BOM) revision and the approved list of alternates.
- **Traceability:** Store lot codes and certificates (Restriction of Hazardous Substances (RoHS), material certificates) for `product-compliance` and quality.
- **Open BOM hygiene:** Prefer vendors who accept a public bill of materials (BOM) where that is possible. Protect only the commercial details that must stay private.
- **Cooperative procurement:** Write down decisions so members can see them. Do not use a single source without an explicit decision to accept that risk.
- **Total cost:** Include shipping, duties, payment terms, and parts that fail quality checks. Do not look at unit price alone.

## Key workflows

### RFQ packet

1. Bill of materials (BOM) line items with manufacturer part number (MPN), quantity breaks, and target dates
2. Required specs and standards. Examples: Restriction of Hazardous Substances (RoHS), EU chemical rules (REACH), and UL or International Electrotechnical Commission (IEC) rules where they apply
3. Packaging and labeling requirements
4. Quality documents needed (certificate of conformity (CoC), test reports)
5. Delivery terms and ship-to address

### Quote comparison matrix

| Vendor | Unit @ qty | MOQ | Lead time | Payment | Alternate OK? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

Escalate a single-source buy or a delay of more than X weeks to `supply-chain-management`.

### PO checklist

- [ ] Approved budget (`finance`)
- [ ] Correct revision and part numbers
- [ ] International delivery terms (Incoterms) and ship-to address checked
- [ ] Required certificates noted on the order
- [ ] Incoming inspection criteria from `production-engineering` or the relevant engineering skill

## Terminology

- Manufacturer part number (MPN), minimum order quantity (MOQ), wait time (lead time, LT), non-cancellable non-returnable (NCNR), certificate of conformity (CoC), approved vendor list (AVL)
- Incoterms 2020 — day-to-day use; legal disputes → `legal-advice`

## Cross-links

| Need | Skill |
| --- | --- |
| BOM source | `mechanical-engineering`, `electrical-engineering` |
| Strategic sourcing | `supply-chain-management` |
| Cost roll-up | `finance` |
| Import/VAT | `belgian-fiscal-tax` |
| Compliance materials | `product-compliance` |

## Practical constraints

- Items with a long wait (microcontrollers (MCUs), optics, machined parts) need early purchase orders (POs). Flag these to `supply-chain-management`.
- Prototype buys may use parts that are not on the approved vendor list (AVL). Production must move to the qualified list.
- Cooperative approval limits may apply. Coordinate with `sociocracy` and `belgian-corporate-law`.
