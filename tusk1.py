import matplotlib.pyplot as plt
import numpy as np
def zikl_plotter(R = 5):
    t = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
    x = R * (t - (np.sin(t)) ** 3)
    y = R * (t - (np.cos(t)) ** 3)
    plt.plot(x, y)
    plt.axis('equal')
    plt.savefig('fig_2.png')
if __name__ == '__main__':
    zikl_plotter() 