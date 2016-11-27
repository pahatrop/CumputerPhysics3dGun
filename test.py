from university_project import *
from matplotlib import pyplot as plt
import math

B = Body("test")
x0 = 0
y0 = 0
E = 1.0E3
m = 0.004
v0 = math.sqrt((2.0 * E) / m)
alpha = 45.0
k = 1.0E-5

x = x0
y = y0
t = 0
xn = []
yn = []
dt = 0.01
vx = v0*math.cos(alpha/180*math.pi)
vy = v0*math.sin(alpha/180*math.pi)
while(y > -0.01):
	v = B.GetVelocities_numerical_v(x, y, vx, vy, m, k, dt)
	x = x + (vx + v[0])/2*dt
	y = y + (vy + v[1])/2*dt
	vx = v[0]
	vy = v[1]
	if(y > -0.01):
		xn.append(x)
		yn.append(y)

plt.plot(xn, yn, label='numerical')
plt.legend()
plt.show()