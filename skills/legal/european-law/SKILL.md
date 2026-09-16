---
name: european-law
description: >-
  EU legal and regulatory rules for startup founders who sell products,
  software, or data services in Europe. Covers regulations versus directives,
  EU privacy law (GDPR), market access, and consumer rules. Use this for
  EU-level rules. Do not use this for Belgian local detail (see belgian-law)
  or for US law.
---
# European Law

Use this skill for EU-level rules that apply across member states: product regulations, digital rules, privacy, basic competition rules, and access to the market.

## How to answer founders

Follow `.agents/rules/communication.md`. Extra for this skill:

- Everyday words first, official term next: the EU product safety mark (CE marking), EU privacy law (GDPR), a data protection impact assessment (DPIA), standard contractual clauses (SCCs).
- In step 4, tell the founder when to call a lawyer.
- Disclaimer: this is not a replacement for a lawyer.
- Do not turn the law into simple myths: GDPR applies to small companies; publishing open-source designs does not skip product law when you put a product on the market; a regulation is not the same as a directive.
- Do not invent extra time to comply (grace periods), GDPR fine amounts as "what you will pay," or CE marking transition dates. If a date matters, say it must be checked against the current official combined text.
- Say "Belgium still has to write this directive into Belgian law" rather than naming an internal skill.

**Bad:** "Regulations vs. directives: know direct applicability vs. national implementation."
**Good:** "Two kinds of EU rules. A regulation (GDPR is one) applies in Belgium automatically. A directive sets a goal; Belgium must write it into Belgian law, so the local text can differ. Do not assume a blog post about 'the EU rule' is what a Belgian inspector will apply."

**Bad:** "Open source ≠ unregulated product."
**Good:** "Putting the design files (CAD) on GitHub is not the same as selling a machine. If you put a finished product on the EU market, product law still applies — CE marking, safety files, the right economic-operator role (manufacturer, importer, or distributor). Open source does not cancel that."

## Scope

**Owns:**
- Overview of EU institutions (Commission, Parliament, CE marking system)
- Regulation versus directive (a direct EU rule versus a rule Belgium must write into Belgian law)
- Selling across the EU, the single market, and free movement of goods
- Map of product laws (machinery, electromagnetic compatibility (EMC), Low Voltage Directive (LVD), Radio Equipment Directive (RED), restricted substances (RoHS), chemicals (REACH), waste electrical equipment (WEEE))
- GDPR principles and roles (the controller decides why data is used; the processor handles data for them) at EU level, including small connected products
- EU consumer rights directives (overview only)
- EU export-control regimes awareness (goods that have civilian and military use, called dual-use) — send this to a lawyer
- Government support to companies (state aid) and cooperative subsidy awareness (overview only)

**Does NOT own:**
- How a member state writes an EU directive into national law (transposition) → `belgian-law`, other member-state lawyers
- Belgian tax → `belgian-fiscal-tax`
- Technical test evidence → `product-compliance`
- US rules that apply outside the US → `us-law`

## Core principles

- **Regulations versus directives:** A regulation applies in EU countries by itself (direct applicability). A directive needs a national law.
- **One product, many member states:** If you sell from Belgium into France or Germany, you are usually still in the EU product and consumer system. You also face local language and local enforcement.
- **Harmonized standards:** Link product design to a presumption of conformity (`product-compliance`). Harmonized standards are agreed technical standards listed by the EU. If you follow them, the law often treats the product as meeting the rule.
- **GDPR is EU-wide and does not depend on company size:** A five-person startup with identifiable usage data still needs a lawful reason (lawful basis) to process it. Fines are not the only risk. A customer or data-protection authority (DPA) complaint can stop a launch.
- **Open source does not mean an unregulated product:** EU product law applies when you put the product on the market (placing on the market).
- **Brexit/UK:** The UK mark (UKCA) is separate. Note this when selling to the UK.

## Key workflows

### Selling across the EU (founder map)

1. What are you putting on the market — goods, services, software, or a connected device?
2. Which EU acts apply (list with citations; do not invent)
3. Who is the manufacturer, importer, or distributor? You can be more than one.
4. Languages of labels, manuals, and consumer terms
5. VAT and invoicing are tax, not this skill → `belgian-fiscal-tax`
6. After sale: support, recalls, GDPR requests to delete data

### EU market entry map (products)

1. Product category and intended use
2. Applicable EU acts (list with citations)
3. How you prove conformity (`product-compliance`)
4. Economic operator roles (manufacturer, importer, distributor)
5. Labeling and documentation languages
6. Duties after the product is on the market

### GDPR for a small connected product

- [ ] What personal data is collected (a serial number plus an email counts; usage traces may count)?
- [ ] Purpose and lawful reason (lawful basis). Consent is not always required, and it is not always enough.
- [ ] Collect only what you need (data minimization), and do not keep it longer than needed (retention). Do not keep logs only because you might need them later.
- [ ] Processor agreements if a cloud vendor stores the data
- [ ] Transfers of data outside the EU/EEA (the European Economic Area). Use standard contractual clauses (SCCs) and extra assessment.
- [ ] Think about a data protection impact assessment (DPIA) when the processing is high-risk (always-on location, body data such as fingerprints (biometrics), large-scale monitoring)
- [ ] A data protection officer (DPO) is required only in defined cases. Do not skip GDPR because you have no DPO.

Size of the company is not an exemption. Send Belgian enforcement context to `belgian-law` (GBA/APD).

### Data from devices (GDPR outline)

- [ ] What personal data is collected?
- [ ] Purpose and lawful reason (lawful basis)
- [ ] Collect only what you need (data minimization), and do not keep it longer than needed (retention)
- [ ] Processor agreements if a cloud vendor stores the data
- [ ] Transfers of data across borders (SCCs and similar)

## Terminology

- CE marking, harmonized standards, notified body (an official testing body)
- GDPR, DPIA, DPO (when required), SCCs (standard contractual clauses for transfers of personal data outside the EU)
- WEEE, RoHS, REACH substances of very high concern (SVHC)
- Regulation (applies by itself) versus directive (needs a national law)
- Putting a product on the market versus publishing source files

## Cross-links

| Need | Skill |
| --- | --- |
| CE execution | `product-compliance` |
| Belgium-specific | `belgian-law` |
| Contracts | `legal-advice` |
| Web3 tokens in the EU | `token-engineering`, `web3-blockchain`, a lawyer (Markets in Crypto-Assets (MiCA) and similar) |

## Practical constraints

- EU law changes. Check current official combined texts for high-stakes decisions.
- Machinery Regulation transition dates matter. Cross-check with `product-compliance`.
- The EU Artificial Intelligence Act (AI Act) and machinery rules can overlap. Watch this for connected products that act on their own.
