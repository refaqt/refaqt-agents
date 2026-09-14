---
name: mechatronic-engineering
description: >-
  Combined motion, actuation, sensing, and control of electromechanical
  systems. Use for motors, drives, kinematics, sensors, and control tuning
  that span mechanical and electrical domains. Do not use this skill for
  pure software apps or legal compliance.
---
# Mechatronic Engineering

Use this skill at the boundary of mechanism, electronics, and control: making things move and sense correctly.

## Scope

**Owns:**
- Actuator selection (motors, solenoids, pneumatics/hydraulics interfaces)
- Drive and encoder feedback architecture
- Kinematic and dynamic analysis (simplified models, simulation)
- Sensor fusion at system level (inertial measurement unit (IMU), force, position)
- Control loop tuning (proportional-integral-derivative (PID), feedforward, limits)
- Mechatronic parts list (BOM): motors, drives, couplings, sensors
- Integration test plans for motion subsystems

**Does NOT own:**
- Detailed printed circuit board (PCB) design → `electrical-engineering`
- Pure mechanical structural computer-aided design (CAD) → `mechanical-engineering`
- Factory programmable logic controller (PLC) integration → `industrial-automation`
- Optical alignment and imaging chains → `optical-engineering`
- Safety validation sign-off → `product-compliance`, `systems-engineering`

## Core principles

- **System thinking:** Motor, gearbox, driver, firmware, and mechanism must be designed together.
- **Margins for real friction:** Models include static friction (stiction), gear slack (backlash), and thermal drift. Validate on hardware.
- **Open documentation:** Publish kinematic diagrams, tuning procedures, and calibration steps where policy allows.
- **Fail-safe motion:** Define limits, torque caps, and emergency-stop (estop) behavior with `software-development` and `industrial-automation`.
- **Service calibration:** Prefer field adjustment without proprietary tools when that is practical.

## Key workflows

### Actuator sizing

1. Load profile (inertia, friction, duty cycle)
2. Speed/accel requirements
3. Drive bus voltage and spare current capacity (headroom)
4. Thermal check at the hardest operating case
5. Commercial availability → `purchasing`

### First power-on (bring-up) and tuning

- [ ] Encoder polarity and counts verified
- [ ] Hardware and software limits commissioned
- [ ] Current/torque limits set below mechanical failure
- [ ] Step response and tracking error recorded
- [ ] Vibration modes noted for `mechanical-engineering` stiffening if needed

### Handoff to production

- Calibration recipe, default parameters, acceptance torque/speed tests → `production-engineering`

## Terminology and standards

- Denavit-Hartenberg robot geometry, Jacobian motion math (as needed)
- International Electrotechnical Commission (IEC) 61800 (drives), International Organization for Standardization (ISO) 9409 mounting flanges
- CiA 402 drive profile (EtherCAT/CANopen contexts)

## Cross-links

| Need | Skill |
| --- | --- |
| Structures and mounts | `mechanical-engineering` |
| Motor drivers PCB | `electrical-engineering` |
| Real-time firmware | `software-development` |
| Precision optics stages | `optical-engineering` |
| Requirements | `systems-engineering` |

## Practical constraints

- High-performance mechatronics can conflict with the lowest BOM cost. Record trade-offs for `finance` and `business-development`.
- Open hardware copies (forks) need clear calibration and safety warnings.
- Harmonic drives and rare encoders affect `supply-chain-management`.
