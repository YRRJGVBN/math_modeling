import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
xdata = []
def circle_move(R, vx0, time):
    x0 = vx0 * time
    alpha = np.arange(0, 2*np.pi, 0.1)
    x = x0  + R*np.cos(alpha) - 10
    y = R*np.sin(alpha)
    return x, y
def animate(i):
    ball.set_data(circle_move(R=0, vx0=0.15, time=i))
if __name__ == '__main__':
 
    fig, ax = plt.subplots()
    ball, = plt.plot([], [], '>', color='r', label='Ball')
 
    edge = 70
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)
    
    ani = FuncAnimation(fig,
                        animate,
                        frames=100,
                        interval=30
                       )
    plt.plot([0, 0], [-100, 100])
    plt.plot([-100, 100], [0, 0])
    plt.grid()
    ani.save('animation_5.gif') 