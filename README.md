# 🚀 Large-Angle Pendulum Simulation
### Section 11B | Group 4 & 10

This repository contains a 3D physics simulation of a pendulum released at **85 degrees**, demonstrating the breakdown of the small-angle approximation.

## 📊 Visual Evidence
![Pendulum Simulation](simulation.gif)

## 🛠️ Project Components
* **Python Script:** `pendulum.py` - Uses Euler's Method for numerical integration.
* **Presentation:** `slides.pdf` - High-quality LaTeX Beamer presentation.
* **3D Visuals:** Powered by VPython/GlowScript.

## 🧪 Simulation Constants
| Variable | Value |
| :--- | :--- |
| **Length (L)** | 5.0 m |
| **Gravity (g)** | 9.8 m/s² |
| **Initial Theta** | 1.48 rad (85°) |

## 👥 Contributors
*Special thanks to our team for their technical contributions:*
- **Sifen, Bemnet, Yordanos, Edlawit** (Documentation & Research)
- **Ephrata, Bitaniya, Wengelawit, Abigiya** (Code Verification)
- **Edidiya, Hana, Nardos, Ruhama** (Physics Analysis)

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
