# Drone digital twin

A handheld drone prototype whose orientation is mirrored live in a PyBullet simulation. An MPU6050 IMU streams over serial, a complementary filter estimates attitude, and the simulated drone follows.

## Status

In progress. There are two iterations, and neither is fully working yet:

| Version | Board | State |
|---|---|---|
| 1 | ESP32 | Responsive, but the simulated drone drifts down slowly and snaps back about every 0.5 s |
| 2 | Raspberry Pi Pico (bare-metal C) | The falling problem is fixed, but there is roughly 1.2 s of lag when orientation changes |

[TODO: update this table as things change.]

## What is here

[TODO: list the actual files, for example:]

| File | What it is |
|---|---|
| `main.c` | Pico firmware: IMU read, complementary filter, serial output |
| [TODO] | PyBullet script that reads serial and moves the drone |
| [TODO] | ESP32 version |

## How it works

1. The MPU6050 gives raw accelerometer and gyroscope readings.
2. A complementary filter blends them into roll and pitch.
3. The board sends the angles over serial.
4. A Python script reads the angles and sets the simulated drone's orientation.

## Run it

> Tested on: [TODO: OS, Python version, PyBullet version, board and toolchain, date]

[TODO: wiring, build/flash steps, and the command that starts the simulation]

## Known issues and open problems

- ESP32: the snap-back every ~0.5 s looks like a serial send-interval problem.
- Pico: the ~1.2 s response lag. It is not yet clear whether the earlier falling fix came from the register initialisation or from software changes.
- Absolute yaw is not available. The MPU6050 has no magnetometer, so yaw drifts.

These are good first contributions. If you fix one, open a PR and describe what you changed and why.

## Related

- Stage 2: reading an IMU
- Stage 3: UART and I2C on the Pico