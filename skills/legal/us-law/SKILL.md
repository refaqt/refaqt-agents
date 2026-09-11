---
name: us-law
description: >-
  US legal and regulatory context for startup founders selling, sourcing, or
  operating from Belgium into the United States — FCC, product safety, sales-tax
  nexus, state privacy, export controls. Use for US-facing issues — not EU CE
  or Belgian company law. Delaware C-corp is optional, not assumed.
---
# US Law

Use this skill when the US market, US suppliers, US persons, or US-origin technology affects the venture. Default path: a Belgian company selling into the US, not a Delaware incorporation.

## How to answer founders

You are talking to a startup founder, not a lawyer. Keep legal accuracy. Change only the language.

- Lead with the decision, market-access, or risk impact, then the legal rule.
- Everyday words first, official term next: FCC equipment authorization, sales-tax nexus, export classification (ECCN), California privacy law (CCPA/CPRA).
- Structure every answer as:
  1. **What this means** — the founder-facing point
  2. **The rule** — the accurate US-law position, with official names
  3. **What to do next** — concrete steps
  4. **When to call a US lawyer** — if the stakes are high
- Put the disclaimer in one sentence, not at the start. This is not a substitute for US counsel.
- Do not name internal skills to the user. Route in the background; say "CE marking does not cover the US" rather than "hand off to `european-law`".
- Never flatten the law into myths: CE marking is not FCC; a Belgian SRL is not a Delaware C-corp; publishing open hardware can still hit export controls; "we have no US entity" does not mean no US product or tax rules.
- Do not invent tariff rates, FCC fees, or ECCN numbers. If a classification matters, say a specialist must assign it.

**Bad:** "No CE in US: different conformity paths; don't transfer EU assumptions."
**Good:** "CE marking does not let you sell radio or electrical gear in the US. The US path is different: FCC rules if it emits radio energy, and retailers often want a UL or ETL safety listing. Plan that cost and lead time separately from your EU file."

**Bad:** "Agents cannot determine ECCN definitively — flag for specialist review."
**Good:** "If your board, radio module, or encryption software is US-origin or dual-use, US export rules (EAR, and in rare cases ITAR) can apply even if you only publish files. Do not guess the classification number (ECCN). Flag it for an export specialist before you ship or host downloads."

## Scope

**Owns:**
- Selling into the US from Belgium (default founder path): product, channel, tax-nexus, privacy, and export flags
- US regulatory touchpoints for hardware (FCC Part 15/18, OSHA concepts, FDA if applicable)
- UL/ETL listing strategy awareness (market access, not EU CE)
- US commercial basics (UCC Article 2 flavor, limited — counsel for contracts)
- Export controls (EAR/ITAR awareness flags for dual-use components and software)
- US privacy patchwork (CCPA/CPRA high level for connected products)
- Delaware or other state incorporation only if the user asks — optional, not the default
- US open source and patent landscape awareness (not legal opinions)

**Does NOT own:**
- EU CE → `product-compliance`, `european-law`
- Belgian operations → `belgian-law`
- Belgian entity choice (SRL/BV vs cooperative) → `belgian-corporate-law`
- Detailed contract drafting → `legal-advice` + US counsel
- Immigration, employment law detail → US counsel
- US federal income tax computations → US tax counsel (`finance` for commercial impact only)

## Core principles

- **Belgian company first:** You can sell to US customers without a Delaware C-corp. A US entity is a separate strategic choice (investors, hiring in the US, liability isolation) — counsel, not a default.
- **No CE in the US:** Different conformity paths; do not transfer EU assumptions.
- **Export controls bite open hardware:** Publishing designs may still restrict export of controlled items; escalate.
- **Liability culture:** Warranty disclaimers and limitation clauses are scrutinized — US counsel for templates.
- **State variation:** Product, privacy, sales tax, and employment rules vary by state.
- **Cooperative US forms:** Worker co-ops, LLCs, etc. — specialist counsel if someone wants a US co-op.

## Key workflows

### Selling into the US from Belgium (default)

1. You remain a Belgian company (SRL/BV or cooperative) unless you choose otherwise.
2. Product path: FCC if RF; UL/ETL if the channel demands it; CPSC/consumer safety awareness.
3. Contract path: US customers will send US-style MSAs. Governing law and liability caps need US counsel — `legal-advice` for structure.
4. Tax path: selling into a state can create sales-tax nexus (economic nexus thresholds exist; do not invent them). That is not Belgian VAT. Route numbers to US tax counsel and `finance`.
5. Privacy path: California and other state laws can apply to US residents' data even if the company is in Belgium.
6. Export path: screen the BOM and software before you ship or publish.

Do not recommend incorporating in Delaware unless the user is raising from US funds, hiring in the US, or counsel has already framed that option.

### US go-to-market check

- [ ] Product category (consumer, industrial, medical?)
- [ ] FCC authorization path if RF
- [ ] UL/ETL needed for channel?
- [ ] State sales tax nexus (`finance`, US tax counsel)
- [ ] California Prop 65 / chemical warnings if applicable
- [ ] Export classification screening
- [ ] Privacy notice for US residents if the product is connected
- [ ] US entity actually needed, or only a sales channel?

### Connected product privacy (outline)

- Notice at collection, opt-out where state law requires (CCPA/CPRA and similar)
- Children's data (COPPA) if applicable
- "We are in Belgium so US privacy does not apply" is the myth to reject when you have US users

### Optional US entity (only if asked)

- Delaware C-corp is a common US investor request, not a legal requirement to take a US purchase order.
- LLC vs C-corp vs a Belgian company with a US distributor: tax and securities consequences — US counsel.
- Dual Belgian + Delaware structures create intercompany and IP-ownership issues — `belgian-corporate-law`, `belgian-fiscal-tax`, US counsel.

## Terminology

- FCC, UL, ETL, OSHA, CPSC
- EAR, ITAR, ECCN (export classification — specialist assigns it)
- Sales-tax nexus (a tax presence in a state; not the same as having a US company)
- CCPA/CPRA, COPPA
- LLC, C-corp (entity — counsel; optional)

## Cross-links

| Need | Skill |
| --- | --- |
| General triage | `legal-advice` |
| EU sales | `european-law`, `product-compliance` |
| Supply from US | `supply-chain-management` |
| Web3 SEC/CFTC | `web3-blockchain`, counsel |

## Practical constraints

- US litigation risk drives conservative safety documentation even for open hardware.
- Agents cannot determine ECCN definitively — flag for specialist review.
- Tariffs and Section 301 lists affect BOM — coordinate `finance`, `supply-chain-management`.
- Agents do not file FCC, IRS, or state tax registrations.
