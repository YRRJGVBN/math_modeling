import matplotlib.pyplot as plt
import numpy as np
def elips_plotter(a = float(input()), b = float(input()), r = float(input())):
    x = np.arange(-2 * r, 2 * r, 0.1)
    y = np.arange(-2 * r, 2 * r, 0.1)

    X, Y = np.meshgrid(x, y)
    fxy = (X ** 2) / (a ** 2) + (Y ** 2) / (b ** 2) - 1

    plt.contour(X, Y, fxy, levels=[0])
    plt.grid()
    plt.savefig('fig_10.png')

if __name__ == '__main__':
    elips_plotter()