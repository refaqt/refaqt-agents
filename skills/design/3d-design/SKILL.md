---
name: 3d-design
description: >-
  Make 3D product models look good and stay usable: form quality in the CAD
  model, standard review views, renders for documentation and sales,
  exploded views and assembly pictures, and 3D viewers in web apps. Use when
  you shape or restyle a part or assembly in CAD (FreeCAD or other), when a
  model "looks wrong" or unfinished, when you need product renders or
  assembly images, or when you put a 3D model in a web page. Works with
  industrial-design for ergonomics and CMF, and with freecad for modelling.
---
# 3D Design

A 3D model is how most people first see our machines: in a pull request, a manual, a website, or a
sales deck. It should look planned and calm, and it should show clearly how the product is used.
This skill covers the visual quality of the model and how to show it.

## Scope

**Owns:**
- Visual form quality of parts and assemblies in CAD: radii, edges, alignment, proportions
- Appearance in the model: colours and materials that match the CMF sheet
- Standard views and screenshots for design review
- Renders for documents, websites, and sales
- Exploded views and pictures for assembly and service instructions
- 3D viewers in web apps

**Does NOT own:**
- Ergonomics, controls placement, and the CMF choices themselves → `industrial-design`
- Parametric modelling, constraints, and FreeCAD problems → `freecad`
- Strength, tolerances, and manufacturing detail → `mechanical-engineering`
- Technical drawings with dimensions → `mechanical-engineering` (TechDraw help in `freecad`)
- Scoring the result → `design-quality`

## Core principles

- **Judge the model from the user's eye.** Look at it from the height and distance where people
  will stand, not only from the default isometric view.
- **Few, consistent form rules.** One small set of fillet radii, one rule for chamfer or fillet,
  one wall thickness family. Inconsistent edges are the first sign of an unfinished model.
- **Line things up.** Edges, joints, holes, and panel gaps line up across parts. Near misses (two
  lines 1 mm apart) look like errors. Make them meet, or move them clearly apart.
- **Show the use.** Touch points in the accent colour, the front clearly the front, the work area
  visible. A viewer should understand where to stand and what to touch.
- **Honest renders.** A render shows the real product: real colours, real materials, real
  proportions, no parts that do not exist. Mark concept images as concepts.
- **Form rules live in parameters.** Radii, gaps, and wall thicknesses are named parameters with a
  reason, like every other dimension (`freecad`, `mechanical-engineering`).

## Gates and measures

| Gate | Pass when |
| --- | --- |
| Appearance matches CMF | Every visible part has the colour and material of the CMF sheet (`industrial-design`) |
| Radii set | All visible fillets come from the agreed set of radii |
| Alignment | No near-miss edges or joints visible in the standard views |
| Touch points | Every operator touch point is in the accent colour, and nothing else is |
| No artefacts | No visible gaps between parts that should touch, no parts through each other, no missing parts |

Measures to compare options and versions:

- Number of distinct radii, colours, and materials visible from outside.
- Number of distinct edge and joint lines on the main faces (fewer is calmer).
- Silhouette readability: can a person name the product and its front from the black silhouette?

## Key workflows

### 1. Standard review views

Make the same set of images for every design review, so versions can be compared side by side:

1. Front, side, top, and isometric, with the same camera, background, and lighting each time.
2. A view from the operator's eye height at the operating position.
3. A black silhouette on white (all parts black) from the front and from the isometric view.
4. Close-ups of the operator area and of the service access.

In the FreeCAD graphical interface, use View, Standard views, then File, Export, or "Save picture".
From the FreeCAD Python console (the graphical interface must be running):

```python
v = Gui.ActiveDocument.ActiveView
for name, set_view in [("front", v.viewFront), ("right", v.viewRight), ("top", v.viewTop), ("iso", v.viewIsometric)]:
    set_view()
    v.fitAll()
    v.saveImage(f"review/{name}.png", 1920, 1080, "White")
```

Put the images in the pull request, next to the images of the previous version.

### 2. Form review

Use the visual quality rubric in `design-quality` on the standard views, with these questions:

