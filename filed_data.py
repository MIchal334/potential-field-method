import point
import charg

negative_el_list = [charg.Charg(point.Point(0.5,0),-1),charg.Charg(point.Point(1.5,1),-1),charg.Charg(point.Point(-1,1),-1)]
positive_el_list = [charg.Charg(point.Point(-0.5,0),1),charg.Charg(point.Point(-1.5,1),1),charg.Charg(point.Point(0,1),1),charg.Charg(point.Point(0,1),1)]
# negative_el_list  = [charg.Charg(point.Point(0.5,0),-1)]
# positive_el_list = [charg.Charg(point.Point(-0.5,0),1)]

charg_list = negative_el_list + positive_el_list

x_range = 3
y_range = 3
squer_size = 0.2

def get_negative_el_list():
    return negative_el_list

def get_positive_el_list():
    return positive_el_list

def get_charg_list():
    return charg_list

def get_x_renge():
    return x_range

def get_y_renge():
    return y_range


def get_squer_size():
    return squer_size

