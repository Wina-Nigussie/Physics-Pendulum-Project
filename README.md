# Large-Angle Pendulum Simulation
**Section 11B | Group 4 & 10**

## Project Overview
This project simulates a simple pendulum released from an 85-degree angle. Instead of using the standard small-angle approximation ($T = 2\pi\sqrt{L/g}$), we used **Euler's Method** for numerical integration to calculate the position and velocity of the bob at every $dt = 0.01$ seconds.

## Tools Used
* **Python (VPython):** For 3D visualization and physics modeling.
* **LaTeX (Beamer):** For the formal presentation.
* **GitHub:** For version control and collaboration.

## How to Run
1. Copy the code from `pendulum.py`.
2. Paste it into [WebVPython.org](https://webvpython.org).
3. Click "Run" to see the simulation.

## Project objective
This simulation investigates the motion of a simple pendulum released from a large angle ($85^{\circ}$). We aim to demonstrate how the period of oscillation deviates from the standard small-angle approximation ($T = 2\pi\sqrt{L/g}$) when using a high-amplitude release.

## Parameter Definitions 
To ensure consistency across the group, we defined specific physical constants for our simulation. The gravitational acceleration ($g$) is $9.8$ m/s², the string length ($L$) is $5.0$ meters, and the starting amplitude ($\theta$) is $1.48$ radians ($85^{\circ}$). These constants serve as the foundation for our numerical integration.
## Final Results 
Our computational model, using Euler's Method with a time step of $dt = 0.01$, calculated a real-world period of 5.14 seconds. This is significantly slower than the theoretical small-angle prediction of 4.49 seconds, proving the impact of large-angle physics.
