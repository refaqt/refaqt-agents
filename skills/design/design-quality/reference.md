# Design Quality: rubrics and reference values

Give this file to the reviewer together with the screenshots and the list of users and tasks.
Score every line. Write one concrete reason per score: name the element, not "some elements".

## 1. Usability: Nielsen's 10 heuristics (0 to 4 each)

General anchors for every heuristic:

| Score | Meaning |
| --- | --- |
| 0 | Missing. Users are lost or stuck |
| 1 | Poor. Most of the time it fails |
| 2 | Partial. Main flows work, clear gaps remain |
| 3 | Good. Small gaps only |
| 4 | Excellent. Nothing to fix |

| # | Heuristic | What to look for |
| --- | --- | --- |
| 1 | Show the system status | Loading and progress, confirmation after save or delete, where am I (active tab, breadcrumbs), live validation |
| 2 | Speak the user's language | Words the user uses, not system words. Order that matches the real task. Icons people know |
| 3 | User control and freedom | Undo, cancel, back, close, clear filters. A way out of every state |
| 4 | Consistency and standards | Same word, same look, same behaviour everywhere. Platform conventions followed |
| 5 | Prevent errors | Safe defaults, limits on input, confirmation or undo before destructive actions, autosave |
| 6 | Recognise, do not recall | Options visible, labels on icons, recent items, no need to remember from the last screen |
| 7 | Flexible and efficient | Shortcuts, bulk actions, remembered settings, for experts, without making it harder for beginners |
| 8 | Simple, focused design | Only what the task needs on each screen. One clear main action |
| 9 | Help users recover from errors | Plain message, says what happened and how to fix it, keeps what the user typed |
| 10 | Help and documentation | Help in context, where the question comes up. Short and task-based |

Mark a heuristic `n/a` only when it truly cannot apply (for example 7 and 10 on a one-page
marketing site). Then score out of 4 times the number you scored, not out of 40.

Rating bands for the total out of 40: 36 to 40 excellent, 30 to 35 good, 22 to 29 needs work,
under 22 poor.

## 2. Visual quality rubric (0 to 4 each, total out of 32)

| # | Criterion | 0 | 2 | 4 |
| --- | --- | --- | --- | --- |
| 1 | Hierarchy | Everything has the same weight. The eye does not know where to start | The main item is clear, the rest is flat | One clear first item, two or three second items, the rest quiet. Works in the squint and grey tests |
| 2 | Alignment and grid | Edges everywhere, nothing lines up | A grid exists but some parts break it without reason | Every element sits on a few shared lines. Breaks from the grid are on purpose |
| 3 | Spacing and rhythm | Random gaps, cramped or empty areas | Mostly regular, some odd gaps | Spacing from one scale. Related items close, groups clearly apart. More space above a heading than below |
| 4 | Typography | Many sizes and weights, long lines, poor line height | One scale, some extra sizes, line length sometimes too long | One clear scale, 1 or 2 families, lines of about 45 to 75 characters, good line height, numbers line up in tables |
| 5 | Colour | Colour used as decoration everywhere, or low contrast | A palette exists, but meaning is not consistent | Few colours, each with one meaning. Neutral base, accent for the main action and for status only |
| 6 | Consistency | Same thing looks different in different places | Small differences between similar parts | One component for one job, everywhere. Same radius, shadow, and icon style rules |
| 7 | Fit with the subject | Could be any product. Generic template look | Some choices fit the product | The look, words, and images come from the product's own world and its users |
| 8 | Finish of states and details | Empty, error, and loading states missing. Default browser focus, broken long text | Main states present, details rough | Every state designed. Focus, selection, scrollbars, long names, and errors all look intended |

Rating bands for the total out of 32: 28 to 32 excellent, 24 to 27 good, 16 to 23 needs work,
under 16 poor.

### Signs of a generic, unchosen look

These are not always wrong. They are wrong when nobody chose them for this product. If the
reviewer finds several, score criterion 7 at 2 or lower.

