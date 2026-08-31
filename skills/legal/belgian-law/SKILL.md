---
name: belgian-law
description: >-
  Belgian legal context for commercial, civil, and regulatory matters affecting
  a cooperative hardware venture in Belgium. Use for Belgium-specific rules,
  institutions, and procedures — escalate binding advice to Belgian counsel;
  not for tax-only or pure corporate statute detail.
---
# Belgian Law

Use this skill when Belgian jurisdiction governs or the venture operates from Belgium.

## Scope

**Owns:**
- Belgian legal system overview (civil law, languages, courts)
- Commercial and consumer law basics (B2B/B2C sales, warranties, unfair terms awareness)
- Employment law touchpoints (if hiring in Belgium — high level)
- Privacy: Belgian DPA (GBA/APD) context with GDPR (`european-law`)
- Product safety/market surveillance interfaces with `product-compliance`
- Dispute resolution venues (Belgian courts, arbitration)
- Public procurement awareness (if selling to Belgian public sector)

**Does NOT own:**
- Detailed tax/VAT → `belgian-fiscal-tax`
- Cooperative company law statutes → `belgian-corporate-law`
- EU-wide regulation text → `european-law` (Belgium as member state implementation)
- US law → `us-law`
- Authoritative legal opinions

## Core principles

- **Federal complexity:** Belgium has federal/regional/community competences; identify which matter (economy, employment, environment).
- **Multilingual:** Contracts and labels may need FR/NL (and DE in some regions) — coordinate `marketing`, `product-compliance`.
- **Cooperative form matters:** Legal shape affects liability and governance — tight link to `belgian-corporate-law`.
- **Token and incentive systems:** Consumer-facing token claims and promotions → `token-engineering`, `belgian-fiscal-tax`.
- **Open hardware still Belgian merchant:** Consumer guarantees and product safety apply.

## Key workflows

### Belgium nexus check

- [ ] Where incorporated? (`belgian-corporate-law`)
- [ ] Where goods ship from?
- [ ] B2B vs B2C?
- [ ] Regulated sector (medical, food contact)? → specialist counsel

### Consumer B2C flags (high level)

- Warranty and conformity rules differ from B2B
- Right of withdrawal where applicable
- Clear pricing and language requirements

## Institutions

- Belgian Economic Law Code (commercial practices — verify current books)
- GBA/APD (data protection)
- FOD Economie (product safety/market surveillance interfaces)

## Cross-links

| Need | Skill |
| --- | --- |
| EU frameworks | `european-law` |
| Tax | `belgian-fiscal-tax` |
| Cooperative statutes | `belgian-corporate-law` |
| Token / incentive systems | `token-engineering` |
| CE marking | `product-compliance` |
| General triage | `legal-advice` |

## Practical constraints

- Language and region affect enforceability of consumer communications.
- Agents must not file with authorities on user's behalf without explicit authorization.
- Cross-border workers/members add immigration and social security complexity — counsel required.
