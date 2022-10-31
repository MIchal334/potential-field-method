class Point:
    X = 0
    Y = 0

    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def update_by_vector(self,dif):
        self.X = self.X + dif[0]
        self.Y = self.Y + dif[1]
