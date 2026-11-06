---
name: industrial-design
description: >-
  Industrial design of physical products and machines: how they look, how
  people use, carry, operate, clean, and service them, and which colours,
  materials, and finishes (CMF) they get. Use when you shape the outside of a
  machine, enclosure, or product, place handles, buttons, displays, and
  access doors, check ergonomics (reach, height, force, posture), choose
  colours and finishes, or plan a product family look. Works with
  mechanical-engineering for the build and with 3d-design for the CAD model
  and renders.
---
# Industrial Design

Industrial design makes a physical product easy to understand, safe and comfortable to use, and
good to look at, and it makes sure all of this can be built. A user should see how to use the
product without a manual: where to hold it, where to press, where to open it, and what state it is
in.

## Scope

**Owns:**
- Product form, proportions, and the visual language of a product family
- Ergonomics: body sizes, reach, working height, posture, forces, and handling
- Placement and design of physical controls, displays, handles, and access points
- Colour, material, and finish (CMF), including the colour of touch points
- Labels, symbols, and markings on the product, together with `product-compliance`
- The experience of unpacking, setting up, cleaning, and servicing the product

**Does NOT own:**
- Structure, tolerances, and detailed design for manufacture → `mechanical-engineering`
- The CAD model quality and renders → `3d-design`, `freecad`
- Operator screens → `machine-hmi-design`
- Safety functions, risk assessment, and CE marking → `product-compliance`
- Production processes and cost → `production-engineering`, `purchasing`

## Core principles

- **The form explains the use.** A handle looks like a handle. The part you press looks pressable.
  The front of the machine is clearly the front. Don Norman calls these signs "signifiers".
- **Fit the body range, not one person.** Design for small and large users. A common target is the
  5th percentile woman to the 95th percentile man of the user population. Use reach for the small
  user and clearance for the large one.
- **Controls map to what they do.** A control is placed near and in the same layout as what it
  controls. Up, right, and clockwise mean more or on. Same function, same control, everywhere on the
  product.
- **One colour for "touch here".** Give every part that the operator is meant to touch (handles,
  latches, adjusters) one accent colour. Everything else stays neutral. Users learn it in seconds.
- **Less, but better.** Every visible line, joint, colour, and screw is either needed or removed.
  Few radii, few materials, few colours, and few fastener types.
- **Service is part of the experience.** Parts that wear or need cleaning are easy to reach, without
  tools where safety allows, and clearly marked.
- **Make it buildable.** Every form choice must work with the chosen process and cost. Check with
  `mechanical-engineering` and `production-engineering` early.

## Gates and measures

These are the industrial-design gates for `design-quality`. A failed gate blocks "done".

| Gate | Pass when |
| --- | --- |
| Reach | Every frequent control is within easy reach of a small user (5th percentile) from the normal position, without bending or stretching |
| Clearance | A large user (95th percentile) fits: knees, feet, head, hands with gloves |
| Working height | Fits the task: precise work above elbow height, light work slightly below, heavy work lower. Adjustable when users differ a lot |
| Force | Forces to operate, open, and lift stay within EN 1005-3 limits (or ISO 11228 for lifting). Hand-carried parts with handles or lifting points when heavy |
| Visibility | The operator can see the work area and the main display from the normal position |
| Controls | Direction of movement matches the effect, functions are grouped, and critical controls are protected from being pressed by accident |
| Emergency stop | Reachable from every operating position, red on yellow, not hidden (ISO 13850, with `product-compliance`) |
| Safety signs | Use ISO 7010 symbols and ISO 3864 colours, placed where the hazard is seen |
| Danger zones | Openings and distances prevent reaching danger zones (ISO 13857, with `product-compliance`) |

Measures to compare options and versions:

- Number of distinct radii, materials, colours, and fastener types visible from outside. Fewer is
  calmer.
- Number of tools needed for daily, weekly, and yearly service. Time to change a wear part.
- Number of operator touch points and steps for the main tasks (start of shift, product change,
  cleaning).
- Gap and flush between panels: same gap width all around, within the stated tolerance.

## Key workflows

### 1. Brief

1. Users (population, size range, skills, gloves or protective equipment), tasks, and the place of
   use (light, dirt, noise, cleaning method, space).
2. Main tasks with the human body: load, unload, adjust, monitor, clean, service, move the machine.
3. The brand and family look, if there is one. Look at two or three good products in the same
   field and write what makes them good.

### 2. Ergonomics first

1. Get body size data for the user population: ISO 7250-1 defines the measures. DIN 33402-2 and
   other national tables give values. EN ISO 14738 gives workstation sizes at machines.
