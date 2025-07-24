# Генератор Фибоначчи

def fibonacci(n):
    n_1, n_2 = 0, 1
    for i in range(n):
        yield n_1
        n_1, n_2 = n_2, n_1 + n_2