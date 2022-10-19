import math

import matplotlib.pyplot as plt
import numpy as np
import point
import charg

negative_el_list = [charg.Charg(point.Point(0.5,0),-1),charg.Charg(point.Point(1.5,1),-1),charg.Charg(point.Point(-1,1),-1)]
positive_el_list = [charg.Charg(point.Point(-0.5,0),1),charg.Charg(point.Point(-1.5,1),1),charg.Charg(point.Point(0,1),1),charg.Charg(point.Point(0,1),1)]
charg_list = negative_el_list + positive_el_list
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
        plt.plot(negative.point.X, negative.point.Y, 'bo')

    for positive in positive_el_list:
        plt.plot(positive.point.X, positive.point.Y, 'ro')


def __calculate_vector(destination_point):

    list_dif_x = []
    list_dif_y = []
    for chrges in charg_list:
        x_dif = (destination_point.X - chrges.point.X)*chrges.is_positive
        y_dif = (destination_point.Y - chrges.point.Y)*chrges.is_positive
        vector_norm = __calculate_vector_norm(x_dif,y_dif)
        x_direction = x_dif / vector_norm
        y_direction = y_dif / vector_norm
        force = __calculate_force_to_vector(vector_norm)
        list_dif_x.append(x_direction*force)
        list_dif_y.append(y_direction*force)
    
    dif = [sum(list_dif_x),sum(list_dif_y)]
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
    eps = 8.8
    Q = 1
    r = vector_norm
    return (1 * Q) / (4 * math.pi * eps * r)


def __calculate_distance_point_to_point(start_point, stop_point):
    return math.sqrt((stop_point.X - start_point.X) ** 2 + (stop_point.Y - start_point.Y) ** 2)


def __calculate_vector_norm(x_dif, y_dif):
    return math.sqrt(x_dif ** 2 + y_dif ** 2)
