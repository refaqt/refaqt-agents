---
name: machine-hmi-design
description: >-
  Design operator screens and control panels for machines and production
  lines (human-machine interface, HMI): touch panels, PLC screens, SCADA
  pages, and machine web interfaces. Use when you lay out an operator screen,
  choose colours for states and alarms, design alarm lists, start/stop and
  mode controls, recipe or setpoint screens, or check that an operator can
  run the machine safely and quickly with gloves, in noise, and at a
  distance. PLC means programmable logic controller; SCADA means a
  supervisory control and data system. Uses ux-design and gui-design as a base and adds industrial rules.
---
# Machine HMI Design

An operator screen is not a website. The operator stands, often wears gloves, looks from a metre
away, is busy with the machine, and must react to a problem in seconds. A good machine screen is
calm when all is normal, so that a problem stands out at once.

## Scope

**Owns:**
- Layout and navigation of operator screens
- Colour rules for normal, abnormal, and alarm states
- Alarm presentation on the screen
- Controls for mode, start, stop, jog, and setpoints on the screen
- Size of text and touch targets for distance and gloves
- Physical buttons and lights next to the screen, together with `industrial-design`

**Does NOT own:**
- Programmable logic controller (PLC) logic, the machine state model, and alarm logic in code → `industrial-automation`
- Safety functions (emergency stop, guards, safe torque off) → `industrial-automation`,
  `product-compliance`. A touch screen is never the only way to stop a machine safely.
- General flows and words → `ux-design`. General visual design → `gui-design`
- Scoring the result → `design-quality`

## Core principles