2. Draw the user in the CAD model: a small and a large manikin, or simple boxes with the key
   sizes (eye height, elbow height, reach). Check the gates above.
3. Place the controls and displays by importance and frequency (EN 894-4): most used and most
   critical in the best zone, in front of the user, between elbow and shoulder height.
4. Build a cheap full-size mock-up (cardboard, foam, or 3D print) for the operator area and test
   with a small and a large person. A mock-up finds problems that no screen shows.

### 3. Form and visual language

- Start from the layout of the parts inside, then wrap them. Do not design a shell and force the
  parts in.
- Give the product a clear front, a clear "face", and a calm overall shape. Keep the visual weight
  low and stable.
- Use simple proportions and line up edges, joints, and features across parts. A joint line that
  continues across two panels looks planned. Lines that almost meet look like a mistake.
- Choose a small set of radii (for example 2, 5, and 20 mm) and a rule for when to use each.
- Hide what the user does not need: cables, screws, rough edges. Where screws must show, use one
  type, in a neat pattern.
- Keep a product family consistent: the same colours, the same handle, the same label style, and
  the same placement of the main controls.

### 4. Colour, material, and finish (CMF)

- A neutral base colour for the body. One accent colour for touch points. Safety colours only for
  safety meaning (red, yellow, blue, green per ISO 3864 and IEC 60204-1).
- Name colours by a standard (for example RAL or Pantone) so suppliers can match them.
- Choose finishes for the place of use: matte or textured surfaces hide fingerprints and scratches;
  smooth, closed surfaces are easier to clean. Food and hygiene machines follow hygienic design rules
  (EN 1672-2, and the guidelines of the European Hygienic Engineering and Design Group, EHEDG).
- Name surface textures by a standard (for example VDI 3400 for moulded parts).
- Make a CMF sheet: one row per visible part, with material, colour code, finish, and supplier.

### 5. Labels and markings

- Use symbols with words, in the user's language. Use ISO 7010 for safety signs and IEC 60417 or
  ISO 7000 for symbols on equipment.
- Put the label next to the thing it labels, readable from the user's position.
- Use one label style (font, size, colour) for the whole product family.

### 6. Review

1. Render the product in standard views and in use (`3d-design`).
2. Check the gates with the manikins and with the mock-up.
3. Score the design with `design-quality`: give the reviewer the renders, the user and tasks, and
   the gates. Use the visual quality rubric for the form (hierarchy, alignment, consistency, fit
   with the subject, finish of details).
4. Compare options in pairs when the look is the question.

## Industrial design checklist

- [ ] Users, size range, tasks, and place of use written down
- [ ] Reach, clearance, height, force, and visibility gates pass for small and large users
- [ ] Controls grouped, mapped, and protected; emergency stop reachable from every position
- [ ] One accent colour for all touch points; safety colours only for safety
- [ ] Few radii, materials, colours, and fastener types; joints and edges line up
- [ ] Service parts reachable and marked; tools for service listed
- [ ] CMF sheet with standard colour and finish codes
- [ ] Labels and safety signs to ISO 7010, placed where needed
- [ ] Full-size mock-up tested, or a reason why not
- [ ] Scored with `design-quality`

## Terminology and standards

- ISO 6385 and EN 614-1: ergonomic principles in the design of work systems and machines.
- ISO 7250-1: basic human body measurements. EN ISO 14738: workstation sizes at machines.
- EN 894-1 to -4: displays and control actuators (general, displays, controls, placement).
- IEC 60447: principles for actuating controls (direction of movement).
- EN 1005-3 and -4: force limits and working postures at machines. ISO 11228-1: manual lifting.
- ISO 13857: safety distances to prevent reaching danger zones.
- ISO 3864 and ISO 7010: safety colours, signs, and registered safety symbols.
- ISO 7000 and IEC 60417: graphical symbols for equipment.
- Dieter Rams, "Ten principles for good design": innovative, useful, aesthetic, understandable,
  unobtrusive, honest, long-lasting, thorough, environmentally friendly, as little design as
  possible.

## Cross-links

| Need | Skill |
| --- | --- |
| Structure, tolerances, design for manufacture | `mechanical-engineering` |
| CAD model quality and renders | `3d-design`, `freecad` |
| Operator screens | `machine-hmi-design` |
| Electrical panels and buttons wiring | `electrical-engineering` |
| Safety and CE marking | `product-compliance` |
| Processes and cost | `production-engineering`, `purchasing` |
| Score and compare designs | `design-quality` |
