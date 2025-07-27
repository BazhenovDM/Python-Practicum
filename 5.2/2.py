# Классная точка 4.0

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


class PatchedPoint(Point):

    def __init__(self, *args):
        if not args:
            super().__init__(0, 0)
        elif len(args) == 1:
            super().__init__(args[0][0], args[0][1])
        else:
            super().__init__(args[0], args[1])

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"PatchedPoint({self.x}, {self.y})"
