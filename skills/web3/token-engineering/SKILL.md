---
name: token-engineering
description: >-
  Design token and incentive systems for Belgian cooperative ventures — utility,
  governance, contribution tracking, and how tokens are distributed, with a low
  tax burden. Use when you define token rules (tokenomics), member rewards, or
  on-chain or off-chain incentives. Always coordinate with belgian-law,
  belgian-fiscal-tax (value-added tax (VAT) law and compliance), and
  belgian-corporate-law. Do not use this skill for securities decisions or tax
  filings.
---
# Token Engineering

Use this skill to **design token and incentive systems** that serve cooperative goals and fit Belgian legal and tax reality. Read this skill together with `belgian-law`, `belgian-fiscal-tax` (Belgian value-added tax (VAT) law and compliance), and `belgian-corporate-law` before you propose any token architecture.

**Mandatory pairing:** Any design where tokens are **granted, earned, or redeemed for work or services** needs a parallel review with `belgian-fiscal-tax`. Token pay for work is still in VAT scope.

## Scope

**Owns:**
- Token system design (utility, governance, reputation, contribution credits)
- Incentive alignment for contributors, members, and the venture
- Tax-aware design choices (structure, timing, labeling, off-chain vs on-chain)
- Value-added tax (VAT) compliance **inputs** for token-for-work flows (rates, where the supply is taxed (place of supply), invoicing flags — the final treatment sits in `belgian-fiscal-tax`)
- Mapping token flows to cooperative governance (`sociocracy`, `belgian-corporate-law`)
- Contribution accounting patterns (hours, deliverables, bill of materials (BOM), maintenance)
- Vesting (delayed unlock), caps, cliffs (the wait before any tokens unlock), and anti-speculation limits
- Separation of **member rights** (in the statutes) from **token mechanics** (operations)
- Token-rule specs for a lawyer and an accountant to review before legal sign-off
- Integration patterns with `web3-blockchain` (when a chain adds value)

**Does NOT own:**
- Securities law, Markets in Crypto-Assets (MiCA) classification, Financial Services and Markets Authority (FSMA) registration → `legal-advice`, `european-law`, a lawyer
- Tax filings, VAT returns, rulings, or the final tax treatment → `belgian-fiscal-tax`, human advisers
- Statutory cooperative governance → `belgian-corporate-law`
- Smart contract implementation → `web3-blockchain`, `software-development`
- Marketing or investment pitches → `marketing`, `business-development`
- General blockchain fit analysis → `web3-blockchain`

## Core principles

- **Belgium first:** Every token design starts with legal form, member status, and where the supply is taxed (place of supply). Do not start from how a whitepaper looks.
- **Tax is part of the design:** Issuance, vesting, redemption, and later activity (including trading) can trigger income tax, VAT, or social charges for the venture and for contributors. Model this before launch.
- **VAT law is not optional:** Paying contributors in tokens, credits, or redeemable points for work is often a **taxable supply of services**. Place of supply, rate, reverse charge (the customer accounts for VAT), and invoice rules apply via `belgian-fiscal-tax`.
- **Cooperative over speculation:** Prefer contribution credits that cannot be transferred, capped governance weight, and surplus through statutory channels. Avoid tradable profit tokens.
- **Statutes before smart contracts:** On-chain rules must not contradict the articles of association or general assembly (GA) decisions (`belgian-corporate-law`).
- **Reduce taxable events:** Prefer deferred recognition, in-kind cooperative benefits, and clear non-cash utility where the law allows it. Verify with `belgian-fiscal-tax`.
- **Label honestly:** "Points", "credits", and "badges" are not the same as "tokens" or "coins" for regulators or tax authorities.
- **Default off-chain:** Use ledgers or databases unless you need less trust between many parties. Run the `web3-blockchain` fit test.

## Belgian coordination (required)

Before you finalize any token system, run these checks across skills:

| Check | Skill | Question |
| --- | --- | --- |
| Legal form | `belgian-corporate-law` | Do tokens map to parts/shares, surpluses, or non-equity rights? |
| Member vs non-member | `belgian-corporate-law` | Who may hold, earn, or redeem? |
| Commercial law | `belgian-law` | Business-to-consumer (B2C) promotion, unfair terms, consumer-facing claims? |
| Income tax & social charges | `belgian-fiscal-tax` | Taxable benefit at grant, vest, transfer, or redemption? |
| **VAT law & compliance** | `belgian-fiscal-tax` | Is token-for-work a taxable supply? Business-to-business (B2B) reverse charge? Invoice required? |
| EU financial rules | `european-law` | Markets in Crypto-Assets (MiCA), electronic money (e-money), or financial promotion exposure? |
| Governance | `sociocracy` | How do tokens relate to circles and consent — not override them? |

