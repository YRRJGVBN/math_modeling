import matplotlib.pyplot as plt
import numpy as np
import math
def polar(b = 0.1):
    t = np.arange(0, math.pi * 8, 0.01)
    x = np.zeros(len(t))
    y = np.zeros(len(t))
    for i in range(len(t)):   
        r = math.e ** (b * t[i])
        x0 = math.cos(t[i]) * r
        x[i] = x0
        y0 = math.sin(t[i]) * r
        y[i] = y0
    plt.plot(x, y)
    plt.savefig('fig_11.png')
if __name__ == '__main__':
	polar()