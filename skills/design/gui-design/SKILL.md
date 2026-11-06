---
name: gui-design
description: >-
  Visual design of graphical user interfaces (GUI): layout, grid, spacing,
  typography, colour, icons, components, states, motion, and a design system
  of tokens. Use when you build or restyle any screen (web app, desktop app,
  mobile app, dashboard, or machine screen), when a screen looks busy, flat,
  generic, or "not professional", or when you set up a design system. Works
  with ux-design (flows) and design-quality (judging the result).
---
# GUI Design

A graphical user interface (GUI) looks good when it is clear first and distinctive second. Clear
means the eye knows where to start, groups are obvious, and nothing fights for attention.
Distinctive means the look was chosen for this product and its users, not taken from a template.

## Scope

**Owns:**
- Visual direction and the design brief for screens
- Design tokens: the named values for colour, type, spacing, radius, shadow, and motion
- Layout, grid, spacing, and visual hierarchy
- Typography and colour
- Components and all their states
- Icons, images, charts style, and motion
- Light and dark themes

**Does NOT own:**
- Users, tasks, flows, and interface words → `ux-design`
- Browser code rules and accessibility code → `web-app-design`
- Alarm colours and operator screens on machines → `machine-hmi-design`
- Detailed chart and dashboard design rules → the data visualisation guidance in the project, or
  ask the user
- Judging and scoring the result → `design-quality`

## Core principles

- **Hierarchy before decoration.** Decide what is first, second, and third on each screen. Show it
  with size, weight, position, and space before you use colour.
- **Few values, used on purpose.** One type scale, one spacing scale, one palette, one radius rule.
  Every value on a screen comes from a token. Random values make a screen look careless even when
  the user cannot say why.
- **Space groups things.** Items that belong together are close. Groups are clearly apart. Use
  space before you use lines and boxes.
- **Colour carries meaning.** A neutral base, one accent for the main action and selection, and
  status colours (error, warning, success, information) used only for status.
- **Spend boldness in one place.** Let one element be the memorable part of the screen. Keep the
  rest quiet and disciplined. Before you finish, remove one decoration.
- **Choose for this product.** The look comes from the product's world: its users, its materials,
  its place of use. A tool for machine builders should not look like a fashion shop or a generic
  software template.
- **Look at it.** Take screenshots and review them at real size, blurred, and in grey (the
  measuring script in `design-quality` makes all three). A picture shows problems that code hides.

## Key workflows

### 1. Write a short design plan before you build

1. Subject, users, and the one main job of the screen (from `ux-design`).
2. **Colour:** 4 to 6 named base values with hex codes, plus status colours. Example: `ink`,
   `paper`, `line`, `muted`, `accent`, and `danger`.
3. **Type:** 1 or 2 font families and their roles. A type scale with a fixed ratio (about 1.2 for
   dense tools, about 1.25 to 1.333 for content pages).
4. **Spacing:** a scale on a 4 px or 8 px base (for example 4, 8, 12, 16, 24, 32, 48, 64).
5. **Layout:** the grid and alignment (left, centred), drawn as a small ASCII wireframe.
6. **The one bold choice** and why it fits this product.
7. Check the plan against the brief: if it would look the same for any other product, change the
   part that is generic, and write what you changed and why.

If the project already has a design system (a `DESIGN.md`, a token file, or a component library),
use it. Do not invent a second one. Add missing tokens to it.

### 2. Layout and spacing

- Pick a grid: columns for content pages, a fixed sidebar plus fluid main area for tools.
- Align every element to a few shared lines. Fewer left edges look calmer.
- More space above a heading than below it, so the heading belongs to its content.
- Related items about 8 px apart, groups 24 px or more apart (adjust to the scale).
- Put the main action where the eye ends: bottom right of a dialog on desktop, a full-width button
  at the bottom on a phone. Follow the platform convention.

### 3. Typography

- Body text at least 16 px on web and mobile. Never under 12 px for anything users must read.
- Line length about 45 to 75 characters. Line height about 1.4 to 1.6 for body text, tighter for
  large headings.
- Use weight and size for hierarchy. Use at most two or three weights.
- Numbers in tables use tabular figures (same width) and align to the right.
- Choose fonts on purpose. A system font is fine for a tool. A content page with a voice deserves a
  chosen face. Load only the weights you use.

### 4. Colour

- Check contrast on every text and control (`design-quality` gates). Grey text on a coloured
  background is a common failure: tint it from the background instead.
