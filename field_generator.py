import math

import matplotlib.pyplot as plt
import numpy as np
import point

negative_el_list = [point.Point(0, 0)]
positive_el_list = []
ax = plt.gca()
x_range = 2
y_range = 2
squer_size = 0.2
step = squer_size / 2


def generate_field():
    ax.set_xlim([-x_range, x_range])
    ax.set_ylim([-y_range, y_range])
    plt.ylim(-y_range, y_range)
    plt.xlim(-x_range, x_range)

    x_points = np.arange(-x_range + step, x_range, 2 * step)
    y_points = np.arange(-y_range + step, y_range, 2 * step)

    __vector_field_generator(x_points, y_points)
    __draw_electric_charge()
    plt.show()


def __draw_electric_charge():
    for negative in negative_el_list:
        plt.plot(negative.X, negative.Y, 'bo')

    for positive in positive_el_list:
        plt.plot(positive.X, positive.Y, 'ro')


def __calculate_vector(destination_point):
    for negative in negative_el_list:
        x_dif = negative.X - destination_point.X
        y_dif = negative.Y - destination_point.Y
        vector_norm = __calculate_vector_norm(x_dif,y_dif)
        x_direction = x_dif / vector_norm
        y_direction = y_dif / vector_norm
        force = __calculate_force_to_vector(vector_norm)
        dif = [x_direction*force,y_direction*force]

    # for positive in positive_el_list:
    #     x_dif = destination_point.X - positive.X
    #     y_dif = destination_point.Y - positive.Y
    #     vector_norm = math.sqrt(x_dif * x_dif + y_dif * y_dif)
    #     direction = [x_dif / vector_norm, y_dif / vector_norm]

    return dif


def __vector_field_generator(x_points, y_points):
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
            direction = __calculate_vector(point.Point(X, Y))
            dif_x = 0.1 * direction[0]
            dif_y = 0.1 * direction[1]
            a = np.array([[dif_x, dif_y]])
            V = np.concatenate((V, a), axis=0)
    origin = np.append(origin, (tempX, tempY), axis=1)
    plt.quiver(*origin, V[:, 0], V[:, 1], scale=3)


def __calculate_force_to_vector(vector_norm):
    eps = 0.5
    Q = 1
    r = vector_norm
    return (1 * Q) / (4 * math.pi * eps * r)


def __calculate_distance_point_to_point(start_point, stop_point):
    return math.sqrt((stop_point.X - start_point.X) ** 2 + (stop_point.Y - start_point.Y) ** 2)


def __calculate_vector_norm(x_dif, y_dif):
    return math.sqrt(x_dif ** 2 + y_dif ** 2)
