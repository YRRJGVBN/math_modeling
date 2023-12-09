import matplotlib.pyplot as plt
import numpy as np
def giperbola_plotter(a = int(input()), N = float(input()), k = int(input())):
    x = np.arange(-a, a, N)
    y = k / x
    plt.plot(x, y)
    plt.savefig('fig_9.png')
if __name__ == '__main__':
	giperbola_plotter()