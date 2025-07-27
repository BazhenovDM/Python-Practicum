# Дроби v0.1

def nod(a: int, b: int):
    if a == 0:
        return b
    if b == 0:
        return a
    return nod(b, a % b)


class Fraction:

    def __init__(self, *args):
        if len(args) == 1:
            self.num, self.den = map(int, args[0].split("/"))
        else:
            self.num, self.den = args[0], args[1]
        self.__reduction()

    def __reduction(self):
        x = nod(abs(self.num), abs(self.den))
        self.num //= x
        self.den //= x

    def numerator(self, number=None):
        if number is None:
            return abs(self.num)
        self.num = number
        self.__reduction()

    def denominator(self, number=None):
        if number is None:
            return abs(self.den)
        self.den = number
        self.__reduction()

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __repr__(self):
        return f"Fraction({self.num}, {self.den})"
