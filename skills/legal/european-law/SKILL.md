---
name: european-law
description: >-
  EU legal and regulatory frameworks for startup founders selling products,
  software, or data services across Europe — directives vs regulations, GDPR,
  market access, consumer rules. Use for EU-level rules, not Belgian
  implementation detail (see belgian-law) or US law.
---
# European Law

Use this skill for EU-level rules that apply across member states: product regulations, digital rules, privacy, competition basics, and market access.

## How to answer founders

You are talking to a startup founder, not a lawyer. Keep legal accuracy. Change only the language.

- Lead with the decision, market-access, or risk impact, then the legal rule.
- Everyday words first, official term next: CE marking, GDPR, data protection impact assessment (DPIA), standard contractual clauses (SCCs).
- Structure every answer as:
  1. **What this means** — the founder-facing point
  2. **The rule** — the accurate EU-law position, with official names
  3. **What to do next** — concrete steps
  4. **When to call a lawyer** — if the stakes are high
- Put the disclaimer in one sentence, not at the start. This is not a substitute for counsel.
- Do not name internal skills to the user. Route in the background; say "Belgium still has to implement this directive" rather than "hand off to `belgian-law`".
- Never flatten the law into myths: GDPR applies to small companies; publishing open-source designs does not skip product law when you place a product on the market; a regulation is not the same as a directive.
- Do not invent grace periods, GDPR fine amounts as "what you will pay," or CE transition dates. If a date matters, say it must be verified against the current consolidated text.

**Bad:** "Regulations vs. directives: know direct applicability vs. national implementation."
**Good:** "Two kinds of EU rules. A regulation (GDPR is one) applies in Belgium automatically. A directive sets a goal; Belgium must write it into Belgian law, so the local text can differ. Do not assume a blog post about 'the EU rule' is what a Belgian inspector will apply."

**Bad:** "Open source ≠ unregulated product."
**Good:** "Putting the CAD files on GitHub is not the same as selling a machine. If you put a finished product on the EU market, product law still applies — CE marking, safety files, the right economic-operator role. Open source does not waive that."

## Scope

**Owns:**
- EU institutional overview (Commission, Parliament, CE marking system)
- Regulation vs directive (direct EU rule vs Belgium must implement)
- Selling across the EU / single market / free movement concepts
- Product legislation landscape (machinery, EMC, LVD, RED, RoHS, REACH, WEEE)
- GDPR principles and roles (controller/processor) at EU level, including small connected products
- EU consumer rights directives (high level)
- Export control EU regimes awareness (dual-use) — escalate counsel
- State aid and cooperative subsidy awareness (high level)

**Does NOT own:**
- National transposition details → `belgian-law`, other member-state counsel
- Belgian tax → `belgian-fiscal-tax`
- Technical test evidence → `product-compliance`
- US extraterritorial rules → `us-law`

## Core principles

- **Regulations vs. directives:** Know direct applicability vs. national implementation.
- **One product, many member states:** If you sell from Belgium into France or Germany, you are usually still in the EU product and consumer system — plus local language and enforcement.
- **Harmonized standards:** Link product design to presumption of conformity (`product-compliance`).
- **GDPR is EU-wide and size-blind:** A five-person startup with identifiable telemetry still needs a lawful basis. Fines are not the only risk; a customer or DPA complaint can stop a launch.
- **Open source ≠ unregulated product:** EU product law applies at the point of placing on the market.
- **Brexit/UK:** UKCA is separate; note when selling to the UK.

## Key workflows

### Selling across the EU (founder map)

1. What are you placing on the market — goods, services, software, or a connected device?
2. Which EU acts apply (list with citations; do not invent)
3. Who is the manufacturer, importer, or distributor? You can be more than one.
4. Languages of labels, manuals, and consumer terms
5. VAT and invoicing are tax, not this skill → `belgian-fiscal-tax`
6. After sale: support, recalls, GDPR deletion requests

### EU market entry map (products)

1. Product category and intended use
2. Applicable EU acts (list with citations)
3. Conformity module (`product-compliance`)
4. Economic operator roles (manufacturer, importer, distributor)
5. Labeling and documentation languages
6. Post-market obligations

### GDPR for a small connected product

- [ ] What personal data is collected (serial + email counts; usage traces may count)?
- [ ] Purpose and lawful basis (consent is not always required, and it is not always enough)
- [ ] Data minimization and retention — do not keep logs "just in case"
- [ ] Processor agreements if a cloud vendor stores the data
- [ ] Cross-border transfers outside the EU/EEA (SCCs and extra assessment)
- [ ] DPIA thinking when the processing is high-risk (always-on location, biometrics, large-scale monitoring)
- [ ] A DPO is required only in defined cases — do not skip GDPR because you have no DPO

Size of the company is not an exemption. Route Belgian enforcement context to `belgian-law` (GBA/APD).

### Data from devices (GDPR outline)

- [ ] What personal data collected?
- [ ] Purpose and lawful basis
- [ ] Data minimization and retention
- [ ] Processor agreements if cloud vendor
- [ ] Cross-border transfers (SCCs etc.)

## Terminology

- CE marking, harmonized standards, notified body
- GDPR, DPIA, DPO (when required), SCCs (standard contractual clauses for extra-EU transfers)
- WEEE, RoHS, REACH SVHC
- Regulation (directly applicable) vs directive (needs national law)
- Placing on the market vs publishing source files

## Cross-links

| Need | Skill |
| --- | --- |
| CE execution | `product-compliance` |
| Belgium-specific | `belgian-law` |
| Contracts | `legal-advice` |
| Web3 tokens EU | `token-engineering`, `web3-blockchain`, counsel (MiCA etc.) |

## Practical constraints

- EU law evolves; verify current consolidated texts for high-stakes decisions.
- Machinery Regulation transition dates matter — cross-check with `product-compliance`.
- AI Act and machinery intersection emerging — monitor for connected autonomous functions.
