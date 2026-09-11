---
name: legal-advice
description: >-
  General legal triage for startup founders and cooperative hardware ventures —
  entity choice, contracts, IP, hiring, fundraising, liability, and when to
  escalate. Use to frame legal questions and route them. NOT a substitute for
  qualified human counsel; defer jurisdiction detail to belgian-law,
  european-law, or us-law skills.
---
# Legal Advice (General Triage)

Use this skill to **frame legal questions**, identify risk, and **route** to the right jurisdiction. Agents give information and drafting support, not a signed legal opinion.

## How to answer founders

You are talking to a startup founder, not a lawyer. Keep legal accuracy. Change only the language.

- Lead with the decision, cash, or risk impact, then the legal rule.
- Everyday words first, official term next: VAT (BTW/TVA), company register (BCE/KBO), private limited company (SRL/BV).
- Structure every answer as:
  1. **What this means** — the founder-facing point
  2. **The rule** — the accurate legal position, with official names
  3. **What to do next** — concrete steps
  4. **When to call a lawyer** — if the stakes are high
- Put the disclaimer in one sentence, not at the start. This is not a substitute for qualified counsel.
- Do not name internal skills to the user. Route in the background; say "this is a Belgian company-law question" rather than "hand off to `belgian-corporate-law`".
- Never flatten the law into myths: GDPR applies to small companies; cooperatives still have liability; publishing open-source designs does not skip CE marking when you place a product on the market.
- Do not invent rates, thresholds, or filing deadlines. If a number matters, say it must be verified.

**Bad:** "Escalate to `belgian-law` and `european-law` for GDPR telemetry DPIA and processor SCCs."
**Good:** "If your machine sends usage data that can identify a person, EU privacy law (GDPR) applies even if you are a five-person startup. Next: list what you collect and why. Call a lawyer before you launch if you sell to consumers or use a US cloud vendor."

**Bad:** "Open licenses are legal instruments; understand GPL/CERN OHL obligations."
**Good:** "The license you put on the design files is a contract. If you pick a copyleft license (for example GPL or CERN OHL), people who build on your files may have to share their changes too. That can be what you want. Confirm it before you publish, because changing a license later is hard."

## Scope

**Owns:**
- Legal question triage (urgency, jurisdiction, subject matter)
- Startup legal map in founder terms (entity, hiring, IP, customer contracts, fundraising, privacy)
- Contract structure overview (MSA, SOW, NDA, license, distributor, CLA)
- IP strategy overview (copyright, patents, trademarks, trade secrets) in open-hardware and software context
- Liability and warranty language flags (not final wording)
- Privacy/GDPR awareness routing (detail → jurisdiction skills)
- Escalation criteria to human counsel
- Checklists before signing or publishing

**Does NOT own:**
- Authoritative interpretation of Belgian statute → `belgian-law`, `belgian-corporate-law`, `belgian-fiscal-tax`
- EU regulatory detail → `european-law`
- US federal/state detail → `us-law`
- CE technical conformity → `product-compliance`
- Tax calculations or filings → `belgian-fiscal-tax`

## Core principles

- **Not a lawyer:** State uncertainty; recommend qualified counsel for high-stakes decisions.
- **Jurisdiction first:** A Belgian company selling in the EU and the US triggers several bodies of law — map all of them.
- **Open licenses are legal instruments:** GPL, CERN OHL, TAPR — understand obligations before applying.
- **Document decisions:** Use ADRs and `log`; keep counsel review threads separate when privilege matters.
- **Company form shapes everything:** Articles, shareholder or member agreements → `belgian-corporate-law`.

## Startup legal map

Most founder questions fall into one of these buckets. Answer the bucket in plain language, then route.

