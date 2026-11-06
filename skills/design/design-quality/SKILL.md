---
name: design-quality
description: >-
  Measure and judge whether a design is good: easy to use, quick to use, and
  pleasant to look at. Use before you call any interface, web app, machine
  screen, product, or 3D model "done", when you review someone else's design,
  when two design options must be compared, or when the user asks "is this
  good design?". Gives hard pass/fail gates, numbers to measure, a scored
  expert review, and a scorecard for the pull request. The other design
  skills build things; this skill decides if they are good enough.
---
# Design Quality

Design feels like taste. Most of it is not. A large part of "good design" can be measured, and the
rest can be judged in a fixed, repeatable way. This skill tells you how to do both, so that you do
not call your own work good just because you made it.

## Scope

**Owns:**
- The definition of "done" for any design work in this kit
- Hard gates (pass or fail), measured numbers, scored reviews, and tests with real users
- The design scorecard that goes into the pull request
- Comparing two or more design options and picking one with reasons

**Does NOT own:**
- How to design the flow or the screens → `ux-design`, `gui-design`
- Web-specific build rules → `web-app-design`
- Machine operator screens → `machine-hmi-design`
- Physical products and 3D models → `industrial-design`, `3d-design`
- Legal accessibility duties for a product on the EU market → `product-compliance`, `european-law`

## The idea in one paragraph

Judge a design on four levels, from the most objective to the most subjective. **Gates** are rules
that pass or fail, like text contrast or button size. **Measures** are numbers, like the seconds
and clicks a main task takes. **Scored review** is a structured expert judgement, done by a
reviewer who did not build the design, with fixed 0 to 4 scales. **User evidence** is what real
people do and say in a test. A design is done when every gate passes, every main task is inside its
budget, the review scores reach the target, and no serious problem is open. Use the higher levels
when you can, but never skip the lower ones.

## Core principles

- **The user's task comes first.** "Good" always means good for a named person doing a named task
  in a named place. Write these down before you judge anything. A screen for a machine operator
  with gloves is judged differently from a marketing page.
- **Measure, then judge.** Run the gates and the numbers first. They are cheap and they do not lie.
  Then do the scored review.
- **Do not review your own work alone.** The builder is the worst judge. Give the review to a
  separate sub-agent (or a person) with the screenshots, the target user, and the rubric, but
  not your opinion. If you must review alone, say so in the report.
- **Look at the real result.** Judge rendered screens, real renders of the 3D model, or photos
  of the real part. Do not judge from code or from a description.
- **Compare, do not only rate.** People and models judge "A or B?" much more reliably than "how good
  is A from 0 to 10?". When the look matters, make two or three options and compare them in pairs.
- **Beauty is partly measurable.** Research on first impressions shows that people judge a screen
  in about 50 milliseconds (Lindgaard and others, 2006), and that appeal is highest when visual
  complexity is low to moderate (Reinecke and others, 2013). People also find good-looking products easier to
  use (the aesthetic-usability effect). So count what makes a screen busy: font sizes, colours,
  alignment lines, and spacing values. Fewer, used on purpose, looks calmer.
- **Be honest with scores.** A 4 means excellent, not "fine". Most real interfaces score between
  20 and 32 out of 40 on the heuristic review. A first version that scores 38 was not reviewed hard
  enough.

## Level 1: Gates (pass or fail)

A failed gate blocks "done". No score can make up for it.

### Software and screens

| Gate | Pass when | Source |
| --- | --- | --- |
| Text contrast | Normal text at least 4.5:1, large text (24 px, or 18.66 px bold) at least 3:1 | WCAG 2.2, 1.4.3 |
| Contrast of controls and icons | Borders of inputs, icons, and focus rings at least 3:1 | WCAG 2.2, 1.4.11 |
| Target size | Every click or touch target at least 24 x 24 px. Aim for 44 x 44 px on touch screens | WCAG 2.2, 2.5.8 and 2.5.5 |
| Keyboard | Every action works with the keyboard alone, and the focus is always visible | WCAG 2.2, 2.1.1 and 2.4.7 |
| Small screens | No sideways scroll at 320 px wide; text can grow to 200 % without loss | WCAG 2.2, 1.4.10 and 1.4.4 |
| Names | Every input has a label, every icon-only button has a name, every meaningful image has alt text | WCAG 2.2, 1.1.1, 4.1.2 |
| Colour is not the only signal | State, errors, and alarms also use text, shape, or position | WCAG 2.2, 1.4.1 |
| Feedback time | The interface reacts to every action within 0.1 s, shows a busy sign after 1 s, and a progress bar with the time left after 10 s | Response time limits (Miller 1968, Nielsen) |
| Destructive actions | Delete, overwrite, or machine-moving actions can be undone, or ask for confirmation | Error prevention heuristic |
| States | Each screen has a designed empty, loading, error, and full state | |

Machine screens and physical products add their own gates. See `machine-hmi-design` and
`industrial-design`.

### How to check the gates on a web page

Run the measuring script on the running page. It checks the gates above that a machine can check,
at phone and desktop size, and saves screenshots for the review:

