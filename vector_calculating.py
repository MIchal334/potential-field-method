
from http.client import IM_USED


import filed_data
import math

charg_list = filed_data.get_charg_list()
squer_size = filed_data.get_squer_size()


def calculate_vector(destination_point):
    list_dif_x = []
    list_dif_y = []
    for chrges in charg_list:
        x_dif = (destination_point.X - chrges.point.X)*chrges.is_positive
        y_dif = (destination_point.Y - chrges.point.Y)*chrges.is_positive
        vector_norm = __calculate_vector_norm(x_dif,y_dif)
        x_direction = x_dif / vector_norm
        y_direction = y_dif / vector_norm
        force = __calculate_force_to_vector(vector_norm,chrges.is_positive)
        list_dif_x.append(x_direction*force)
        list_dif_y.append(y_direction*force)


    sum_x = sum(list_dif_x)
    sum_y = sum(list_dif_y)
    
    if(abs(sum_x) > squer_size*0.6 ):
        sum_x = (abs(sum_x)/sum_x)* squer_size*0.6

    if(abs(sum_y) > squer_size*0.6 ):
        sum_y = (abs(sum_y)/sum_y)* squer_size*0.6

    dif = [sum_x,sum_y]
    return dif


def __calculate_vector_norm(x_dif, y_dif):
    return math.sqrt(x_dif ** 2 + y_dif ** 2)



def __calculate_force_to_vector(vector_norm,is_positive):
    if is_positive == -1:
    	return 0.5

    eps = 0.8
    Q = 1
    r = vector_norm
    return (1 * Q) / (4 * math.pi * eps * r)
