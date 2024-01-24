import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
def sloumotion():
    fig, ax = plt.subplots()
    ax.set_xlim(0, 5)
    ax.set_ylim(-2, 2)

    line, = ax.plot([], [], lw=2)

    v0 = 1
    a = -0.5
    
    t = np.linspace(0, 5, 100)
    x = v0 * t + 0.5 * a * t ** 2 

    def init():
        line.set_data([], [])
        return line,

    def animate(i):
        xdata = t[:i]
        ydata = x[:i]
        line.set_data(xdata, ydata)
        return line,

ani = animation.FuncAnimation(fig, animate, frames=len(t), init_func=init, blit=True)

ani.save('move.gif', writer='pillow', fps=10)