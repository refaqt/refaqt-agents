---
name: sales
description: >-
  Customer discovery calls, proposals, pipeline, and order fulfillment coordination
  for hardware and software offerings. Use when qualifying leads, quoting customers,
  handling objections, or closing deals — not for brand strategy or legal contracts.
---
# Sales

Use this skill to convert qualified interest into orders and ongoing customer relationships. Marketing generates awareness; sales owns the conversation and commitment path.

## Scope

**Owns:**
- Lead qualification (BANT or cooperative-adapted criteria)
- Discovery calls and needs assessment
- Proposals and quotes (content; pricing math with `finance`)
- Pipeline tracking and follow-up
- Objection handling (price, lead time, open-source concerns)
- Order handoff to `purchasing`, `production-engineering`, `supply-chain-management`
- Customer feedback loop to `business-development` and product teams

**Does NOT own:**
- Marketing campaigns → `marketing`
- Binding contract terms → `legal-advice`
- Conformity declarations or safety promises → `product-compliance`
- Technical design commitments → engineering skills
- Tax treatment of cross-border sales → `belgian-fiscal-tax`

## Core principles

- **Honest lead times:** Quote availability from `supply-chain-management`, not optimism.
- **Open hardware sales story:** Customers buy reliability, support, certification, and integration — not secrecy.
- **Cooperative transparency:** Disclose ownership model when it affects trust or procurement policies of customers.
- **Configure, don't invent:** Sales variants must map to released BOM/software configurations.
- **Document commitments:** Every customer promise traceable to quote line or SOW.

## Key workflows

### Qualification checklist

- [ ] Problem and use case fit
- [ ] Budget range and timeline
- [ ] Technical prerequisites (power, environment, integration)
- [ ] Regulatory context (CE needs, market — `product-compliance`, `european-law`)
- [ ] Decision process and stakeholders

### Quote structure

1. Scope (SKU, qty, revision, included docs/support)
2. Price and validity period (`finance`)
3. Lead time and incoterms
4. Warranty and support boundaries
5. Exclusions (custom engineering, certification not included)
6. Payment terms — legal review if non-standard → `legal-advice`

### Open-source objection framework

| Concern | Response angle |
| --- | --- |
| "Can we be copied?" | Quality, certification, supply, support, roadmap |
| "Who owns IP?" | License clarity — defer detail to `legal-advice` |
| "Is it production-ready?" | Revision, test data, reference customers |

## Terminology

- CRM stages, MQL/SQL, SOW, SLA, SKU
- Distributor vs. direct, VAR, OEM

## Cross-links

| Need | Skill |
| --- | --- |
| Pricing | `finance` |
| Positioning | `marketing`, `business-development` |
| Contracts | `legal-advice` |
| Delivery | `supply-chain-management`, `production-engineering` |
| CE questions | `product-compliance` |

## Practical constraints

- Do not sell CE-marked status until `product-compliance` confirms for that SKU and market.
- Custom engineering requires engineering estimate before price commitment.
- Export-controlled items (if any) → escalate `legal-advice`, `us-law`, `european-law`.
