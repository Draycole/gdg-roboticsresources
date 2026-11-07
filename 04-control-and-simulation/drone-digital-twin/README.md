# <center>GDG Robotics & Embedded Systems Track
### <center> Drone Simulation
---

  
Hi Team👋

The idea is to work on a drone this semester, amongst our other projects. So we'll start off with simulation, so we can wrap our minds around the math and code needed to describe a drone in space.

An important thing we'll be focusing on right now is how to handle our IMU (Inertial Measurement Unit). An IMU is an device that measures  a body's  force, angular rate, and orientation using accelerometers and gyroscopes. It is important for navigation in drones, aircraft, and vehicles, as well as in motion tracking for smartphones and VR.
  
We'll be using it to track our drone's location, speed and tilt in various axes. I've also linked the datasheet to the IMU in this repo [here](./docs)

In the [drone simulation](./drone_simulation) folder, We were able to work on a script that allows you to visualize the IMU as a real-life drone. We used Python and PyBullet for the simulation. The microcontroller code picked the relevant data and sent it over a COM port where python was able to parse and plot the data. 

Good news even, we were able to come up with functioning code for both an [ESP32](./drone_simulation/esp32) and an [Arduino](./drone_simulation/arduino). We also got the code up for those using a [Raspberry Pi Pico](./drone_simulation/raspberry_pi)
The Arduino code is portable for both an UNO and Nano, so feel free to try it on both if you can lay your hands on an IMU. For the Pi Pico, the executable uf2 file is in the [build](./drone_simulation/raspberry_pi/build/) folder (we've gone through the hassle of building it for you guys.)

We're using a custom URDF for the simulation/visualization accessible also in [docs](./docs). And if you run into any problems reading your ESP as a COM Port on your laptop, we also uploaded the [Universal Windows Driver](./docs/CP210x_Universal_Windows_Driver.zip) that you can run from your Device Manager to help your ESP show up as a COM port.

Reach out to Erica or I if you've got any problems/questions/code you'll like us to deploy. 

Cheers  
⚡🤖
