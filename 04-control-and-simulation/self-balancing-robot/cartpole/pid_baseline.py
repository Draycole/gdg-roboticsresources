"""
Robotics Track - a classical controller for the same pole-on-cart, no learning.

    python pid_baseline.py
    python pid_baseline.py --render        (macOS: use mjpython)

The observation is 4 numbers:
    x      cart position
    theta  pole angle (0 = upright)
    xdot   cart velocity
    thdot  pole angular velocity

The controller is just a weighted sum of those four numbers:
    force = KX*x + KTH*theta + KXD*xdot + KTHD*thdot

THE GAINS BELOW WORK, but they are only one choice. Your take-home challenge:
  1. Set KXD to 0. The score drops a lot. Why? (Hint: watch what the cart does
     over time, and remember the track is not infinitely long.)
  2. Find gains that get a perfect 1000 and recover from a bigger push.
  3. Compare with your PPO agent: which is more robust? Which was easier to build?
"""

import argparse

import gymnasium as gym
import numpy as np

ENV_ID = "InvertedPendulum-v5"

# --- tune these -----------------------------------------------------------
KX = 0.0      # push back toward the centre of the track
KTH = 5.0     # react to the pole's lean (proportional term)
KXD = 0.5     # react to the cart's speed
KTHD = 1.0    # react to how fast the pole is falling (derivative term)
# ---------------------------------------------------------------------------


def controller(obs):
    x, theta, xdot, thdot = obs
    force = KX * x + KTH * theta + KXD * xdot + KTHD * thdot
    return np.clip(force, -3.0, 3.0)  # the motor can only push so hard


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--episodes", type=int, default=5)
    parser.add_argument("--render", action="store_true")
    args = parser.parse_args()

    env = gym.make(ENV_ID, render_mode="human" if args.render else None)
    scores = []
    for ep in range(args.episodes):
        obs, _ = env.reset(seed=123 + ep)
        done, total = False, 0.0
        while not done:
            action = np.array([controller(obs)], dtype=np.float32)
            obs, reward, terminated, truncated, _ = env.step(action)
            total += reward
            done = terminated or truncated
        scores.append(total)
        print(f"Episode {ep + 1}: score = {total:.0f} / 1000")
    env.close()
    print(f"\nAverage: {np.mean(scores):.0f} / 1000")


if __name__ == "__main__":
    main()
