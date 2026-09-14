# Communication

This rule applies to **every text you write**: chat replies, logs, decisions, mistake notes, architecture docs, patterns, README files, comments, commit messages, and pull-request text.

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

## Markdown and length

- Use code citations as ```startLine:endLine:filepath blocks on their own line; skip large irrelevant regions with `...`.
- In non-citation code blocks, write full commands with no `...` omissions.
- Use markdown links for paths and URLs with full strings.
- Write in complete sentences.
- Keep responses proportional to task complexity.
- Use bold and backticks sparingly; avoid section symbols in user-facing text.
- Do not end by asking if the reader wants more help. Ask a direct question only when the next step is unclear.
