import numpy as np
import json
from ball import Ball
from numpy.linalg import norm as nm
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Table:
    
    def __init__(self):
        
        self.balls = []
        self.positions = []
        
        with open('balls.json') as f:
            ball_params = json.load(f)
            
        self.iterations = ball_params["num_iterations"]
        self.timestep = ball_params["timestep"]
        self.k = ball_params["k"]
        
        for a in ball_params["balls"]:
            ball = Ball(a["name"], a["radius"], a["mass"], a["position"], a["velocity"], a["color"])
            ball.p = ball.mass * ball.velocity
            self.balls.append(ball)
            
        for i in self.balls:
            self.positions.append(i.position)
            
        print(f"Initial momentum of ball 1 is {self.balls[0].p}")
        print(f"Initial momentum of ball 2 is {self.balls[1].p}")
            
    
    def motion(self):
        
        self.all_pos = [[], []]
        
        ball1 = self.balls[0]
        ball2 = self.balls[1]
        
        self.all_pos[0].append(ball1.position.copy())
        self.all_pos[1].append(ball2.position.copy())
        
        rd = ball1.radius + ball2.radius
        
        force = np.zeros(2)
        
        
        for step in range(self.iterations):
            force = np.zeros(2)
            d = self.all_pos[0][step] - self.all_pos[1][step]
            
            
            if nm(d) <= nm(rd):
                direction = d/nm(d)
                force = self.k*(rd - nm(d))*direction
                
            ball1.p = ball1.p + force*self.timestep
            ball2.p = ball2.p - force*self.timestep
            
            ball1.velocity = ball1.p/ball1.mass
            ball2.velocity = ball2.p/ball2.mass
            
            ball1.position = ball1.position + ball1.p*self.timestep/ball1.mass
            ball2.position = ball2.position + ball2.p*self.timestep/ball2.mass
            
            self.all_pos[0].append(ball1.position.copy())
            self.all_pos[1].append(ball2.position.copy())
    
        print(f"Final momentum of ball 1 is {self.balls[0].p}")
        print(f"Final momentum of ball 2 is {self.balls[1].p}")
            
            
        
            

t = Table()
t.motion()

ball1_motion = np.array(t.all_pos[0])
ball2_motion = np.array(t.all_pos[1])

fig, ax = plt.subplots()

# Set the limits of the table
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)

ax.set_aspect("equal")

# Create the balls
ball1 = plt.Circle(
    ball1_motion[0],
    t.balls[0].radius,
    color=t.balls[0].color
)

ball2 = plt.Circle(
    ball2_motion[0],
    t.balls[1].radius,
    color=t.balls[1].color
)

ax.add_patch(ball1)
ax.add_patch(ball2)


def update(frame):

    ball1.center = ball1_motion[frame]
    ball2.center = ball2_motion[frame]

    return ball1, ball2


animation = FuncAnimation(
    fig,
    update,
    frames=range(0, len(ball1_motion), 10),
    interval=20,
    blit=True
)

plt.show()



              
                
                
                
                
            
                
                
    
    
            
              