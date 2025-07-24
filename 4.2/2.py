# Генератор матриц

def make_matrix(size: int | tuple, value: int = 0):
    if isinstance(size, tuple):
        a, b = size
    else:
        a = b = size
    return [[value for _ in range(a)] for _ in range(b)]
