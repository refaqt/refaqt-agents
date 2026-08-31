---
name: us-law
description: >-
  United States legal and regulatory context for selling, sourcing, or operating
  US-facing aspects of a hardware venture. Use for FCC, OSHA awareness, export
  controls, and US commercial basics — not EU CE or Belgian law.
---
# US Law

Use this skill when the US market, US suppliers, US persons, or US-origin technology affects the venture.

## Scope

**Owns:**
- US regulatory touchpoints for hardware (FCC Part 15/18, OSHA concepts, FDA if applicable)
- UL/ETL listing strategy awareness (market access, not EU CE)
- US commercial basics (UCC Article 2 flavor, limited — counsel for contracts)
- Export controls (EAR/ITAR awareness flags for dual-use components and software)
- US privacy patchwork (CCPA/CPRA high level for connected products)
- Delaware/other state incorporation only if user context — default defer to counsel
- US open source and patent landscape awareness (not legal opinions)

**Does NOT own:**
- EU CE → `product-compliance`, `european-law`
- Belgian operations → `belgian-law`
- Detailed contract drafting → `legal-advice` + US counsel
- Immigration, employment law detail → US counsel

## Core principles

- **No CE in US:** Different conformity paths; don't transfer EU assumptions.
- **Export controls bite open hardware:** Publishing designs may still restrict export of controlled items; escalate.
- **Liability culture:** Warranty disclaimers and limitation clauses scrutinized — US counsel for templates.
- **State variation:** Product, privacy, and employment rules vary by state.
- **Cooperative US forms:** Worker co-ops, LLCs, etc. — specialist counsel.

## Key workflows

### US go-to-market check

- [ ] Product category (consumer, industrial, medical?)
- [ ] FCC authorization path if RF
- [ ] UL/ETL needed for channel?
- [ ] State sales tax nexus (`finance`, US tax counsel)
- [ ] California Prop 65 / chemical warnings if applicable
- [ ] Export classification screening

### Connected product privacy (outline)

- Notice at collection, opt-out where state law requires
- Children's data (COPPA) if applicable

## Terminology

- FCC, UL, OSHA, CPSC
- EAR, ITAR, ECCN (export)
- LLC, C-Corp (entity — counsel)

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
