import math
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

xdata = []
ydata = []
V = 60
N = 0.5

def car1():
    V0 = V / 3.6
    Stotal = (V0 ** 2) / (2 * N * 9.8)
    a = -(V0 ** 2) / (2 * Stotal)
    t = -V0 / a
    def car_move(V0, time):
        x0 = V0 * time
        x = x0 - 75
        y = 0
        return x, y, t, a, Stotal
    

def car2():
    fig, ax = plt.subplots()
    ax.set_xlim(0, 5)
    ax.set_ylim(-2, 2)

    line, = ax.plot([], [], lw=2)

    global a, V0

    t = np.linspace(0, 5, 100)
    x = V0 * t + 0.5 * a * t ** 2 

    def init():
        line.set_data([], [])
        return line,

def animate(i):
    global line, t, x
    if (car1(V0, time=i)[0]) == 0:
        car2.set_data(car2(V0, time=i))
    if (car1(V0, time=i)[0]) < 0:
        xdata = t[:i]
        ydata = x[:i]
        line.set_data(xdata, ydata)
        return line,

if __name__ == '__main__':
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