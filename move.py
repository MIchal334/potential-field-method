
from time import sleep
import point
import random
import filed_data
import vector_calculating
import matplotlib.pyplot as plt
import field_generator
import numpy as np

class move_generator:
    __destination_point = point.Point(0,0)
    __current_position = point.Point(0,0)
    __err =0.2
    def __init__(self):
        # __x_c = 2*filed_data.get_x_renge()*random.random() - filed_data.get_x_renge()
        # __y_c = 2*filed_data.get_y_renge()*random.random() - filed_data.get_y_renge()
        __x_c = 0
        __y_c = 2.5
        self.__current_position = point.Point(__x_c,__y_c)
        self.__destination_point = filed_data.get_destination_point()
    


    def move(self):
        
        while True:
    
            dif = vector_calculating.calculate_vector(self.__current_position)
            self.__current_position.update_by_vector(dif)
            plt.plot(self.__current_position.X, self.__current_position.Y, 'go')
            field_generator.generate_field()
            filed_data.update_additiona_positive_list(self.__current_position.X, self.__current_position.Y)
            
            if (abs(self.__current_position.X - self.__destination_point.X) < self.__err and abs(self.__current_position.Y - self.__destination_point.Y) < self.__err):
                break




    