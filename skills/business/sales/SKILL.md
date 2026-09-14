---
name: sales
description: >-
  Customer discovery calls, proposals, the deal list (pipeline), and handing
  orders to delivery for hardware and software offers. Use when you check if a
  lead is a fit, send a quote, answer objections, or close a deal — not for
  brand strategy or legal contracts.
---
# Sales

Use this skill to turn a checked lead into orders and ongoing customer relationships. Marketing creates awareness. Sales owns the conversation and the path to a commitment.

## Scope

**Owns:**
- Checking if a lead is a fit (budget, authority, need, timeline (BANT), or similar criteria adapted for a cooperative)
- Discovery calls and needs assessment
- Proposals and quotes (the content; price math with `finance`)
- Tracking the deal list (pipeline) and follow-up
- Handling objections (price, wait time, open-source concerns)
- Handing the order to `purchasing`, `production-engineering`, `supply-chain-management`
- Sending customer feedback to `business-development` and product teams

**Does NOT own:**
- Marketing campaigns → `marketing`
- Binding contract terms → `legal-advice`
- Conformity declarations or safety promises → `product-compliance`
- Technical design commitments → engineering skills
- Tax treatment of cross-border sales → `belgian-fiscal-tax`

## Core principles

- **Honest wait times (lead times):** Quote the dates `supply-chain-management` gives you. Do not quote a hopeful date.
- **Open hardware sales story:** Customers buy reliability, support, certification, and integration. They do not buy secrecy.
- **Cooperative transparency:** Explain the ownership model when it affects trust or the customer's buying rules.
- **Configure, do not invent:** Sales variants must map to released bill of materials (BOM) and software configurations.
- **Document commitments:** Every customer promise must link to a quote line or a statement of work (SOW).

## Key workflows

### Qualification checklist

- [ ] Problem and use case fit
- [ ] Budget range and timeline
- [ ] Technical prerequisites (power, environment, integration)
- [ ] Regulatory context (CE needs, market — `product-compliance`, `european-law`)
- [ ] Decision process and stakeholders

### Quote structure

1. Scope (stock keeping unit (SKU), quantity, revision, included docs and support)
2. Price and how long the quote stays valid (`finance`)
3. Wait time and international delivery terms (Incoterms)
4. Warranty and support boundaries
5. Exclusions (custom engineering, certification not included)
6. Payment terms — legal review if they are not standard → `legal-advice`

### Open-source objection framework

| Concern | Response angle |
| --- | --- |
| "Can we be copied?" | Quality, certification, supply, support, roadmap |
| "Who owns IP?" | License clarity — send detail to `legal-advice` |
| "Is it production-ready?" | Revision, test data, reference customers |

## Terminology

- Customer relationship management (CRM) stages, marketing-qualified lead (MQL), sales-qualified lead (SQL), statement of work (SOW), service level agreement (SLA), stock keeping unit (SKU)
- Distributor versus direct, value-added reseller (VAR), original equipment manufacturer (OEM)

## Cross-links

| Need | Skill |
| --- | --- |
| Pricing | `finance` |
| How we describe the offer | `marketing`, `business-development` |
| Contracts | `legal-advice` |
| Delivery | `supply-chain-management`, `production-engineering` |
| CE questions | `product-compliance` |

## Practical constraints

- Do not sell CE-marked status until `product-compliance` confirms it for that stock keeping unit (SKU) and market.
- Custom engineering needs an engineering estimate before you commit to a price.
- Items under export control (if any) → escalate to `legal-advice`, `us-law`, `european-law`.
