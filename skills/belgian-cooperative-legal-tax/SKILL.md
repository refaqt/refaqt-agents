---
name: belgian-cooperative-legal-tax
description: >-
  Use when a question touches Belgian or EU law or tax for Refaqt: company form (SRL/BV, CV/SC), VAT, company tax, salary vs dividend, first hire, consumer sales, GDPR, R&D incentives, or cooperative tokens and credits.
---
# Belgian Cooperative Law and Tax

Refaqt is a Belgian open-hardware cooperative. Many questions mix company law, tax, and EU
rules. This skill keeps the Belgian and cooperative facts that a model often gets wrong. Use the
`advice` skill for the shape of the answer.

## How to answer

- Order: what it means, the rule, what to do next, when to call a specialist.
- Everyday words first, official term next: "a private limited company (SRL/BV)".
- Do not name internal skills. Say "that is a tax question" or "that is a company-law question".
- Do not invent rates, minimum capital, majority percentages, notice periods, warranty lengths,
  filing deadlines, grace periods, fine amounts or transition dates. If a number matters, say it
  must be checked: tax against current FPS Finance (FOD Financiën / SPF Finances) guidance, law
  against the current official combined text, company rules with a lawyer.
- Agents never file with authorities (BCE/KBO, VAT returns, BELcotax), never sign a Declaration
  of Conformity, and never present a tax amount as final.
- Official terms and their French/Dutch names: see [reference.md](reference.md).

### Myths to correct

- VAT is not profit. It is not yours to keep.
- A cooperative surplus can still be taxable.
- "Only dividends, no salary" to skip social security often ends in a tax assessment.
- Limited liability does not protect a director from fraud, unpaid social security, or trading
  while the company cannot pay its debts.
- A cooperative still has liability rules. Old names (CVBA/SCRL, SPRL/BVBA) are not always the
  current names.
- A freelancer who works like an employee can be treated as an employee.
- A US SAFE is not automatically valid Belgian company law.

## Bad and good answers

**Bad:** "Statute change requires GA + notary; verify current nomenclature for SC/CV vs SCRL/CVBA."
**Good:** "Changing the company's rulebook (articles of association) is not a board vote you can
record in a notes app. In Belgium it usually needs a members' meeting and a notary. Plan for
several weeks. Confirm the current form name before you file."

**Bad:** "VAT cash flow matters; import VAT and deferment schemes affect runway."
**Good:** "VAT (BTW/TVA) is not yours to keep. If you import parts, you may have to pay Belgian
import VAT to customs before you sell the product. That uses cash even if you deduct it later. Ask
your accountant about a delay account (deferment) so you do not pay at the border."

**Bad:** "PCC awareness only; VenB / personal tax — route members to personal advisers."
**Good:** "A Belgian employee costs more than the gross salary. The company also pays social
security, and it withholds payroll tax (BV / précompte professionnel). Paying yourself only in
dividends to avoid that is a tax and social-security risk. Ask an accountant to model salary vs
dividend. Company income tax (VenB/ISOC) is a tax on profit, separate from VAT."

**Bad:** "Employment law touchpoints (if hiring in Belgium — high level)."
**Good:** "Your first Belgian hire is a legal event, not only a payroll line. If someone works on
your schedule, with your tools, and only for you, Belgian law may treat them as an employee even if
the invoice says 'freelance'. You may then owe past social security and tax. Get the contract and
status checked before they start."

**Bad:** "Warranty and conformity rules differ from B2B."
**Good:** "Selling a kit to a consumer is not the same as selling to a factory. Consumers have legal
rights that the product matches what was promised (conformity) and, for many online sales, a
period to cancel (withdrawal). Small print on the website cannot remove those rights. Business
customers can agree stricter terms, but Belgium still controls unfair business (B2B) clauses."

**Bad:** "Regulations vs. directives: know direct applicability vs. national implementation."
**Good:** "There are two kinds of EU rules. A regulation (GDPR is one) applies in Belgium by itself.
A directive sets a goal, and Belgium must write it into Belgian law, so the local text can differ."

## Company form: SRL/BV or cooperative (CV/SC)

| Topic | Private limited company (SRL/BV) | Cooperative (CV/SC) |
| --- | --- | --- |
| Who owns it | Shareholders | Members |
| Typical use | Default for outside investors and most hardware startups | When member ownership is the point |
| Money in | Shares; later share issues | Member parts; capital can go up and down |
| Control | Voting per the articles, often by share | Member voting per the articles; democracy has legal limits |
| Old names | SPRL/BVBA | CVBA/SCRL |
| Change the articles | General meeting, often a notary | General meeting, often a notary |

- Choose a cooperative because member democracy and variable capital are the goal, not because
  it "sounds fairer". Worker and consumer cooperatives have different rules.
- A public limited company (NV/SA) is usually the wrong first form. Send the founder to a lawyer.
- The articles and the Code of Companies and Associations (WVV/CSA) win over internal rules,
  sociocracy circles, side letters, and smart contracts.
- Some decisions need a special majority and often a notary: changing the articles, new shares,
  merger, split, dissolution. A chat poll is not a valid company act.
- New shares change ownership. Check the existing owners' first right to buy (pre-emption).
- A SAFE or convertible note must be mapped to a Belgian share issue or loan with a lawyer.
- Forming the company: form, articles, financial plan, notarial deed, filing in the company
  register (BCE/KBO) and the Official Gazette (BS/MB), then bank, VAT and social security.
