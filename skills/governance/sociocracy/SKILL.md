---
name: sociocracy
description: >-
  Sociocracy 3.0 (S3) patterns for how a cooperative makes decisions — circles,
  consent, tensions, and writing policy. Use when you structure decisions,
  meetings, and role duties (accountabilities) in the venture — not as a
  replacement for Belgian company law.
---
# Sociocracy 3.0

Use this skill to run flexible governance with Sociocracy 3.0 (S3) patterns inside a cooperative hardware venture.

## Scope

**Owns:**
- Circle structure and a clear domain for each circle
- Consent decision-making (proposals, objections, and changing a proposal to remove harm (integration))
- Role definitions (purpose, ongoing duties (accountabilities), domains)
- Working through tensions and the list of governance work (governance backlog)
- Meeting formats (check-in, building proposals, consent rounds)
- Strategy and goal alignment across circles (objectives and key results (OKRs) style)
- Links between circles (two-way links, called double linking)

**Does NOT own:**
- Legal general assembly (GA) and board decisions → `belgian-corporate-law`
- Legal contract approval → `legal-advice`
- Day-to-day work-cycle delivery (sprints) → `agile`
- External community governance on its own → `open-source-community`
- Tax or budget accounting → `finance`, `belgian-fiscal-tax`

## Core principles

- **Equivalence:** Every voice matters. Integrate objections. Do not let a majority vote override them by default.
- **Transparency:** Record policies, roles, and decisions where people can find them (`log`, `docs/decisions/`).
- **Governance based on experience:** Treat policies as tests. Review them and change them.
- **Cooperative plus S3:** Company statutes set hard limits. Sociocracy 3.0 (S3) works inside those limits.
- **Work aligns to purpose:** Keep the open hardware mission visible in each circle's aims.

## Key workflows

### Proposal template

- **Driver:** What tension or opportunity?
- **Proposal:** A specific policy or project change
- **Impact:** Who or what is affected (budget → `finance`; safety → `product-compliance`)
- **Consent round:** Clarifying questions → quick reactions → objections → integration

### Objection test

An objection is valid if the proposal would cause **harm** that the role cannot accept. A mere preference is not a valid objection.

### Role description (S3)

| Field | Content |
| --- | --- |
| Purpose | Why the role exists |
| Domains | Where authority applies |
| Accountabilities | Ongoing activities |
| Dependencies | Other skills or circles |

Map agent **skills** to human **roles** where that helps. Skills do not replace consent.

### Circle startup

1. Define domain and purpose
2. Elect or consent a facilitator and a secretary
3. First list of roles (engineering, business, legal contacts)
4. Link to the parent circle's strategy

## Terminology

- Circle, sub-circle, general circle
- Consent (not the same as everyone agreeing, which is consensus)
- Tension, driver, proposal, integration
- Double link, delegate, representative link (rep link)

## Cross-links

| Need | Skill |
| --- | --- |
| Corporate limits | `belgian-corporate-law` |
| Budget proposals | `finance` |
| Delivery | `agile` |
| Community | `open-source-community` |
| Web3 governance experiments | `web3-blockchain` |

## Practical constraints

- Consent does not skip regulatory or safety duties (`product-compliance`).
- Write integrations in `docs/decisions/` so there is an audit trail.
- Circles that work remotely or at different times need written proposals.
