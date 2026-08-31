---
name: token-engineering
description: >-
  Design token and incentive systems for Belgian cooperative ventures — utility,
  governance, contribution tracking, and distribution mechanics with low tax
  burden. Use when defining tokenomics, member rewards, or on-chain/off-chain
  incentive structures — always coordinate with belgian-law, belgian-fiscal-tax
  (VAT law and compliance), and belgian-corporate-law; not for securities
  determinations or tax filings.
---
# Token Engineering

Use this skill to **design token and incentive systems** that serve cooperative goals while fitting Belgian legal and fiscal reality. Read this skill together with `belgian-law`, `belgian-fiscal-tax` (Belgian VAT law and compliance), and `belgian-corporate-law` before proposing any token architecture.

**Mandatory pairing:** Any design where tokens are **granted, earned, or redeemed for work or services** requires parallel review with `belgian-fiscal-tax` — token compensation is not outside VAT scope.

## Scope

**Owns:**
- Token system design (utility, governance, reputation, contribution credits)
- Incentive alignment for contributors, members, and the venture
- Tax-aware design choices (structure, timing, labeling, off-chain vs on-chain)
- VAT compliance **inputs** for token-for-work flows (rates, place of supply, invoicing flags — definitive treatment in `belgian-fiscal-tax`)
- Mapping token flows to cooperative governance (`sociocracy`, `belgian-corporate-law`)
- Contribution accounting patterns (hours, deliverables, BOM, maintenance)
- Vesting, caps, cliffs, and anti-speculation guardrails
- Separation of **member rights** (statutory) from **token mechanics** (operational)
- Pre-legal tokenomics specs for counsel and accountant review
- Integration patterns with `web3-blockchain` (when chain adds value)

**Does NOT own:**
- Securities law, MiCA classification, FSMA registration → `legal-advice`, `european-law`, counsel
- Tax filings, VAT returns, rulings, or definitive treatment → `belgian-fiscal-tax`, human advisers
- Statutory cooperative governance → `belgian-corporate-law`
- Smart contract implementation → `web3-blockchain`, `software-development`
- Marketing or investment pitches → `marketing`, `business-development`
- General blockchain fit analysis → `web3-blockchain`

## Core principles

- **Belgium first:** Every token design starts with legal form, member status, and place of supply — not whitepaper aesthetics.
- **Tax is design, not afterthought:** Issuance, vesting, redemption, and secondary activity can trigger income, VAT, or social charges for the venture and contributors — model before launch.
- **VAT law is not optional:** Paying contributors in tokens, credits, or redeemable points for work is often a **taxable supply of services** — place of supply, rate, reverse charge, and invoice rules apply via `belgian-fiscal-tax`.
- **Cooperative over speculation:** Prefer non-transferable contribution credits, capped governance weight, and surplus via statutory channels over tradable profit tokens.
- **Statutes before smart contracts:** On-chain rules must not contradict articles of association or GA decisions (`belgian-corporate-law`).
- **Minimize taxable events:** Favor deferred recognition, in-kind cooperative benefits, and clear non-cash utility where lawful — verify with `belgian-fiscal-tax`.
- **Label honestly:** "Points", "credits", and "badges" are not interchangeable with "tokens" or "coins" for regulators or tax authorities.
- **Default off-chain:** Use ledgers or databases unless multi-party trust minimization requires a chain (`web3-blockchain` fit test).

## Belgian coordination (required)

Before finalizing any token system, run these checks across skills:

| Check | Skill | Question |
| --- | --- | --- |
| Legal form | `belgian-corporate-law` | Do tokens map to parts/shares, surpluses, or non-equity rights? |
| Member vs non-member | `belgian-corporate-law` | Who may hold, earn, or redeem? |
| Commercial law | `belgian-law` | B2C promotion, unfair terms, consumer-facing claims? |
| Income tax & social charges | `belgian-fiscal-tax` | Taxable benefit at grant, vest, transfer, or redemption? |
| **VAT law & compliance** | `belgian-fiscal-tax` | Is token-for-work a taxable supply? B2B reverse charge? Invoice required? |
| EU financial rules | `european-law` | MiCA, e-money, or financial promotion exposure? |
| Governance | `sociocracy` | How do tokens relate to circles and consent — not override them? |

