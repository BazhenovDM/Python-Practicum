# Классная точка 2.0

class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self, x: int, y: int):
        self.x += x
        self.y += y

    def length(self, other):
        x, y = other.x, other.y
        length = ((self.x - x) ** 2 + (self.y - y) ** 2) ** 0.5
        return round(length, 2)
