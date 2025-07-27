# Дроби v0.3

def nod(a: int, b: int):
    if a == 0:
        return b
    if b == 0:
        return a
    return nod(b, a % b)


class Fraction:

    def __init__(self, *args):
        args = (
            tuple(map(int, args[0].split("/")))
            if isinstance(args[0], str)
            else args
        )
        self.sign = 1 if args[0] * args[1] >= 0 else -1
        self.__num, self.__den = abs(args[0]), abs(args[1])
        self.__reduction()

    def __reduction(self):
        x = nod(self.__num, self.__den)
        self.__num //= x
        self.__den //= x

    def numerator(self, number=None):
        if number:
            self.__init__(self.sign * number, self.denominator())
        return abs(self.__num)

    def denominator(self, number=None):
        if number:
            self.__init__(self.sign * self.numerator(), number)
        return abs(self.__den)

    def __str__(self):
        return f"{self.sign * self.numerator()}/{self.denominator()}"

    def __repr__(self):
        return f"Fraction('{self.sign * self.numerator()}/{self.denominator()}')"

    def __neg__(self):
        return Fraction(self.numerator() * self.sign * -1, self.denominator())

    def __add__(self, other):
        num = self.sign * self.numerator() * other.denominator() + other.sign * other.numerator() * self.denominator()
        den = self.denominator() * other.denominator()
        return Fraction(num, den)

    def __iadd__(self, other):
        num = self.sign * self.numerator() * other.denominator() + other.sign * other.numerator() * self.denominator()
        den = self.denominator() * other.denominator()
        self.__init__(num, den)
        return self

    def __sub__(self, other):
        return self.__add__(-other)

    def __isub__(self, other):
        return self.__iadd__(-other)
