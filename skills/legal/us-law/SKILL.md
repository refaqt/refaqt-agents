---
name: us-law
description: >-
  US legal and regulatory context for startup founders who sell, buy, or
  operate from Belgium into the United States. Covers radio rules (FCC),
  product safety, sales-tax presence (nexus), state privacy, and export
  controls. Use this for US-facing issues. Do not use this for EU CE marking
  or Belgian company law. A Delaware C-corporation is optional, not assumed.
---
# US Law

Use this skill when the US market, US suppliers, people who count as US persons under export rules, or technology that comes from the US affects the company. Default path: a Belgian company selling into the US, not a Delaware company.

## How to answer founders

You are talking to a startup founder, not a lawyer. Keep legal accuracy. Change only the language.

- Start with the decision, access to the market, or the risk. Then state the legal rule.
- Everyday words first, official term next: FCC equipment authorization (US radio approval), sales-tax presence (nexus), export classification (ECCN), California privacy law (CCPA/CPRA).
- Structure every answer as:
  1. **What this means** — the point the founder needs
  2. **The rule** — the accurate US-law position, with official names
  3. **What to do next** — concrete steps
  4. **When to call a US lawyer** — if the stakes are high
- Put the disclaimer in one sentence. Do not put it at the start. This is not a replacement for a US lawyer.
- Do not name internal skills to the user. Send the question to the right skill without naming it. Say "CE marking does not cover the US" rather than "hand off to `european-law`".
- Do not turn the law into simple myths: CE marking is not FCC approval; a Belgian private limited company (SRL) is not a Delaware C-corporation; publishing open hardware can still fall under export controls; "we have no US company" does not mean no US product or tax rules.
- Do not invent tariff rates, FCC fees, or ECCN numbers. If a classification matters, say a specialist must assign it.

**Bad:** "No CE in US: different conformity paths; don't transfer EU assumptions."
**Good:** "CE marking does not let you sell radio or electrical gear in the US. The US path is different: FCC rules if it emits radio energy, and retailers often want a UL or ETL safety listing. Plan that cost and the extra time separately from your EU file."

**Bad:** "Agents cannot determine ECCN definitively — flag for specialist review."
**Good:** "If your board, radio module, or encryption software comes from the US or has civilian and military use (dual-use), US export rules can apply even if you only publish files. Those rules are the Export Administration Regulations (EAR), and in rare cases the International Traffic in Arms Regulations (ITAR). Do not guess the classification number (ECCN). Flag it for an export specialist before you ship or host downloads."

## Scope

**Owns:**
- Selling into the US from Belgium (default founder path): product, sales channel, tax presence (nexus), privacy, and export flags
- US regulatory flags for hardware (FCC Part 15/18, US workplace safety rules (OSHA), US Food and Drug Administration (FDA) rules if they apply)
- UL or ETL listing strategy awareness (US safety listing marks for access to the US market, not EU CE marking)
- US commercial basics (sales rules in the style of Uniform Commercial Code (UCC) Article 2, limited — a lawyer for contracts)
- Export controls (EAR/ITAR awareness flags for dual-use components and software)
- US privacy rules that differ by state (CCPA/CPRA overview for connected products)
- Delaware or other state company formation only if the user asks — optional, not the default
- US open source and patent overview (not legal opinions)

**Does NOT own:**
- EU CE marking → `product-compliance`, `european-law`
- Belgian operations → `belgian-law`
- Belgian company form (SRL/BV vs cooperative) → `belgian-corporate-law`
- Detailed contract drafting → `legal-advice` + a US lawyer
- Immigration and employment-law detail → a US lawyer
- US federal income tax calculations → a US tax lawyer (`finance` for commercial impact only)

## Core principles

- **Belgian company first:** You can sell to US customers without a Delaware C-corporation. A US company is a separate strategic choice (investors, hiring in the US, isolating legal risk). That needs a lawyer. It is not a default.
- **No CE marking in the US:** The US has different ways to show a product is allowed. Do not copy EU assumptions.
- **Export controls still apply to open hardware:** Publishing designs may still restrict export of controlled items. Send this to a specialist.
- **Lawsuits are common:** Warranty disclaimers and limitation clauses are examined closely. Use a US lawyer for templates.
- **State variation:** Product, privacy, sales tax, and employment rules vary by state.
- **Cooperative US forms:** Worker co-ops, limited liability companies (LLCs), and similar forms need a specialist lawyer if someone wants a US co-op.

## Key workflows

### Selling into the US from Belgium (default)

1. You remain a Belgian company (SRL/BV or cooperative) unless you choose otherwise.
2. Product path: FCC if the product uses radio; UL or ETL if the sales channel demands it; US consumer product safety rules (CPSC).
3. Contract path: US customers will send US-style main customer contracts (MSAs). Governing law and liability caps need a US lawyer — `legal-advice` for structure.
4. Tax path: selling into a state can create a sales-tax presence (economic nexus thresholds exist; do not invent them). That is not Belgian VAT. Send numbers to a US tax lawyer and `finance`.
5. Privacy path: California and other state laws can apply to US residents' data even if the company is in Belgium.
6. Export path: screen the bill of materials (BOM) and software before you ship or publish.

Do not recommend forming a company in Delaware unless the user is raising money from US funds, hiring in the US, or a lawyer has already set out that option.

### Check before selling in the US (go-to-market)

- [ ] Product category (consumer, industrial, medical?)
- [ ] FCC authorization path if the product uses radio
- [ ] UL or ETL needed for the sales channel?
- [ ] State sales-tax presence (`finance`, a US tax lawyer)
- [ ] California Proposition 65 / chemical warnings if they apply
- [ ] Export classification screening
- [ ] Privacy notice for US residents if the product is connected
- [ ] Is a US company actually needed, or only a sales channel?

### Connected product privacy (outline)

- Tell people when you collect their data (notice at collection), and a right to opt out where state law requires it (CCPA/CPRA and similar)
- Children's data (COPPA) if it applies
- "We are in Belgium so US privacy does not apply" is the myth to reject when you have US users

### Optional US entity (only if asked)

- A Delaware C-corporation is a common US investor request. It is not a legal requirement to take a US purchase order.
- LLC versus C-corporation versus a Belgian company with a US distributor: tax consequences and rules on selling company shares (securities) — a US lawyer.
- Dual Belgian + Delaware structures create issues between the companies and about who owns intellectual property (IP) — `belgian-corporate-law`, `belgian-fiscal-tax`, a US lawyer.

## Terminology

- FCC (US radio rules), UL, ETL (US safety listing marks), OSHA (US workplace safety), CPSC (US consumer product safety)
- EAR (Export Administration Regulations), ITAR (International Traffic in Arms Regulations), ECCN (export classification — a specialist assigns it)
- Sales-tax nexus (a tax presence in a state; not the same as having a US company)
- CCPA/CPRA (California privacy law), COPPA (US children's privacy law)
- LLC, C-corp (company forms — a lawyer; optional)

## Cross-links

| Need | Skill |
| --- | --- |
| General first sorting | `legal-advice` |
| EU sales | `european-law`, `product-compliance` |
| Supply from the US | `supply-chain-management` |
| Web3 tokens and US securities or commodities regulators (SEC/CFTC) | `web3-blockchain`, a lawyer |

## Practical constraints

- Risk of being sued in the US leads to careful safety documentation even for open hardware.
- Agents cannot assign an ECCN with certainty. Flag this for specialist review.
- Tariffs and US extra tariff lists (Section 301) affect the bill of materials. Coordinate `finance` and `supply-chain-management`.
- Agents do not file FCC, Internal Revenue Service (IRS), or state tax registrations.
