---
name: mechatronic-engineering
description: >-
  Integrated motion, actuation, sensing, and control of electromechanical systems.
  Use for motors, drives, kinematics, sensors, and control tuning spanning
  mechanical and electrical domains — not pure software apps or legal compliance.
---
# Mechatronic Engineering

Use this skill at the boundary of mechanism, electronics, and control: making things move and sense correctly.

## Scope

**Owns:**
- Actuator selection (motors, solenoids, pneumatics/hydraulics interfaces)
- Drive and encoder feedback architecture
- Kinematic and dynamic analysis (simplified models, simulation)
- Sensor fusion at system level (IMU, force, position)
- Control loop tuning (PID, feedforward, limits)
- Mechatronic BOM (motors, drives, couplings, sensors)
- Integration test plans for motion subsystems

**Does NOT own:**
- Detailed PCB design → `electrical-engineering`
- Pure mechanical structural CAD → `mechanical-engineering`
- Factory PLC integration → `industrial-automation`
- Optical alignment and imaging chains → `optical-engineering`
- Safety validation sign-off → `product-compliance`, `systems-engineering`

## Core principles

- **System thinking:** Motor, gearbox, driver, firmware, and mechanism must be co-designed.
- **Margins for real friction:** Models include stiction, backlash, thermal drift; validate on hardware.
- **Open documentation:** Publish kinematic diagrams, tuning procedures, and calibration steps where policy allows.
- **Fail-safe motion:** Limits, torque caps, and estop behavior defined with `software-development` and `industrial-automation`.
- **Service calibration:** Field-adjustable without proprietary tools when feasible.

## Key workflows

### Actuator sizing

1. Load profile (inertia, friction, duty cycle)
2. Speed/accel requirements
3. Drive bus voltage and current headroom
4. Thermal check at worst case
5. Commercial availability → `purchasing`

### Bring-up and tuning

- [ ] Encoder polarity and counts verified
- [ ] Hard/soft limits commissioned
- [ ] Current/torque limits set below mechanical failure
- [ ] Step response and tracking error recorded
- [ ] Vibration modes noted for `mechanical-engineering` stiffening if needed

### Handoff to production

- Calibration recipe, default parameters, acceptance torque/speed tests → `production-engineering`

## Terminology and standards

- Denavit-Hartenberg, Jacobian (as needed)
- IEC 61800 ( drives ), ISO 9409 mounting flanges
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

- High-performance mechatronics conflicts with lowest BOM cost — document trade-offs for `finance` and `business-development`.
- Open hardware forks need clear calibration and safety warnings.
- Harmonic drives and rare encoders affect `supply-chain-management`.
