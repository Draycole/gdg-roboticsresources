# Self-balancing robot: simulation, reinforcement learning, and sim-to-real

A two-wheeled robot that balances itself, tackled three ways: classical PID, LQR, and a reinforcement-learning policy (PPO) trained in MuJoCo. This is the GDG Robotics Track's project for the 2026-27 session. Semester 1 covers simulation and the three controllers. Semester 2 builds the hardware and deploys the best controller on it.

Everything here is open. Take it, run it, and break it.

## What you will learn

- Modelling a balancing robot as an inverted pendulum
- Designing PID and LQR controllers and seeing where they struggle
- Setting up an RL environment: observations, actions, rewards
- Training a PPO policy and reading the training curves
- Comparing all three controllers on the same task

## Quick start

> Tested on: [TODO: OS, Python version, MuJoCo version, date]

```bash
git clone https://github.com/Draycole/gdg-roboticsresources.git
cd gdg-roboticsresources/04-control-and-simulation/self-balancing-robot

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# [TODO: replace with your real commands]
python training/train.py          # train a policy
python scripts/evaluate.py        # watch a trained policy balance the robot
```

No time to train? A pretrained policy is available in the [Releases](../../../../releases) page. [TODO: add link once the release exists]

## What is in this folder

| Path | What it is |
|---|---|
| `models/` | The robot model (MuJoCo XML and any meshes) |
| `envs/` | The simulation environment: observations, actions, rewards |
| `controllers/` | PID and LQR baselines |
| `training/` | PPO training script and configuration |
| `scripts/` | Evaluate, record, and compare controllers |
| `results/` | Plots and GIFs |
| `docs/` | Theory notes: dynamics, reward design, how to read the curves |
| `requirements.txt` | Pinned package versions |

[TODO: adjust the table to match the actual folders]

## Results

| Controller | Time balanced | Recovers from a push | Notes |
|---|---|---|---|
| PID | [TODO] | [TODO] | |
| LQR | [TODO] | [TODO] | |
| PPO | [TODO] | [TODO] | |

![Training curve](results/training-curve.png)
[TODO: add one plot and one GIF. People judge projects by what they can see.]

## Prerequisites

Comfortable Python, plus the basics from the earlier stages: [PID](../pid), [state-space and LQR](../state-space-lqr), and [PyBullet and MuJoCo basics](../pybullet-basics). [TODO: adjust links to folders that exist]

## Roadmap

- [x] Simulation environment
- [x] PPO training
- [ ] PID and LQR baselines compared against PPO
- [ ] Hardware build: 3D-printed chassis, motors, IMU, microcontroller
- [ ] Sim-to-real deployment

## Known issues

[TODO: list anything that does not work yet. An honest list is the easiest first contribution for someone else.]

## Credits and license

Built by the GDG Robotics Track, [TODO: names]. Code is MIT licensed. Third-party packages keep their own licenses.

Session notes and checkpoints for this cohort are in [`cohorts/2026-27`](../../cohorts/2026-27).