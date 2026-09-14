---
name: optical-engineering
description: >-
  Optics, illumination, imaging, and photonics for measurement or process
  machines. Use for lens selection, alignment, optical parts list (BOM), and
  image-chain design. Do not use this skill as the main owner of general
  software user interface or mechanical structure.
---
# Optical Engineering

Use this skill when the light path, image quality, or photonic measurement sets system performance.

## Scope

**Owns:**
- Optical architecture (objective, tube, sensor, illumination)
- Lens and sensor specification (field of view (FOV), numerical aperture (NA), modulation transfer function (MTF) targets, distortion)
- Illumination design (LED wavelength, uniformity, short light pulses (strobing))
- Optomechanical interface requirements (with `mechanical-engineering`)
- Alignment procedures and tolerance budgets (optical + mechanical)
- Optical BOM and vendor selection
- Calibration targets and test imagery acceptance criteria

**Does NOT own:**
- Image processing algorithms as the main owner → `software-development` (joint work)
- Printed circuit board (PCB) for camera interfaces → `electrical-engineering`
- Laser product safety classification paperwork → `product-compliance`
- General machine safety → `product-compliance`, `systems-engineering`

## Core principles

- **Tolerance stacks are optical:** Small mechanical errors dominate image quality. Design mounts together with `mechanical-engineering`.
- **Environment matters:** Dust, vibration, and temperature drift affect results. Record operating windows.
- **Open hardware:** Publish optical stack diagrams, part lists, and alignment steps when you are not making regulated medical claims.
- **Metrology traceability:** Measurement systems need calibration records so customers can trust the results.
- **Avoid over-specifying:** Expensive optics rarely fix bad mechanics or color-filter errors in software (demosaic artifacts).

## Key workflows

### Optical design review

- [ ] Object size and working distance defined
- [ ] Resolution and contrast targets at the Nyquist limit of the sensor
- [ ] Illumination angle avoids bright mirror reflections that hide detail (specular blowout)
- [ ] Corner darkening (vignetting) and distortion acceptable for algorithm
- [ ] Cover glass/window included in model
- [ ] Safety for lasers/UV → `product-compliance`

### Alignment procedure (template)

1. Mechanical coarse alignment references
2. Centering and focus iteration with metric (MTF, sharpness score)
3. Illumination uniformity check
4. Record shim (spacer) values and torque specs
5. Validation images archived with revision ID

### Vendor and BOM

- Prefer commercial off-the-shelf (COTS) lenses with documented computer-aided design (CAD). Use custom glass only with a lead-time flag → `supply-chain-management`

## Terminology and standards

- F-number (F/#), NA, MTF, root-mean-square (RMS) spot size, chief ray angle
- International Organization for Standardization (ISO) 10993 (only if a body-contact safety path (biocompatibility) applies — rare; send this to experts)
- International Electrotechnical Commission (IEC) 60825 laser safety (design input; classification → `product-compliance`)

## Cross-links

| Need | Skill |
| --- | --- |
| Motion stages | `mechatronic-engineering` |
| Vision pipeline | `software-development` |
| Enclosures | `mechanical-engineering` |
| System requirements | `systems-engineering` |
| Production optical quality control (QC) | `production-engineering` |

## Practical constraints

- Dust-clean assembly may need a clean-bench standard operating procedure (SOP) from `production-engineering`.
- Open publication of optical recipes may affect competitive position. Align with `business-development`.
- Sensor supply limits often block the whole subsystem. Involve `purchasing` early.
