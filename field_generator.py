import matplotlib.pyplot as plt
import numpy as np
import point


def generate_field():
    x_range = 4
    y_range = 4
    squer_size = 0.2
    step = squer_size / 2

    plt.ylim(-y_range, y_range)
    plt.xlim(-x_range, x_range)

    x_points = np.arange(-x_range + step , x_range , 2*step)
    y_points = np.arange(-y_range + step , y_range , 2*step)

    for x_p in x_points:
        for y_p in y_points:
            plt.plot(x_p, y_p, 'bo')

    plt.show()
