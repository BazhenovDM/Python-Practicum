# Цезарю — Цезарево

def roman(a, b):
    roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    def to_roman(n):
        result = ""
        for value, symbol in roman_map:
            while n >= value:
                result += symbol
                n -= value
        return result

    ra = to_roman(a)
    rb = to_roman(b)
    rs = to_roman(a + b)

    return f"{ra} + {rb} = {rs}"