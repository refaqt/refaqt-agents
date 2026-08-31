---
name: legal-advice
description: >-
  General legal triage for cooperative hardware ventures — when to research,
  what to escalate, and how to scope questions. Use for contracts, IP, liability,
  and compliance routing. NOT a substitute for qualified human counsel; defer
  jurisdiction-specific detail to belgian-law, european-law, or us-law skills.
---
# Legal Advice (General Triage)

Use this skill to **frame legal questions**, identify risk areas, and **route** to the right jurisdiction or specialist skill. Agents provide information and drafting support, not authoritative legal advice.

## Scope

**Owns:**
- Legal question triage (urgency, jurisdiction, subject matter)
- Contract structure overview (MSA, SOW, NDA, license, distributor, CLA)
- IP strategy overview (copyright, patents, trademarks, trade secrets) in open-hardware context
- Liability and warranty language flags (not final wording)
- Privacy/GDPR awareness routing (detail → `european-law`, `belgian-law`)
- Escalation criteria to human counsel
- Checklists before signing or publishing

**Does NOT own:**
- Authoritative interpretation of Belgian statute → `belgian-law`, `belgian-corporate-law`, `belgian-fiscal-tax`
- EU regulatory detail → `european-law`
- US federal/state detail → `us-law`
- CE technical conformity → `product-compliance`
- Tax calculations → `belgian-fiscal-tax`

## Core principles

- **Not a lawyer:** State uncertainty; recommend qualified counsel for high-stakes decisions.
- **Jurisdiction first:** Belgian cooperative selling in EU and US triggers multiple skills — map all.
- **Open licenses are legal instruments:** GPL, CERN OHL, TAPR — understand obligations before applying.
- **Document decisions:** Use ADRs and `log`; preserve privilege by separating legal review threads when counsel involved.
- **Cooperative governance intersects law:** Articles, member agreements → `belgian-corporate-law`.

## When to use this vs. jurisdiction skills

| Situation | Start here | Then |
| --- | --- | --- |
| "Can we use this license on our PCB files?" | `legal-advice` | `european-law` if EU enforcement; counsel if mixed assets |
| "Is this clause enforceable in Belgium?" | Route to `belgian-law` | Counsel for signing |
| "GDPR for our device telemetry?" | `legal-advice` outline | `european-law`, `belgian-law` |
| "Delaware customer warranty dispute?" | `us-law` | Counsel |
| "VAT on imports?" | `belgian-fiscal-tax` | not general legal |
| "Do we need CE?" | `product-compliance` | `european-law` for framework |

## Key workflows

### Contract review triage

1. Parties, jurisdiction, governing law
2. Scope, deliverables, acceptance
3. IP ownership and license grants
4. Liability cap, indemnity, insurance
5. Termination, assignment, dispute resolution
6. Flag red lines → human counsel

### Open hardware IP checklist

- [ ] License on mechanical, electrical, firmware, docs — compatible?
- [ ] Third-party components: license stack documented
- [ ] Trademarks on product name — clearance needed?
- [ ] Contributor License Agreement or DCO policy (`open-source-community`)
- [ ] Patent grant clauses understood?

### Escalation triggers (always human counsel)

- Personal liability, criminal exposure, regulatory investigation
- Notified body or authority correspondence
- Funding instruments with covenants
- Member expulsion or cooperative restructuring
- Cross-border M&A or major asset sale

## Cross-links

| Need | Skill |
| --- | --- |
| Belgium | `belgian-law`, `belgian-corporate-law`, `belgian-fiscal-tax` |
| EU | `european-law` |
| US | `us-law` |
| CE | `product-compliance` |
| Web3 tokens | `web3-blockchain` + counsel |

## Practical constraints

- Never represent that agent output satisfies statutory duties (company secretary, tax adviser, notified body).
- Cooperative statutes and worker co-op rules vary — default Belgium context only when user confirms.
- Keep privileged counsel documents out of public repos.
