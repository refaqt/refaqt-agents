---
name: finance
description: >-
  Budgeting, costing, cash flow, pricing math, and financial planning for hardware
  cooperatives. Use when estimating BOM costs, margins, runway, invoices, budgets,
  financial scenarios, or cooperative financial governance — not for tax filings.
---
# Finance

Use this skill for numbers that drive decisions: costs, prices, budgets, and runway. Tax compliance and statutory accounts belong in `belgian-fiscal-tax` with `legal-advice`.

## Scope

**Owns:**
- BOM and landed cost roll-ups (materials, assembly, overhead allocation)
- Margin and break-even analysis
- Budgets, forecasts, and scenario modeling
- Pricing support (cost-plus, value-based inputs from `business-development`)
- Cash flow timing (inventory, deposits, payment terms)
- Invoice and quote structure (line items, incoterms awareness — legal terms → `legal-advice`)
- Cooperative financial reporting needs (management accounts, member capital summaries)

**Does NOT own:**
- Tax returns, VAT filing, payroll tax → `belgian-fiscal-tax`
- Statutory annual accounts interpretation → `belgian-fiscal-tax`, `belgian-corporate-law`
- Contract payment clauses → `legal-advice`
- Vendor selection → `purchasing`
- CE testing budgets as technical scope → `product-compliance`

## Core principles

- **Unit economics first:** Hardware fails quietly when BOM, scrap, warranty, and logistics are underestimated.
- **Open BOM transparency:** Internal and (where appropriate) public BOM clarity supports trust and community contribution; protect only genuinely sensitive commercial terms.
- **Cash is timing:** Lead times and MOQs dominate cooperative survival more than spreadsheet margin.
- **Separate opex vs. capex:** Tooling, certification, and R&D machines are not recurring COGS.
- **Document assumptions:** Every model lists sources, dates, and confidence.

## Key workflows

### BOM cost roll-up

1. Gather BOM from engineering (`mechanical-engineering`, `electrical-engineering`) with revision and quantity breaks
2. Add purchased parts from `purchasing` quotes (currency, MOQ, lead time)
3. Add assembly/test labor, packaging, scrap factor
4. Allocate overhead (facility, equipment depreciation) explicitly
5. Output: per-unit cost at volume tiers; flag single-source cost risk → `supply-chain-management`

### Pricing support checklist

- [ ] Landed COGS at target volume
- [ ] Warranty and support reserve
- [ ] Certification amortization (`product-compliance`)
- [ ] Channel/discount structure (coordinate `sales`, `marketing`)
- [ ] Cooperative surplus / member allocation policy (coordinate `sociocracy`, `belgian-corporate-law`)

### Runway and scenario

| Scenario | Variables |
| --- | --- |
| Base | Orders, lead times, burn, receivables |
| Downside | Delayed certification, supplier slip, lower conversion |
| Upside | Volume discount, grant, partnership prepayment |

## Terminology

- COGS, gross margin, contribution margin, MOQ, NRE, capex/opex
- Incoterms (EXW, DDP, etc.) — commercial meaning; legal wording → `legal-advice`
- Cooperative surplus, member shares — jurisdiction-specific → `belgian-corporate-law`

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

- Quote validity dates must match supplier lead times.
- Open hardware may reduce ASP; model service, kits, and certification paths explicitly.
- Multi-currency BOMs: document FX assumptions and hedging policy if any.