- Content cut into many identical rounded cards with the same soft shadow. Cards inside cards.
- A small all-capitals label above every heading.
- A big number with a small label and a gradient accent as the main hero.
- Section numbers (01, 02, 03) on content that is not a sequence.
- Gradient text, decorative glass and blur, purple-to-blue gradients.
- One word in the headline in a different colour or italic.
- The same fade-and-slide entrance on every section.
- Emoji or text symbols in place of real icons.
- A monospace font used to look "technical" for normal text.

## 3. Cognitive load checklist (yes or no)

Count the "no" answers. 0 or 1 is good. 2 or 3 needs work. 4 or more is a P1 problem.

1. Can the user do the main task without other elements pulling their attention away?
2. Is information shown in small groups of about four items or fewer?
3. Are related items clearly grouped (closeness, a shared background, or a line)?
4. Is it clear at once what is most important on the screen?
5. Does the user make one decision at a time?
6. Are there four or fewer visible options at each decision point, with the rest grouped?
7. Can the user act without remembering anything from an earlier screen?
8. Is complex detail shown only when the user needs it?

## 4. Severity

| Severity | Meaning |
| --- | --- |
| P0 | Blocks a main task, causes harm or data loss, or breaks a legal duty |
| P1 | Slows or confuses most users on a main task |
| P2 | Annoying or slow on a less common path |
| P3 | Polish |

## 5. Reviewer report shape

```markdown
Target: <screen, flow, or product>. User: <who>. Tasks: <list>.
Reviewer: <separate sub-agent / person / self only>.

| # | Heuristic | Score | Main reason |
| ... | ... | ... | ... |
Total: <n>/<max>

| # | Visual criterion | Score | Main reason |
| ... | ... | ... | ... |
Total: <n>/32

Cognitive load failures: <n> (<which>)

What works (2 or 3 points, specific).

Problems, most serious first:
- [P?] <what> — <why it matters for this user> — <concrete fix>
```

## 6. Keystroke-Level Model (KLM) operator times

From Card, Moran and Newell (1980). Use them to compare designs, not to promise exact times.

| Operator | Meaning | Seconds |
| --- | --- | --- |
| K | Press one key. Best typist 0.08, good 0.12, average skilled 0.20, average non-secretary 0.28, unfamiliar keyboard 1.20 | 0.28 (default in the script) |
| P | Point at a target with a mouse | 1.10 |
| B | Press or release a mouse button (a click is B twice) | 0.10 |
| H | Move the hand between keyboard and mouse | 0.40 |
| M | Mental step: decide, find, or remember | 1.35 |
| R | Wait for the system | as measured |

Where to put M: before each new decision, before each search for a target, and before typing a
value the user must think of. Not between keys of one word, and not before a step the user does
as a habit.

For touch screens and physical controls, the classic values do not fit exactly. Keep the counts of
taps, decisions, and screen changes. Measure real times in a test if the time matters.

## 7. Questionnaires for user tests

### Single Ease Question (SEQ), after each task

"Overall, how difficult or easy was the task to complete?" 1 = very difficult, 7 = very easy.
The average across many studies is about 5.5.

### System Usability Scale (SUS), after the whole test

Each answer from 1 (strongly disagree) to 5 (strongly agree).

1. I think that I would like to use this system frequently.
2. I found the system unnecessarily complex.
3. I thought the system was easy to use.
4. I think that I would need the support of a technical person to be able to use this system.
5. I found the various functions in this system were well integrated.
6. I thought there was too much inconsistency in this system.
7. I would imagine that most people would learn to use this system very quickly.
8. I found the system very cumbersome to use.
9. I felt very confident using the system.
10. I needed to learn a lot of things before I could get going with this system.

Scoring: for odd questions, take the answer minus 1. For even questions, take 5 minus the answer.
Add the ten numbers and multiply by 2.5. The result is 0 to 100. It is not a percentage. About 68
is average; above 80 is in the top group.

### Test plan in short

1. Five users of one user type for each round.
2. Three to five tasks, written as goals, not as instructions ("Make the machine run slower",
   not "Click Settings, then Speed").
3. Record: finished without help (yes or no), time, errors, SEQ, and what they said.
4. SUS at the end.
5. Report the problems with severity, and fix P0 and P1 before the next round.
