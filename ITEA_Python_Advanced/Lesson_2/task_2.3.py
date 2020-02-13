class Points:

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_z(self):
        return self._z

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def set_z(self, z):
        self._z = z

    def __add__(self, obj):
        return Points(self.get_x() + obj.get_x(),
                      self.get_y() + obj.get_y(),
                      self.get_z() + obj.get_z())

    def __sub__(self, obj):
        return Points(self.get_x() - obj.get_x(),
                      self.get_y() - obj.get_y(),
                      self.get_z() - obj.get_z())

    def __mul__(self, obj):
        return Points(self.get_x() * obj.get_x(),
                      self.get_y() * obj.get_y(),
                      self.get_z() * obj.get_z())

    def __truediv__(self, obj):
        return Points(self.get_x() / obj.get_x(),
                      self.get_y() / obj.get_y(),
                      self.get_z() / obj.get_z())


point_1 = Points(1, 2, 3)
point_2 = Points(1, 2, 3)
point_3 = point_1 * point_2

print(point_3.get_x())
print(point_3.get_y())
print(point_3.get_z())
