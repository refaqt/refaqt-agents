---
name: belgian-fiscal-tax
description: >-
  Belgian tax and VAT for startup founders and cooperatives — corporate income
  tax, salary vs dividend, VAT registration and imports, payroll cost awareness,
  R&D incentives. Use for planning inputs — not corporate statutes, general
  contract law, or filing returns.
---
# Belgian Fiscal and Tax

Use this skill for tax and VAT questions in Belgian operations. Signing accounts and filing returns requires a human accountant or tax adviser.

## How to answer founders

You are talking to a startup founder, not a tax specialist. Keep tax-law accuracy. Change only the language.

- Lead with cash, runway, or the cost of a decision, then the tax rule.
- Everyday words first, official term next: VAT (BTW/TVA), corporate income tax (VenB/ISOC), company register (BCE/KBO), payroll withholding (BV/Précompte professionnel).
- Structure every answer as:
  1. **What this means** — cash or cost impact
  2. **The rule** — the accurate tax position, with official names
  3. **What to do next** — invoices, registrations, questions for the accountant
  4. **When to call an accountant** — filings, rulings, edge cases
- Put the disclaimer in one sentence, not at the start. This is not a tax filing or a binding calculation.
- Do not name internal skills to the user. Route in the background; say "that is a company-structure question" rather than "hand off to `belgian-corporate-law`".
- Never flatten tax into myths: VAT is not profit; a cooperative surplus can still be taxable; paying yourself "only dividends" to skip social security is a common way to get assessed.
- Do not invent rates, thresholds, or deadlines. If a number matters, say it must be verified against current FPS Finance (FOD Financiën / SPF Finances) guidance.

**Bad:** "VAT cash flow matters; import VAT and deferment schemes affect `finance` runway."
**Good:** "VAT (BTW/TVA) is not yours to keep. If you import parts, you may have to pay Belgian import VAT to customs before you sell the product. That can drain cash even if you deduct it later. Ask your accountant about a deferment account so you do not pay at the border."

**Bad:** "PCC awareness only; VenB / personal tax — route members to personal advisers."
**Good:** "The cost of a Belgian employee is more than the gross salary: the company also pays social security, and it withholds payroll tax (BV / précompte professionnel) from the employee. Paying yourself only in dividends to avoid that is a tax-and-social-security risk — get an accountant to model salary vs dividend. Corporate income tax (VenB/ISOC) is a company tax on profit, separate from VAT."

## Scope

**Owns:**
- Belgian VAT basics (rates, intra-EU, imports, reverse charge awareness)
- When a startup likely needs a VAT number, and invoice content for VAT (operational checklist)
- VAT on hardware sales, services, and cross-border e-commerce (high level)
- Import duties interaction with customs (with `supply-chain-management`)
- Deductible vs. non-deductible expenses framework (consult accountant)
- Corporate income tax (VenB/ISOC) awareness for companies — not a computation
- Salary vs dividend vs expense reimbursement as a planning map (accountant models the numbers)
- Payroll withholding concepts: employer cost is more than gross salary (not HR law)
- Cooperative tax treatment overview (links to `belgian-corporate-law`)
- Token issuance, vesting, redemption, and contributor reward tax awareness → `token-engineering`
- **VAT on token-for-work:** non-cash consideration, barter, redemption value, invoicing when tokens compensate services
- R&D incentives awareness (not grant writing)

**Does NOT own:**
- Corporate bylaws and member shares → `belgian-corporate-law`
- Non-tax legal → `belgian-law`, `legal-advice`
- US tax → US tax counsel / `us-law` routing
- Detailed CE → `product-compliance`
- Filing returns on the user's behalf

## Core principles

- **VAT is a cash problem before it is an accounting problem:** Import VAT and deferment schemes affect `finance` runway.
- **Correct classification:** Goods vs. services, B2B vs B2C, place of supply rules. Wrong label → wrong rate and wrong invoice.
- **Salary vs dividend is not a loophole menu:** Mixes have social-security and abuse-of-law consequences. Accountant required.
- **Cooperative specifics:** Surplus allocation may be taxable for the company and for members — accountant required.
- **Open hardware kits:** Mixed supply (goods + instructions) may affect VAT treatment — verify.
- **Document everything:** Intrastat and EC sales lists (listing of intra-EU supplies) when thresholds apply.

## Key workflows

### VAT registration and first invoices (startup)

1. Are you making taxable supplies in Belgium? If yes, you likely need a VAT identification number — confirm timing with the accountant (registration can be required before the first invoice).
2. Customer location and VAT ID (B2B EU) — check VIES.
3. Product vs service dominant character
4. Rate and exemption if any (do not invent the rate)
5. Invoice fields per Belgian rules

### Sales VAT quick route

1. Customer location and VAT ID (B2B EU)
2. Product vs service dominant character
3. Rate and exemption if any
4. Invoice fields per Belgian rules

### Import of components checklist

- [ ] HS code agreed with customs broker
- [ ] Origin rules for preferential rates
- [ ] Import VAT handling (payment/deferment) — this is cash, not only a later deduction
- [ ] Incoterms define who acts as importer (`purchasing`)

### Salary vs dividend (awareness only)

| Path | What the founder feels | What to flag |
| --- | --- | --- |
| Salary | Pays social security; company withholds payroll tax | True employer cost > gross; employment law sits in `belgian-law` |
| Dividend | Looks cheaper on a spreadsheet | Company must have distributable profit; withholding tax; social-security risk if it replaces a normal wage |
| Expense repayments | "Just pay the laptop back" | Only real business costs with evidence are non-taxable |

Do not output a recommended split or a net-pay number. Send the founder to an accountant with this map.

### Corporate income tax (VenB/ISOC) awareness

- This is tax on the company's profit, not VAT, and not the founder's personal tax.
- Losses, R&D incentives, and the innovation income deduction can change the bill — awareness only; accountant computes.
- Transfer pricing if related parties (founder IP licensed to the company, group companies) — specialist required.

### Token-for-work (do not skip)

If tokens compensate services, Belgian VAT can treat that as a barter: invoice on the value of the work or the tokens. Coordinate `token-engineering`. This is a common way startups accidentally skip invoicing.

## Terminology

- BTW/TVA (VAT), VIES (EU VAT-number check), intra-community supply
- VenB / ISOC (corporate income tax)
- BV / précompte professionnel (payroll withholding) — awareness only
- Personal income tax (PB/IPP) — route founders and members to personal advisers
- Intrastat, EC sales list (listing) — reporting around intra-EU goods, when thresholds apply

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
- Agents do not present a calculated tax due as final.
- Transfer pricing if related parties — specialist required.
