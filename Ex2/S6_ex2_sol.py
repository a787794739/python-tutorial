import numpy as np
import matplotlib.pyplot as plt

"""
Below code does simulation of falling particles.
Insert missing code so that you get output similar to pyplot2.mp4.
"""

N = 100
P = np.random.rand(100,2)*0.8 + 0.1
S = np.random.randn(100,2)
g = np.array([0, -9.8])

# the space constraints
p_min = np.array([0.0, 0.0])
p_max = np.array([1.0, 1.0])

dt = 0.01

plt.ion()
while True:
    # check for collisions with the wall
    Out = (P + S * dt < p_min) | (p_max < P + S * dt);
    # update points speed on collison
    S[Out] = -S[Out] * 0.5
    # update point location
    P = P + S * dt
    # apply gravity to speed
    S = S + g * dt

    plt.clf()

    plt.scatter(P[:,0],P[:,1])
    plt.xlim(p_min[0]-0.1, p_max[0]+0.1)
    plt.ylim(p_min[0]-0.1, p_max[0]+0.1)
    plt.plot([0,0,1,1,0],[0,1,1,0,0])
    plt.show()

    plt.pause(0.001)