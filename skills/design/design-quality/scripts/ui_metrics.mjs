#!/usr/bin/env node
// Measure a rendered web page against the design gates in ../SKILL.md.
//
// Usage:
//   node ui_metrics.mjs <url> [--out report.json] [--shots folder] [--axe]
//
// The script opens the page at a phone size and a desktop size. It checks text contrast, touch
// target size, sideways scrolling, labels, alt text, heading order, and it counts font sizes,
// font families, colours, alignment lines and spacing values. With --shots it saves a normal
// screenshot, a blurred one (squint test) and a grey one (colour-free test) for each size.
// With --axe it also runs the axe-core accessibility rules (needs network access to cdnjs).
//
// Exit code: 0 = all gates pass, 1 = at least one gate fails, 2 = the page could not be measured.
// Needs Playwright for Node.js: `npm i -D playwright` in the project, or a global install.

import { createRequire } from "node:module";
import fs from "node:fs";
import path from "node:path";

const require = createRequire(import.meta.url);
let chromium;
try {
  ({ chromium } = require("playwright"));
} catch {
  console.error("Playwright for Node.js is missing. Install it with: npm i -D playwright");
  process.exit(2);
}

const args = process.argv.slice(2);
const url = args.find((a) => !a.startsWith("--"));
const opt = (name) => {
  const i = args.indexOf(name);
  return i >= 0 ? args[i + 1] : undefined;
};
if (!url) {
  console.error("Usage: node ui_metrics.mjs <url> [--out report.json] [--shots folder] [--axe]");
  process.exit(2);
}
const outFile = opt("--out");
const shotDir = opt("--shots");
const runAxe = args.includes("--axe");

const VIEWPORTS = [
  { name: "phone", width: 375, height: 812 },
  { name: "desktop", width: 1440, height: 900 },
];

// Soft limits for the counted values. Above these, a page usually looks busy or unplanned.
// They are warnings, not gates: a data-heavy tool can have good reasons to go over.
const SOFT = { fontSizes: 6, fontFamilies: 2, colours: 12, leftEdges: 12, offGridSpacingPct: 20 };