**Agents must not launch or promise token value** without accountant and lawyer sign-off on the specific design.

## Tax-aware design patterns (Belgium-oriented)

These are **design hypotheses**. Confirm them with `belgian-fiscal-tax` and professional advisers before you implement.

| Pattern | Typical use | Tax picture (high level) | Risk if misused |
| --- | --- | --- | --- |
| Contribution credits that cannot be transferred | Track hours, reviews, bill of materials (BOM) work | Often lower tax at once if there is no cash value and the rules are clear | The tax office may treat them as wages or as a hidden dividend (recharacterization) |
| Vested utility access | Priority ordering, tooling access | May avoid being treated as an investment | Financial Services and Markets Authority (FSMA) / Markets in Crypto-Assets (MiCA) if marketed as an investment |
| Governance weight cap | Member votes (off-chain mirror) | Align with one-member-one-vote statutes | Concentration conflicts with cooperative law |
| Surplus via general assembly (GA) distribution | Profit sharing to members | Follow cooperative tax rules — this is not a token | A token as a profit-right with no legal basis |
| Redemption for cooperative services | Discount on kits, events, training | A non-cash benefit (benefit in kind) is possible | VAT and how you value the benefit get complex |
| External tradability | Secondary market | High tax and regulatory risk | Almost always ask a lawyer |

**Venture burden:** Issuance, free token drops (airdrops), and treasury management may create corporate tax and VAT events. Keep treasury flows in `finance` models.

**Contributor burden:** Tokens paid for work may be employment income, professional fees, or miscellaneous income. The relationship decides which. Never assume crypto is untaxed.

## VAT compliance (cooperate with `belgian-fiscal-tax`)

Belgian value-added tax (VAT) law applies to many token-for-work arrangements. This skill captures **design inputs**. `belgian-fiscal-tax` owns **compliance rules**. Run both skills together whenever tokens pay for labour or services.

### When VAT review is mandatory

- A contributor earns tokens for design, firmware, docs, support, or review work
- A member receives credits instead of a cash invoice for professional services
- A customer pays in tokens for hardware, kits, or support (barter / mixed consideration)
- Tokens are redeemed for taxable goods or services at a stated or implied value
- Cross-border contributors or recipients (intra-EU business-to-business (B2B), reverse charge, One-Stop Shop (OSS))

### Token-for-work VAT checklist (route to `belgian-fiscal-tax`)

- [ ] **Supply character:** Service vs goods; single vs mixed supply
- [ ] **Consideration value:** How the VAT (BTW/TVA) base is set when payment is not cash (`belgian-fiscal-tax`)
- [ ] **Place of supply:** Contributor or customer location; business-to-business (B2B) vs business-to-consumer (B2C)
- [ ] **Rate and exemption:** Standard, reduced, or zero; verify any cooperative-specific exemptions
- [ ] **Reverse charge:** Intra-EU B2B services to or from the cooperative (the customer accounts for VAT)
- [ ] **Invoice / credit note:** Required fields even when settlement is in tokens or credits
- [ ] **Recipient VAT ID:** VAT Information Exchange System (VIES) check for intra-EU B2B
- [ ] **Redemption VAT:** Separate event at redemption vs at grant — the accountant confirms
- [ ] **Cash flow:** VAT due may come before you can turn the tokens into cash. Model this in `finance`

### Design choices that affect VAT (hypotheses only)

| Choice | VAT relevance | Coordinate with |
| --- | --- | --- |
| Fixed euro-denominated credit | Clear consideration value | `belgian-fiscal-tax`, `finance` |
| Pure reputation (no redemption value) | May reduce how often VAT applies — verify | `belgian-fiscal-tax`, a lawyer |
| Redemption only for exempt or internal items | Rate or exemption depends on the item | `belgian-fiscal-tax`, `product-compliance` |
| Token grant at a delivery milestone | Aligns with when VAT becomes due (time of supply) | `belgian-fiscal-tax`, `legal-advice` |
| Barter with hardware | Goods plus services classification | `belgian-fiscal-tax`, `sales` |

Do not finalize token schedules or contributor-facing terms until `belgian-fiscal-tax` has stated the VAT treatment for each earn and redeem path.

## Key workflows

### Token system design (Belgian cooperative)

