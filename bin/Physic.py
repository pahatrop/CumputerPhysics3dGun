import math

class PhysicImpact:
    def Collision(self, body):
        raise Exception('Not implemented exception')
    def Force(self, force):
        raise Exception('Not implemented exception')
    g = 9.80665
    # Analytical and F~v solution isn't required.
    """
    def GetVelocities_numerical_v(self, x0, y0, vx0, vy0, m, k, dt):
        # This function takes coordinates, velocities, mass, air drag coefficient at the moment t
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
    """
    def GetVelocities(self, v_max, dt):
    # Takes initial coordinates, initial velocities, terminal velocity (!) and time step.
    # Returns numerical solution for velocities of body at t+dt.
        if(dt < 0 or v_max < 0):
            raise Exception("Wrong parameters")
        v = math.sqrt(self.VX*self.VX + self.VY*self.VY)
        self.VX = self.VX - self.g*(v*self.VX/(v_max*v_max))*dt
        self.VY = self.VY  + ( -self.g*v*self.VY/(v_max*v_max) - self.g ) * dt
        return [self.VX, self.VY]
    
    def Move(self, x, y, z):
        self.Y = y
        self.X = x
        self.Z = z
    
class Body(PhysicImpact):
    X0 = 0
    Y0 = 0
    E = 1.0E3
    Z = 0
    X = 0
    Y = 0
    VX = 0
    VY = 0
    Width = 0
    Height = 0
    RVector = [0,0]
    Mass = 0
    Alpha = 0 # Regarding of the horison.
    VMax = 0
    V0 = 0
    #...
    def __init__(self, name, mass, alpha, x0, y0):
        self.Name = name
        self.Mass = mass
        self.V0 = math.sqrt((2.0 * self.E) / mass)
        self.Alpha = alpha
        self.X0 = x0
        self.Y0 = y0
        self.X = x0
        self.Y = y0
class Scene:
    Bodies = []
    def __init__(self, name):
        self.Name = name

