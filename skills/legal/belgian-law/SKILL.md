---
name: belgian-law
description: >-
  Belgian commercial, civil, employment, and regulatory law for startup
  founders and hardware cooperatives. Use this for Belgium-specific rules,
  the first hire, consumer versus business sales, contract language, and
  disputes. Binding advice must go to a Belgian lawyer. Do not use this for
  tax-only questions or for company-form detail.
---
# Belgian Law

Use this skill when Belgian law applies, or when the venture operates from Belgium.

## How to answer founders

Follow `.agents/rules/communication.md`. Extra for this skill:

- Everyday words first, official term next: the Belgian Data Protection Authority (GBA/APD), the Economic Law Code (WER/CDE), the company register (BCE/KBO).
- In step 4, tell the founder when to call a Belgian lawyer.
- Disclaimer: this is not a replacement for a Belgian lawyer.
- Do not turn the law into simple myths: a freelancer who works like an employee can be treated as an employee instead; consumer buyers have stronger rights than business buyers; French or Dutch language rules can make a consumer contract hard to enforce.
- Do not invent notice periods, warranty lengths, or court fees.
- Say "that is a tax question" rather than naming an internal skill.

**Bad:** "Employment law touchpoints (if hiring in Belgium — high level)."
**Good:** "Your first Belgian hire is a legal event, not only a payroll line. If someone works on your schedule, with your tools, and only for you, Belgian law may treat them as an employee even if the invoice says 'freelance'. That can mean you owe past social security and tax. Get the contract and status checked before they start."

**Bad:** "Warranty and conformity rules differ from B2B."
**Good:** "Selling a kit to a consumer in Belgium is not the same as selling to a factory. Consumers get legal rights that the product must match what was promised (conformity) and, for many distance sales, a period when they can cancel (withdrawal). You cannot remove those rights with website terms in small text. Business customers can agree stricter terms. Still watch unfair clauses in sales to businesses (B2B)."

## Scope

**Owns:**
- Overview of the Belgian legal system (civil law based on written codes, languages, courts)
- Basics of commercial and consumer law (sales to businesses (B2B) and to consumers (B2C), warranties, unfair terms awareness)
- First-hire and employment-law flags (employee vs freelance — overview only)
- Contract language (French/Dutch, and German in some regions) and what that does to whether a court will apply the contract
- What happens if a customer sues (Belgian courts, private dispute process (arbitration)) — which court may hear the case, not a litigation plan
- Privacy: the Belgian Data Protection Authority (GBA/APD) with EU privacy law (GDPR) (`european-law`)
- Product safety and market surveillance links with `product-compliance`
- Public buying (public procurement) if selling to the Belgian public sector

**Does NOT own:**
- Detailed tax and VAT → `belgian-fiscal-tax`
- Company rulebooks, shares, directors → `belgian-corporate-law`
- EU-wide regulation text → `european-law` (Belgium as a member state that must apply or implement the rule)
- US law → `us-law`
- Official legal opinions

## Core principles

- **Several layers of government:** Belgium splits powers across federal, regional, and community governments. Name which layer you are in (economy, employment, environment) before you guess the rule.
- **Several languages:** Consumer contracts and product labels may need Dutch and/or French (and German in some areas). Coordinate `marketing` and `product-compliance`.
- **Company form matters:** A private limited company (SRL/BV) versus a cooperative changes legal risk (liability) and how the company is run. Tight link to `belgian-corporate-law`.
- **Status of workers matters:** Calling someone a freelancer does not make it so.
- **Token and incentive systems:** Consumer-facing token claims and promotions → `token-engineering`, `belgian-fiscal-tax`.
- **Open hardware is still a Belgian seller:** Consumer guarantees and product safety still apply.

## Key workflows

### Belgium connection check (nexus)

- [ ] Where is the company formed? (`belgian-corporate-law`)
- [ ] Where do goods ship from?
- [ ] Sales to businesses (B2B) or to consumers (B2C)?
- [ ] First hire or long-term freelancer in Belgium?
- [ ] Contract language versus customer language?
- [ ] Regulated sector (medical, food contact)? → a specialist lawyer

### First hire (employee vs freelance)

| Signal | Why it matters |
| --- | --- |
| You set hours, tools, and tasks | Looks like employment (the worker is under your control, called subordination) |
| They invoice several clients | Supports genuine self-employed status |
| They write code or design files (CAD) for you | Intellectual property (IP) must be given to the company in the contract — `legal-advice` |
| "We'll see after three months" | Status and social security still matter from day one |

Payroll cost (employer social security, tax taken from wages) is a tax question → `belgian-fiscal-tax`. This skill owns the legal status and contract flags. Workers who cross borders add immigration and social security complexity. A lawyer is required.

### Consumer B2C vs business B2B (high level)

- Warranty and conformity rules are stronger for consumers than for business buyers
- Right to cancel (withdrawal) where distance sales or sales away from the shop (off-premises) apply — do not invent the number of days
- Clear pricing and language requirements
- Business customers (B2B) can negotiate harder terms. Belgium still controls unfair B2B clauses. Do not assume "they are a company so anything is allowed"

### If a customer sues

1. Which contract and which law applies? Belgian courts often stay involved if you sell from Belgium to Belgian customers.
2. Consumer disputes are slower. They protect the buyer more than disputes between businesses.
3. Private dispute process (arbitration) only helps if the clause is valid for that type of customer.
4. Product safety complaints can also go to market surveillance (FOD Economie / SPF Economie). Coordinate `product-compliance`.
5. Do not draft a court plan. Flag a lawyer when a letter from a lawyer or an authority arrives.

### Contract language

- A consumer-facing contract or webshop only in English can fail Belgian language and transparency rules.
- English contracts between businesses (B2B) are common. Still say which language wins if there is a translation.
- Labels and safety manuals follow product rules — `product-compliance`.

## Institutions

- Belgian Economic Law Code (WER/CDE) — commercial practices. Verify the current books.
- GBA/APD (data protection authority)
- FOD Economie / SPF Economie (product safety / market surveillance links)
- Labour courts for employment disputes. Enterprise courts for many commercial disputes.

## Cross-links

| Need | Skill |
| --- | --- |
| EU frameworks | `european-law` |
| Tax | `belgian-fiscal-tax` |
| Company statutes | `belgian-corporate-law` |
| Token / incentive systems | `token-engineering` |
| CE marking | `product-compliance` |
| General first sorting | `legal-advice` |

## Practical constraints

- Language and region affect whether consumer messages can be enforced.
- Agents must not file with authorities on the user's behalf without explicit authorization.
- Workers or members who cross borders add immigration and social security complexity. A lawyer is required.
