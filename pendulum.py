from vpython import *

# 1. Setup the Window and Constants
scene = canvas(title="Large Angle Pendulum: Group 4 & 9", width=800, height=600)
g = 9.8            # Gravity
L = 5.0            # Length of string
m = 1.0            # Mass of bob
dt = 0.01          # Small time step (Numerical Integration)

# 2. Initial Conditions (The prompt asks for 85 degrees)
theta = 85 * pi / 180  
omega = 0              # Initial angular velocity
t = 0

# 3. Create Visual Objects
ceiling = box(pos=vec(0, 0, 0), size=vec(2, 0.1, 2), color=color.gray(0.5))
bob = sphere(pos=vec(L*sin(theta), -L*cos(theta), 0), radius=0.3, color=color.red, make_trail=True)
string = cylinder(pos=ceiling.pos, axis=bob.pos - ceiling.pos, radius=0.05)

# Labels for the screen
label_t = label(pos=vec(3, 5, 0), text='Time: 0')

# 4. The Physics Loop (Euler's Method)
print("Simulation Running...")

while t < 20:
    rate(100) # Speed of animation
    
    # Calculate Angular Acceleration: alpha = -(g/L) * sin(theta)
    alpha = -(g / L) * sin(theta)
    
    # Update Velocity: omega = omega + alpha * dt
    omega = omega + alpha * dt
    
    # Update Angle: theta = theta + omega * dt
    theta = theta + omega * dt
    
    # Update Visuals
    bob.pos = vec(L * sin(theta), -L * cos(theta), 0)
    string.axis = bob.pos - ceiling.pos
    
    t = t + dt
    label_t.text = "Time: " + str(round(t, 2)) + "s"