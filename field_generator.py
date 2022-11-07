import math
from time import sleep

import matplotlib.pyplot as plt
import numpy as np
import point
import charg
import vector_calculating
import filed_data



negative_el_list = filed_data.get_negative_el_list()
positive_el_list = filed_data.get_positive_el_list()
additional_positive = filed_data.get_aditiona_positice()
charg_list = filed_data.get_charg_list()
x_range = filed_data.get_x_renge()
y_range = filed_data.get_y_renge()
squer_size = filed_data.get_squer_size()
step = filed_data.get_squer_size() / 2
ax = plt.gca()


def generate_field():
    ax.set_xlim([-x_range, x_range])
    ax.set_ylim([-y_range, y_range])
    plt.ylim(-y_range, y_range)
    plt.xlim(-x_range, x_range)

    x_points = np.arange(-x_range + step, x_range, 2 * step)
    y_points = np.arange(-y_range + step, y_range, 2 * step)

    __vector_field_generator(x_points, y_points)
    __draw_electric_charge()
    plt.draw()
    plt.pause(0.3)

def __draw_electric_charge():
    for negative in negative_el_list:
        plt.plot(negative.point.X, negative.point.Y, 'bo')

    for positive in positive_el_list:
        plt.plot(positive.point.X, positive.point.Y, 'ro')
    



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
            direction = vector_calculating.calculate_vector(point.Point(X, Y))
            dif_x = direction[0]
            dif_y = direction[1]
            a = np.array([[dif_x, dif_y]])
            V = np.concatenate((V, a), axis=0)


    origin = np.append(origin, (tempX, tempY), axis=1)
    plt.quiver(*origin, V[:, 0], V[:, 1], scale=8)