- Build each colour as a small ramp (for example 50 to 900) so hover, borders, and backgrounds stay
  in the family.
- A dark theme is its own palette, not an inverted light theme. Use dark grey, not pure black, for
  large surfaces, and lower the saturation of accents.
- Never use colour as the only signal. Add an icon, a word, or a shape.
- Pick light or dark from the place of use (a bright workshop, a dark control room), not from
  fashion.

### 5. Components and states

Every interactive component needs these states, designed and visible:

| State | Rule |
| --- | --- |
| Default | Looks clickable if it is clickable (signifier) |
| Hover | Small, clear change. Not the only sign that it is clickable |
| Focus | Clearly visible ring with at least 3:1 contrast. Never removed |
| Pressed or active | Instant feedback |
| Selected or on | Different from hover, and not by colour alone |
| Disabled | Clearly inactive, and the reason is shown nearby or in a tooltip |
| Loading | The control shows progress and cannot be pressed twice |
| Error | Message next to the control, in words |

- One component for one job. Do not make three kinds of button that look almost the same.
- Button hierarchy: one primary per screen area, then secondary, then text-only buttons.
- Icons from one library with one stroke width and one size grid. Icon-only buttons need a label
  for screen readers and, for unclear icons, a visible label or tooltip.

### 6. Motion

- Use motion to show what changed: an item that opens, moves, or appears.
- Short: about 150 to 300 ms for interface changes. Ease out when things enter.
- One planned moment is better than effects everywhere. Do not animate every section on scroll.
- Respect the "reduce motion" setting of the operating system.

### 7. Review your own screens, then hand over

1. Screenshot at phone and desktop size (or the real screen size of the device).
2. Squint test, grey test, five-second test (`design-quality`).
3. Fill long names, empty data, and errors, and look again.
4. Remove one decoration.
5. Give the screenshots to a separate reviewer with the rubric in `design-quality`.

## Avoid the generic look

These patterns appear when no one made a choice. Use one only when the brief asks for it or it
truly fits the product.

- Everything in identical rounded cards with the same soft shadow. Cards inside cards.
- A small all-capitals label above every heading. Section numbers on content that is not a
  sequence.
- The "big number, small label, gradient" hero. Gradient text. Purple-to-blue gradients.
- One headline word in a different colour or italic.
- Glass and blur effects as decoration.
- A thick coloured stripe on the left of every card or alert.
- The same fade-in on every section. Hover effects on every card.
- Emoji or text symbols instead of real icons. Monospace text to look "technical".
- A warm cream background with a serif headline and a clay-orange accent, or a near-black page with
  one neon accent, chosen by habit rather than for the product.

## GUI review checklist

- [ ] Design plan written: palette, type scale, spacing scale, layout, one bold choice
- [ ] Every value comes from a token
- [ ] Clear hierarchy in the squint and grey tests
- [ ] Text at least 16 px body, lines 45 to 75 characters, contrast gates pass
- [ ] All component states designed, focus always visible
- [ ] Empty, loading, error, long text, and full data all look intended
- [ ] Works at the smallest and largest screen size of the product
- [ ] Light and dark themes both checked, if the product has both
- [ ] No generic patterns that nobody chose
- [ ] Scored with `design-quality`

## Terminology and standards

- Design tokens: named values for colour, type, and spacing, shared by design and code. The W3C
  Design Tokens Community Group format is a common file format for them.
- Platform guidelines: Apple Human Interface Guidelines, Google Material Design 3, Microsoft
  Fluent 2. Follow the one for the platform when you build a native app.
- Gestalt principles: proximity, similarity, continuity, closure, common region. They explain why
  space and alignment create groups.
- Robert Bringhurst, "The Elements of Typographic Style": the base for type scale, line length,
  and line height.

## Cross-links

| Need | Skill |
| --- | --- |
| Flows and words | `ux-design` |
| Web build rules | `web-app-design` |
| Machine operator screens | `machine-hmi-design` |
| Score and compare designs | `design-quality` |
| Brand voice and marketing pages | `marketing` |

## Sources and credits

- The design plan, the "spend boldness in one place" rule, the list of generic patterns, and the
  guidance on motion are adapted from the frontend-design skill by Anthropic
  (https://github.com/anthropics/skills, Apache License 2.0) and from Impeccable by Paul Bakaus
  (https://github.com/pbakaus/impeccable, Apache License 2.0).
- Refactoring UI (Wathan and Schoger) for practical hierarchy, spacing, and colour ramps.
