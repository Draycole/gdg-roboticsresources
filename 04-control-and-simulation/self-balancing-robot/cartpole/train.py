"""
Robotics Track - train a PPO agent to balance a pole on a cart (MuJoCo).

Run the default (takes a few minutes on a normal laptop CPU):
    python train.py

Useful options:
    python train.py --timesteps 200000 --seed 1
    python train.py --run-name my_experiment

What you get afterwards, inside runs/<run-name>/ :
    model.zip     the trained agent (the "policy")
    monitor.csv   a log of every episode's score (used by plot_results.py)
"""

import argparse
import os
import time

import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.monitor import Monitor

ENV_ID = "InvertedPendulum-v5"


def main():
    parser = argparse.ArgumentParser(description="Train PPO on InvertedPendulum.")
    parser.add_argument("--timesteps", type=int, default=100_000,
                        help="how many simulation steps to train for (default 100000)")
    parser.add_argument("--seed", type=int, default=0,
                        help="random seed; change it to get a different training run")
    parser.add_argument("--run-name", type=str, default=None,
                        help="folder name for this run inside runs/")
    args = parser.parse_args()

    run_name = args.run_name or f"ppo_seed{args.seed}_{args.timesteps // 1000}k"
    run_dir = os.path.join("runs", run_name)
    os.makedirs(run_dir, exist_ok=True)

    # The environment: a cart with a pole on top. Reward is +1 for every step the
    # pole stays up. Max score per episode is 1000.
    env = Monitor(gym.make(ENV_ID), os.path.join(run_dir, "monitor.csv"))

    # The agent: PPO with a small neural network (MlpPolicy). CPU is plenty here.
    model = PPO(
        "MlpPolicy",
        env,
        seed=args.seed,
        verbose=1,
        device="cpu",
        tensorboard_log="tb_logs",
    )

    print(f"\nTraining '{run_name}' for {args.timesteps} steps. Sit tight...\n")
    start = time.time()
    model.learn(total_timesteps=args.timesteps, tb_log_name=run_name)
    minutes = (time.time() - start) / 60

    model.save(os.path.join(run_dir, "model"))
    print(f"\nDone in {minutes:.1f} min. Saved to {run_dir}/model.zip")
    print("Next: python evaluate.py --model " + os.path.join(run_dir, "model.zip") + " --render")


if __name__ == "__main__":
    main()
