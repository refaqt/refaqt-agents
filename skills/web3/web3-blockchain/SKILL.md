---
name: web3-blockchain
description: >-
  Practical blockchain and web3 tools for cooperatives — voting tools, proof of
  origin, and token design. Do not use marketing exaggeration. Use when you assess a
  shared ledger, votes on a blockchain, supply-chain proof, or token rules.
  Always work with a lawyer.
---
# Web3 / Blockchain

Use this skill to assess and build blockchain tools. Use them only when they solve a cooperative or supply-chain problem better than a normal database.

## Scope

**Owns:**
- Fit analysis (including when **not** to use a blockchain)
- Architecture choices: a main chain or a faster chain on top (L1/L2), a private chain shared by a group (consortium), or off-chain file storage plus hashes (IPFS + hashes)
- High-level specs for programs that run on a blockchain (smart contracts)
- Putting a governance token **on the chain** (voting, delegation, caps) — detailed token rules → `token-engineering`
- Supply-chain origin records and audit trails (store a hash on the chain, called hash anchoring)
- How you store wallets and keys in daily work (operational security)
- Integration with `software-development` stacks
- Open-source licenses for contract code

**Does NOT own:**
- Securities law, Markets in Crypto-Assets (MiCA), US Securities and Exchange Commission (SEC) decisions → `legal-advice`, `european-law`, `us-law`, a human lawyer
- Token system design and tax-aware token rules → `token-engineering`
- Tax treatment of tokens → `belgian-fiscal-tax`, a lawyer or accountant
- Cooperative rules in company statutes → `belgian-corporate-law`, `sociocracy`
- Marketing exaggeration or investment pitches → `marketing`, `business-development`
- CE marking or product safety → `product-compliance`

## Core principles

- **Default to a normal database (Postgres):** Use a blockchain only when you need less trust between parties, timestamps that others can believe, or public checks.
- **Cooperative first:** Tokens must not weaken democratic member control or invite harmful speculation.
- **Treat rules seriously:** Most governance tokens can fall under securities or financial-promotion rules. Talk to a lawyer early.
- **Open interfaces:** Document the contract call interface (ABI) and the programming interface (API). Do not use hidden admin keys without multi-signature (multisig) control and a written policy.
- **Energy use:** Prefer a low-energy faster chain (L2) or a consortium chain so the choice matches cooperative values.

## When to consider web3

| Use case | Fit | Caution |
| --- | --- | --- |
| Public bill of materials (BOM) or firmware proof | Medium — hash on-chain, data off-chain | Errors stay forever |
| Member vote record | Low–Medium | Must match `belgian-corporate-law` |
| Supply-chain chain of custody (CoC) | Medium in multi-party networks | Keep private data off-chain |
| Internal accounting | Poor fit | Use `finance` systems |
| Fundraising token | High legal risk | A lawyer is required |

## Key workflows

### Fit test (blockchain?)

1. Do distrusting parties need to write to a shared record?
2. Do you need the public to check the record?
3. Can a signed database plus a public log do the same job?
4. If yes to 1–2 and no to 3, assess a chain. Otherwise stop.

### Token and governance design outline (before legal review)

Work with `token-engineering` for full token rules. This skill covers chain-side concerns:

- Keep utility tokens separate from governance tokens
- Vesting, caps, and no profit expectation for members
- Multi-signature (multisig) admin and upgrade policy
- Talk off-chain (`sociocracy`). Put a result on-chain only if the law allows it

### Smart contract delivery

- Spec → review → test network (testnet) → external audit → live network (mainnet)
- Coordinate `software-development` for automated tests and deployment pipelines (CI)
- Write an incident plan for attacks

## Terminology

- Ethereum Virtual Machine (EVM), multi-signature wallet (multisig), decentralized autonomous organization (DAO), off-chain file storage (IPFS), Merkle proof (a compact proof that data sits in a hashed tree)
- Markets in Crypto-Assets (MiCA, EU), Howey test awareness (US test for a security) — this is not legal analysis

## Cross-links

| Need | Skill |
| --- | --- |
| Legal | `legal-advice`, `european-law`, `us-law` |
| Token design | `token-engineering` |
| Tax | `belgian-fiscal-tax` |
| Governance | `sociocracy`, `belgian-corporate-law` |
| Community | `open-source-community` |
| Supply provenance | `supply-chain-management` |

## Practical constraints

- Do not launch tokens to US or EU persons without legal clearance.
- Open hardware plus non-fungible token (NFT) extras rarely help builders. Treat those extras with doubt.
- Lost keys cannot be undone. You need written operating procedures.
- Marketing exaggeration damages cooperative trust. Speak plainly via `marketing`.
