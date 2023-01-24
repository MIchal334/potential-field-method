
import filed_data
import math

charg_list = filed_data.get_charg_list()
squer_size = filed_data.get_squer_size()


def calculate_vector(current_point):
    list_dif_x = []
    list_dif_y = []
    forces = []
    charg_list = filed_data.get_charg_list()
    magnetic_list = filed_data.get_additional_list()
    
    for chrges in charg_list:
        x_dif = (current_point.X - chrges.point.X)*chrges.is_positive
        y_dif = (current_point.Y - chrges.point.Y)*chrges.is_positive
        vector_norm = __calculate_vector_norm(x_dif,y_dif)
        x_direction = x_dif / vector_norm
        y_direction = y_dif / vector_norm
        force = __calculate_force_to_vector(vector_norm,chrges.is_positive)
        forces.append(force)
        list_dif_x.append(x_direction*force)
        list_dif_y.append(y_direction*force)


    sum_x = sum(list_dif_x)
    sum_y = sum(list_dif_y)
    
    rotate = math.atan2(sum_y,sum_x)

    final_rotate = 0 

    for m in magnetic_list:
        final_rotate = final_rotate + rotate_vector(m.point,current_point)
    
    filne_angle = rotate + final_rotate
  

    if final_rotate != 0:
        sum_y = sum_x*math.tan(filne_angle)
        ## Trzeba przesklować przesunięcia

    sum_x_b = sum_x
    sum_y_b = sum_y

    if sum_y == 0:
        sum_y = 0.0001

    ratio_of_number_before = sum_x/sum_y
    
    if(abs(sum_x) > squer_size*0.6 ):
        sum_x = (abs(sum_x)/sum_x)* squer_size*0.6

    if(abs(sum_y) > squer_size*0.6 ):
        sum_y = (abs(sum_y)/sum_y)* squer_size*0.6

    ratio_of_number_after = sum_x/sum_y

    if abs(ratio_of_number_after) != abs(ratio_of_number_before):
        if abs(ratio_of_number_before) > 1:
            sum_y = sum_x * (sum_y_b/sum_x_b)
        else:
            sum_x = sum_y*(sum_x_b/sum_y_b)


    dif = [sum_x,sum_y]
    return dif


def __calculate_vector_norm(x_dif, y_dif):
    return math.sqrt(x_dif ** 2 + y_dif ** 2)



def __calculate_force_to_vector(vector_norm,is_positive):
    Q_plus = 0.1
    Q_minus = 2.5
    r = vector_norm

    if is_positive == -1:
        return Q_minus
    else:
        if r < 0.05:
            return 100
        return (Q_plus)/(r*r)
    

def rotate_vector(magnetic_charge,point):
    Vx = (magnetic_charge.X - point.X)
    Vy = (magnetic_charge.Y - point.Y)
    R = math.sqrt(Vx**2 + Vy**2)
    alfa = math.atan2(Vy,Vx)
    rotate = -0.5*math.cos(alfa)*(1/R)

    return rotate





