import math
import filed_data
import charg
import random
import point

x_dif = 0
y_dif = 0
x_blocker = 0
y_blocker = 0

def __turn_off_nagtive_charg():
    nagative_charges = filed_data.get_negative_el_list()
    nagative_charges.clear()

def turn_on_nagtive_charg():
    nagative_charges = filed_data.get_negative_el_list()
    destination_point = filed_data.get_destination_point()
    if len(nagative_charges) == 0:
        nagative_charges.append(charg.Charg(destination_point,-1))
    return True

def turn_on_artifical_potential(currentPose):
        destination_point = filed_data.get_destination_point()
        nagative_charges = filed_data.get_negative_el_list()
    
        if x_dif > y_dif:
               X = currentPose.X + (random.random() - 0.5) 
               Y = destination_point.Y + 2*(random.random() - 0.5)
        else:
               Y = currentPose.Y + (random.random() - 0.5) 
               X = destination_point.X + 2*(random.random() - 0.5)

     
        
        nagative_charges.append(charg.Charg(point.Point(X,Y),-1)) 

def turn_off_artifical_potential():
    __turn_off_nagtive_charg()

def check_last_pose(currentPose):
    last_positions = filed_data.get_last_positions()
    potential_on = True
    for pose in last_positions:
        if math.sqrt((pose.X - currentPose.X)**2 + (pose.Y - currentPose.Y)**2) < 0.01:
            __turn_off_nagtive_charg()
            x_dif = abs(pose.X - currentPose.X)
            y_dif = abs(pose.Y - currentPose.Y)
            potential_on = False
            break
    
    return potential_on