- Directors (bestuurders / administrateurs) can be personally liable for trading while the
  company cannot pay its debts, for ignored conflicts, or for missed legal filings.

## Tax and VAT

### VAT (BTW/TVA)

- VAT is a cash problem before it is an accounting problem. Import VAT can leave before the sale.
- Registration can be needed before the first invoice. Confirm timing with the accountant.
- Sales route: customer location and VAT ID (check in VIES for EU business customers), product or
  service, rate or exemption (do not invent the rate), invoice fields per Belgian rules.
- A wrong label (goods or services, B2B or B2C, place of supply) gives the wrong rate and invoice.
- An open-hardware kit (goods plus instructions) can be a mixed supply. Verify the treatment.
- Imports: HS code agreed with the customs broker, origin rules for lower duty, import VAT
  payment or deferment, Incoterms that say who is the importer.
- Intrastat and the EC sales list apply when thresholds are met.

### Company income tax (VenB/ISOC)

- Tax on the company's profit. Not VAT, and not the founder's personal tax.
- Losses, R&D incentives, and the innovation income deduction can change the bill. The
  accountant computes. Agents give awareness only, not grant writing.
- Founder IP licensed to the company, or group companies, raise transfer pricing: prices must
  match those between independent parties. A specialist is required.
- How a cooperative shares its surplus can be taxable for the company and for members.

### Salary vs dividend (map only)

| Path | What the founder feels | What to flag |
| --- | --- | --- |
| Salary | Pays social security; the company withholds payroll tax | Employer cost is more than gross pay |
| Dividend | Looks cheaper on a spreadsheet | Needs distributable profit; withholding tax; social-security risk if it replaces a normal wage |
| Expense repayments | "Just pay the laptop back" | Only real business costs with evidence are non-taxable |

Never output a recommended split or a net-pay number. Give the map and send the founder to an
accountant. Mixes can fall under the tax rule against abuse of law.

## Hiring, customers, language

- Signs of employment: you set hours, tools and tasks. Signs of real self-employment: several
  clients. The status matters from day one. Write the IP transfer (CAD, code) into the contract.
- Consumer (B2C) rights are stronger than business (B2B) rights. Do not invent the number of
  withdrawal days.
- Belgium splits powers across federal, regional and community governments. Name the level first.
- Consumer contracts, webshops and labels may need Dutch and/or French (German in some areas). An
  English-only consumer contract can fail. For B2B in English, say which language wins.
- Product safety complaints can go to market surveillance (FOD Economie / SPF Economie).
- When a letter from a lawyer or an authority arrives, call a lawyer. Do not draft a court plan.

## EU layer

- Open source does not mean an unregulated product. Placing a product on the market triggers
  product law (CE marking, technical file, the role of manufacturer, importer or distributor).
- GDPR for a small connected product: what personal data (a serial number plus an email counts),
  purpose and lawful basis, collect only what you need, keep it only as long as needed, a
  processor agreement with cloud vendors, SCCs for transfers outside the EU/EEA, a DPIA for
  high-risk processing. Not having a DPO does not mean GDPR does not apply. Belgian authority:
  GBA/APD.
- The UK mark (UKCA) is separate from CE.
- Dual-use export control: always a lawyer.

## Cooperative tokens and credits

Design starts from legal form, member status and place of supply, not from a whitepaper.

- Prefer contribution credits that cannot be transferred, capped voting weight, and surplus
  through the general meeting under the articles. Avoid tradable profit tokens.
- Surplus rights belong in company law. Do not rebuild them with tokens.
- "Points", "credits" and "badges" are not the same as "tokens" or "coins" for regulators. Label
  honestly. No price or return language.
- Tokens paid for work can be wages, professional fees or miscellaneous income for the
  contributor. Open-source contributors are not automatically non-employees.
- The tax office may treat credits as wages or a hidden dividend (recharacterization).
- Public offers or tradable tokens: screen for MiCA, e-money and FSMA rules with a lawyer.
- Default to an off-chain ledger. A smart contract that breaks cooperative law is worse than none.

### Warning: VAT on token-for-work

If tokens, credits or redeemable points pay for work or services, Belgian VAT can treat it as a
swap of value (barter). VAT may be due on the value of the work or the tokens, and an invoice may
be needed. Startups often miss this. Check every earn and redeem path:

- [ ] Service or goods; single or mixed supply
- [ ] VAT base when payment is not cash (consideration in kind)
- [ ] Place of supply; B2B or B2C
- [ ] Rate or exemption (verify any cooperative exemption)
- [ ] Reverse charge for EU B2B services; VIES check of the VAT ID
- [ ] Invoice or credit note, even when settled in tokens
- [ ] Redemption as a separate event from the grant
- [ ] Cash: VAT can be due before the tokens turn into cash

Do not publish token rules or contributor terms until an accountant has stated the VAT
treatment and a lawyer has reviewed the design. Never promise token value.

## When to call a specialist

- **Lawyer:** company form, articles, new shares or members, member expulsion, shareholder
  disputes, merger or liquidation, first hire status, cross-border workers, consumer terms,
  letters from authorities or lawyers, token design, MiCA or FSMA, export control.
- **Accountant or tax adviser:** VAT registration, salary vs dividend, surplus distribution,
  R&D incentives, transfer pricing, token VAT and income tax, any filing or ruling.

This is information, not a replacement for a Belgian lawyer or accountant.
