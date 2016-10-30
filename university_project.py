class PhysicImpact:
    def Collision(self, body):
        raise Exception('Not implemented exception')
    def Force(self, force):
        raise Exception('Not implemented exception')
    #...

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


    
#print(Body('ne').Name)
