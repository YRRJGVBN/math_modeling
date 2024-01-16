import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
xdata = []
def circle_move(R, vx0, time):
    x0 = vx0 * time
    alpha = np.arange(0, 2*np.pi, 0.1)
    x = x0  + R*np.cos(alpha) -5
    y = R*np.sin(alpha)
    return x, y
def animate(i):
    ball.set_data(circle_move(R=0, vx0=0.1, time=i))
if __name__ == '__main__':
 
    fig, ax = plt.subplots()
    ball, = plt.plot([], [], 'o', color='r', label='Ball')
 
    edge = 10
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)
    
    ani = FuncAnimation(fig,
                        animate,
                        frames=100,
                        interval=30
                       )
    plt.plot([0, 0], [-10, 10])
    plt.plot([-100, 100], [0, 0])
    ani.save('animation_4.gif') 