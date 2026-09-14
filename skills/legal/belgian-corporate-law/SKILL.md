---
name: belgian-corporate-law
description: >-
  Belgian company and cooperative law for startup founders. Covers the
  private limited company (SRL/BV), cooperatives (CV/SC), founding the
  company, how the company is run (governance), shares, raising money, and
  legal filing duties. Use this for company form and company actions in
  Belgium. Do not use this for tax filings or product compliance.
---
# Belgian Corporate Law

Use this skill for the **legal form and basic rules** of a Belgian company or cooperative: the company's rulebook (articles of association), company bodies, meetings, shares or member parts, and company actions.

## How to answer founders

You are talking to a startup founder, not a lawyer. Keep legal accuracy. Change only the language.

- Start with the decision, the cash, or the risk. Then state the legal rule.
- Everyday words first, official term next: a private limited company (SRL/BV), a cooperative (CV/SC), the company register (BCE/KBO), the Belgian Official Gazette (BS/MB).
- Structure every answer as:
  1. **What this means** — the point the founder needs
  2. **The rule** — the accurate company-law position, with official names
  3. **What to do next** — concrete steps
  4. **When to call a lawyer** — if the stakes are high
- Put the disclaimer in one sentence. Do not put it at the start. This is not a replacement for a Belgian lawyer.
- Do not name internal skills to the user. Send the question to the right skill without naming it. Say "that is a tax question" rather than "hand off to `belgian-fiscal-tax`".
- Do not turn the law into simple myths: a cooperative still has liability rules; limited liability does not protect you from fraud or unpaid social security; older form names (CVBA/SCRL) are not always the current names.
- Do not invent minimum capital amounts, majority percentages, or filing deadlines. If a number matters, say it must be verified with a lawyer.

**Bad:** "Statute change requires GA + notary; verify current nomenclature for SC/CV vs SCRL/CVBA."
**Good:** "Changing the company's rulebook (articles of association) is not a board vote you can record in a notes app. In Belgium it usually needs a shareholders' or members' meeting and a notary. Plan for several weeks. The default startup form is a private limited company (SRL in French / BV in Dutch). A cooperative (CV/SC) is a different form. You may still see old labels such as CVBA/SCRL on older papers. Confirm the current form before you file."

**Bad:** "Member democracy has limits; certain decisions require supermajorities."
**Good:** "You cannot always decide this in a chat. Some decisions — changing the articles, issuing shares, merger — need a special majority and sometimes a notary. Check the articles before you promise an investor or a new member anything."

## Scope

**Owns:**
- Belgian startup company forms, with **SRL/BV first** (private limited company — the usual founder default)
- Other common forms at overview level: NV/SA (public limited company); cooperative CV/SC (including worker versus consumer cooperatives)
- Older names founders still see on documents (CVBA/SCRL, SPRL/BVBA) — verify current labels with a lawyer
- The company's rulebook (articles of association, also called statutes) and internal rules structure
- Shareholders versus members; share issuance and fundraising company steps
- Admission, withdrawal, and expulsion of members (cooperatives) — process outline
- General meeting and board / management powers (overview only)
- Capital, shares/parts, and money or assets contributed
- Token or contribution-credit schemes versus parts or shares that company law recognizes (statutory parts/shares) — coordinate `token-engineering`
- Director liability awareness (not a defense plan)
- Legal publication and registry (BS/MB, BCE/KBO) requirements overview
- Merge, split, or liquidation triggers → always a lawyer

**Does NOT own:**
- Tax treatment of salary, dividends, or distributions → `belgian-fiscal-tax`
- Employment contracts → `belgian-law`, an HR lawyer
- Product liability → `product-compliance`, `legal-advice`
- Sociocracy operating system → `sociocracy` (culture and process on top of law)
- Day-to-day agile delivery → `agile`

## Core principles

- **SRL/BV is the default founder form:** A limited liability company with shareholders. Use a cooperative (CV/SC) when member democracy and capital that can go up and down (variable capital) are the point, not because it "sounds fairer."
- **Articles are binding:** Internal sociocracy or extra shareholder agreements (side-letters) must fit inside company law (`sociocracy` coordination). If they conflict, the articles and the Code of Companies and Associations (WVV/CSA) win.
- **Limited liability has limits:** The company is a separate person. Founders and directors can still be personally liable for keeping the company trading when it cannot pay its debts (wrongful trading), unpaid social security, or not keeping proper accounts.
- **Decision thresholds are real:** Certain decisions need special majorities or a notarial deed (a document signed with a notary). Do not treat a chat poll as a valid company act.
- **Capital discipline:** Starting with too little money is a director risk and a finance problem. Coordinate `finance`.
- **Foreign shareholders or members:** Extra identity checks (KYC) and tax implications — `belgian-fiscal-tax`, a lawyer.