// Runs inside the page. Keep it free of outside references.
function measure() {
  const parse = (c) => {
    const m = c.match(/rgba?\(([^)]+)\)/);
    if (!m) return null;
    const p = m[1].split(/[ ,/]+/).filter(Boolean).map(Number);
    return { r: p[0], g: p[1], b: p[2], a: p.length > 3 ? p[3] : 1 };
  };
  const lum = ({ r, g, b }) => {
    const f = (v) => {
      v /= 255;
      return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
    };
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b);
  };
  const ratio = (a, b) => {
    const [x, y] = [lum(a), lum(b)].sort((m, n) => n - m);
    return (x + 0.05) / (y + 0.05);
  };
  const blend = (top, under) => ({
    r: top.r * top.a + under.r * (1 - top.a),
    g: top.g * top.a + under.g * (1 - top.a),
    b: top.b * top.a + under.b * (1 - top.a),
    a: 1,
  });
  // Walk up the tree to find the colour behind an element. Returns null over images or gradients.
  const background = (el) => {
    const layers = [];
    for (let n = el; n && n.nodeType === 1; n = n.parentElement) {
      const cs = getComputedStyle(n);
      if (cs.backgroundImage && cs.backgroundImage !== "none") return null;
      const c = parse(cs.backgroundColor);
      if (c && c.a > 0) {
        layers.push(c);
        if (c.a >= 1) break;
      }
    }
    let bg = { r: 255, g: 255, b: 255, a: 1 };
    for (let i = layers.length - 1; i >= 0; i--) bg = blend(layers[i], bg);
    return bg;
  };
  const visible = (el) => {
    const r = el.getBoundingClientRect();
    const cs = getComputedStyle(el);
    return r.width > 0 && r.height > 0 && cs.visibility !== "hidden" && cs.display !== "none" && Number(cs.opacity) > 0;
  };
  const describe = (el) => {
    const id = el.id ? `#${el.id}` : "";
    const cls = typeof el.className === "string" && el.className.trim() ? "." + el.className.trim().split(/\s+/).slice(0, 2).join(".") : "";
    const text = (el.innerText || el.getAttribute("aria-label") || el.getAttribute("alt") || "").trim().slice(0, 40);
    return `${el.tagName.toLowerCase()}${id}${cls}${text ? ` "${text}"` : ""}`;
  };

  const all = [...document.querySelectorAll("body *")].filter(visible);
  const fontSizes = new Set();
  const fontFamilies = new Set();
  const colours = new Set();
  const leftEdges = new Set();
  const spacing = [];
  const contrastFails = [];
  const smallText = [];
  const longLines = [];

  for (const el of all) {
    const cs = getComputedStyle(el);
    const hasText = [...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim().length > 0);
    for (const prop of ["marginTop", "marginBottom", "paddingTop", "paddingBottom", "paddingLeft", "paddingRight", "rowGap", "columnGap"]) {
      const v = parseFloat(cs[prop]);
      if (v > 0) spacing.push(v);
    }
    const bgc = parse(cs.backgroundColor);
    if (bgc && bgc.a > 0) colours.add(`${bgc.r},${bgc.g},${bgc.b}`);
    if (!hasText) continue;

    const size = parseFloat(cs.fontSize);
    fontSizes.add(Math.round(size));
    fontFamilies.add(cs.fontFamily.split(",")[0].replace(/["']/g, "").trim());
    const fg = parse(cs.color);
    if (fg) colours.add(`${fg.r},${fg.g},${fg.b}`);
    const r = el.getBoundingClientRect();
    if (cs.display !== "inline") leftEdges.add(Math.round(r.left / 2) * 2);
    if (size < 12) smallText.push(describe(el));
    if (el.tagName === "P" && size > 0) {
      const chars = (el.innerText || "").length;
      const lines = Math.max(1, Math.round(r.height / (parseFloat(cs.lineHeight) || size * 1.4)));
      if (lines > 1 && chars / lines > 85) longLines.push(`${describe(el)} ~${Math.round(chars / lines)} characters per line`);
    }
    const bg = background(el);
    if (fg && bg) {
      const weight = Number(cs.fontWeight) || 400;
      const large = size >= 24 || (size >= 18.66 && weight >= 700);
      const need = large ? 3 : 4.5;
      const got = ratio(blend(fg, bg), bg);
      if (got < need) contrastFails.push(`${describe(el)} ${got.toFixed(2)}:1 (needs ${need}:1)`);
    }
  }

  // Touch and click targets. Inline links inside running text are exempt (WCAG 2.2, 2.5.8).
  const targetSel = "a[href], button, input:not([type=hidden]), select, textarea, summary, [role=button], [role=link], [role=tab], [role=checkbox], [role=menuitem], [tabindex]:not([tabindex='-1'])";
  const tooSmall = [];
  const under44 = [];
  for (const el of document.querySelectorAll(targetSel)) {
    if (!visible(el)) continue;
    const cs = getComputedStyle(el);
    if (el.tagName === "A" && cs.display === "inline") continue;
    const r = el.getBoundingClientRect();
    const minSide = Math.min(r.width, r.height);
    if (minSide < 24) tooSmall.push(`${describe(el)} ${Math.round(r.width)}x${Math.round(r.height)} px`);
    else if (minSide < 44) under44.push(describe(el));
  }

  const unlabelled = [];
  for (const el of document.querySelectorAll("input, select, textarea")) {
    if (["hidden", "submit", "button", "reset", "image"].includes(el.type)) continue;
    if (!visible(el)) continue;
    const named = el.labels?.length || el.getAttribute("aria-label") || el.getAttribute("aria-labelledby") || el.getAttribute("title");
    if (!named) unlabelled.push(describe(el));
  }
  const iconButtons = [...document.querySelectorAll("button, a[href], [role=button]")]
    .filter((el) => visible(el) && !(el.innerText || "").trim() && !el.getAttribute("aria-label") && !el.getAttribute("aria-labelledby") && !el.getAttribute("title") && !el.querySelector("img[alt]:not([alt=''])"))
    .map(describe);
  const noAlt = [...document.querySelectorAll("img")].filter((i) => visible(i) && !i.hasAttribute("alt")).map(describe);

  const headings = [...document.querySelectorAll("h1,h2,h3,h4,h5,h6")].filter(visible).map((h) => Number(h.tagName[1]));
  const headingSkips = [];
  for (let i = 1; i < headings.length; i++) if (headings[i] > headings[i - 1] + 1) headingSkips.push(`h${headings[i - 1]} -> h${headings[i]}`);

  const offGrid = spacing.filter((v) => Math.abs(v / 4 - Math.round(v / 4)) > 0.05).length;
  return {
    gates: {
      contrastFails,
      targetsUnder24px: tooSmall,
      sidewaysScroll: document.documentElement.scrollWidth > window.innerWidth + 1,
      unlabelledInputs: unlabelled,
      unnamedIconButtons: iconButtons,
      imagesWithoutAlt: noAlt,
      textUnder12px: smallText,
    },
    warnings: {
      targetsUnder44px: under44,
      headingSkips,
      h1Count: headings.filter((h) => h === 1).length,
      longLines,
    },
    counts: {
      fontSizes: [...fontSizes].sort((a, b) => a - b),
      fontFamilies: [...fontFamilies],
      colours: colours.size,
      leftEdges: leftEdges.size,
      spacingValues: new Set(spacing.map((v) => Math.round(v))).size,
      offGridSpacingPct: spacing.length ? Math.round((100 * offGrid) / spacing.length) : 0,
    },
  };
}

const browser = await chromium.launch();
const report = { url, measuredAt: new Date().toISOString(), viewports: {} };
let failed = false;
try {
  for (const vp of VIEWPORTS) {
    const page = await browser.newPage({ viewport: { width: vp.width, height: vp.height } });
    await page.goto(url, { waitUntil: "networkidle", timeout: 60000 });
    const result = await page.evaluate(measure);
    if (runAxe) {
      try {
        await page.addScriptTag({ url: "https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.10.2/axe.min.js" });
        const axe = await page.evaluate(async () => (await window.axe.run()).violations.map((v) => `${v.impact}: ${v.id} (${v.nodes.length}x) ${v.help}`));
        result.gates.axeViolations = axe;
      } catch (e) {
        result.notes = [`axe-core could not run: ${e.message.split("\n")[0]}`];
      }
    }
    if (shotDir) {
      fs.mkdirSync(shotDir, { recursive: true });
      await page.screenshot({ path: path.join(shotDir, `${vp.name}.png`), fullPage: true });
      await page.addStyleTag({ content: "html{filter:blur(6px)!important}" });
      await page.screenshot({ path: path.join(shotDir, `${vp.name}-squint.png`) });
      await page.addStyleTag({ content: "html{filter:grayscale(1)!important}" });
      await page.screenshot({ path: path.join(shotDir, `${vp.name}-grey.png`) });
    }
    report.viewports[vp.name] = result;
    await page.close();
  }
} catch (e) {
  console.error(`Could not measure ${url}: ${e.message.split("\n")[0]}`);
  await browser.close();
  process.exit(2);
}
await browser.close();

// Print a short summary that a person can read.
for (const [name, r] of Object.entries(report.viewports)) {
  console.log(`\n== ${name} ==`);
  for (const [gate, v] of Object.entries(r.gates)) {
    const bad = Array.isArray(v) ? v.length > 0 : v === true;
    failed ||= bad;
    const n = Array.isArray(v) ? v.length : v ? 1 : 0;
    console.log(`${bad ? "FAIL" : "pass"}  ${gate}${bad ? ` (${n})` : ""}`);
    if (Array.isArray(v)) v.slice(0, 5).forEach((x) => console.log(`        ${x}`));
  }
  const c = r.counts;
  const warn = (ok) => (ok ? "ok  " : "WARN");
  console.log(`${warn(c.fontSizes.length <= SOFT.fontSizes)}  font sizes: ${c.fontSizes.length} [${c.fontSizes.join(", ")}] (soft limit ${SOFT.fontSizes})`);
  console.log(`${warn(c.fontFamilies.length <= SOFT.fontFamilies)}  font families: ${c.fontFamilies.length} [${c.fontFamilies.join(", ")}]`);
  console.log(`${warn(c.colours <= SOFT.colours)}  distinct colours: ${c.colours} (soft limit ${SOFT.colours})`);
  console.log(`${warn(c.leftEdges <= SOFT.leftEdges)}  alignment lines (left edges): ${c.leftEdges} (soft limit ${SOFT.leftEdges})`);
  console.log(`${warn(c.offGridSpacingPct <= SOFT.offGridSpacingPct)}  spacing off the 4 px grid: ${c.offGridSpacingPct} % (${c.spacingValues} distinct values)`);
  const w = r.warnings;
  console.log(`${warn(!w.targetsUnder44px.length)}  targets between 24 and 44 px: ${w.targetsUnder44px.length}`);
  console.log(`${warn(!w.headingSkips.length && w.h1Count === 1)}  headings: ${w.h1Count} h1, skips: ${w.headingSkips.join(", ") || "none"}`);
  console.log(`${warn(!w.longLines.length)}  paragraphs over 85 characters per line: ${w.longLines.length}`);
  (r.notes || []).forEach((n) => console.log(`note  ${n}`));
}
if (outFile) fs.writeFileSync(outFile, JSON.stringify(report, null, 2));
console.log(`\n${failed ? "Result: at least one gate FAILS." : "Result: all gates pass."}${outFile ? ` Full report: ${outFile}` : ""}`);
process.exit(failed ? 1 : 0);
