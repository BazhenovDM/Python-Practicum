# Дроби v0.6


def nod(a: int, b: int):
    if a == 0:
        return b
    if b == 0:
        return a
    return nod(b, a % b)


class Fraction:
    def __init__(self, *args):
        args = (
            (args[0], 1)
            if len(args) == 1 and isinstance(args[0], int)
            else args
        )
        if isinstance(args[0], str):
            args = (
                tuple(map(int, args[0].split("/")))
                if "/" in args[0]
                else (int(args[0]), 1)
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

    def reverse(self):
        return Fraction(self.sign * self.denominator(), self.numerator())

    def __str__(self):
        return f"{self.sign * self.numerator()}/{self.denominator()}"

    def __repr__(self):
        return f"Fraction('{self.sign * self.numerator()}/{self.denominator()}')"

    def __neg__(self):
        return Fraction(self.numerator() * self.sign * -1, self.denominator())

    def __add__(self, other):
        other = Fraction(other) if type(other) is not Fraction else other
        num = (
                self.sign * self.numerator() * other.denominator()
                + other.sign * other.numerator() * self.denominator()
        )
        den = self.denominator() * other.denominator()
        return Fraction(num, den)

    def __iadd__(self, other):
        other = Fraction(other) if type(other) is not Fraction else other
        num = (
                self.sign * self.numerator() * other.denominator()
                + other.sign * other.numerator() * self.denominator()
        )
        den = self.denominator() * other.denominator()
        self.__init__(num, den)
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return self.__add__(-other)

    def __isub__(self, other):
        return self.__iadd__(-other)

    def __rsub__(self, other):
        return self.__neg__().__add__(other)

    def __mul__(self, other):
        other = Fraction(other) if type(other) is not Fraction else other
        num = self.sign * self.numerator() * other.sign * other.numerator()
        den = self.denominator() * other.denominator()
        return Fraction(num, den)

    def __imul__(self, other):
        other = Fraction(other) if type(other) is not Fraction else other
        num = self.sign * self.numerator() * other.sign * other.numerator()
        den = self.denominator() * other.denominator()
        self.__init__(num, den)
        return self

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        return self.__mul__(other.reverse())

    def __itruediv__(self, other):
        return self.__imul__(other.reverse())

    def __rtruediv__(self, other):
        return self.reverse().__mul__(other)

    def __eq__(self, other):
        other = Fraction(other) if type(other) is not Fraction else other
        num1, num2 = (
            self.sign * self.numerator() * other.denominator(),
            other.sign * other.numerator() * self.denominator(),
        )
        return num1 == num2

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        other = Fraction(other) if type(other) is not Fraction else other
        num1, num2 = (
            self.sign * self.numerator() * other.denominator(),
            other.sign * other.numerator() * self.denominator(),
        )
        return num1 < num2

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        return not self.__lt__(other) and not self.__eq__(other)

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)