**Agents must not launch or promise token value** without accountant and counsel sign-off on the specific design.

## Tax-aware design patterns (Belgium-oriented)

These are **design hypotheses** — confirm with `belgian-fiscal-tax` and professional advisers before implementation.

| Pattern | Typical use | Tax posture (high level) | Risk if misused |
| --- | --- | --- | --- |
| Non-transferable contribution credits | Track hours, reviews, BOM work | Often lower immediate tax if no cash value and clear rules | Recharacterization as wages or disguised dividend |
| Vested utility access | Priority ordering, tooling access | May avoid investment characterization | FSMA/MiCA if marketed as investment |
| Governance weight cap | Member votes (off-chain mirror) | Align with one-member-one-vote statutes | Concentration conflicts with cooperative law |
| Surplus via GA distribution | Profit sharing to members | Follow cooperative fiscal rules — not a token | Token as profit-right without legal basis |
| Redemption for coop services | Discount on kits, events, training | Benefit-in-kind treatment possible | VAT and benefit valuation complexity |
| External tradability | Secondary market | High tax and regulatory risk | Almost always escalate counsel |

**Venture burden:** Issuance, airdrops, and treasury management may create corporate tax and VAT events — keep treasury flows in `finance` models.

**Contributor burden:** Tokens paid for work may be employment income, professional fees, or miscellaneous income depending on relationship — never assume "crypto = untaxed."

## VAT compliance (cooperate with `belgian-fiscal-tax`)

Belgian VAT law applies to many token-for-work arrangements. This skill captures **design inputs**; `belgian-fiscal-tax` owns **compliance rules**. Run both skills together whenever tokens compensate labour or services.

### When VAT review is mandatory

- Contributor earns tokens for design, firmware, docs, support, or review work
- Member receives credits instead of cash invoice for professional services
- Customer pays in tokens for hardware, kits, or support (barter / mixed consideration)
- Tokens are redeemed for taxable goods or services at a stated or implied value
- Cross-border contributors or recipients (intra-EU B2B, reverse charge, OSS)

### Token-for-work VAT checklist (route to `belgian-fiscal-tax`)

- [ ] **Supply character:** Service vs goods; single vs mixed supply
- [ ] **Consideration value:** How BTW/TVA base is determined when payment is non-cash (`belgian-fiscal-tax`)
- [ ] **Place of supply:** Contributor/customer location; B2B vs B2C
- [ ] **Rate and exemption:** Standard/reduced/zero; cooperative-specific exemptions verified
- [ ] **Reverse charge:** Intra-EU B2B services to/from the cooperative
- [ ] **Invoice / credit note:** Required fields even when settlement is in tokens or credits
- [ ] **Recipient VAT ID:** VIES check for intra-EU B2B
- [ ] **Redemption VAT:** Separate event at redemption vs at grant — accountant confirms
- [ ] **Cash flow:** VAT due may precede token liquidity — model in `finance`

### Design choices that affect VAT (hypotheses only)

| Choice | VAT relevance | Coordinate with |
| --- | --- | --- |
| Fixed euro-denominated credit | Clear consideration value | `belgian-fiscal-tax`, `finance` |
| Pure reputation (no redemption value) | May reduce VAT surface — verify | `belgian-fiscal-tax`, counsel |
| Redemption only for exempt/internal items | Rate/exemption depends on item | `belgian-fiscal-tax`, `product-compliance` |
| Token grant at delivery milestone | Time of supply alignment | `belgian-fiscal-tax`, `legal-advice` |
| Barter with hardware | Goods + services classification | `belgian-fiscal-tax`, `sales` |

Do not finalize token schedules or contributor-facing terms until `belgian-fiscal-tax` has flagged VAT treatment for each earn and redeem path.

## Key workflows

### Token system design (Belgian cooperative)

