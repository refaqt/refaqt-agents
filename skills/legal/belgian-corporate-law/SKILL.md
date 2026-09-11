---
name: belgian-corporate-law
description: >-
  Belgian company and cooperative law for startup founders — private limited
  company (SRL/BV), cooperatives (CV/SC), incorporation, governance, shares,
  fundraising, and statutory obligations. Use for company form and corporate
  actions in Belgium — not tax filings or product compliance.
---
# Belgian Corporate Law

Use this skill for the **legal form and governance skeleton** of a Belgian company or cooperative: articles of association, organs, meetings, shares or member parts, and corporate actions.

## How to answer founders

You are talking to a startup founder, not a lawyer. Keep legal accuracy. Change only the language.

- Lead with the decision, cash, or risk impact, then the legal rule.
- Everyday words first, official term next: private limited company (SRL/BV), cooperative (CV/SC), company register (BCE/KBO), Belgian Official Gazette (BS/MB).
- Structure every answer as:
  1. **What this means** — the founder-facing point
  2. **The rule** — the accurate company-law position, with official names
  3. **What to do next** — concrete steps
  4. **When to call a lawyer** — if the stakes are high
- Put the disclaimer in one sentence, not at the start. This is not a substitute for Belgian counsel.
- Do not name internal skills to the user. Route in the background; say "that is a tax question" rather than "hand off to `belgian-fiscal-tax`".
- Never flatten the law into myths: a cooperative still has liability rules; limited liability is not a shield for fraud or unpaid social security; older form names (CVBA/SCRL) are not always the current names.
- Do not invent capital minima, majority thresholds, or filing deadlines. If a number matters, say it must be verified with counsel.

**Bad:** "Statute change requires GA + notary; verify current nomenclature for SC/CV vs SCRL/CVBA."
**Good:** "Changing the company's rulebook (articles of association) is not a board vote you can do in Notion. In Belgium it usually needs a shareholders' or members' meeting and a notary. Plan weeks of lead time. The default startup form is a private limited company (SRL in French / BV in Dutch). A cooperative (CV/SC) is a different form. You may still see old labels such as CVBA/SCRL on older papers — confirm the current form before you file."

**Bad:** "Member democracy has limits; certain decisions require supermajorities."
**Good:** "You cannot always decide this in a chat. Some decisions — changing the articles, issuing shares, merger — need a special majority and sometimes a notary. Check the articles before you promise an investor or a new member anything."

## Scope

**Owns:**
- Belgian startup company forms, with **SRL/BV first** (private limited company — the usual founder default)
- Other common forms at overview level: NV/SA (public limited company); cooperative CV/SC (including worker vs consumer cooperatives)
- Older names founders still see on documents (CVBA/SCRL, SPRL/BVBA) — verify current labels with counsel
- Articles of association (statutes) and internal rules structure
- Shareholders vs members; share issuance and fundraising corporate steps
- Admission, withdrawal, expulsion of members (cooperatives) — process outline
- General meeting and board / management competencies (high level)
- Capital, shares/parts, and financial contributions
- Token or contribution-credit schemes vs statutory parts/shares — coordinate `token-engineering`
- Director liability awareness (not defense strategy)
- Statutory publication and registry (BS/MB, BCE/KBO) requirements overview
- Merge/split/liquidation triggers → always counsel

**Does NOT own:**
- Tax treatment of salary, dividends, or distributions → `belgian-fiscal-tax`
- Employment contracts → `belgian-law`, HR counsel
- Product liability → `product-compliance`, `legal-advice`
- Sociocracy operating system → `sociocracy` (cultural/process layer on top of law)
- Day-to-day agile delivery → `agile`

## Core principles

- **SRL/BV is the default founder form:** Limited liability company with shareholders. Use a cooperative (CV/SC) when member democracy and variable capital are the point, not because it "sounds fairer."
- **Articles are binding:** Internal sociocracy or shareholder side-letters must fit inside company law (`sociocracy` coordination). If they conflict, the articles and the Code of Companies and Associations (WVV/CSA) win.
- **Limited liability has limits:** The company is a separate person. Founders and directors can still be personally on the hook for wrongful trading, unpaid social security, or not keeping proper accounts.
- **Decision thresholds are real:** Certain decisions need special majorities or a notarial deed. Do not treat a Slack poll as a valid corporate act.
- **Capital discipline:** Starting undercapitalized is a director-risk and a finance problem — coordinate `finance`.
- **Foreign shareholders or members:** Extra KYC and tax implications — `belgian-fiscal-tax`, counsel.

