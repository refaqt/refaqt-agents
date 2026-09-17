# Reporting work

This rule covers every text you publish about work you did: pull request titles and descriptions,
commit messages, comments and review replies on GitHub, issues, and entries in `docs/log/`,
`docs/decisions/`, and `docs/mistakes/`.

Write all of it in B2 English. Follow [communication.md](communication.md) and pass the manager
test in that file.

**Your reader is a manager, not a developer.** They decide whether to merge, whether to worry, and
what to tell a customer. They will not open the code. Write for that person. Developers who need
detail get their own block at the end.

## Pull request title

One line, at most 72 characters. Say what a person can now do, or what stopped being broken. No
function names. No file names, unless the file is the point of the change.

**Bad:** `refactor(cli): dispatch gates via cli.GATES, add doqs.sh/doqs.bat launchers`

**Good:** `Add one command to run all project checks`

## Pull request body

Use these four headings, in this order, spelled exactly like this. Then one closed block for the
technical detail.

```markdown
## What changed

## Why it matters

## What you need to do

## How it was checked

<details>
<summary>Notes for reviewers</summary>

</details>
```

| Heading | What goes in it |
| --- | --- |
| **What changed** | Two to four sentences. The result, in plain words. Start with the sentence a reader would repeat to someone else. |
| **Why it matters** | The problem this solves, in the reader's terms: time lost, risk, cost, confusion. If it solves nothing on its own, say which larger piece of work it belongs to and link that work. |
| **What you need to do** | What changes for the people who use the project. "Nothing" is a good answer. Write it anyway. |
| **How it was checked** | What you ran and what passed. Numbers are fine. Say clearly if something is untested, and why. |
| **Notes for reviewers** | Everything technical: file names, function names, test names, trade-offs, known gaps. No length limit, because the block is closed until someone opens it. |

Rules for the body:

- Everything above `<details>` stays under 200 words.
- Do not invent a heading. Do not use a heading as a joke.
- Link other pull requests and issues as full markdown links with the owner and repository name,
  for example [refaqt/doqs#18](https://github.com/refaqt/doqs/pull/18). Never write a bare `#18`.
- Copy [`templates/pull-request.md`](../templates/pull-request.md) to
  `.github/pull_request_template.md` so the box on GitHub starts with these headings.

## Commit messages

First line: `type(scope): what changed, in plain words`. At most 72 characters.

Types: `feat`, `fix`, `docs`, `test`, `refactor`, `chore`.

Add a body only when the first line is not enough. The body says why, not how.

**Bad:** `refactor(cli): hoist GATES, drop --warnings-only no-op`

**Good:** `refactor(cli): keep the list of checks in one place`

## Comments and review replies

- Answer the question that was asked. One point per comment.
- Say what you did, or why you did not do it. Leave out the steps in between.
- If you disagree, say so in one sentence and give the reason.
- Do not post a comment that only repeats what the change already shows.

## Issues

The title is the problem, not the fix. The body says what happens, what you expected, how someone
else can see it, and how bad it is. Keep the same order: the effect first, the technical detail
last.

## Log entries

`docs/log/`, `docs/decisions/`, and `docs/mistakes/` keep their own headings. See
[living-docs.md](living-docs.md) and the `log` skill.

The manager test still applies to the text under those headings. Write the outcome first. Put
command output, error traces, and file listings in a closed `<details>` block or in a linked file,
never in the running text.

## Checklist before you publish

- [ ] The first sentence makes sense to someone who does not have the repository open.
- [ ] Everything above "Notes for reviewers" is under 200 words.
- [ ] No function name, error name, or test name outside the closed block, unless the reader has to
      type it.
- [ ] Every pull request and issue reference is a full markdown link.
- [ ] The headings are the four standard ones, spelled the same way.
- [ ] No sentence fragments. No clever headings.

## Worked example

This is a real pull request description, shortened, and the same work written again.

**Bad:**

> ### The problem
>
> `scripts/` holds nineteen files you can run. Nothing tells you which one, or in what order.
>
> ### One name
>
> `doqs.sh check`, `doqs.sh generate`, `doqs.sh list`. Both launchers call `python doqs/doqs.py`,
> which dispatches from `scripts/cli.py`.
>
> ### The compatibility promise
>
> `validate_all.py` still runs the same seven gates, and nothing else. Proven, not assumed — output
> captured before and after, on all three fixtures. Byte-identical output, same exit codes. The
> gate list now lives in `cli.GATES` and `validate_all.py` imports it, so the two cannot drift
> apart.
>
> ### One deviation from the plan
>
> The plan said to call each gate in-process, for speed. I kept subprocess dispatch, which is what
> `validate_all.py` has always done.

**Good:**

> ## What changed
>
> The project had nineteen separate scripts and no instructions about which one to run. There is
> now one command, `doqs.sh`, with three actions: `check`, `generate`, and `list`. `doqs.bat` does
> the same on Windows.
>
> ## Why it matters
>
> New people, and agents, had to guess which script to run and in what order. They guessed wrong.
> One command with three clear actions removes the guessing.
>
> ## What you need to do
>
> Nothing. Every old script still works exactly as before. Use the new command when you want to.
>
> ## How it was checked
>
> The old check command was run before and after the change, on three test projects. The output was
> identical every time. 240 automated tests pass, up from 215.
>
> <details>
> <summary>Notes for reviewers</summary>
>
> - `validate_all.py` now imports the check list from `cli.GATES`, so the two lists cannot drift
>   apart.
> - Checks still run as separate processes, not in one process as the plan suggested. One check
>   that crashes cannot take down the whole run.
> - `check_links.py`, `validate_build.py`, and `aggregate_bom.py` now have a `main(argv)`, so they
>   can be imported and tested.
> - `check_names.py --warnings-only` did nothing and was removed.
> - `build_graph.py` gained `--check`. It is deliberately not part of `doqs check`.
>
> </details>
