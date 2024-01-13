import matplotlib.pyplot as plt
import numpy as np
def astr_plotter(R = 4):
    t = np.arange(-2 * np.pi, 2 * np.pi, 0.01)
    x = R * (np.cos(t) ** 3)
    y = R * (np.sin(t) ** 3)
    plt.plot(x, y)
    plt.axis('equal')
    plt.savefig('fig_3.png')
if __name__ == '__main__':
    astr_plotter() 