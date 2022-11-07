
from time import sleep
import point
import random
import filed_data
import vector_calculating
import matplotlib.pyplot as plt
import field_generator
import numpy as np
import potential_switch as ps

class move_generator:
    __destination_point = point.Point(0,0)
    __current_position = point.Point(0,0)
    __err =0.15
    def __init__(self):
        # __x_c = 2*filed_data.get_x_renge()*random.random() - filed_data.get_x_renge()
        # __y_c = 2*filed_data.get_y_renge()*random.random() - filed_data.get_y_renge()
        __x_c = 0
        __y_c = 1.5
        self.__current_position = point.Point(__x_c,__y_c)
        self.__destination_point = filed_data.get_destination_point()
    


    def move(self):
        potential_on = True
        step_counter = 0 
        step_without_potential = 12
        # step_of_random_move = 2

        while True:
            plt.plot(self.__current_position.X, self.__current_position.Y, 'go')
            
            filed_data.update_last_position(self.__current_position)
            dif = vector_calculating.calculate_vector(self.__current_position)
            self.__current_position.update_by_vector(dif)
            field_generator.generate_field()
            
            if potential_on:
                potential_on = ps.check_last_pose(self.__current_position)
            else:
                step_counter = step_counter + 1

            # if step_counter >= 5  and  step_counter < 8: 
            #     random_dif = [filed_data.get_squer_size()*random.random(),filed_data.get_squer_size()*random.random()]
            #     self.__current_position.update_by_vector(random_dif)
            
            if step_counter ==  step_without_potential/2: 
                ps.turn_on_artifical_potential(self.__current_position)
 
            if step_counter > step_without_potential:
                ps.turn_off_artifical_potential()
                potential_on = ps.turn_on_nagtive_charg()
                step_counter = 0


            if (abs(self.__current_position.X - self.__destination_point.X) < self.__err and abs(self.__current_position.Y - self.__destination_point.Y) < self.__err):
                break




    