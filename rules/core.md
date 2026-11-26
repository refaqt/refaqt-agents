# Core rules

These rules apply to every task. Everything else loads only when a task needs it: see the table
"Read only when the task needs it" in `AGENTS.md`.

## Write B2 English

Every reply and every file: chat, code comments, commits, pull requests, docs.

- Short sentences, one idea each. Common words. Active voice. No idioms, no slang.
- Explain an acronym or a technical term the first time: the everyday meaning first.
- Keep file names, commands, code names, units and numbers exactly as they are.
- **Manager test.** Read each sentence as a manager without the repository open. Say the result,
  not the route. A file or function name stays only if the reader must open or type it; other
  detail goes in a closed block at the end. No bare `#18`: write `owner/repo#18` as a link.
- Do not invent rates, dates, limits or classifications. Say a number must be checked.

## Work

- Follow user, tool and skill instructions completely. Use the real shell. Do not give up after one
  failure. When you are not sure, do less and ask.
- Start each task by reading `docs/mistakes/README.md`, the index only. Say in one line which
  prevention rules apply. Open a note only when its rule matches the task.
- Before larger work, read `docs/architecture.md` (a short overview) and the index
  `docs/decisions/README.md`. Do not read whole folders.
- Work on a new branch, not on `main`, unless the user says otherwise.
- Read the code before you write. Match the local style. Keep diffs small. Do not refactor files
  you do not need to touch.
- Done means checked against reality: run the tests or the checks, and say clearly what is
  untested. A value from a data sheet or a standard beats a value from memory.
- Ask before you delete files, change the environment, or publish anything.

## Keep the living docs

One file per entry, in B2 English. Update the folder's `README.md` index in the same change.

| What | Where |
| --- | --- |
| Work done, worth recording | `docs/log/YYYY-MM-DD_topic.md` (skill `log`) |
| Why a real choice was made | `docs/decisions/YYYY-MM-DD_topic.md` |
| A mistake and its prevention rule | `docs/mistakes/YYYY-MM-DD_topic.md` (skill `mistake-log`) |
| A coding pattern that proved useful | `.agents-local/skills/patterns/SKILL.md` (skill `maintain-patterns`) |

If one of these folders is missing, create it from `.agents/bootstrap/docs/`.
