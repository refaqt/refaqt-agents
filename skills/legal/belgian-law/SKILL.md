---
name: belgian-law
description: >-
  Belgian commercial, civil, employment, and regulatory law for startup founders
  and cooperative hardware ventures. Use for Belgium-specific rules, first hire,
  consumer vs B2B sales, contract language, and disputes — escalate binding
  advice to Belgian counsel; not for tax-only or pure corporate statute detail.
---
# Belgian Law

Use this skill when Belgian jurisdiction governs or the venture operates from Belgium.

## How to answer founders

You are talking to a startup founder, not a lawyer. Keep legal accuracy. Change only the language.

- Lead with the decision, cash, or risk impact, then the legal rule.
- Everyday words first, official term next: Belgian Data Protection Authority (GBA/APD), Economic Law Code (WER/CDE), company register (BCE/KBO).
- Structure every answer as:
  1. **What this means** — the founder-facing point
  2. **The rule** — the accurate Belgian-law position, with official names
  3. **What to do next** — concrete steps
  4. **When to call a lawyer** — if the stakes are high
- Put the disclaimer in one sentence, not at the start. This is not a substitute for Belgian counsel.
- Do not name internal skills to the user. Route in the background; say "that is a tax question" rather than "hand off to `belgian-fiscal-tax`".
- Never flatten the law into myths: a freelancer who works like an employee can be reclassified; consumer buyers have stronger rights than business buyers; French/Dutch language rules can make a consumer contract hard to enforce.
- Do not invent notice periods, warranty lengths, or court fees. If a number matters, say it must be verified.

**Bad:** "Employment law touchpoints (if hiring in Belgium — high level)."
**Good:** "Your first Belgian hire is a legal event, not only a payroll line. If someone works on your schedule, with your tools, and only for you, Belgian law may treat them as an employee even if the invoice says 'freelance'. That can trigger back social security and tax. Get the contract and status checked before they start."

**Bad:** "Warranty and conformity rules differ from B2B."
**Good:** "Selling a kit to a consumer in Belgium is not the same as selling to a factory. Consumers get legal conformity rights and, for many distance sales, a withdrawal period. You cannot contract those away with website small print. Business customers can agree tighter terms — still watch unfair B2B clauses."

## Scope

**Owns:**
- Belgian legal system overview (civil law, languages, courts)
- Commercial and consumer law basics (B2B/B2C sales, warranties, unfair terms awareness)
- First-hire and employment-law touchpoints (employee vs freelance — high level)
- Contract language (FR/NL, and DE in some regions) and what that does to enforceability
- What happens if a customer sues (Belgian courts, arbitration) — venue awareness, not litigation strategy
- Privacy: Belgian DPA (GBA/APD) context with GDPR (`european-law`)
- Product safety/market surveillance interfaces with `product-compliance`
- Public procurement awareness (if selling to Belgian public sector)

**Does NOT own:**
- Detailed tax/VAT → `belgian-fiscal-tax`
- Company statutes, shares, directors → `belgian-corporate-law`
- EU-wide regulation text → `european-law` (Belgium as member state implementation)
- US law → `us-law`
- Authoritative legal opinions

## Core principles

- **Federal complexity:** Belgium splits powers across federal, regional, and community governments. Name which layer you are in (economy, employment, environment) before you guess the rule.
- **Multilingual:** Consumer contracts and product labels may need Dutch and/or French (and German in some areas) — coordinate `marketing`, `product-compliance`.
- **Company form matters:** SRL vs cooperative changes liability and governance — tight link to `belgian-corporate-law`.
- **Status of workers matters:** Calling someone a freelancer does not make it so.
- **Token and incentive systems:** Consumer-facing token claims and promotions → `token-engineering`, `belgian-fiscal-tax`.
- **Open hardware still a Belgian merchant:** Consumer guarantees and product safety apply.

## Key workflows

### Belgium nexus check

- [ ] Where incorporated? (`belgian-corporate-law`)
- [ ] Where goods ship from?
- [ ] B2B vs B2C?
- [ ] First hire or long-term freelancer in Belgium?
- [ ] Contract language vs customer language?
- [ ] Regulated sector (medical, food contact)? → specialist counsel

### First hire (employee vs freelance)

| Signal | Why it matters |
| --- | --- |
| You set hours, tools, and tasks | Looks like employment (subordination) |
| They invoice several clients | Supports genuine self-employed status |
| They write code/CAD for you | IP must be assigned in the contract — `legal-advice` |
| "We'll see after three months" | Still a status and social-security question from day one |

Payroll cost (employer social security, withholding) is a tax question → `belgian-fiscal-tax`. This skill owns the legal status and contract flags. Cross-border workers add immigration and social security complexity — counsel required.

### Consumer B2C vs business B2B (high level)

- Warranty and conformity rules are stronger for consumers than for business buyers
- Right of withdrawal where distance/off-premises rules apply — do not invent the number of days
- Clear pricing and language requirements
- B2B customers can negotiate harder terms; Belgium still polices unfair B2B clauses — do not assume "they are a company so anything goes"

### If a customer sues

1. Which contract and which governing law? (Belgian courts often stay in play if you sell from Belgium to Belgian customers.)
2. Consumer disputes are slower and more protective of the buyer than B2B.
3. Arbitration only helps if the clause is valid for that customer type.
4. Product safety complaints can also go to market surveillance (FOD Economie) — coordinate `product-compliance`.
5. Do not draft a court strategy. Flag counsel when a letter from a lawyer or an authority arrives.

### Contract language

- A consumer-facing contract or webshop only in English can fail Belgian language and transparency rules.
- B2B English contracts are common; still say which language wins if there is a translation.
- Labels and safety manuals follow product rules — `product-compliance`.

## Institutions

- Belgian Economic Law Code (WER/CDE) — commercial practices; verify current books
- GBA/APD (data protection authority)
- FOD Economie / SPF Economie (product safety / market surveillance interfaces)
- Labour courts for employment disputes; enterprise courts for many commercial disputes

## Cross-links

| Need | Skill |
| --- | --- |
| EU frameworks | `european-law` |
| Tax | `belgian-fiscal-tax` |
| Company statutes | `belgian-corporate-law` |
| Token / incentive systems | `token-engineering` |
| CE marking | `product-compliance` |
| General triage | `legal-advice` |

## Practical constraints

- Language and region affect enforceability of consumer communications.
- Agents must not file with authorities on the user's behalf without explicit authorization.
- Cross-border workers/members add immigration and social security complexity — counsel required.
