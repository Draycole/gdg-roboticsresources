# 04: Control and simulation

Make things move correctly, and test them in simulation before building hardware.

## Projects in this stage

| Project | What it is | Status |
|---|---|---|
| [self-balancing-robot](self-balancing-robot) | A two-wheeled robot balanced three ways: PID, LQR, and a PPO policy trained in MuJoCo | Simulation working; hardware planned for semester 2 |
| [drone-digital-twin](drone-digital-twin) | IMU data from a handheld drone prototype streamed into a PyBullet simulation | In progress |

## Planned

These topics will get their own folders as the material is written:

- PID control: tuning, anti-windup, a worked example
- State-space models and LQR (inverted pendulum)
- PyBullet and MuJoCo basics
- Sim-to-hardware: serial data formats, latency, sensor fusion

## Prerequisites

Stage 3 (embedded systems) and comfortable Python.

## How each folder here is laid out

Every project or tutorial has a README with: what it is, how to run it, what you should see, a "tested on" line, and known issues.