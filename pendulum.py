#from vpython import 
scene = canvas(title="Advanced Pendulum Analysis: Group 4 & 9", width=800, height=600, background=color.black)
scene.center = vec(0, -2, 0)
gd = graph(title="<b>Angular Displacement vs. Time</b>", xtitle="Time (s)", ytitle="Angle (radians)", 
           width=500, height=300, fast=False)
angle_curve = gcurve(color=color.cyan, width=2, label="Theta (85 deg)")
g = 9.8
L = 5.0
dt = 0.01
t = 0
theta = 85 * pi / 180  
omega = 0              
floor = box(pos=vec(0, -L-1, 0), size=vec(10, 0.2, 10), color=color.gray(0.3))
ceiling = box(pos=vec(0, 0, 0), size=vec(2, 0.1, 2), color=color.white)
bob = sphere(pos=vec(L*sin(theta), -L*cos(theta), 0), radius=0.4, 
             color=color.orange, make_trail=True, trail_type="points", interval=10, retain=50)
string = cylinder(pos=ceiling.pos, axis=bob.pos - ceiling.pos, radius=0.04, color=color.gray(0.8))
label_data = label(pos=vec(4, 2, 0), text='', box=False, height=15)
while t < 30:
    rate(100)
    alpha = -(g / L) * sin(theta)
    omega = omega + alpha * dt
    theta = theta + omega * dt
    bob.pos = vec(L * sin(theta), -L * cos(theta), 0)
    string.axis = bob.pos - ceiling.pos
    angle_curve.plot(t, theta)
    label_data.text = f'Time: {round(t,2)}s\nAngle: {round(degrees(theta),1)}°'
    t = t + dt