```bash
node .agents/skills/design/design-quality/scripts/ui_metrics.mjs http://localhost:5173 --shots design-review/shots --out design-review/metrics.json --axe
```

- Exit code 0 means all automatic gates pass. 1 means at least one fails. 2 means it could not run.
- `--axe` adds the axe-core accessibility rules. It needs network access to cdnjs.
- The script cannot check keyboard use, feedback time, or states. Check those by hand, with
  Playwright, or in a test. Say in the report which gates you checked by hand.
- For a native app or a machine screen, take screenshots and check contrast and target sizes with
  the same numbers by hand.

## Level 2: Measures (numbers)

### Flow cost: how short is each main task?

1. List the three to five tasks that matter most. Name them as the user would ("change the
   spindle speed", not "edit config").
2. For each task, write the shortest path as steps, and count **screens**, **clicks or taps**,
   **typed characters**, and **decisions** (each time the user must stop and think or search).
3. Give each task a **budget** before you design. A good start: the most frequent task needs at
   most one screen change and three actions from the home screen. No task needs more than one
   decision per screen.
4. Estimate the time with the Keystroke-Level Model (KLM), a method that gives each small action a
   fixed time. Write the flows in a small text file and run:

```bash
python .agents/skills/design/design-quality/scripts/flow_cost.py design-review/flows.txt
```

```text
task: Change the spindle speed | budget=6
M click H type:4 K
```

`M` is a decision (1.35 s), `click` is point and click (1.3 s), `H` moves the hand to the keyboard
(0.4 s), `type:4` is four keys, and `K` is one key (0.28 s each). Give two files to compare the old
and new design, task by task. The script exits with code 1 when a task is over budget. The full
operator table is in [reference.md](reference.md).

KLM predicts the time of a skilled user who makes no mistakes. It is a fair way to compare two
designs. It does not tell you how a first-time user will do. For that, see Level 4.

### Visual complexity: how busy does it look?

The measuring script also counts these. They are warnings, not gates. A dense tool for experts can
have good reasons to go higher.

| Measure | Calm target | Why |
| --- | --- | --- |
| Font sizes on one screen | 6 or fewer, from one type scale | Each size is a level of importance. Too many levels means no clear order |
| Font families | 1 or 2 | More families look unplanned |
| Distinct colours | 12 or fewer, from one palette | Colour should carry meaning, not decoration |
| Alignment lines (left edges) | 12 or fewer, as few as the layout allows | Fewer edges means a clearer grid |
| Spacing values off the 4 px or 8 px grid | Under 20 % | Random gaps look careless |
| Options at one decision point | 4 or fewer visible, group the rest | People can hold about four things in mind (Cowan, 2001) |

### Fitts and Hick: size, distance, and choice

- **Fitts's law:** a target is faster to hit when it is bigger and closer. Put the most used
  controls large and near where the hand or pointer already is. Screen edges and corners are easy
  to hit with a mouse.
- **Hick's law:** decision time grows with the number of choices. Show the common choice first,
  and put rare choices one level down.

## Level 3: Scored review

Give the review to a separate sub-agent, or to a person. Give them: the screenshots (normal,
blurred, and grey), the target user and their tasks, the flow cost results, and the rubrics in
[reference.md](reference.md). Do not give them your opinion of the design.

The reviewer scores three things:

1. **Usability: Nielsen's 10 heuristics**, each 0 to 4, total out of 40. These are ten general
   rules for usable interfaces, from "show the system status" to "help and documentation".
2. **Visual quality rubric**, eight criteria, each 0 to 4, total out of 32: hierarchy, alignment
   and grid, spacing and rhythm, typography, colour, consistency, fit with the subject, and finish
   of states and details.
3. **Cognitive load checklist**, eight yes or no questions. Count the failures.

Three quick visual tests help the reviewer:

- **Squint test:** look at the blurred screenshot. The most important thing on the screen must
  still stand out, and the groups must still be visible.
- **Grey test:** look at the grey screenshot. The order of importance must still work without
  colour.
- **Five-second test:** look at the screen for five seconds, then look away. Can you say what the
  screen is for and what the main action is? If not, the hierarchy is wrong.

Each problem gets a severity:

| Severity | Meaning |
| --- | --- |
| P0 | Blocks a main task, causes harm or data loss, or breaks a legal duty. Fix before release |
| P1 | Slows or confuses most users on a main task. Fix before release |
| P2 | Annoying or slow on a less common path. Fix soon |
| P3 | Polish. Fix when you are in the area |

## Level 4: User evidence

Real users beat every other level. An agent cannot be the user, but it can plan the test, write
the script, and analyse the results.

- **Five users** of one type find most of the large problems in a flow (Nielsen and Landauer,
  1993). Test early with five, fix, and test again.
- **Task success rate:** the share of users who finish the task without help. Aim for 90 % or more
  on main tasks.
- **Time on task:** compare with the KLM estimate. A big gap shows where people get lost.
- **Single Ease Question (SEQ):** after each task, "Overall, how difficult or easy was the task to
  complete?" from 1 to 7. The average across many studies is about 5.5. Below that, the task needs
  work.
- **System Usability Scale (SUS):** ten questions after the test, scored 0 to 100. About 68 is
  average. Above 80 is in the top group. The questions and the scoring are in
  [reference.md](reference.md).
- **Simulated users are a proxy, not evidence.** A sub-agent that walks through the flow as a
  named persona (for example "first-day operator" or "expert in a hurry") finds real problems.
  Label its results as a walkthrough, never as a user test.

## Key workflows

### Before you design

1. Write down the target users, their main tasks, and where they use the product (light, noise,
   gloves, screen size, distance).
2. Set the budgets: time and steps per main task, and the targets for the review scores.
3. Measure the current version if there is one. That is your baseline.

### Before you call a design done

1. Run the gates. Fix every failure.
2. Run the flow cost. Fix every task over budget.
3. Get the scored review from a separate reviewer. Fix every P0 and P1.
4. Run the gates and the review again after the fixes. Do not trust a fix you did not measure.
5. Put the scorecard in the pull request.

**Targets for done** (change them per project and write them in the project patterns):
all gates pass, all main tasks inside budget, heuristic total at least 30 out of 40 with no
heuristic under 2, visual rubric at least 24 out of 32 with no criterion under 2, at most one
cognitive load failure, and no open P0 or P1.

### Comparing design options

1. Make two or three real options. Each must differ in one clear way (for example layout, not
   only colour).
2. Run the gates and flow cost on each. Drop any option that fails a gate.
3. Show the reviewer the options in pairs, in a random order, and ask which is better for the named
   user and task, and why.
4. Pick the winner. Write the reasons in a decision note (`docs/decisions/`).

## Design scorecard

Put this in the "How it was checked" part of the pull request, filled in. Keep the full review in
the closed technical block.

```markdown
Design check for <screen or product>, for <user> doing <task>.
- Gates: <all pass / list failures>. Checked by script: <list>. Checked by hand: <list>.
- Main tasks: <task> <before s> to <after s>, <steps> steps, budget <s>. (one line per task)
- Usability review: <n>/40. Visual review: <n>/32. Cognitive load failures: <n>.
- Reviewer: <separate sub-agent / person / self only>.
- Open problems: <P0 n, P1 n, P2 n, P3 n>.
- User evidence: <none yet / SUS, SEQ, success rate with n users>.
```

## Tools

| Tool | What it does |
| --- | --- |
| `scripts/ui_metrics.mjs` | Gates and visual counts on a rendered web page, plus squint and grey screenshots |
| `scripts/flow_cost.py` | KLM time, clicks, keys, and decisions per task, with budgets and before/after |
| axe-core (`--axe`) | Open-source accessibility rule engine, used by many browser tools |
| Impeccable (`npx impeccable detect <folder or url>`) | Open-source detector for common generated-design patterns and quality problems; optional |
| Lighthouse (Chrome DevTools) | Accessibility and performance scores for web pages |

## Terminology and standards

- ISO 9241-11:2018: usability means effectiveness, efficiency, and satisfaction for named users,
  tasks, and context of use. Use these three words when you report.
- ISO 9241-110:2020: seven interaction principles (fit with the task, self-descriptive, matches
  expectations, easy to learn, user in control, robust against use errors, engaging).
- Web Content Accessibility Guidelines (WCAG) 2.2, level AA: the accessibility floor for every
  screen. EN 301 549 is the European standard that points to it.
- European Accessibility Act: since 28 June 2025, many consumer products and services in the EU must
  be accessible. Check with `product-compliance` if it applies to your product.
- IEC 62366-1: usability engineering for medical devices. Use it if the product is medical.

## Cross-links

| Need | Skill |
| --- | --- |
| Design the flows and screens | `ux-design`, `gui-design` |
| Web build rules | `web-app-design` |
| Machine operator screens | `machine-hmi-design` |
| Physical product and 3D model | `industrial-design`, `3d-design` |
| Legal accessibility duties | `product-compliance`, `european-law` |
| Record the chosen option | `docs/decisions/` (decision template) |

## Sources and credits

- Nielsen, "10 Usability Heuristics for User Interface Design", Nielsen Norman Group.
- Card, Moran, Newell, "The keystroke-level model for user performance time with interactive
  systems" (1980), and their book "The Psychology of Human-Computer Interaction" (1983).
- Lindgaard and others, "Attention web designers: You have 50 milliseconds to make a good first
  impression!" (2006). Reinecke and others, "Predicting users' first impressions of website
  aesthetics" (CHI 2013).
- Brooke, "SUS: a quick and dirty usability scale" (1996). Sauro and Lewis, "Quantifying the User
  Experience" (2016), for SUS and SEQ reference values.
- The 0 to 4 heuristic scoring, the cognitive load checklist, and the separate-reviewer method are
  adapted from Impeccable by Paul Bakaus (https://github.com/pbakaus/impeccable, Apache License
  2.0).
- W3C, Web Content Accessibility Guidelines (WCAG) 2.2 (https://www.w3.org/TR/WCAG22/).
