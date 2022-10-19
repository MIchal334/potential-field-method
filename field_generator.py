import matplotlib.pyplot as plt
import numpy as np
import point


def generate_field():
    ax = plt.gca()
    x_range = 2
    y_range = 2
    squer_size = 0.2
    step = squer_size / 2

    ax.set_xlim([-x_range, x_range])
    ax.set_ylim([-y_range, y_range])
    plt.ylim(-y_range, y_range)
    plt.xlim(-x_range, x_range)

    x_points = np.arange(-x_range + step, x_range, 2 * step)
    y_points = np.arange(-y_range + step, y_range, 2 * step)

    tempX = []
    tempY = []
    V = np.array([[0, 0]])
    origin = np.zeros((2, 1))

    for x_p in x_points:
        for y_p in y_points:
            X = x_p
            Y = y_p
            tempX = np.append(tempX, [X])
            tempY = np.append(tempY, [Y])
            dif_x = 0.1
            dif_y = 0.1
            a = np.array([[dif_x, dif_y]])
            V = np.concatenate((V, a), axis=0)

    origin = np.append(origin, (tempX, tempY), axis=1)

    plt.quiver(*origin, V[:, 0], V[:, 1], scale=3)
    plt.show()
