---
name: machine-hmi-design
description: >-
  Use when you design or review an operator screen or control panel for a machine (HMI, PLC touch panel, SCADA page): layout, state and alarm colours, alarm lists, start/stop, jog, setpoints, gloves and distance.
---
# Machine HMI Design

An operator screen is not a website. The operator stands, often wears gloves, looks from a metre
away, and must react to a fault in seconds. The screen is calm when all is normal, so a problem
stands out at once.

## Core rules

- **Grey is normal, colour is a problem.** Light grey base, dark text, running equipment in
  neutral tones. Strong colours only for abnormal states and alarms (ANSI/ISA-101.01).
- **Show the state, not only the value:** "182 °C, target 180, rising", not "182".
- **Show the confirmed state.** After "Start", show "Starting…" until the machine reports it runs.
- **Safety is in hardware.** The emergency stop is a red mushroom button on a yellow background,
  wired to the safety circuit (ISO 13850). The screen may show the stop state. It is never part
  of the safety function and never the only way to stop.
- **Every alarm needs an action.** No action needed means a message or log entry, not an alarm.
- **Same place on every screen:** machine name, mode (auto, manual, setup), state, active alarm
  count, user, time, and Home.

## Screen structure (ISA-101 levels)

| Level | Screen | Purpose |
| --- | --- | --- |
| 1 | Overview | Whole machine or line. Is all normal? |
| 2 | Area or unit | Start, stop, setpoints for one part |
| 3 | Detail | One module or device |
| 4 | Diagnostics | Fault finding and service; may need a password |

Navigation bar with about seven items at most. A main task is at most two taps from the overview.
If the machine uses PackML (ISA-TR88.00.02), use the same state names on the screen.

## Colour (IEC 60204-1, IEC 60073; check the current edition)

| Colour | Meaning |
| --- | --- |
| Red | Emergency or dangerous state. Act now |
| Yellow or amber | Abnormal state. A problem is coming |
| Blue | The operator must do something |
| Green | Normal or safe state |
| White, grey, black | No special meaning |

- Never use red or yellow for decoration, logos or normal equipment.
- Colour is never the only signal. Add a shape, a symbol and a word.
- Blink only for new, unacknowledged alarms. Stop on acknowledge.
- Light grey for bright workshops; dark can suit a dark control room. Test in the real light.

## Size, gloves, distance

- Capital letters at least about 6 mm high per metre of viewing distance (MIL-STD-1472).
- Touch targets at least about 10 mm bare hand, about 15 mm with gloves, more for thick gloves.
  Measure in millimetres on the real panel, not in pixels. Leave space between targets.
- No swipe, pinch or long press for main tasks.
- Units next to every value; the same decimals for the same value everywhere.

## Controls

- Moves, start and mode changes need a deliberate action: a dedicated button or select-then-confirm.
- The screen stop button is large and always in the same place. It adds to the hardware stop.
- Jog and manual moves are hold-to-run: they stop when released.
- Setpoints show unit and limits, refuse values outside them and say why, and show old and new
  values before saving.
- Show the active recipe on every screen. A recipe change during a run needs a confirmation that
  names the effect.

## Alarms (ISA-18.2, IEC 62682, EEMUA 191)

- List newest first: time, priority, plain description, action. "Coolant level low. Refill tank
  B.", not "ERR 2041".
- Three or four priorities at most. Most alarms are low priority.
- Guide: on average not more than about one alarm every ten minutes in normal running, no floods.
- Acknowledged and cleared alarms leave the active list but stay in the history.

## Language and roles

Plain words in the operator's language, for every market you sell to. Icons with a word under
them. Roles (operator, setter, maintenance, admin) see only the screens they need, but everyone
sees the machine state.

## Review checklist

- [ ] Grey base; strong colours only for abnormal states and alarms
- [ ] Colour meanings per IEC 60204-1 / IEC 60073; never colour alone
- [ ] State, mode, alarm count and user always in the same place
- [ ] Confirmed state shown, not only the command
- [ ] Main tasks within two taps of the overview
- [ ] Text and targets sized for the real distance and gloves
- [ ] Hold-to-run jog; confirmations; setpoint limits
- [ ] Every alarm has a plain text and an action; low alarm rate
- [ ] Emergency stop is hardware
- [ ] Tested on the real panel, with gloves, in the real light, with a real operator if possible

Score the result with `design-quality`.
