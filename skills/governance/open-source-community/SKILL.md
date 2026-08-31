---
name: open-source-community
description: >-
  Build and sustain contributor communities around open-source hardware and
  software. Use for contributor onboarding, CLA/DCO, governance of repos,
  events, and maintainer workflows — not corporate marketing or legal opinions.
---
# Open Source Community Building

Use this skill to grow healthy contributor ecosystems for open hardware, firmware, docs, and tooling.

## Scope

**Owns:**
- Contributor onboarding paths (good first issues, mentorship)
- Communication norms (CODE_OF_CONDUCT, discussion forums, chat)
- Maintainer workload and release cadence expectations
- Recognition and attribution practices
- Community metrics (contributors, issues, time-to-first-review) — lightweight
- Event formats (build days, office hours, hackathons)
- Relationship between core cooperative team and wider community
- DCO vs CLA policy recommendation (legal review → `legal-advice`)

**Does NOT own:**
- Brand campaigns → `marketing`
- Statutory cooperative membership → `belgian-corporate-law`, `sociocracy`
- License selection final say → `legal-advice`
- Technical architecture → engineering skills
- Token incentives → `web3-blockchain` (careful coupling)

## Core principles

- **Maintainers are scarce:** Protect them with clear scope and review SLAs.
- **Open hardware needs physical empathy:** Document tools, costs, and safety for builders.
- **Welcome ≠ low bar:** Contribution guidelines and tests keep quality (`software-development`, `maintain-patterns`).
- **Credit fairly:** CONTRIBUTORS file, release notes, talk invitations.
- **Commercial cooperative + community:** Be explicit about what's community-governed vs. employer roadmap.

## Key workflows

### Repository health checklist

- [ ] README: what, why, build, license
- [ ] CONTRIBUTING.md with PR flow
- [ ] CODE_OF_CONDUCT and enforcement contact
- [ ] Issue templates (bug, feature, docs)
- [ ] Label taxonomy and triage rotation
- [ ] Security disclosure process (`legal-advice` for advisories)

### Contributor ladder

1. User/report issues
2. Docs and small fixes
3. Subsystem maintainer
4. Governance participant (see `sociocracy`)

### Conflict resolution

1. Clarify facts in issue/thread
2. Refer to CoC if interpersonal
3. Escalate to governance circle if persistent
4. Legal harassment/threats → `legal-advice` immediately

## Terminology

- DCO, CLA, fork, downstream, upstream
- OSHWA, Open Source Hardware Association practices
- Maintainer, triager, emeritus maintainer

## Cross-links

| Need | Skill |
| --- | --- |
| Licenses | `legal-advice` |
| Cooperative decisions | `sociocracy` |
| Public messaging | `marketing` |
| Activity log | `log` |
| Agile cadence | `agile` |

## Practical constraints

- Publishing CAD/BOM invites forks — nurture downstream with semver and migration guides.
- Safety-critical repos need tighter merge gates (`product-compliance` awareness in CONTRIBUTING).
- Don't promise governance tokens without `web3-blockchain` and counsel review.
