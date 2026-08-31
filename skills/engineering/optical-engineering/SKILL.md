---
name: optical-engineering
description: >-
  Optics, illumination, imaging, and photonics for measurement or process
  machines. Use for lens selection, alignment, optical BOM, and image chain
  design — not general software UI or mechanical structure primary ownership.
---
# Optical Engineering

Use this skill when light path, image quality, or photonic measurement defines system performance.

## Scope

**Owns:**
- Optical architecture (objective, tube, sensor, illumination)
- Lens and sensor specification (FOV, NA, MTF targets, distortion)
- Illumination design (LED wavelength, uniformity, strobing)
- Optomechanical interface requirements (with `mechanical-engineering`)
- Alignment procedures and tolerance budgets (optical + mechanical)
- Optical BOM and vendor selection
- Calibration targets and test imagery acceptance criteria

**Does NOT own:**
- Image processing algorithms primary ownership → `software-development` (joint work)
- PCB for camera interfaces → `electrical-engineering`
- Laser product safety classification paperwork → `product-compliance`
- General machine safety → `product-compliance`, `systems-engineering`

## Core principles

- **Tolerance stacks are optical:** Small mechanical errors dominate image quality; co-design mounts with `mechanical-engineering`.
- **Environment matters:** Dust, vibration, temperature drift — document operating windows.
- **Open hardware:** Publish optical stack diagrams, part lists, and alignment steps when not exposing regulated medical claims.
- **Metrology traceability:** Measurement systems need calibration records for customer trust.
- **Avoid overspec:** Expensive optics rarely fix bad mechanics or software demosaic artifacts.

## Key workflows

### Optical design review

- [ ] Object size and working distance defined
- [ ] Resolution and contrast targets at Nyquist on sensor
- [ ] Illumination angle avoids specular blowout
- [ ] Vignetting and distortion acceptable for algorithm
- [ ] Cover glass/window included in model
- [ ] Safety for lasers/UV → `product-compliance`

### Alignment procedure (template)

1. Mechanical coarse alignment references
2. Centering and focus iteration with metric (MTF, sharpness score)
3. Illumination uniformity check
4. Record shim values and torque specs
5. Validation images archived with revision ID

### Vendor and BOM

- Prefer COTS lenses with documented CAD; custom glass only with lead time flag → `supply-chain-management`

## Terminology and standards

- F/#, NA, MTF, RMS spot size, chief ray angle
- ISO 10993 (only if biocompatibility path — rare; defer experts)
- IEC 60825 laser safety (design input; classification → `product-compliance`)

## Cross-links

| Need | Skill |
| --- | --- |
| Motion stages | `mechatronic-engineering` |
| Vision pipeline | `software-development` |
| Enclosures | `mechanical-engineering` |
| System requirements | `systems-engineering` |
| Production optical QC | `production-engineering` |

## Practical constraints

- Dust-clean assembly may require `production-engineering` clean bench SOP.
- Open publication of optical recipes may affect competitive positioning — align with `business-development`.
- Sensor supply constraints often gate entire subsystem — early `purchasing` engagement.
