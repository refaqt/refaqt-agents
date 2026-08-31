---
name: purchasing
description: >-
  Sourcing, quoting, purchase orders, and vendor management for hardware BOMs and
  services. Use when selecting suppliers, comparing quotes, placing orders, or
  managing vendor relationships — not for strategic supply chain design.
---
# Purchasing

Use this skill to buy parts and services efficiently and traceably. Strategic network design and risk programs belong in `supply-chain-management`.

## Scope

**Owns:**
- RFQ/RFP preparation from engineering BOMs
- Quote comparison (price, MOQ, lead time, terms, alternates)
- Purchase order creation and order tracking
- Vendor onboarding data (contacts, payment terms, incoterms)
- Receiving alignment with inventory records
- Spot-buy and prototype purchasing

**Does NOT own:**
- Long-term dual-sourcing strategy → `supply-chain-management`
- Budget approval and cost modeling → `finance`
- Contract negotiation and liability terms → `legal-advice`
- Technical accept/reject criteria → engineering skills
- Customs classification detail → `supply-chain-management`, `belgian-fiscal-tax` (VAT/import)

## Core principles

- **Revision control:** Every PO references drawing/BOM revision and approved alternates list.
- **Traceability:** Lot codes and certificates (RoHS, material certs) stored for `product-compliance` and quality.
- **Open BOM hygiene:** Prefer vendors comfortable with public BOM exposure where possible; protect only necessary commercial confidentiality.
- **Cooperative procurement:** Document decisions for member visibility; avoid sole-source without explicit risk acceptance.
- **Total cost:** Include shipping, duties, payment terms, and quality fallout — not unit price alone.

## Key workflows

### RFQ packet

1. BOM line items with MPN, qty breaks, target dates
2. Required specs and standards (RoHS, REACH, UL/IEC where relevant)
3. Packaging and labeling requirements
4. Quality documentation needs (CoC, test reports)
5. Delivery terms and ship-to

### Quote comparison matrix

| Vendor | Unit @ qty | MOQ | Lead time | Payment | Alternate OK? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

Escalate sole-source or >X week slip to `supply-chain-management`.

### PO checklist

- [ ] Approved budget (`finance`)
- [ ] Correct revision and part numbers
- [ ] Incoterms and ship-to validated
- [ ] Required certs attached to order notes
- [ ] Receiving inspection criteria from `production-engineering` or relevant engineering skill

## Terminology

- MPN, MOQ, LT, NCNR, CoC, AVL (approved vendor list)
- Incoterms 2020 — operational use; legal disputes → `legal-advice`

## Cross-links

| Need | Skill |
| --- | --- |
| BOM source | `mechanical-engineering`, `electrical-engineering` |
| Strategic sourcing | `supply-chain-management` |
| Cost roll-up | `finance` |
| Import/VAT | `belgian-fiscal-tax` |
| Compliance materials | `product-compliance` |

## Practical constraints

- Long-lead items (MCUs, optics, machined parts) trigger early POs — flag to `supply-chain-management`.
- Prototype buys may use non-AVL parts; production must converge on qualified list.
- Cooperative approval thresholds may apply — coordinate with `sociocracy` and `belgian-corporate-law`.
