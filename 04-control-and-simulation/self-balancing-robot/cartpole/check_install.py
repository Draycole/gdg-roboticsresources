"""
Robotics Track - one-command install check. Works with NO internet.

    python check_install.py

If everything is fine it ends with: ALL GOOD
If something is missing, it tells you exactly which package and what to do.
"""

import importlib
import sys

print(f"Python {sys.version.split()[0]}")
major, minor = sys.version_info[:2]
if (major, minor) < (3, 10) or (major, minor) > (3, 12):
    print("  WARNING: we recommend Python 3.10 to 3.12. Other versions may still work,")
    print("  but if installs fail, this is the first thing to check.")

if sys.prefix == sys.base_prefix:
    print("  WARNING: you are NOT inside the virtual environment.")
    print("  Activate it first (you should see (.venv) at the start of the terminal line).")

packages = [
    "mujoco", "gymnasium", "stable_baselines3", "torch",
    "numpy", "scipy", "matplotlib", "control", "tensorboard",
]

missing = []
for name in packages:
    try:
        module = importlib.import_module(name)
        version = getattr(module, "__version__", "?")
        print(f"  OK       {name} {version}")
    except Exception as exc:  # noqa: BLE001
        print(f"  MISSING  {name}  ({type(exc).__name__})")
        missing.append(name)

if missing:
    print("\nSomething is missing. With (.venv) showing, run:")
    print("    pip install -r requirements.txt")
    sys.exit(1)

# Try the actual simulator for a few steps
import gymnasium as gym  # noqa: E402

env = gym.make("InvertedPendulum-v5")
obs, _ = env.reset(seed=0)
for _ in range(50):
    obs, reward, terminated, truncated, _ = env.step(env.action_space.sample())
    if terminated or truncated:
        obs, _ = env.reset()
env.close()
print("  OK       simulator ran 50 steps")

print("\nALL GOOD")
