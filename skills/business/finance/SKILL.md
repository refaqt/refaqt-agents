---
name: finance
description: >-
  Budgets, product costs, cash timing (cash flow), price math, and money plans
  for hardware cooperatives. Use when you estimate bill of materials (BOM)
  costs, profit margins, months of cash left (runway), invoices, budgets, money
  scenarios, or how the cooperative reports money — not for tax filings.
---
# Finance

Use this skill for numbers that drive decisions: costs, prices, budgets, and months of cash left (runway). Tax rules and official annual accounts belong in `belgian-fiscal-tax` with `legal-advice`.

## Scope

**Owns:**
- Bill of materials (BOM) and full arrived cost (landed cost): materials, assembly, and a share of overhead
- Profit margin and the volume where we stop losing money (break-even)
- Budgets, forecasts, and scenario models
- Pricing support (price from cost plus a margin (cost-plus), and value-based inputs from `business-development`)
- Cash timing (stock, deposits, payment terms)
- Invoice and quote structure (line items, and awareness of international delivery terms (Incoterms) — legal wording → `legal-advice`)
- Cooperative money reporting needs (management accounts, member capital summaries)

**Does NOT own:**
- Tax returns, value-added tax (VAT) filing, payroll tax → `belgian-fiscal-tax`
- Reading official annual accounts → `belgian-fiscal-tax`, `belgian-corporate-law`
- Contract payment clauses → `legal-advice`
- Choosing vendors → `purchasing`
- CE testing budgets (EU safety mark) as technical scope → `product-compliance`

## Core principles

- **Cost per unit first:** A hardware business can run out of money if you underestimate the bill of materials (BOM), scrap, warranty, and shipping.
- **Open BOM transparency:** A clear internal bill of materials, and a public one where that is appropriate, supports trust and community help. Protect only real commercial secrets.
- **Cash is timing:** Wait times (lead times) and minimum order quantities (MOQs) matter more for survival than a good margin on a spreadsheet.
- **Separate running costs from one-time investment:** Tooling, certification, and research and development (R&D) machines are not repeating cost of goods sold (COGS). Keep running costs (opex) separate from one-time investment (capex).
- **Document assumptions:** Every model lists sources, dates, and how sure you are.

## Key workflows

### BOM cost roll-up

1. Get the bill of materials (BOM) from engineering (`mechanical-engineering`, `electrical-engineering`) with the revision and quantity breaks
2. Add purchased parts from `purchasing` quotes (currency, minimum order quantity (MOQ), wait time)
3. Add assembly and test labor, packaging, and a scrap factor
4. Allocate overhead (building, equipment depreciation) in an explicit way
5. Output: cost per unit at volume tiers. Flag cost risk from a single supplier → `supply-chain-management`

### Pricing support checklist

- [ ] Full arrived cost of goods sold (landed COGS) at the target volume
- [ ] Warranty and support reserve
- [ ] Spreading certification cost over units (amortization) (`product-compliance`)
- [ ] Channel and discount structure (coordinate `sales`, `marketing`)
- [ ] Cooperative surplus / member allocation policy (coordinate `sociocracy`, `belgian-corporate-law`)

### Runway and scenario

| Scenario | Variables |
| --- | --- |
| Base | Orders, wait times, cash spent per month (burn), money customers still owe (receivables) |
| Downside | Delayed certification, supplier delay, fewer sales |
| Upside | Volume discount, grant, partnership prepayment |

## Terminology

- Cost of goods sold (COGS), gross margin, contribution margin, minimum order quantity (MOQ), one-time engineering fee (NRE), one-time investment versus running costs (capex/opex)
- International delivery terms (Incoterms), such as Ex Works (EXW) and Delivered Duty Paid (DDP) — commercial meaning; legal wording → `legal-advice`
- Cooperative surplus, member shares — rules depend on the country → `belgian-corporate-law`

## Cross-links

| Need | Skill |
| --- | --- |
| Vendor pricing | `purchasing` |
| Market pricing | `business-development`, `sales` |
| Tax and VAT | `belgian-fiscal-tax` |
| Corporate structure | `belgian-corporate-law` |
| Safety testing costs | `product-compliance` |
| Activity log | `log` |

## Practical constraints

- The date a quote expires must match how long the supplier needs to deliver.
- Open hardware may lower the average selling price (ASP). Model services, kits, and certification paths in an explicit way.
- Bills of materials (BOMs) in several currencies: write down exchange-rate (FX) assumptions and any hedging policy (a plan to reduce currency risk), if you have one.
