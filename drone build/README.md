# <center>GDG Robotics & Embedded Systems Track
### <center> Drone Simulation
---

  
Hi Team👋

The idea is to work on a drone this semester, amongst our other projects. So we'll start off with simulation, so we can wrap our minds around the math and code needed to describe a drone in space.

An important thing we'll be focusing on right now is how to handle our IMU (Inertial Measurement Unit). An IMU is an device that measures  a body's  force, angular rate, and orientation using accelerometers and gyroscopes. It is important for navigation in drones, aircraft, and vehicles, as well as in motion tracking for smartphones and VR.
  
We'll be using it to track our drone's location, speed and tilt in various axes. I've also linked the datasheet to the IMU in this repo [here](./docs)

In the [drone simulation](./drone_simulation) folder, We were able to work on a script that allows you to visualize the IMU as a real-life drone. We used Python and PyBullet for the simulation. The microcontroller code picked the relevant data and sent it over a COM port where python was able to parse and plot the data. 

Good news even, we were able to come up with functioning code for both an [ESP32](./drone_simulation/esp32) and a [Raspberry Pi Pico](./drone_simulation/raspberry_pi). We're working on getting one for the Arduino UNO up soon since that's the most common microcontroller.

We're using a custom URDF for the simulation/visualization accessible also in [docs](./docs). And if you run into any problems reading your ESP as a COM Port on your laptop, we also uploaded the Universal Windows Driver that you can run to help your ESP come up as a COM port.

Reach out to Erica or I if you've got any problems/questions/code you'll like us to deploy. 

Cheers  
⚡🤖
