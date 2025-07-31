# Контроль параметров

def only_positive_even_sum(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError
    elif a <= 0 or a % 2 != 0 or b <= 0 or b % 2 != 0:
        raise ValueError
    return a + b