## SRL/BV vs cooperative (founder comparison)

| Topic | Private limited company (SRL/BV) | Cooperative (CV/SC) |
| --- | --- | --- |
| Who owns it | Shareholders | Members |
| Typical startup use | Default for venture-style and most hardware companies | When the project is member-owned by design |
| Money in | Shares; later share issues for fundraising | Member parts / contributions; rules differ |
| Control | Voting usually follows the articles (often share-based) | Member voting rules in the articles; democracy has legal limits |
| Older names you may see | SPRL/BVBA | CVBA/SCRL |
| Changing the rulebook | General meeting + often a notary | General meeting + often a notary |

Worker cooperative vs consumer cooperative rules differ — confirm the form at incorporation. NV/SA is usually the wrong first vehicle for an early-stage startup; flag and send to counsel.

## Key workflows

### Incorporation outline (SRL/BV or cooperative)

1. Choose the form with counsel (SRL/BV unless there is a clear cooperative purpose)
2. Draft articles of association (statutes): purpose, shares or parts, directors, meeting rules
3. Financial plan / initial equity story — coordinate `finance`; tax → `belgian-fiscal-tax`
4. Notarial deed where required
5. File and publish: company register (BCE/KBO) and Official Gazette (BS/MB)
6. Open the bank account, VAT and social-security registrations as needed (tax/admin, not this skill's filing)

Agents do not file BCE forms without explicit user authorization and counsel review.

### Governance mapping

| Decision type | Typical organ | Legal threshold |
| --- | --- | --- |
| Day-to-day ops | Management / daily directors | Articles may delegate |
| Budget approval | Board and/or general meeting, per articles | Check the articles |
| New share issue / investor in | General meeting; often notary | Dilution and pre-emption rights |
| Major asset purchase | Often general meeting | May need a special majority |
| Statute / articles change | General meeting + notary | Special majority; plan lead time |
| Dissolve / merge / split | General meeting + counsel | Always counsel |

Align with `sociocracy` circles without contradicting the articles.

### Fundraising (corporate steps, not term-sheet drafting)

- Issuing new shares in an SRL/BV changes ownership. Check pre-emption (existing shareholders' first-refusal) in the articles.
- A US SAFE or convertible note is not automatically valid Belgian company law. Map it onto a share issue, a loan, or a Belgian instrument with counsel.
- Many capital and article changes need a notary and publication. Do not promise a close date that ignores that lead time.
- Tax on the money in, and on later salary vs dividend, is a tax question → `belgian-fiscal-tax`.

### New shareholder or member onboarding (legal outline)

1. Eligibility per articles
2. Share/part acquisition and payment
3. Register update (share register and, where required, BCE/KBO)
4. Shareholder or member agreement and IP/CLA if any → `legal-advice`, `open-source-community`

### Director liability in plain language

Directors (bestuurders / administrateurs) run the company and can be personally exposed if they keep trading when the company is hopelessly in debt, ignore conflicts, or skip legally required filings. This skill flags that risk. It does not design a defense.

## Cross-links

| Need | Skill |
| --- | --- |
| Tax on contributions, salary, dividends | `belgian-fiscal-tax` |
| Token and incentive design | `token-engineering` |
| Operating governance | `sociocracy` |
| Contracts | `legal-advice` |
| EU cooperative context | `european-law` |

## Practical constraints

- Notarial deeds are required for many changes — plan lead time.
- Agents do not file BCE/KBO forms without explicit user authorization and counsel review.
- Worker cooperative vs consumer cooperative rules differ — confirm form at incorporation.
- Do not quote a minimum capital figure or a majority percentage unless the user supplies the articles and counsel has confirmed current WVV/CSA rules.
