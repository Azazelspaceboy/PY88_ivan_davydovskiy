class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle(Point):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.radius = radius

    def __sub__(self, other):
        sc = other.radius
        if self.radius - sc == 0:
            result = Point(self.x, self.y)
            return result
        elif self.radius - sc != 0:
            result = Circle(self.x, self.y, (self.radius - sc))
            return result


a = Circle(2, 4, 8)
b = Circle(2, 2, 8)
d = a.__sub__(b)
print(d.__dict__)
