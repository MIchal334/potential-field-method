
import filed_data
import math

charg_list = filed_data.get_charg_list()
squer_size = filed_data.get_squer_size()
additiona_charges = filed_data.get_last_visited_list()
dictinary_of_point_potential = {} 


def calculate_vector(current_point):
    list_dif_x = []
    list_dif_y = []


    for chrges in charg_list:
        x_dif = (current_point.X - chrges.point.X)*chrges.is_positive
        y_dif = (current_point.Y - chrges.point.Y)*chrges.is_positive
        vector_norm = __calculate_vector_norm(x_dif,y_dif)
        if vector_norm == 0:
            x_direction = x_dif*(-1)
            y_direction = y_dif*(-1)
        else:
            x_direction = x_dif / vector_norm
            y_direction = y_dif / vector_norm
        force = __calculate_force_to_vector(vector_norm,chrges.is_positive)
        list_dif_x.append(x_direction*force)
        list_dif_y.append(y_direction*force)


    i = 0
    for chrges in filed_data.get_aditiona_positice():
        x_dif = (current_point.X - chrges.point.X)*chrges.is_positive
        y_dif = (current_point.Y - chrges.point.Y)*chrges.is_positive
        vector_norm = __calculate_vector_norm(x_dif,y_dif)
        if vector_norm == 0:
            x_direction = x_dif*(-1)
            y_direction = y_dif*(-1)
        else:
            x_direction = x_dif / vector_norm
            y_direction = y_dif / vector_norm
        force = __calculate_force_to_vector(vector_norm,chrges.is_positive)*(0.2+0.2*i)
        list_dif_x.append(x_direction*force)
        list_dif_y.append(y_direction*force)
        i = i + 1



    sum_x = sum(list_dif_x)
    sum_y = sum(list_dif_y)
    
    if(abs(sum_x) > squer_size ):
        sum_x = (abs(sum_x)/sum_x)* squer_size

    if(abs(sum_y) > squer_size ):
        sum_y = (abs(sum_y)/sum_y)* squer_size

    dif = [sum_x,sum_y]
    return dif



def __calculate_vector_norm(x_dif, y_dif):
    return math.sqrt(x_dif ** 2 + y_dif ** 2)



def __calculate_force_to_vector(vector_norm,is_positive):
    
    Q_plus = 0.2
    Q_minus = 5
    r = vector_norm

    if is_positive == -1:
        return Q_minus
    else:
        if r < 0.01:
            return 10000000
        return (Q_plus)/(r*r)
    


