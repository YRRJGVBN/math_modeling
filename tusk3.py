import matplotlib.pyplot as plt
import numpy as np
def elips_plotter(a = int(input()), b = int(input()), rx = int(input()), ry = int(input())):
    x = np.arange(-rx, rx, 0.01)
    y = np.arange(-ry, ry, 0.01)

    X, Y = np.meshgrid(x, y)
    fxy = (X ** 2) / (a ** 2) + (Y ** 2) / (b ** 2)

    plt.contour(X, Y, fxy, levels=[0])
    plt.savefig('fig_10.png')

if __name__ == '__main__':
    elips_plotter()