---
name: european-law
description: >-
  European Union legal and regulatory frameworks affecting products, commerce,
  data, and cross-border operations. Use for EU directives, regulations, market
  access, and GDPR context — not national implementation detail (see belgian-law)
  or US law.
---
# European Law

Use this skill for EU-level rules that harmonize across member states: product regulations, digital rules, competition basics, and market access.

## Scope

**Owns:**
- EU institutional overview (Commission, Parliament, CE marking system)
- Product legislation landscape (machinery, EMC, LVD, RED, RoHS, REACH, WEEE)
- GDPR principles and roles (controller/processor) at EU level
- EU consumer rights directives (high level)
- Single market / free movement concepts
- Export control EU regimes awareness (dual-use) — escalate counsel
- State aid and cooperative subsidy awareness (high level)

**Does NOT own:**
- National transposition details → `belgian-law`, other MS counsel
- Belgian tax → `belgian-fiscal-tax`
- Technical test evidence → `product-compliance`
- US extraterritorial rules → `us-law`

## Core principles

- **Regulations vs. directives:** Know direct applicability vs. national implementation.
- **Harmonized standards:** Link product design to presumption of conformity (`product-compliance`).
- **GDPR is EU-wide:** Data from connected machines needs lawful basis and DPIA thinking.
- **Open source ≠ unregulated product:** EU product law applies at point of placing on market.
- **Brexit/UK:** UKCA separate; note when selling to UK.

## Key workflows

### EU market entry map

1. Product category and intended use
2. Applicable EU acts (list with citations)
3. Conformity module (`product-compliance`)
4. Economic operator roles (manufacturer, importer, distributor)
5. Labeling and documentation languages
6. Post-market obligations

### Data from devices (GDPR outline)

- [ ] What personal data collected?
- [ ] Purpose and lawful basis
- [ ] Data minimization and retention
- [ ] Processor agreements if cloud vendor
- [ ] Cross-border transfers (SCCs etc.)

## Terminology

- CE, harmonized standards, notified body
- GDPR, DPIA, DPO (when required)
- WEEE, RoHS, REACH SVHC

## Cross-links

| Need | Skill |
| --- | --- |
| CE execution | `product-compliance` |
| Belgium-specific | `belgian-law` |
| Contracts | `legal-advice` |
| Web3 tokens EU | `web3-blockchain`, counsel (MiCA etc.) |

## Practical constraints

- EU law evolves; verify current consolidated texts for high-stakes decisions.
- Machinery Regulation transition dates matter — cross-check with `product-compliance`.
- AI Act and machinery intersection emerging — monitor for connected autonomous functions.
