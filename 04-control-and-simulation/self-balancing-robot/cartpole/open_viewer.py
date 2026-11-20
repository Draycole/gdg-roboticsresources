"""
Robotics Track - open the pole-on-cart model in the MuJoCo viewer. Works offline.

    python open_viewer.py

The model file ships inside the gymnasium package, so there is nothing to download.

Things to try in the window:
  - Double-click a body, then Ctrl + right-drag (Cmd on Mac) to push it.
  - Press Space to pause or resume the simulation.
  - Open the "Control" panel on the right and move the slider: that is the
    actuator (the motor pushing the cart).
  - Count what you see: bodies (parts), joints (how parts connect),
    actuators (motors). The timestep is how often the physics updates.
"""

import os

import gymnasium
import mujoco
import mujoco.viewer

model_path = os.path.join(
    os.path.dirname(gymnasium.__file__), "envs", "mujoco", "assets", "inverted_pendulum.xml"
)
model = mujoco.MjModel.from_xml_path(model_path)
data = mujoco.MjData(model)

print(f"Bodies: {model.nbody}   Joints: {model.njnt}   Actuators: {model.nu}")
print(f"Simulation timestep: {model.opt.timestep} s")
print("Close the window to exit.")

mujoco.viewer.launch(model, data)
