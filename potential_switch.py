import math
import filed_data
import charg
import random
import point

x_dif = 0
y_dif = 0
blocker_pose = 0

def __turn_off_nagtive_charg():
    nagative_charges = filed_data.get_negative_el_list()
    nagative_charges.clear()

def turn_on_nagtive_charg():
    nagative_charges = filed_data.get_negative_el_list()
    destination_point = filed_data.get_destination_point()
    if len(nagative_charges) == 0:
        nagative_charges.append(charg.Charg(destination_point,-1))
    return True

def turn_on_artifical_potential(pose_new_charge,sign):
    __turn_off_nagtive_charg()
    nagative_charges = filed_data.get_negative_el_list()
    nagative_charges.append(charg.Charg(pose_new_charge,sign))



def calculate_artifical_nagtive(currentPose):
        global blocker_pose
        destination_point = filed_data.get_destination_point()
        list_of_charge_pose = []

        if abs(blocker_pose.X - currentPose.X) > 0.3:
            degree_of_function = __calculate_parmter_of_linear_function(blocker_pose,currentPose)
            scale_of_function1 = currentPose.Y - (-1/degree_of_function)*currentPose.X
            scale_of_function2 = blocker_pose.Y - (-1/degree_of_function)*blocker_pose.X
          
            X = currentPose.X + 2*(random.random())*random.choice([-1,1])
            Y1 = (-1/degree_of_function)*X + scale_of_function1
            Y2 = (-1/degree_of_function)*X + scale_of_function2
            
        else:
            X = currentPose.X + 2*(random.random() +0.5)*random.choice([-1,1])
            Y1 = currentPose.Y
            Y2 = blocker_pose.Y

        list_of_charge_pose.append(point.Point(X,Y1))
        list_of_charge_pose.append(point.Point(X,Y2))

        return list_of_charge_pose





def turn_off_artifical_potential():
    __turn_off_nagtive_charg()

def check_last_pose(currentPose):
    global blocker_pose

    last_positions = filed_data.get_last_positions()
    potential_on = True
    for pose in last_positions:
        if math.sqrt((pose.X - currentPose.X)**2 + (pose.Y - currentPose.Y)**2) < 0.01:
            __turn_off_nagtive_charg()
            blocker_pose = point.Point(currentPose.X,currentPose.Y)
            x_dif = abs(pose.X - currentPose.X)
            y_dif = abs(pose.Y - currentPose.Y)
            potential_on = False
            break
    
    return potential_on


def __calculate_parmter_of_linear_function(P1,P2):
    return (P2.X - P1.X)/(P2.Y-P1.Y)


