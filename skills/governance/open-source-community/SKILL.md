---
name: open-source-community
description: >-
  Build and keep contributor communities around open-source hardware and
  software. Use for welcoming new contributors, contributor license or sign-off
  rules (CLA/DCO), how repositories are run, events, and maintainer workflows —
  not company marketing or legal opinions.
---
# Open Source Community Building

Use this skill to grow healthy contributor groups for open hardware, firmware, docs, and tools.

## Scope

**Owns:**
- Paths for new contributors (good first issues, mentorship)
- Communication norms (code of conduct (`CODE_OF_CONDUCT`), discussion forums, chat)
- Maintainer workload and expected release rhythm
- Recognition and credit practices
- Simple community numbers (contributors, issues, time to first review)
- Event formats (build days, office hours, hackathons)
- The relationship between the core cooperative team and the wider community
- Advice on Developer Certificate of Origin (DCO) versus Contributor License Agreement (CLA) (legal review → `legal-advice`)

**Does NOT own:**
- Brand campaigns → `marketing`
- Legal cooperative membership → `belgian-corporate-law`, `sociocracy`
- Final license choice → `legal-advice`
- Technical architecture → engineering skills
- Token incentives → `token-engineering` (coordinate `belgian-fiscal-tax` and a lawyer)

## Core principles

- **Maintainers are scarce:** Protect them with a clear scope and review response times (service level agreements, SLAs).
- **Open hardware needs care for the physical build:** Document tools, costs, and safety for people who build it.
- **A welcome is not a lower quality bar:** Contribution guidelines and tests keep quality (`software-development`, `maintain-patterns`).
- **Credit fairly:** CONTRIBUTORS file, release notes, talk invitations.
- **Commercial cooperative and community:** Be clear about what the community governs versus what the employer roadmap covers.

## Key workflows

### Repository health checklist

- [ ] README: what, why, build, license
- [ ] CONTRIBUTING.md with pull request (PR) flow
- [ ] CODE_OF_CONDUCT and enforcement contact
- [ ] Issue templates (bug, feature, docs)
- [ ] Set of labels (taxonomy) and who sorts incoming issues, in rotation
- [ ] Security disclosure process (`legal-advice` for advisories)

### Contributor ladder

1. User / report issues
2. Docs and small fixes
3. Subsystem maintainer
4. Governance participant (see `sociocracy`)

### Conflict resolution

1. Clarify facts in the issue or thread
2. Point to the code of conduct (CoC) if the problem is between people
3. Escalate to the governance circle if it continues
4. Legal harassment or threats → `legal-advice` immediately

## Terminology

- Developer Certificate of Origin (DCO), Contributor License Agreement (CLA), a copy of a project (fork), projects that use our work (downstream), projects we use (upstream)
- Open Source Hardware Association (OSHWA) practices
- Maintainer, person who sorts incoming issues (triager), former maintainer (emeritus maintainer)

## Cross-links

| Need | Skill |
| --- | --- |
| Licenses | `legal-advice` |
| Cooperative decisions | `sociocracy` |
| Public messaging | `marketing` |
| Activity log | `log` |
| Agile cadence | `agile` |

## Practical constraints

- Publishing computer-aided design (CAD) files and the bill of materials (BOM) invites copies (forks). Support those copies with semantic versioning (semver) and migration guides.
- Safety-critical repositories need stricter merge rules. Put `product-compliance` awareness in CONTRIBUTING.
- Do not promise governance tokens without `token-engineering`, `web3-blockchain`, and a lawyer's review.
