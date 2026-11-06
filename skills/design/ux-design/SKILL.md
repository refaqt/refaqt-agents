---
name: ux-design
description: >-
  User experience design for any software: who the users are, what they need
  to do, and the shortest, clearest path to do it. Use when you plan a new
  app, screen, feature, or flow, when users get lost or a task takes too many
  steps, when you design navigation, forms, onboarding, errors, or the words
  in an interface. Works for web, desktop, mobile, and machine screens. For
  the look of the screens use gui-design; to judge the result use
  design-quality.
---
# UX Design

User experience (UX) design decides what the user sees, in which order, and what happens when
they act. Good UX makes the main tasks short, makes the next step obvious, and makes mistakes hard
to make and easy to undo.

## Scope

**Owns:**
- Users, their tasks, and the context of use
- Structure of the product: screens, navigation, and names of things (information architecture)
- Flows: the steps for each task, including errors, empty states, and first use
- Interaction rules: feedback, undo, confirmation, defaults, shortcuts
- Interface words: labels, buttons, messages, help text
- Wireframes: simple layouts without visual styling

**Does NOT own:**
- Colour, type, spacing, components, and visual polish → `gui-design`
- Browser-specific rules and accessibility code → `web-app-design`
- Operator screens on machines → `machine-hmi-design` (it uses this skill as a base)
- Measuring and judging the result → `design-quality`
- Product requirements and their trace → `systems-engineering`

## Core principles

- **Start from tasks, not from features.** A feature list gives a menu of buttons. A task list
  ("set up a new job in under a minute") gives a flow.
- **The main task is the shortest path.** The most frequent task gets the fewest steps, the
  biggest target, and the first place on the screen. Rare tasks may take longer.
- **One screen, one main job, one main action.** If you cannot name the one main action of a
  screen, the screen does too much.
- **Show, do not make them remember.** Keep the information needed for a decision on the same
  screen as the decision.
- **Good defaults remove steps.** Pre-fill what you know. Remember the last choice. Most users
  never change a default.
- **Prevent errors, then make them cheap.** Limit input to valid values. Prefer undo over "Are
  you sure?". Confirm only actions that cannot be undone.
- **Always answer the user.** Every action gets visible feedback within 0.1 s. Anything slower
  than 1 s shows a busy sign. Anything slower than 10 s shows a progress bar with the time left and
  lets the user do something else.
- **Follow conventions.** Users spend most of their time in other products. Use the patterns they
  already know, unless yours is clearly better and you tested it.
- **Design every state.** Empty, loading, partial, full, error, no permission, offline. The empty
  state is the first thing a new user sees.

## Key workflows

### 1. Understand the users and tasks

1. Name two or three user types. For each: their goal, their skill level, how often they use the
   product, and where (desk, phone on the move, machine floor with gloves, bright or dark room).
2. List the tasks. Mark each as frequent, occasional, or rare, and as critical or not. The
   frequent and critical tasks are the main tasks.
3. Write each main task as a short story: "As an operator, I want to change the speed while the
   machine runs, so that I can fix the finish without stopping the job."
4. Set a budget for each main task in steps and seconds (see `design-quality`).
5. If you do not know who the users are, ask. Do not invent them. If you must assume, write the
   assumption down so the user can correct it.

### 2. Structure and navigation

1. Group the content and actions as the user thinks about them, not as the code is built. A card
   sort (users group cards with names) is the cheapest test for this.
2. Keep the top level small: about five to seven main sections. Name them with plain nouns.
3. Always show where the user is (active tab, title, breadcrumbs) and how to go back.
4. Keep the depth low. A main task should not need more than two levels of menu.
5. Use the same name for the same thing everywhere: in the menu, the title, the button, and the
   message.

### 3. Design each flow

1. Write the happy path as a numbered list of steps. Count screens, actions, and decisions.
2. Cut steps: remove, combine, pre-fill, or move to later. Ask for each step: "What breaks if we
   drop this?"
3. Add the other paths: errors, empty data, cancel, back, timeout, no network, no permission.
4. Draw a wireframe for each screen: a box layout with real words, no colour. ASCII is fine for a
   first draft.
5. Run the flow cost (`design-quality`) on the main tasks. Compare with the budget and with the old
   version.
6. Walk through each flow as a first-time user: at each step, will the user know what to do, see
   how to do it, and understand the result? (This is a cognitive walkthrough.)

### 4. Forms and input

- Ask only for what you need now. Every field costs time and some users give up.
- One column. Label above the field. Mark the optional fields, not the required ones, when most
  are required.
- Use the right control: a choice of 2 to 5 options is radio buttons, more is a list with search.
  Numbers with a unit show the unit. Dates use a date picker, plus typing.
- Check the input while the user types or when they leave the field, not only at the end. Put the
  error message next to the field. Keep what the user typed.
- The submit button says what it does: "Create job", not "Submit".

### 5. Words in the interface

- Name things by what the user knows, not by how the system works. "Notifications", not "webhook
  config".
- Buttons are verbs that say what happens: "Save changes", "Start job". The message after says
  the same word: "Job started".
- Error messages say what happened, why if useful, and what to do now. They do not blame the user
  and are never vague ("Something went wrong").
- Empty states say what goes here and give the action to add the first one.
- Use sentence case, short sentences, and the same word for the same thing. Write in plain
  English that a non-native speaker understands. If the product is translated, leave about 30 %
  extra room for longer words.

### 6. First use and help

- Let users do the real task first, and teach on the way. Avoid long tours before the first
  action.
- Use examples and sample data so the first screen is not empty.
- Put help where the question comes up: a short hint next to the field, a link to the exact page.

## UX review checklist

- [ ] Users, tasks, and context of use written down
- [ ] Each main task has a budget, and the design is inside it
- [ ] Each screen has one main job and one clear main action
- [ ] Navigation shows where the user is and how to go back
- [ ] Every state designed: empty, loading, error, full, offline, no permission
- [ ] Destructive actions can be undone, or are confirmed with the consequence named
- [ ] Every action gives feedback, and slow actions show progress
- [ ] Labels and messages in the user's words, same word for the same thing
- [ ] Keyboard use and screen readers considered from the start (`web-app-design`)
- [ ] Scored with `design-quality` by a separate reviewer

## Terminology and standards

- ISO 9241-210: human-centred design process (understand context, specify needs, design,
  evaluate, repeat).
- ISO 9241-110:2020: seven interaction principles. Fit with the task, self-descriptive, matches
  expectations, easy to learn, user in control, robust against use errors, engaging.
- Laws of UX (lawsofux.com): short summaries of Fitts, Hick, Jakob, Miller, Tesler, the
  peak-end rule, and others.
- Don Norman, "The Design of Everyday Things": signifiers (signs that show what to do), mapping
  (controls placed like what they control), feedback, constraints, and conceptual models.

## Cross-links

| Need | Skill |
| --- | --- |
| Visual design of the screens | `gui-design` |
| Build it for the browser | `web-app-design` |
| Operator screens on a machine | `machine-hmi-design` |
| Measure and score the result | `design-quality` |
| Requirements from the system | `systems-engineering` |
| Code and tests | `software-development` |

## Sources and credits

- Nielsen Norman Group articles on heuristics, response times, forms, and error messages
  (https://www.nngroup.com/articles/).
- The guidance on interface words is adapted in part from the frontend-design skill by Anthropic
  (https://github.com/anthropics/skills, Apache License 2.0).
