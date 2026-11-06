---
name: web-app-design
description: >-
  Build and review web apps and web pages so they are usable, accessible,
  fast, and good-looking in the browser. Use when you write or review HTML,
  CSS, React, Vue, Svelte, or other front-end code, when you need responsive
  layouts, accessible forms and controls, keyboard support, dark mode, or
  page speed, or when the user asks to "review the UI", "check
  accessibility", or "audit the front end". Turns ux-design and gui-design
  into browser code and checks it with design-quality.
---
# Web App Design

This skill turns a good design into a good web page. Most web usability problems are small code
choices: a `div` that should be a `button`, a removed focus ring, a field that blocks paste, a
layout that jumps while it loads. Each one is easy to fix and easy to check.

## Scope

**Owns:**
- Semantic HTML, accessible names, and keyboard support
- Responsive layout from 320 px phones to large screens
- Forms in the browser
- Loading speed and layout stability (Core Web Vitals)
- Light and dark themes in CSS, motion settings, touch behaviour
- Testing a running page: screenshots, gates, keyboard walk, accessibility rules

**Does NOT own:**
- Flows, structure, and interface words → `ux-design`
- Visual direction, tokens, and components → `gui-design`
- Scoring and the definition of done → `design-quality`
- Back-end, build pipeline, and release → `software-development`

## Core principles

- **Use the platform.** A real `<button>`, `<a>`, `<label>`, `<select>`, and `<dialog>` give
  keyboard support, screen reader support, and correct behaviour for free. Add ARIA (extra attributes
  that describe a control to screen readers) only when no HTML element fits.
- **Accessible is the floor, not a feature.** WCAG 2.2 level AA on every page. It is also the law
  for many products in the EU (European Accessibility Act).
- **Mobile first.** Design and test at 375 px first, then grow. Check 320 px as the smallest.
- **Stable and fast.** Content must not jump while it loads. Every click answers at once.
- **The URL is part of the interface.** Filters, tabs, search, and pages are in the URL, so users
  can share, bookmark, and go back.
- **Test the real page in a real browser.** Use Playwright (already present in most of our
  environments) to load, click, screenshot, and measure.

## Rules

