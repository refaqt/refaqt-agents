---
name: belgian-fiscal-tax
description: >-
  Belgian tax and value-added tax (VAT, in Belgium BTW/TVA) for startup
  founders and cooperatives. Covers company income tax, salary versus
  dividend, VAT registration and imports, payroll cost awareness, and
  research incentives (R&D). Use this for planning inputs. Do not use this
  for company rulebooks, general contract law, or filing tax returns.
---
# Belgian Fiscal and Tax

Use this skill for tax and VAT questions in Belgian operations. Signing accounts and filing returns requires a human accountant or tax adviser.

## How to answer founders

Follow `.agents/rules/communication.md`. Extra for this skill:

- Everyday words first, official term next: value-added tax, VAT (in Belgium BTW/TVA); company income tax (VenB/ISOC); the company register (BCE/KBO); tax taken from wages (BV / précompte professionnel).
- In step 4, tell the founder when to call an accountant. Use that step for filings, rulings, and unusual cases.
- Disclaimer: this is not a tax filing or a binding calculation.
- Do not turn tax into simple myths: VAT is not profit; a cooperative surplus can still be taxable; paying yourself "only dividends" to skip social security is a common way to get a tax assessment.
- If a number matters, say it must be checked against current FPS Finance (FOD Financiën / SPF Finances) guidance.
- Say "that is a company-structure question" rather than naming an internal skill.

**Bad:** "VAT cash flow matters; import VAT and deferment schemes affect `finance` runway."
**Good:** "VAT (BTW/TVA) is not yours to keep. If you import parts, you may have to pay Belgian import VAT to customs before you sell the product. That can use up cash even if you deduct it later. Ask your accountant about a delay account (deferment) so you do not pay at the border."

**Bad:** "PCC awareness only; VenB / personal tax — route members to personal advisers."
**Good:** "The cost of a Belgian employee is more than the gross salary: the company also pays social security, and it withholds payroll tax (BV / précompte professionnel) from the employee. Paying yourself only in dividends to avoid that is a tax-and-social-security risk — get an accountant to model salary vs dividend. Corporate income tax (VenB/ISOC) is a company tax on profit, separate from VAT."

## Scope

**Owns:**
- Belgian VAT basics (rates, sales between EU countries, imports, reverse charge awareness: the customer accounts for VAT instead of the seller)
- When a startup likely needs a VAT number, and what a VAT invoice must contain (operational checklist)
- VAT on hardware sales, services, and cross-border online sales (overview only)
- Import duties and how they work with customs (with `supply-chain-management`)
- Which costs you can deduct and which you cannot (ask an accountant)
- Company income tax (VenB/ISOC) awareness for companies — not a calculation
- Salary versus dividend versus paying costs back, as a planning map (the accountant models the numbers)
- Payroll withholding concepts: employer cost is more than gross salary (not HR law)
- Cooperative tax treatment overview (links to `belgian-corporate-law`)
- Token issuance, tokens that unlock over time (vesting), cashing them in (redemption), and contributor reward tax awareness → `token-engineering`
- **VAT on token-for-work:** non-cash payment, swap of value (barter), redemption value, invoicing when tokens pay for services
- Research and development (R&D) incentives awareness (not grant writing)

**Does NOT own:**
- Company bylaws and member shares → `belgian-corporate-law`
- Non-tax legal questions → `belgian-law`, `legal-advice`
- US tax → a US tax lawyer / `us-law` routing
- Detailed CE marking → `product-compliance`
- Filing returns on the user's behalf

## Core principles

- **VAT is a cash problem before it is an accounting problem:** Import VAT and delay schemes (deferment) affect remaining cash in `finance`.
- **Correct classification:** Goods versus services, sales to businesses (B2B) versus to consumers (B2C), and which country VAT applies in (place of supply). A wrong label leads to the wrong rate and the wrong invoice.
- **Salary versus dividend is not a list of legal tricks:** Mixes have social-security consequences and consequences under the tax rule against abuse of law. An accountant is required.
- **Cooperative specifics:** How surplus is shared may be taxable for the company and for members. An accountant is required.
- **Open hardware kits:** A mixed supply (goods plus instructions) may change VAT treatment. Verify this.
- **Document everything:** Intrastat (EU statistics on goods moving between EU countries) and EC sales lists (listing of supplies between EU countries) when thresholds apply.

## Key workflows

### VAT registration and first invoices (startup)

1. Are you making sales that VAT applies to in Belgium (taxable supplies)? If yes, you likely need a VAT identification number. Confirm timing with the accountant. Registration can be required before the first invoice.
2. Customer location and VAT ID (B2B EU) — check VIES (the EU VAT-number check).
3. Whether the deal is mainly a product or mainly a service
4. Rate and exemption if any (do not invent the rate)
5. Invoice fields per Belgian rules

### Sales VAT quick route

1. Customer location and VAT ID (B2B EU)
2. Whether the deal is mainly a product or mainly a service
3. Rate and exemption if any
4. Invoice fields per Belgian rules

### Import of components checklist

- [ ] Harmonized System customs code (HS code) agreed with the customs broker
- [ ] Origin rules for lower duty rates (preferential rates)
- [ ] Import VAT handling (payment or delay / deferment) — this is cash, not only a later deduction
- [ ] Incoterms (international delivery terms) define who acts as importer (`purchasing`)

### Salary vs dividend (awareness only)

| Path | What the founder feels | What to flag |
| --- | --- | --- |
| Salary | Pays social security; the company withholds payroll tax | True employer cost is more than gross pay; employment law sits in `belgian-law` |
| Dividend | Looks cheaper on a spreadsheet | The company must have profit it can distribute; withholding tax; social-security risk if it replaces a normal wage |
| Expense repayments | "Just pay the laptop back" | Only real business costs with evidence are non-taxable |

Do not output a recommended split or a net-pay number. Send the founder to an accountant with this map.

### Corporate income tax (VenB/ISOC) awareness

- This is tax on the company's profit, not VAT, and not the founder's personal tax.
- Losses, R&D incentives, and the innovation income deduction can change the bill. This is awareness only. The accountant computes.
- Transfer pricing if related parties (founder intellectual property (IP) licensed to the company, group companies). A specialist is required. Transfer pricing means prices between related companies must match prices between independent companies.

### Token-for-work (do not skip)

If tokens pay for services, Belgian VAT can treat that as a swap of value (barter): invoice on the value of the work or the tokens. Coordinate `token-engineering`. This is a common way startups miss invoicing by accident.

## Terminology

- BTW/TVA (VAT), VIES (EU VAT-number check), intra-community supply (a sale of goods between EU countries)
- VenB / ISOC (company income tax)
- BV / précompte professionnel (tax taken from wages) — awareness only
- Personal income tax (PB/IPP) — send founders and members to personal advisers
- Intrastat (EU statistics on goods moving between EU countries), EC sales list (listing) — reporting around goods moving between EU countries, when thresholds apply

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

- Tax law changes often. Check current FPS Finance guidance for filings.
- Agents do not submit BELcotax (the Belgian payroll tax filing system) or VAT returns.
- Agents do not present a calculated tax due as final.
- Transfer pricing if related parties — a specialist is required.