- **Grey is normal, colour is a problem.** Use a calm, light grey base and dark text. Show equipment
  that runs normally in neutral tones. Keep strong colours for abnormal states and alarms only. Then
  one red item is seen at once. (This follows ANSI/ISA-101.01 and "The High Performance HMI
  Handbook".)
- **Show the state, not only the value.** Next to a number, show whether it is normal, the target,
  and the trend. "Temperature 182 °C, target 180, rising" helps more than "182".
- **Command and real state are different.** After "Start", show "Starting…" until the machine
  reports that it runs. Never show a state that the machine did not confirm.
- **Safety is in hardware.** The emergency stop is a red mushroom button on a yellow background,
  wired to the safety circuit. The screen may show the stop state but never replaces the button.
- **Every alarm needs an action.** If the operator does not need to do anything, it is not an
  alarm. Make it a message or a log entry.
- **Same place, every screen.** Machine state, mode, active alarm, user, and the home button are in
  the same place on every screen.
- **Design for the worst moment.** Test the screen during a fault, with gloves, in bright light,
  from the normal standing position.

## Key rules

### Screen structure

Use a small hierarchy of screens (ISA-101 uses four levels):

| Level | Screen | Purpose |
| --- | --- | --- |
| 1 | Overview | The whole machine or line on one screen. Is everything normal? |
| 2 | Area or unit | Run one part of the machine: start, stop, setpoints |
| 3 | Detail | One module or device, for adjustment |
| 4 | Diagnostics | Fault finding and service. May be password protected |

- A fixed top bar on every screen: machine name, mode (auto, manual, setup), state (running,
  stopped, fault), active alarm count, logged-in user, and time.
- A fixed navigation bar with at most about seven items. Home (the overview) is always one tap away.
- A main task is at most two taps from the overview.

### Colour

Use colour for meaning only. The common meanings for indicator lights and screen states follow
IEC 60204-1 and IEC 60073. Check the current edition for your product.

| Colour | Meaning |
| --- | --- |
| Red | Emergency or dangerous state. Act now |
| Yellow or amber | Abnormal state. A problem is coming |
| Blue | The operator must do something (a mandatory action) |
| Green | Normal or safe state |
| White, grey, black | No special meaning |

- Never use red or yellow for decoration, logos, or normal equipment.
- Colour is never the only signal. Add a shape, a symbol, and a word (for example a red triangle
  with "High pressure").
- Blinking only for new, not yet acknowledged alarms. It stops when the operator acknowledges.
- A light grey background works best in bright workshops. A dark theme can suit a dark control
  room. Choose from the real light, and test there.

### Text, targets, and distance

- Text must be readable from the normal operating position. A practical rule: capital letters at
  least about 6 mm high for each metre of viewing distance (about 20 to 22 minutes of arc, from
  MIL-STD-1472). Measure on the real panel.
- Touch targets with bare hands at least about 10 mm. Measure in millimetres on the real panel: how
  many pixels that is depends on the pixel density of the screen. With gloves
  at least about 15 mm, and larger for thick gloves. Leave space between targets. Test with the real
  gloves.
- Avoid gestures (swipe, pinch, long press) for main tasks. Many industrial touch screens and
  gloves handle them badly.
- Show units next to every value. Use the same number of decimals everywhere for the same value.

### Controls

- Start, stop, and mode changes that move the machine need a clear, deliberate action: a
  dedicated button, or "select, then confirm". Show what will happen before it happens.
- The stop button on the screen is large and always in the same place. It is an extra to the
  hardware stop, not a replacement.
- Jog and manual moves work only while the button is held (hold-to-run), and stop when released.
- Setpoints show the limits and the unit. The screen refuses values outside the limits and says
  why. Show the old and new value before saving.
- Recipes: show the active recipe name on every screen. Changing a recipe during a run needs a
  confirmation that names the effect.

### Alarms

- Alarm list: newest first, with time, priority, a short plain description, and the action to take.
- Three or four priorities at most. Most alarms are low priority. Only a few are high.
- A healthy machine raises few alarms. As a guide from alarm management practice (ISA-18.2,
  IEC 62682, EEMUA 191): on average not more than about one alarm every ten minutes in normal
  running, and no alarm floods.
- An alarm text says what is wrong and what to do: "Coolant level low. Refill tank B." Not
  "ERR 2041".
- Acknowledged and cleared alarms leave the active list but stay in the history.

### Language and users

- Plain words in the operator's language. Offer the languages of the markets you sell to.
- Icons always with a word under them, at least on the main screens.
- Roles (operator, setter, maintenance, admin) see only the screens they need. Do not hide the
  machine state from anyone.

## Key workflows

### Design an operator screen

1. List the operator tasks and the operating situations: start of shift, normal running, product
   change, fault, cleaning, maintenance (`ux-design`).
2. Agree the machine states and modes with `industrial-automation`. If the machine uses the
   PackML state model (ISA-TR88.00.02), use the same state names on the screen.
3. Draw the level 1 overview first. Ask: can the operator see in five seconds whether all is
   normal?
4. Draw the top bar and the navigation, then the level 2 screens for the main tasks.
5. Set the colours, sizes, and targets from the rules above in a small token table.
6. Count taps for the main tasks and for "react to the most common fault" (`design-quality`
   flow cost).
7. Review on the real panel, at the real distance, with gloves, in the real light. Score with
   `design-quality`.

### HMI review checklist

- [ ] Grey base. Strong colours only for abnormal states and alarms
- [ ] Colour meanings match IEC 60204-1 and IEC 60073, and colour is never the only signal
- [ ] Machine state, mode, alarm count, and user always visible in the same place
- [ ] Shows the confirmed machine state, not only the command
- [ ] Main tasks within two taps of the overview
- [ ] Text readable from the operating position; targets large enough for the gloves used
- [ ] Hold-to-run for jog; confirmation for moves and recipe changes; limits on setpoints
- [ ] Every alarm has a plain text and an action; alarm rate is low in normal running
- [ ] The emergency stop is hardware; the screen is not part of the safety function
- [ ] Tested on the real panel with a real operator, if possible

## Terminology and standards

- ANSI/ISA-101.01: human-machine interfaces for process automation systems (high-performance HMI).
- ANSI/ISA-18.2 and IEC 62682: management of alarm systems. EEMUA 191: alarm system guide.
- IEC 60204-1: electrical equipment of machines. Colours of push buttons and indicator lights.
- IEC 60073: coding of indicators and actuators by colour, shape, and position.
- ISO 13850: emergency stop function.
- IEC 61310 (series): marking and signals on machines (visual, sound, touch).
- ISO 11064 (series): ergonomic design of control centres.
- ISA-TR88.00.02 (PackML): standard machine states and modes.
- Bill Hollifield and others, "The High Performance HMI Handbook".

## Cross-links

| Need | Skill |
| --- | --- |
| PLC logic, states, alarm logic | `industrial-automation` |
| Safety functions and CE marking | `product-compliance` |
| Physical buttons, panel layout, ergonomics | `industrial-design` |
| General flows and words | `ux-design` |
| General visual design | `gui-design` |
| Web-based HMI code | `web-app-design` |
| Score the result | `design-quality` |