1. **Purpose:** What behavior or outcome does the system reward?
2. **Legal anchor:** Map to member rights, contracts, or pure internal accounting (`belgian-corporate-law`).
3. **Holder classes:** Members, contributors, customers — different rules per class.
4. **Lifecycle:** Earn → hold → use/redeem → expire (avoid an open-ended tradable supply).
5. **Tax map:** List events (grant, vest, transfer, redeem, burn) and route each to the `belgian-fiscal-tax` checklist.
6. **VAT map (mandatory if work is paid this way):** Run the token-for-work VAT checklist with `belgian-fiscal-tax` in parallel. Do not skip this because the label is not cash.
7. **Regulatory screen:** Markets in Crypto-Assets (MiCA), electronic money (e-money), crowdfunding, Financial Services and Markets Authority (FSMA) — `european-law`, `legal-advice`.
8. **Governance fit:** Confirm general assembly (GA) or board authority for economic rights (`belgian-corporate-law`, `sociocracy`).
9. **Implementation:** Off-chain ledger vs on-chain (`web3-blockchain` fit test).
10. **Documentation:** Plain-language member explanation (French (FR) / Dutch (NL) as needed — `belgian-law`).
11. **Review gate:** Accountant plus lawyer before a public announcement. A tax adviser must sign off VAT treatment where tokens pay for services.

### Low-burden contributor rewards checklist

- [ ] Reward tied to a documented contribution (issue, bill of materials (BOM), support), not speculation
- [ ] Cannot be transferred by default; transfer exceptions need legal review
- [ ] No public price or return-on-investment (ROI) language (`marketing`, `open-source-community`)
- [ ] Redemption limited to cooperative goods or services where possible
- [ ] Vesting schedule matches delivery milestones
- [ ] Clear tax wording in contributor agreements → `legal-advice`
- [ ] **VAT path confirmed** for every earn and redeem route → `belgian-fiscal-tax` (invoice, rate, place of supply)
- [ ] Treasury and issuance budget in the `finance` forecast (include VAT cash timing)
- [ ] Markets in Crypto-Assets (MiCA) / Financial Services and Markets Authority (FSMA) screen complete if any public offering is planned

### Token vs statutory surplus (do not mix these)

| Mechanism | Governing layer | Skill |
| --- | --- | --- |
| General assembly (GA)-approved surplus allocation | Statutes, corporate income tax (VenB) rules | `belgian-corporate-law`, `belgian-fiscal-tax` |
| Contribution credits | Internal policy / contract | `token-engineering` |
| On-chain vote record | Technical audit trail | `web3-blockchain` (if lawful) |

Surplus distribution rights belong in corporate law. Do not rebuild those rights through tradable tokens.

## Terminology

- Contribution credit, reputation point, governance weight (prefer these over "coin" unless a lawyer approves)
- Vesting cliff (the wait before any tokens unlock), redemption window, treasury policy
- Markets in Crypto-Assets (MiCA), crypto-asset service provider (CASP), electronic money token (e-money token), a token backed by assets (asset-referenced token) — routing only (`european-law`)
- VAT (BTW/TVA), VAT Information Exchange System (VIES), supply of goods between EU countries (intracommunity supply), reverse charge (the customer accounts for VAT), when VAT becomes due (time of supply)
- A non-cash benefit (benefit in kind / avantage de toute nature) — tax routing (`belgian-fiscal-tax`)
- Non-cash payment (consideration in kind) — VAT base (`belgian-fiscal-tax`)

## Cross-links

| Need | Skill |
| --- | --- |
| Belgian commercial/regulatory context | `belgian-law` |
| **VAT law, BTW/TVA compliance, token-for-work treatment** | `belgian-fiscal-tax` |
| Income tax and payroll withholding on token grants | `belgian-fiscal-tax` |
| Cooperative statutes and member rights | `belgian-corporate-law` |
| EU Markets in Crypto-Assets (MiCA) and financial promotion | `european-law`, `legal-advice` |
| Chain fit and smart contracts | `web3-blockchain` |
| Operating governance | `sociocracy` |
| Contributor agreements | `open-source-community`, `legal-advice` |
| Treasury and months of cash left (runway) | `finance` |
| Community messaging | `marketing` |

## Practical constraints

- Paying contributors in tokens does not skip Belgian value-added tax (VAT). Treat this as a supply design problem with `belgian-fiscal-tax`.
- Do not design tokens mainly to avoid tax. Recharacterization risk falls on members and the cooperative.
- People in the US and contributors in other countries add `us-law` complexity. Exclude them until you map the rules.
- Open-source contributors are not automatically non-employees. Token grants can still trigger payroll and social charges.
- A smart contract that cannot be changed and that breaks Belgian cooperative law is worse than using no chain.
- Publish token rules in the same languages as member-facing statutes where the law requires it (`belgian-law`).