1. **Purpose:** What behavior or outcome does the system incentivize?
2. **Legal anchor:** Map to member rights, contracts, or pure internal accounting (`belgian-corporate-law`).
3. **Holder classes:** Members, contributors, customers — different rules per class.
4. **Lifecycle:** Earn → hold → use/redeem → expire (avoid open-ended tradable supply).
5. **Tax map:** List events (grant, vest, transfer, redeem, burn) and route each to `belgian-fiscal-tax` checklist.
6. **VAT map (mandatory if work compensated):** Run token-for-work VAT checklist with `belgian-fiscal-tax` in parallel — do not skip for non-cash labels.
7. **Regulatory screen:** MiCA, e-money, crowdfunding, FSMA — `european-law`, `legal-advice`.
8. **Governance fit:** Confirm GA/board authority for economic rights (`belgian-corporate-law`, `sociocracy`).
9. **Implementation:** Off-chain ledger vs on-chain (`web3-blockchain` fit test).
10. **Documentation:** Plain-language member explanation (FR/NL as needed — `belgian-law`).
11. **Review gate:** Accountant + counsel before public announcement; VAT treatment signed off by tax adviser where tokens pay for services.

### Low-burden contributor rewards checklist

- [ ] Reward tied to documented contribution (issue, BOM, support), not speculation
- [ ] Non-transferable by default; transfer exceptions require legal review
- [ ] No public price or ROI language (`marketing`, `open-source-community`)
- [ ] Redemption limited to cooperative goods/services where possible
- [ ] Vesting schedule matches delivery milestones
- [ ] Clear tax wording in contributor agreements → `legal-advice`
- [ ] **VAT path confirmed** for every earn/redeem route → `belgian-fiscal-tax` (invoice, rate, place of supply)
- [ ] Treasury and issuance budget in `finance` forecast (include VAT cash timing)
- [ ] MiCA/FSMA screen complete if any public offering contemplated

### Token vs statutory surplus (do not conflate)

| Mechanism | Governing layer | Skill |
| --- | --- | --- |
| GA-approved surplus allocation | Statutes, VenB rules | `belgian-corporate-law`, `belgian-fiscal-tax` |
| Contribution credits | Internal policy / contract | `token-engineering` |
| On-chain vote record | Technical audit trail | `web3-blockchain` (if lawful) |

Surplus distribution rights belong in corporate law — do not recreate them implicitly via tradable tokens.

## Terminology

- Contribution credit, reputation point, governance weight (prefer over "coin" unless counsel approves)
- Vesting cliff, redemption window, treasury policy
- MiCA, CASP, e-money token, asset-referenced token — routing only (`european-law`)
- BTW/TVA, VIES, intracommunity supply, reverse charge, time of supply
- Benefit in kind / avantage de toute nature — tax routing (`belgian-fiscal-tax`)
- Consideration in kind / non-cash payment — VAT base (`belgian-fiscal-tax`)

## Cross-links

| Need | Skill |
| --- | --- |
| Belgian commercial/regulatory context | `belgian-law` |
| **VAT law, BTW/TVA compliance, token-for-work treatment** | `belgian-fiscal-tax` |
| Income tax and payroll withholding on token grants | `belgian-fiscal-tax` |
| Cooperative statutes and member rights | `belgian-corporate-law` |
| EU MiCA and financial promotion | `european-law`, `legal-advice` |
| Chain fit and smart contracts | `web3-blockchain` |
| Operating governance | `sociocracy` |
| Contributor agreements | `open-source-community`, `legal-advice` |
| Treasury and runway | `finance` |
| Community messaging | `marketing` |

## Practical constraints

- Paying contributors in tokens does not bypass Belgian VAT — treat as a supply design problem with `belgian-fiscal-tax`.
- Do not design tokens primarily to avoid tax — recharacterization risk falls on members and the cooperative.
- US persons and cross-border contributors add `us-law` complexity — default exclude until mapped.
- Open-source contributors are not automatically non-employees — token grants can still trigger payroll/social charges.
- Immutable smart contracts that violate Belgian cooperative law are worse than no chain.
- Publish token rules in the same languages as member-facing statutes where required (`belgian-law`).