## SRL/BV vs cooperative (founder comparison)

| Topic | Private limited company (SRL/BV) | Cooperative (CV/SC) |
| --- | --- | --- |
| Who owns it | Shareholders | Members |
| Typical startup use | Default for companies that want outside investors, and for most hardware companies | When the project is member-owned by design |
| Money in | Shares; later share issues for fundraising | Member parts / contributions; rules differ |
| Control | Voting usually follows the articles (often based on shares) | Member voting rules in the articles; democracy has legal limits |
| Older names you may see | SPRL/BVBA | CVBA/SCRL |
| Changing the rulebook | General meeting + often a notary | General meeting + often a notary |

Worker cooperative versus consumer cooperative rules differ. Confirm the form when you form the company. A public limited company (NV/SA) is usually the wrong first company form for an early-stage startup. Flag this. Send the founder to a lawyer.

## Key workflows

### Forming the company (SRL/BV or cooperative)

1. Choose the form with a lawyer (SRL/BV unless there is a clear cooperative purpose)
2. Draft articles of association (statutes): purpose, shares or parts, directors, meeting rules
3. Financial plan and how ownership starts (equity) — coordinate `finance`; tax → `belgian-fiscal-tax`
4. Notarial deed where required
5. File and publish: company register (BCE/KBO) and Official Gazette (BS/MB)
6. Open the bank account, VAT and social-security registrations as needed (tax and admin, not this skill's filing)

Agents do not file BCE forms without explicit user authorization and review by a lawyer.

### Governance mapping

| Decision type | Typical company body (organ) | Legal threshold |
| --- | --- | --- |
| Day-to-day operations | Management / daily directors | The articles may delegate |
| Budget approval | Board and/or general meeting, per the articles | Check the articles |
| New share issue / investor in | General meeting; often a notary | Ownership share gets smaller (dilution) and existing shareholders' first right to buy (pre-emption) |
| Major asset purchase | Often general meeting | May need a special majority |
| Statute / articles change | General meeting + notary | Special majority; plan extra time |
| Dissolve / merge / split | General meeting + a lawyer | Always a lawyer |

Align with `sociocracy` circles without contradicting the articles.

### Fundraising (company steps, not term-sheet drafting)

- Issuing new shares in an SRL/BV changes ownership. Check existing shareholders' first right to buy (pre-emption) in the articles.
- A US SAFE or convertible note is not automatically valid Belgian company law. Map it onto a share issue, a loan, or a Belgian legal form with a lawyer.
- Many capital and article changes need a notary and publication. Do not promise a completion date that ignores that extra time.
- Tax on the money in, and on later salary versus dividend, is a tax question → `belgian-fiscal-tax`.

### New shareholder or member joining (legal outline)

1. Who may join, per the articles
2. How the share or part is acquired and paid
3. Register update (share register and, where required, BCE/KBO)
4. Shareholder or member agreement and intellectual property (IP) / contributor license (CLA) if any → `legal-advice`, `open-source-community`

### Director liability in plain language

Directors (bestuurders / administrateurs) run the company. They can be personally liable if they keep trading when the company cannot pay its debts, ignore conflicts, or skip legally required filings. This skill flags that risk. It does not design a defense.

## Cross-links

| Need | Skill |
| --- | --- |
| Tax on contributions, salary, dividends | `belgian-fiscal-tax` |
| Token and incentive design | `token-engineering` |
| Operating governance | `sociocracy` |
| Contracts | `legal-advice` |
| EU cooperative context | `european-law` |

## Practical constraints

- Notarial deeds are required for many changes. Plan extra time.
- Agents do not file BCE/KBO forms without explicit user authorization and review by a lawyer.
- Worker cooperative versus consumer cooperative rules differ. Confirm the form when you form the company.
- Do not quote a minimum capital figure or a majority percentage unless the user supplies the articles and a lawyer has confirmed current WVV/CSA rules.