- **Hierarchy:** What does the eye see first? It should be the face of the machine and its main
  controls, not a cable, a bracket, or a sticker.
- **Alignment:** Do edges, gaps, and panel joints continue across parts?
- **Consistency:** Same radius rule, same fasteners, same handle design everywhere?
- **Proportion and weight:** Does the product look stable? Heavy parts low, a clear base.
- **Clutter:** Remove or hide every visible element that the user does not need.
- **Fit with the subject:** Does it look like a serious tool for its users, in the family of our
  other products?

Give the images and the rubric to a separate reviewer (`design-quality`). Compare options in pairs
when the look is the question.

### 3. Renders

- **Model:** export the assembly as glTF (keeps colours and is light) or STEP. Blender (free and open
  source) with the Cycles renderer gives good results. Check that colours and materials came across.
- **Materials:** use physically based materials (base colour, metal or not, roughness). Painted
  steel and plastic are not metal. Brushed and bead-blasted metal have a higher roughness than
  polished metal. Take colours from the CMF sheet.
- **Light:** a soft studio setup. A large key light from the front and side, a fill light on the
  other side, and a rim light from behind to separate the product from the background. Or a neutral
  studio 360° light image (HDRI) as the light source. Avoid hard black shadows and burned-out highlights.
- **Camera:** a normal to long lens, about 50 to 100 mm in 35 mm film terms, so the product is not
  distorted. Camera at the eye height of a user for large machines. Keep vertical lines vertical.
- **Ground:** a soft contact shadow under the product so it stands on the floor, not in the air.
- **Background:** plain and neutral for documents; a real or simple setting for "in use" images,
  with a person for scale when size matters.
- **Output:** at least 2x the display size. Use the same camera and light set for every product in
  a family.

### 4. Exploded views and instructions

- One step, one action. Show only the parts of that step in colour; the rest in light grey.
- The same view direction for all steps, unless the work moves to another side.
- Move the parts along their assembly direction, with thin lines that show the path.
- Number the parts and use the same numbers as the bill of materials.
- Show the tool and the hand position when it is not obvious. Use as few words as possible.

### 5. 3D in a web app

- Use glTF or GLB, compressed (for example Draco or meshopt), and reduce the polygon count for the
  web. Aim for a file of a few megabytes, and show a still image while it loads.
- Start from a good, fixed view (the "hero" view), not from a random angle.
- Limit the orbit: no view from below the floor, no zoom into the inside unless that is the point.
- Add a "reset view" button, and buttons for the main views. Keyboard users need them, and
  everybody gets lost when orbiting.
- Respect "reduce motion": no automatic rotation for those users.
- Provide a text description and a still image for screen readers and for users without WebGL.
- The `<model-viewer>` web component (open source, from Google) gives many of these defaults.
  three.js gives full control.
- Check the page with `web-app-design` and the measuring script in `design-quality`.

## 3D design checklist

- [ ] Standard review views made with the same camera and light as the previous version
- [ ] Appearance matches the CMF sheet; touch points in the accent colour only
- [ ] Radii from the agreed set; no near-miss edges; joints line up across parts
- [ ] Silhouette readable; front and use are clear from the operator's eye height
- [ ] No gaps, overlaps, or missing parts in the views
- [ ] Renders honest, lit softly, not distorted, with a contact shadow
- [ ] Exploded views: one action per step, part numbers match the bill of materials
- [ ] Web viewer: fixed start view, limits, reset button, still image, small file
- [ ] Scored with `design-quality` by a separate reviewer

## Terminology and standards

- glTF 2.0 (Khronos Group): open file format for 3D scenes with materials, good for web and
  renders.
- Physically based rendering (PBR): materials described by colour, metalness, and roughness.
- ISO 128 and ISO 5456: rules for technical drawings and projections, for views on drawings.

## Cross-links

| Need | Skill |
| --- | --- |
| Ergonomics, controls, CMF choices | `industrial-design` |
| FreeCAD modelling and problems | `freecad` |
| Structure, tolerances, drawings | `mechanical-engineering` |
| 3D viewer page code | `web-app-design` |
| Score and compare designs | `design-quality` |
| Renders for marketing | `marketing` |
