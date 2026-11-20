"""
Robotics Track - watch (or score) a trained agent.

    python evaluate.py --model runs/ppo_seed0_100k/model.zip --render
    python evaluate.py --model pretrained/pendulum_ppo.zip --render
    python evaluate.py --model runs/ppo_seed0_100k/model.zip --episodes 20

--render opens the MuJoCo window so you can watch.
macOS users: run with `mjpython evaluate.py ... --render` instead of `python`.
Without --render it just prints the scores (works anywhere, even over SSH).

A perfect episode scores 1000 (pole stayed up for the whole time).
"""

import argparse

import gymnasium as gym
import numpy as np
from stable_baselines3 import PPO

ENV_ID = "InvertedPendulum-v5"


def main():
    parser = argparse.ArgumentParser(description="Evaluate a trained PPO agent.")
    parser.add_argument("--model", type=str, default="pretrained/pendulum_ppo.zip",
                        help="path to a saved model (.zip)")
    parser.add_argument("--episodes", type=int, default=5)
    parser.add_argument("--render", action="store_true", help="open the MuJoCo window")
    parser.add_argument("--seed", type=int, default=123)
    args = parser.parse_args()

    env = gym.make(ENV_ID, render_mode="human" if args.render else None)
    model = PPO.load(args.model, device="cpu")

    scores = []
    for ep in range(args.episodes):
        obs, _ = env.reset(seed=args.seed + ep)
        done = False
        total = 0.0
        while not done:
            # deterministic=True: use the agent's best guess, no exploration noise
            action, _ = model.predict(obs, deterministic=True)
            obs, reward, terminated, truncated, _ = env.step(action)
            total += reward
            done = terminated or truncated
        scores.append(total)
        print(f"Episode {ep + 1}: score = {total:.0f} / 1000")

    env.close()
    print(f"\nAverage over {args.episodes} episodes: {np.mean(scores):.0f} / 1000")


if __name__ == "__main__":
    main()
