# Классный прямоугольник

class Rectangle:

    def __init__(self, first_angle: tuple, second_angle: tuple):
        self.x1, self.x2 = first_angle[0], second_angle[0]
        self.y1, self.y2 = first_angle[1], second_angle[1]
        self.length = abs(self.x2 - self.x1)
        self.width = abs(self.y2 - self.y1)

    def perimeter(self):
        return round(2 * (self.length + self.width), 2)

    def area(self):
        return round(self.length * self.width, 2)
