# Классный прямоугольник 2.0

class Rectangle:

    def __init__(self, first_angle: tuple, second_angle: tuple):
        self.x1 = min(first_angle[0], second_angle[0])
        self.x2 = max(first_angle[0], second_angle[0])
        self.y1 = max(first_angle[1], second_angle[1])
        self.y2 = min(first_angle[1], second_angle[1])
        self.length = self.x2 - self.x1
        self.width = self.y1 - self.y2

    def perimeter(self):
        return round(2 * (self.length + self.width), 2)

    def area(self):
        return round(self.length * self.width, 2)

    def get_pos(self):
        return round(self.x1, 2), round(self.y1, 2)

    def get_size(self):
        return round(self.length, 2), round(self.width, 2)

    def move(self, dx, dy):
        self.x1 += dx
        self.x2 += dx
        self.y1 += dy
        self.y2 += dy

    def resize(self, width, height):
        self.x2 = self.x1 + width
        self.y2 = self.y2 - height
        self.length = self.x2 - self.x1
        self.width = self.y1 - self.y2
