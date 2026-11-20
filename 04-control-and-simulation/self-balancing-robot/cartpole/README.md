# Robotics Track: Self-Balancing Robot (Sim to Real)

This session we are taking one project all the way from a simulation to a real robot. Semester 1 is simulation, control and reinforcement learning on our laptops. Semester 2 is building a two-wheeled self-balancing robot and running our trained controller on it.

This repo is where all our code lives. Everything here works **offline** once it is installed.

## What is in here

| File | What it does |
|---|---|
| `check_install.py` | Checks that your setup works. Run this first. |
| `open_viewer.py` | Opens the pole-on-cart model in the MuJoCo window so you can poke at it. |
| `train.py` | Trains an AI agent (PPO) to balance a pole on a cart. |
| `evaluate.py` | Watches or scores a trained agent. |
| `plot_results.py` | Draws the learning curves of your runs. |
| `pid_baseline.py` | A classical (non-learning) controller for the same task. |
| `pretrained/pendulum_ppo.zip` | A ready-trained agent, in case your training is slow. |
| `docs/RL_IN_PLAIN_ENGLISH.md` | One page: what reinforcement learning actually is. |
| `TASKS.md` | Your take-home tasks for the break. |

## Setup (you already did this)

1. Get this repo onto your laptop: **Code, then Download ZIP** on GitHub, unzip it, and open the folder in VS Code. (If you know git: `git clone` it instead.)
2. Open a terminal in VS Code and activate your virtual environment. You must see `(.venv)` at the start of the line.
   - Windows: `.venv\Scripts\Activate.ps1`
   - Mac/Linux: `source .venv/bin/activate`
3. Check everything works:

```
python check_install.py
```

It should end with **ALL GOOD**. If a package is missing, run `pip install -r requirements.txt` and try again.

> The `.venv` folder can sit inside this repo folder or next to it. Just make sure you activate the one you installed the packages into.

## The 3-step workflow

**1. Train** (about 1 to 5 minutes on a normal laptop):

```
python train.py
```

**2. Watch** your agent:

```
python evaluate.py --model runs/ppo_seed0_100k/model.zip --render
```

- A MuJoCo window opens and you watch the agent balance the pole.
- **Mac users:** use `mjpython` instead of `python` for anything with `--render`.
- A perfect episode scores **1000**.
- No window? Drop `--render` and it just prints the scores.

**3. Plot** how it learned:

```
python plot_results.py
```

This saves `learning_curves.png`. Compare yours with `docs/example_learning_curves.png`.

## If your training is slow or something breaks

Use the pre-trained agent so you can still follow along:

```
python evaluate.py --model pretrained/pendulum_ppo.zip --render
```

## Troubleshooting

- **`(.venv)` is not showing:** you forgot to activate. Run the activate command above.
- **`ModuleNotFoundError`:** you are probably outside the venv, or the install did not finish. Activate, then `pip install -r requirements.txt`.
- **Window does not open on Mac:** use `mjpython`, not `python`.
- **`Environment InvertedPendulum-v5 doesn't exist`:** your Gymnasium is too old. Run `pip install -U "gymnasium[mujoco]"`.
- **Training seems frozen:** it is not. PPO prints a progress table every few seconds. Be patient.
- **Anything else:** screenshot the full error and send it in the group chat.

## Further reading (for the curious, all optional)

- OpenAI Spinning Up: a friendly introduction to deep RL (spinningup.openai.com)
- Stable-Baselines3 docs: the library we use for PPO (stable-baselines3.readthedocs.io)
- Gymnasium docs: the environments (gymnasium.farama.org)
- MuJoCo docs: the physics engine (mujoco.readthedocs.io)
- Sutton and Barto, *Reinforcement Learning: An Introduction*: the classic free textbook (incompleteideas.net/book/the-book-2nd.html)

## The plan

1. **Semester 1:** simulate, then compare PID, LQR and RL on a balancing task.
2. **Design freeze:** pick the real motor, wheels, battery and IMU, then update the simulation to match.
3. **Semester 2:** build the robot (3D-printed chassis, ESP32), balance it with classical control first, then run the RL policy on it.
