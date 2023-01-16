
from cmath import sqrt
from time import sleep
import point
import random
import filed_data
import vector_calculating
import matplotlib.pyplot as plt
import field_generator
import numpy as np
import math
import zero_potential_finder as checker

class move_generator:
    __destination_point = point.Point(0,0)
    __current_position = point.Point(0,0)
    __err =0.15
    def __init__(self):
        # __x_c = 2*filed_data.get_x_renge()*random.random() - filed_data.get_x_renge()
        # __y_c = 2*filed_data.get_y_renge()*random.random() - filed_data.get_y_renge()
        __x_c = 0
        __y_c = 2
        self.__current_position = point.Point(__x_c,__y_c)
        self.__destination_point = filed_data.get_destination_point()
    


    def move(self):

        while True:
            plt.plot(self.__current_position.X, self.__current_position.Y, 'go')
            dif = vector_calculating.calculate_vector(self.__current_position)
            self.__current_position.update_by_vector(dif)
            field_generator.generate_field()
            zero_potential_points = checker.check_filed(0.75,self.__current_position)
            print("ZNALEZIONO N PUNKOTOW N = ",len(zero_potential_points))
            for pt in zero_potential_points:
                filed_data.updata_additional_positive_list(pt)


            plt.draw()
            plt.pause(0.3)
            if (abs(self.__current_position.X - self.__destination_point.X) < self.__err and abs(self.__current_position.Y - self.__destination_point.Y) < self.__err):
                break




    