import math
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

xdata = []
ydata = []
V = 60
N = 0.5

V0 = V / 3.6
Stotal = (V0 ** 2) / (2 * N * 9.8)
a = -(V0 ** 2) / (2 * Stotal)
t = -V0 / a


def circle_move(vx0, time):
    x0 = vx0 * time
    x = x0 - 75
    y = 0
    return x, y

def circle_move2(vx0, time, a, t):
    x0 = vx0 * time
    x = vx0 * t + (a * t ** 2) / 2
    y = 0
    return x, y

def animate(i):
    if (circle_move(vx0 = V0, time=i)[0])<= 0:
        ball.set_data(circle_move(vx0 = V0, time=i))
    else:
        ball2.set_data(circle_move2(vx0 = V0, time=i, a = a, t = t))

if __name__ == '__main__':
    print(circle_move(vx0 = V0, time=1)[0])
    fig, ax = plt.subplots()
    ball, = plt.plot([], [], '>', color='r', label='Ball')
    ball2, = plt.plot([], [], '>', color='r', label='Ball2')

    edge = 100
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)


    ani = FuncAnimation(fig,
                        animate,
                        frames=np.arange(0, math.ceil(Stotal), 0.1),
                        interval=30
                       )
    plt.plot([0, 0], [-100, 100])
    plt.plot([-150, 150], [0, 0])
    plt.grid()
    ani.save('animation_3.gif') 