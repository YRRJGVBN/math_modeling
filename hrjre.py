import numpy as np
import matplotlib.pyplot as plt
	
def parabola_plotter(k = 0):
 
    x = np.arange(-10, 10, 0.01)
    y = k * x
 
    plt.plot(x, y)
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.savefig('fig_3.png')
if __name__ == '__main__':
	parabola_plotter()

