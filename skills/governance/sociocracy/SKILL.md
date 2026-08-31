---
name: sociocracy
description: >-
  Sociocracy 3.0 (S3) patterns for cooperative governance — circles, consent,
  tensions, and policy creation. Use when structuring decisions, meetings, and
  role accountabilities in the venture — not replacing Belgian corporate law.
---
# Sociocracy 3.0

Use this skill to run adaptive governance with S3 patterns inside a cooperative hardware venture.

## Scope

**Owns:**
- Circle structure and domain clarity
- Consent decision-making (proposals, objections, integrations)
- Role definitions (purpose, accountabilities, domains)
- Tension processing and governance backlog
- Meeting formats (check-in, building proposals, consent rounds)
- Strategy and OKR-style alignment across circles
- Linking between circles (double linking concept)

**Does NOT own:**
- Statutory GA/board decisions → `belgian-corporate-law`
- Legal contract approval → `legal-advice`
- Day-to-day sprint execution → `agile`
- External community governance alone → `open-source-community`
- Tax or budget accounting → `finance`, `belgian-fiscal-tax`

## Core principles

- **Equivalence:** Voices matter; integrate objections, not majority override by default.
- **Transparency:** Record policies, roles, and decisions accessibly (`log`, `docs/decisions/`).
- **Empirical governance:** Policies are experiments — review and evolve.
- **Cooperative + S3:** Statutes set hard bounds; S3 operates inside them.
- **Work aligns to purpose:** Open hardware mission visible in circle aims.

## Key workflows

### Proposal template

- **Driver:** What tension or opportunity?
- **Proposal:** Specific policy/project change
- **Impact:** Who/what affected (budget → `finance`; safety → `product-compliance`)
- **Consent round:** Clarifying questions → quick reactions → objections → integration

### Objection test

Objection valid if proposal causes **harm** outside role's capacity to accept, not mere preference.

### Role description (S3)

| Field | Content |
| --- | --- |
| Purpose | Why role exists |
| Domains | Where authority applies |
| Accountabilities | Ongoing activities |
| Dependencies | Other skills/circles |

Map agent **skills** to human **roles** where helpful — skills don't replace consent.

### Circle startup

1. Define domain and purpose
2. Elect/consent facilitator and secretary
3. Initial role inventory (engineering, business, legal liaisons)
4. Link to parent circle strategy

## Terminology

- Circle, sub-circle, general circle
- Consent (not consensus unanimity)
- Tension, driver, proposal, integration
- Double link, delegate, rep link

## Cross-links

| Need | Skill |
| --- | --- |
| Corporate limits | `belgian-corporate-law` |
| Budget proposals | `finance` |
| Delivery | `agile` |
| Community | `open-source-community` |
| Web3 governance experiments | `web3-blockchain` |

## Practical constraints

- Consent does not bypass regulatory or safety mandates (`product-compliance`).
- Document integrations in `docs/decisions/` for audit trail.
- Remote/async circles need written proposal discipline.
