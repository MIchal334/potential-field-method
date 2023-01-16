import math
import filed_data as fd
import numpy as np
import vector_calculating as vc
import point

step = 0.005

zero_potential = []
def check_filed(radius, central_point):
    x_points = np.arange(central_point.X - radius, central_point.X+radius ,  step)
    y_points = np.arange(central_point.Y - radius, central_point.Y+radius ,  step)
    print("ILE = ", len(x_points)*len(y_points))
    
    for i in x_points:
        for j in y_points:
            temp_point = point.Point(i,j)
            move_vector = vc.calculate_vector(temp_point)
            norm = math.sqrt(move_vector[0]**2 + move_vector[1]**2)
            if norm <= 0.005:
                zero_potential.append(temp_point)

    return zero_potential
