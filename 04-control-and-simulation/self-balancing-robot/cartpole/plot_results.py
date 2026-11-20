"""
Robotics Track - plot the learning curves of your training runs.

    python plot_results.py                      # plots every run found in runs/
    python plot_results.py runs/ppo_seed0_100k  # plots just one run
    python plot_results.py --no-show            # only saves the picture

Saves the picture as learning_curves.png. This is the picture to post in the
group chat for the take-home tasks.

X axis = how much the agent has practised (simulation steps)
Y axis = score per episode (max 1000), smoothed so the trend is readable
"""

import argparse
import glob
import os

import matplotlib.pyplot as plt
import numpy as np


def load_monitor(path):
    """Read an SB3 monitor.csv: returns (cumulative_steps, episode_scores)."""
    data = np.genfromtxt(path, delimiter=",", skip_header=2)  # line 1 is a comment, line 2 the header
    data = np.atleast_2d(data)
    scores = data[:, 0]
    steps = np.cumsum(data[:, 1])
    return steps, scores


def smooth(values, window):
    window = max(1, min(window, len(values)))
    kernel = np.ones(window) / window
    return np.convolve(values, kernel, mode="valid")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("runs", nargs="*", help="run folders (default: everything in runs/)")
    parser.add_argument("--window", type=int, default=20, help="smoothing window (episodes)")
    parser.add_argument("--no-show", action="store_true")
    args = parser.parse_args()

    run_dirs = args.runs or sorted(glob.glob(os.path.join("runs", "*")))
    run_dirs = [d for d in run_dirs if os.path.exists(os.path.join(d, "monitor.csv"))]
    if not run_dirs:
        print("No runs found. Train something first:  python train.py")
        return

    plt.figure(figsize=(8, 5))
    for run_dir in run_dirs:
        steps, scores = load_monitor(os.path.join(run_dir, "monitor.csv"))
        smoothed = smooth(scores, args.window)
        plt.plot(steps[len(steps) - len(smoothed):], smoothed, label=os.path.basename(run_dir))

    plt.axhline(1000, color="gray", linestyle="--", linewidth=0.8)
    plt.xlabel("Training steps")
    plt.ylabel("Episode score (max 1000)")
    plt.title("Learning curves")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("learning_curves.png", dpi=150)
    print("Saved learning_curves.png")
    if not args.no_show:
        plt.show()


if __name__ == "__main__":
    main()
