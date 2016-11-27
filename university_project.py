import math

class PhysicImpact:
    def Collision(self, body):
        raise Exception('Not implemented exception')
    def Force(self, force):
        raise Exception('Not implemented exception')
    g = 9.80665
    def GetVelocities_numerical_v(self, x0, y0, vx0, vy0, m, k, dt):
        # This function takes coordinates, velocities, mass, air drag coefficient at moment t
        # and returns velocities at the next moment (t + dt). 
        if(m < 0 or k < 0 or dt < 0):
            raise Exception("Wrong parameters")
        vx = vx0 - (k / m) * vx0 * dt
        vy = vy0 - (self.g + (k / m)*vy0)*dt
        return [vx, vy]

    def GetVelocities_numerical_v2(self, x0, y0, vx0, vy0, m, k, dt):
        # Same as previous function for F ~ v^2.
        if(m < 0 or k < 0 or dt < 0):
                raise Exception("Wrong parameters")
        v = math.sqrt(vx0*vx0 + vy0*vy0)
        vx = vx0 - (k / m) * v * vx0 * dt
        vy = vy0  + ( -self.g - (k / m) * v * vy0) * dt
        return [vx, vy]
    
    def GetCoordinates_analytical_v(self, x0, y0, E, m, alpha, k, t):
        # Initial coordinates, kinetical energy, mass, angle, air drag coefficient, time.
        # Function returns analytical solution for coordinates of body.
        if(E < 0 or m < 0 or alpha < 0 or alpha > 180 or k < 0 or t < 0):
            raise Exception("Wrong parameters")
        alpha = alpha / 180 * math.pi
        v = math.sqrt((2.0 * E) / m)
        vx0 = v * math.cos(alpha)
        vy0 = v * math.sin(alpha)
        if(k == 0): # No air drag.
                x = x0 + vx0*t
                y = y0 + vy0*t - self.g*t*t/2
                return [x, y]
        else: 
            x = (vx0*m/k)*(1-math.exp(-k/m*t))
            y = (m/k)*((vy0 + m*self.g/k) * (1 - math.exp(-k/m*t)) - self.g*t)
            return [x, y]

class Body(PhysicImpact):
    X = 0
    y = 0
    Width = 0
    Height = 0
    RVector = [0,0]
    Mass = 0
    #...
    def __init__(self, name):
        self.Name = name
        
class Scene:
    Bodies = []
    def __init__(self, name):
        self.Name = name

