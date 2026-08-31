---
name: belgian-fiscal-tax
description: >-
  Belgian fiscal, tax, and VAT matters for cooperatives and hardware ventures.
  Use for VAT treatment, deductions, payroll tax awareness, imports, and planning
  inputs — not corporate governance statutes or general contract law.
---
# Belgian Fiscal and Tax

Use this skill for tax and VAT questions in Belgian operations. Statutory accounts signing requires human accountants/tax advisers.

## Scope

**Owns:**
- Belgian VAT basics (rates, intra-EU, imports, reverse charge awareness)
- VAT on hardware sales, services, and cross-border e-commerce (high level)
- Import duties interaction with customs (with `supply-chain-management`)
- Deductible vs. non-deductible expenses framework (consult accountant)
- Cooperative tax treatment overview (links to `belgian-corporate-law`)
- Token issuance, vesting, redemption, and contributor reward tax awareness → `token-engineering`
- R&D incentives awareness (not grant writing)
- Payroll withholding concepts (not HR law)
- Invoice content requirements for VAT (operational checklist)

**Does NOT own:**
- Corporate bylaws and member shares → `belgian-corporate-law`
- Non-tax legal → `belgian-law`, `legal-advice`
- US tax → US tax counsel / `us-law` routing
- Detailed CE → `product-compliance`
- Filing returns on user's behalf

## Core principles

- **VAT cash flow matters:** Import VAT and deferment schemes affect `finance` runway.
- **Correct classification:** Goods vs. services, B2B vs B2C, place of supply rules.
- **Cooperative specifics:** Surplus allocation may have tax implications for members — accountant required.
- **Open hardware kits:** Mixed supply (goods + instructions) may affect VAT treatment — verify.
- **Document everything:** Intrastat, EC sales lists when thresholds apply.

## Key workflows

### Import of components checklist

- [ ] HS code agreed with customs broker
- [ ] Origin rules for preferential rates
- [ ] Import VAT handling (payment/deferment)
- [ ] Incoterms define who acts as importer (`purchasing`)

### Sales VAT quick route

1. Customer location and VAT ID (B2B EU)
2. Product vs service dominant character
3. Rate and exemption if any
4. Invoice fields per Belgian rules

## Terminology

- BTW/TVA, VIES, intracommunity supply
- PCC (payroll tax) — awareness only
- VenB / personal tax — route members to personal advisers

## Cross-links

| Need | Skill |
| --- | --- |
| Corporate form | `belgian-corporate-law` |
| Token system design | `token-engineering` |
| Legal contracts | `legal-advice`, `belgian-law` |
| EU VAT directives | `european-law` |
| Pricing | `finance` |
| Logistics | `supply-chain-management` |

## Practical constraints

- Tax law changes frequently; verify current FPS Finance guidance for filings.
- Agents do not submit BELcotax or VAT returns.
- Transfer pricing if related parties — specialist required.
