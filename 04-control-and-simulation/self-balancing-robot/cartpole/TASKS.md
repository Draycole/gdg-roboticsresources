# Take-Home Tasks (the break plan)

We won't meet in person for a while, so the track keeps going here. Do as much as you like. **Level 1 is the minimum**, and everything after it is for fun and bragging rights.

## How to hand in your work

Post in the group chat with:
1. A screenshot (your `learning_curves.png`, or the terminal showing your scores).
2. **One line** on what you noticed. ("Seed 3 learned way slower than seed 1, not sure why.")

Half-working results count. Questions count too. Post them.

**Task drops:** one new task every two weeks, announced in the chat. Check-in call before the break ends: *[date to be announced]*.

---

## Level 1: Run your own experiment (everyone)

Train two more runs with different settings, then plot them together:

```
python train.py --seed 1
python train.py --seed 2 --timesteps 50000
python plot_results.py
```

Answer in your post:
- Did all runs learn at the same speed? Why might they differ?
- Did the 50,000-step run reach a perfect 1000? What does that tell you about "how much practice is enough"?

## Level 2: Change what the agent cares about

**A. Change a setting.** Open `train.py` and find the line `model = PPO(...)`. Add one extra setting and re-train with a new `--run-name`. Pick one:

```python
learning_rate=1e-3,    # how big each learning step is (default 0.0003)
n_steps=1024,          # how much experience before each update (default 2048)
gamma=0.98,            # how much the agent cares about the future (default 0.99)
```

Compare with your original run. Did it help or hurt?

**B. Change the reward.** Right now the agent is paid +1 for every moment the pole stays up, and nothing else. Add this to `train.py` (above `main()`), and wrap your environment with it:

```python
class CenteredReward(gym.RewardWrapper):
    """Punish the cart for drifting away from the middle."""
    def reward(self, reward):
        x = self.env.unwrapped.data.qpos[0]   # cart position
        return reward - 0.5 * abs(x)
```

```python
env = CenteredReward(Monitor(gym.make(ENV_ID), os.path.join(run_dir, "monitor.csv")))
```

Re-train, then watch it with `evaluate.py --render`. Does the agent behave differently? Try changing `0.5` to a bigger number. This is what real robotics engineers spend a lot of time on: **the agent does what you pay it for, not what you meant.**

## Level 3: Beat the robot with a classical controller

Open `pid_baseline.py`. The gains at the top already balance the pole (no learning needed).

1. Run it: `python pid_baseline.py`.
2. Set `KXD = 0` and run it again. What happens, and why?
3. Tune the four gains to get a perfect score and look good doing it.
4. Write a short note: PPO versus your controller. Which was easier to build? Which was more robust? Which would you trust on a real robot?

## Hardware-free sensor lab (optional, but the best preview of real robotics)

Your phone is a real IMU, the same kind of sensor the robot will use.

1. Install **Phyphox** (free) on your phone.
2. Record the accelerometer and gyroscope while you tilt the phone slowly back and forth, then export the data as CSV.
3. In Python, estimate the tilt angle two ways: from the accelerometer alone, and from the gyroscope alone (integrate the rate over time).
4. Notice what goes wrong with each. (Accelerometer: noisy. Gyroscope: drifts.)
5. Combine them with a **complementary filter**:

```
angle = 0.98 * (angle + gyro_rate * dt) + 0.02 * accel_angle
```

Plot all three. This exact filter will run on our robot.

---

## Stuck?

Post your question in the chat with a screenshot of the **full** error message. Nobody gets laughed at. Everyone gets stuck on something.
