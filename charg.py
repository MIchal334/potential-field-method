import point

class Charg:
    point = point.Point(0,0)
    is_positive = 1

    def __init__(self, point, positive):
        self.point = point
        self.is_positive = positive
