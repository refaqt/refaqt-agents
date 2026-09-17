# Communication

This rule applies to **every text you write**: chat replies, quotes, specs, work instructions, drafts, logs, decisions, mistake notes, architecture docs, patterns, README files, code comments, commit messages, pull-request text, issues, and comments and review replies on GitHub.

## Language (B2 English)

Write so a non-native speaker can read you easily. Use CEFR B2 English (clear, everyday English at an upper-intermediate level).

- Use short sentences. One idea per sentence.
- Use common words. Prefer simple language over jargon.
- Use the active voice.
- Do not use idioms, slang, or unexplained acronyms.
- If you need a technical or legal name, give the everyday meaning first, then the exact term.
- Keep meaning exact: file names, commands, official titles, units, and numbers stay as they are.
- Do not name internal skills in text meant for people. Say what the topic is.
- If you quote a person, you may keep their words in quotation marks. Your own sentences stay B2.

**Bad (chat):** "I'll orchestrate a refactor to encapsulate persistence and mitigate the race."

**Good (chat):** "I will put the database code in one place. That should stop two parts of the program from writing at the same time."

**Bad (repo):** "Escalate repeated failures into standing guidance after a process gap."

**Good (repo):** "If the same mistake happens twice, write a clear rule so it does not happen again."

Do not change code names, programming interface names (APIs), file paths, or shell commands to make them simpler.

## The manager test

Before you send any text, read your own sentences as a manager who does not have the repository
open. Every sentence must pass all three checks.

1. **No hidden nouns.** If a sentence holds a file name, a function name, an error name, or a
   command, ask what it is doing there. Keep it only if the reader must type it or open it. If it
   is there as proof, move it to the technical block at the end of the text.
2. **Says the point, not the route.** Write the result. Do not write the steps you took to get
   there.
3. **Stands alone.** No bare `#18`, no "as planned", no "the parity test". Name the thing in full,
   or leave it out.

Also: no clever headings, no sentence fragments, and no line that only makes sense to someone who
already read the code.

**Bad:** "Kept subprocess dispatch, so the `SystemExit` that `aggregate_bom.collect()` raises from
library code stays harmless."

**Good:** "Each check still runs as its own small program. If one check crashes, the others still
finish, and you still get a full report."

## Reporting work

Pull requests, commit messages, comments and review replies on GitHub, issues, and entries in
`docs/log/` have a fixed shape. Follow [reporting.md](reporting.md). Use the four standard
headings and put the technical detail in one closed block at the end.

## How to answer people

Use this shape in chat replies and in documents (quotes, specs, work instructions, drafts, and decision notes).

You are talking to a startup founder, a shop-floor colleague, or a cooperative member — not a specialist in your field. Keep the facts accurate. Change only the language.

- Start with the decision, the cash, the risk, or what is going wrong. Then state the accurate rule.
- Everyday words first, official term next.
- Structure advice in this order:
  1. **What this means** — the point the reader needs
  2. **The rule** — the accurate position, with official names
  3. **What to do next** — concrete steps
  4. **When to get a human specialist** — a lawyer, accountant, notified body (official testing body), or domain expert, if the stakes are high
- A skill may name these parts differently. Keep the same order of ideas.
- Put a disclaimer in one sentence. Do not put it at the start.
- Do not invent rates, thresholds, dates, or classifications. If a number matters, say it must be verified.

**Bad:** "Escalate to `product-compliance` and `european-law` for EMC/LVD applicability and the CE technical file."

**Good:** "If you sell a machine that uses mains power in the EU, you need a product safety file and the EU product safety mark (CE marking). Next: list what the machine does, which parts take power, and which countries you sell in. Call a notified body (an official testing body) or a lawyer if you are unsure which tests you need."

## Markdown and length

- Use code citations as ```startLine:endLine:filepath blocks on their own line; skip large irrelevant regions with `...`.
- In non-citation code blocks, write full commands with no `...` omissions.
- Use markdown links for paths and URLs with full strings.
- Write in complete sentences.
- Keep responses proportional to task complexity.
- Use bold and backticks sparingly; avoid section symbols in user-facing text.
- Do not end by asking if the reader wants more help. Ask a direct question only when the next step is unclear.
