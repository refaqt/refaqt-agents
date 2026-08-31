---
name: web3-blockchain
description: >-
  Practical blockchain and web3 for cooperatives — governance tooling, provenance,
  and token design without hype. Use when evaluating distributed ledgers, on-chain
  voting, supply chain attestation, or tokenomics — always pair with legal counsel.
---
# Web3 / Blockchain

Use this skill for **sober** evaluation and implementation of blockchain-related tools where they solve cooperative or supply-chain problems better than conventional databases.

## Scope

**Owns:**
- Use-case fit analysis (when **not** to use a blockchain)
- Architecture options (L1/L2, private consortium, IPFS + hashes)
- Smart contract functional specs (high level)
- Governance token **design patterns** ( voting, delegation, caps) — not securities advice
- Supply chain provenance and audit trails (hash anchoring)
- Wallet/key management operational security
- Integration with `software-development` stacks
- Open-source licensing of contract code

**Does NOT own:**
- Securities law, MiCA, SEC determinations → `legal-advice`, `european-law`, `us-law`, human counsel
- Tax treatment of tokens → `belgian-fiscal-tax`, counsel
- Cooperative statutory governance → `belgian-corporate-law`, `sociocracy`
- Marketing hype or investment pitches → `marketing`, `business-development`
- CE or product safety → `product-compliance`

## Core principles

- **Default to Postgres:** Use blockchain only for multi-party trust minimization, credible timestamps, or public verifiability needs.
- **Cooperative first:** Tokens must not undermine democratic member control or create exploitative speculation.
- **Regulatory humility:** Most governance tokens touch securities/financial promotion rules — counsel early.
- **Open interfaces:** ABI/API documented; avoid opaque admin keys without multisig and policy.
- **Environmental reality:** Prefer low-energy L2 or consortium chains for alignment with cooperative values.

## When to consider web3

| Use case | Fit | Caution |
| --- | --- | --- |
| Public BOM/firmware attestation | Medium — hash on-chain, data off-chain | Immutability of errors |
| Member vote record | Low–Medium | Must align with `belgian-corporate-law` |
| Supply chain CoC | Medium in multi-party nets | Private data off-chain |
| Internal accounting | Poor fit | Use `finance` systems |
| Fundraising token | High legal risk | Counsel required |

## Key workflows

### Fit test (blockchain?)

1. Need shared write among distrusting parties?
2. Need public verifiability?
3. Can a signed database + transparency log suffice?
4. If yes to 1–2 and no to 3, evaluate chain; else stop.

### Token/governance design outline (pre-legal)

- Utility vs. governance separation
- Vesting, caps, no-profit expectation for members
- Multisig admin and upgrade policy
- Off-chain deliberation (`sociocracy`) → on-chain execution only if lawful

### Smart contract delivery

- Spec → review → testnet → audit (external) → mainnet
- Coordinate `software-development` for CI and deployment pipelines
- Incident response plan for exploits

## Terminology

- EVM, multisig, DAO, IPFS, Merkle proof
- MiCA (EU), Howey test awareness (US) — not legal analysis

## Cross-links

| Need | Skill |
| --- | --- |
| Legal | `legal-advice`, `european-law`, `us-law` |
| Tax | `belgian-fiscal-tax` |
| Governance | `sociocracy`, `belgian-corporate-law` |
| Community | `open-source-community` |
| Supply provenance | `supply-chain-management` |

## Practical constraints

- Do not launch tokens to US/EU persons without legal clearance.
- Open hardware + NFT gimmicks rarely help builders — skepticism default.
- Key loss = irreversible; operational playbooks required.
- Hype damages cooperative trust — communicate plainly via `marketing`.
