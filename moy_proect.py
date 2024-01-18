import math
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def fizica_schitat(V, N):
    V0 = V / 3.6
    Stotal = (V0 ** 2) / (2 * N * 9.8)
    a = -(V0 ** 2) / (2 * Stotal)
    t = -V0 / a
    return Stotal, t, V0


def circle_move(R, vx0, time):
    x0 = vx0 * time
    alpha = np.arange(0, 2*np.pi, 0.1)
    x = x0  + R*np.cos(alpha) - 75
    y = R*np.sin(alpha)
    return x, y


def animate(i):
    global V0
    ball.set_data(circle_move(R=0, vx0=V0, time=i))


if __name__ == '__main__':
    xdata = []
    V = float(input())
    N = float(input())

    fig, ax = plt.subplots()
    ball, = plt.plot([], [], '>', color='r', label='Ball')
 
    edge = 70
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    Stotal = fizica_schitat(V, N)[0]

    ani = FuncAnimation(fig,
                        animate,
                        frames=np.arange(0, math.ceil(Stotal), 0.1),
                        interval=30
                       )
    plt.plot([0, 0], [-100, 100])
    plt.plot([-100, 100], [0, 0])
    plt.grid()
    ani.save('animation_3.gif') 