Give each finding as `file:line - problem - fix`. The rules below are a short set. For a full,
current list, read the Vercel Web Interface Guidelines
(https://github.com/vercel-labs/web-interface-guidelines) before a large review.

### Accessibility and keyboard

- Actions are `<button>`. Navigation is `<a href>`. Never a `div` or `span` with a click handler.
- Every input has a `<label>` (or `aria-label`). Every icon-only button has `aria-label`.
- Images have `alt`. Decorative images and icons have `alt=""` or `aria-hidden="true"`.
- Headings go in order (`h1` then `h2`, no skips). One `h1` per page. Add a "skip to content" link.
- The focus ring is always visible. Never `outline: none` without a replacement. Use
  `:focus-visible`.
- Sticky headers and footers must not hide the focused element.
- Messages that appear by themselves (toasts, live validation) use `aria-live="polite"`.
- Dialogs trap focus while open, close with Escape, and return focus to the button that opened
  them.
- Drag, swipe, and pinch actions also have a click and keyboard alternative.

### Forms

- Correct `type` and `inputmode` (`email`, `tel`, `url`, `number`) so phones show the right
  keyboard. Correct `autocomplete` so browsers can fill the fields.
- Never block paste.
- The whole label and the checkbox or radio button are one click target.
- The submit button stays active until the request starts, then shows progress.
- Errors appear next to the field. On submit, move the focus to the first error.
- Warn before the user leaves a page with unsaved changes.

### Layout and responsive design

- Use flexbox and grid, not JavaScript measurement, for layout.
- No sideways scroll at 320 px. Long words, names, and numbers wrap or truncate with a full value
  in a tooltip.
- Flex children that hold text need `min-width: 0` so they can shrink.
- Never disable zoom (`user-scalable=no` or `maximum-scale=1`).
- Respect safe areas on phones with a notch (`env(safe-area-inset-*)`).
- Touch targets at least 44 x 44 px on touch screens, with space between them.

### Speed and stability

- Targets at the 75th percentile of real visits (Core Web Vitals, "good"): Largest Contentful Paint
  (main content shown) 2.5 s or less, Interaction to Next Paint (reaction to a click) 200 ms or
  less, Cumulative Layout Shift (content jumping) 0.1 or less.
- Give every image a `width` and `height` (or an aspect ratio) so the page does not jump.
  Load images below the first screen only when the user scrolls to them (lazy loading).
- Animate only `transform` and `opacity`. Never `transition: all`.
- Long lists (more than about 50 rows) use virtual scrolling.
- Load only the font weights you use, with `font-display: swap`.

### Theme, motion, and touch

- Dark theme: set `color-scheme: dark` and a matching `<meta name="theme-color">`. Check contrast in
  both themes.
- Honour `prefers-reduced-motion`: keep the change of state, drop the movement.
- Show a skeleton or a spinner within about 1 s for slow content. Text ends with "…" while loading
  ("Saving…").
- `touch-action: manipulation` on controls removes the tap delay.

### Content and language

- Format dates, numbers, and currencies with `Intl.DateTimeFormat` and `Intl.NumberFormat`.
- Set `lang` on `<html>`. Mark brand names and code with `translate="no"`.
- Buttons name the action ("Save speed"). Errors say how to fix the problem.

### Navigation and state

- The URL holds filters, tabs, sorting, and page number.
- Links work with Ctrl or Cmd click and middle click (real `<a href>`).
- Destructive actions have undo or a confirmation that names what will be lost.

## Key workflows

### Review a web interface

1. Read `ux-design` notes and the design plan from `gui-design`, if they exist.
2. Start the app and run the measuring script from `design-quality` with `--axe` and `--shots`.
3. Read the source of the screens in scope and check the rules above. Report as
   `file:line - problem - fix`.
4. Do a keyboard walk: with Playwright, press Tab through the page and screenshot the focus each
   time, or do it by hand. Every control must be reachable, in a logical order, and visible.
5. Optional: run `npx impeccable detect <folder or url>` for common generated-design patterns.
   Treat its findings as hints and confirm each one.
6. Hand the screenshots to the scored review in `design-quality`.

### Build a new screen

1. Start from the flow (`ux-design`) and the design plan and tokens (`gui-design`).
2. Build the semantic HTML first, then the layout, then the style, then the motion.
3. Build the empty, loading, and error states at the same time as the full state.
4. Test at 375 px and 1440 px after each larger step. Fix problems before you add more.
5. Run the gates and the review before you call it done.

### Example: a keyboard walk with Playwright

```js
const { chromium } = require("playwright");
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  await page.goto("http://localhost:5173");
  for (let i = 0; i < 30; i++) {
    await page.keyboard.press("Tab");
    const el = await page.evaluate(() => {
      const a = document.activeElement;
      return `${a.tagName} ${(a.innerText || a.getAttribute("aria-label") || "").trim().slice(0, 30)}`;
    });
    console.log(i + 1, el);
    await page.screenshot({ path: `focus-${String(i + 1).padStart(2, "0")}.png` });
  }
  await browser.close();
})();
```

## Web review checklist

- [ ] Measuring script passes all gates at phone and desktop size
- [ ] No serious or critical axe-core findings
- [ ] Keyboard walk: every control reachable, order logical, focus visible
- [ ] Works at 320 px, 375 px, 768 px, and 1440 px wide, and at 200 % text size
- [ ] No layout jump while loading. Images have sizes
- [ ] Forms: labels, types, autocomplete, paste allowed, inline errors
- [ ] URL holds the state of filters, tabs, and pages
- [ ] Reduced motion and dark theme checked
- [ ] Scored with `design-quality`

## Terminology and standards

- WCAG 2.2 (Web Content Accessibility Guidelines), level AA. EN 301 549 is the European standard
  that uses it.
- WAI-ARIA Authoring Practices Guide: patterns for menus, tabs, dialogs, and other widgets
  (https://www.w3.org/WAI/ARIA/apg/).
- Core Web Vitals: the three speed and stability measures from Google (https://web.dev/vitals/).

## Cross-links

| Need | Skill |
| --- | --- |
| Flows and words | `ux-design` |
| Visual design and tokens | `gui-design` |
| Gates, scores, scorecard | `design-quality` |
| Code, tests, and release | `software-development` |
| Legal accessibility duties | `product-compliance`, `european-law` |

## Sources and credits

- Vercel Web Interface Guidelines (https://github.com/vercel-labs/web-interface-guidelines). The
  rules above are written in our own words from that list and from WCAG 2.2.
- W3C WAI, WCAG 2.2 and the ARIA Authoring Practices Guide.
- Google, web.dev, Core Web Vitals thresholds.
