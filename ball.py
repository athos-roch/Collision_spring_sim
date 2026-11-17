import numpy as np


class Ball:
    
    def __init__(self, name, radius, mass, position, velocity, color):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.position = np.array(position)
        self.velocity = np.array(velocity)
        self.color = color
        
        
    
        