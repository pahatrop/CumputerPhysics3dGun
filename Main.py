from Physic import *
import math
import time
import bge

"""B = Body("test")
# Initial conditions:
x0 = 0
y0 = 0
E = 1.0E3
m = 0.4
alpha = 45.0
v_max = 50

v0 = math.sqrt((2.0 * E) / m)

x = x0
y = y0
t = 0
xn = []
yn = []
dt = 0.01
vx = v0*math.cos(alpha/180*math.pi)
vy = v0*math.sin(alpha/180*math.pi)
while(y > -0.01):
	v = B.GetVelocities(x, y, vx, vy, v_max, dt)
	x = x + (vx + v[0])/2*dt # Predictor-corrector.
	y = y + (vy + v[1])/2*dt
	vx = v[0]
	vy = v[1]
	if(y > -0.01):
		xn.append(x)
		yn.append(y)

plt.plot(xn, yn, label='numerical', marker='.', color='black', linewidth=0)
#plt.legend()
plt.savefig("test.png")"""


class Cannonball:
        def __init__(self):
                storage = bge.logic.globalDict
                if not "cannonball" in storage:
                        storage["cannonball"] = Body("Cannonball", 0.4)
                print(storage["test"])
                storage["test"] = storage["test"] + 1




















        