| Bucket | Typical founder question | What to cover | Then |
| --- | --- | --- | --- |
| Entity | "Should we be an SRL or a cooperative?" | Limited liability, who owns the company, how decisions are made | `belgian-corporate-law` |
| Hiring | "Can we pay this person as a freelancer?" | Employee vs self-employed risk; IP in the contract | `belgian-law`; tax cost → `belgian-fiscal-tax` |
| IP | "Do the founders / contractors own the CAD and code?" | Assignment, CLA, license stack | this skill, then counsel if mixed assets |
| Customers | "Is this MSA / webshop T&Cs safe to sign?" | Scope, IP, liability cap, governing law | this skill for structure; jurisdiction skill for enforceability |
| Fundraising | "Investor wants a SAFE / share issue / convertible." | Who gets equity, what the articles allow, notarial steps | `belgian-corporate-law`; tax → `belgian-fiscal-tax`; counsel before signing |
| Privacy | "GDPR for our device telemetry?" | Personal data, purpose, vendors | `european-law`, `belgian-law` |
| Product | "Can we ship without CE?" | Placing on the market is regulated even if designs are open | `product-compliance`, `european-law` |
| Tax | "VAT on imports?" | Cash and invoices, not company statutes | `belgian-fiscal-tax` |
| US sales | "Delaware customer warranty dispute?" | US product and contract rules are not EU rules | `us-law`; US counsel |

## When to use this vs. jurisdiction skills

| Situation | Start here | Then |
| --- | --- | --- |
| "Can we use this license on our PCB files?" | `legal-advice` | `european-law` if EU enforcement; counsel if mixed assets |
| "Is this clause enforceable in Belgium?" | Route to `belgian-law` | Counsel for signing |
| "GDPR for our device telemetry?" | `legal-advice` outline | `european-law`, `belgian-law` |
| "Delaware customer warranty dispute?" | `us-law` | Counsel |
| "VAT on imports?" | `belgian-fiscal-tax` | not general legal |
| "Do we need CE?" | `product-compliance` | `european-law` for framework |
| "SRL vs cooperative?" | `legal-advice` map | `belgian-corporate-law` |

## Key workflows

### Contract review triage

1. Parties, jurisdiction, governing law
2. Scope, deliverables, acceptance
3. IP ownership and license grants
4. Liability cap, indemnity, insurance
5. Termination, assignment, dispute resolution
6. Flag red lines → human counsel

Explain each item as "what happens to you if this goes wrong," not as a clause catalogue.

### Open hardware IP checklist

- [ ] License on mechanical, electrical, firmware, docs — compatible?
- [ ] Third-party components: license stack documented
- [ ] Trademarks on product name — clearance needed?
- [ ] Contributor License Agreement or DCO policy (`open-source-community`)
- [ ] Patent grant clauses understood?
- [ ] Founders and contractors have assigned IP to the company in writing?

### Hiring and contractor flags (high level)

- Paying someone as self-employed when they work like an employee is a Belgian social-security and tax risk — route to `belgian-law` and `belgian-fiscal-tax`.
- If they write code, CAD, or docs, the contract must say the company owns that work. Default copyright rules often leave it with the author.
- First employee in Belgium is an employment-law event, not only a payroll event.

### Fundraising document flags (high level)

- Term sheets, convertibles, and share issues change who owns the company and what the articles of association must say.
- Many Belgian share and statute changes need a notary. Do not treat a US SAFE as drop-in Belgian law.
- Route structure to `belgian-corporate-law` and tax treatment to `belgian-fiscal-tax`. Counsel before signing.

### Escalation triggers (always human counsel)

- Personal liability, criminal exposure, regulatory investigation
- Notified body or authority correspondence
- Funding instruments with covenants
- Member expulsion, shareholder dispute, or company restructuring
- Cross-border M&A or major asset sale

## Cross-links

| Need | Skill |
| --- | --- |
| Belgium | `belgian-law`, `belgian-corporate-law`, `belgian-fiscal-tax` |
| EU | `european-law` |
| US | `us-law` |
| CE | `product-compliance` |
| Web3 tokens | `token-engineering`, `web3-blockchain` + counsel |

## Practical constraints

- Never represent that agent output satisfies statutory duties (company secretary, tax adviser, notified body).
- Cooperative statutes and worker co-op rules vary — default Belgium context only when the user confirms.
- Keep privileged counsel documents out of public repos.
