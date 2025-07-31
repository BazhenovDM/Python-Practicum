# Слияние с проверкой

def merge(a, b):
    # Проверка 1: оба аргумента должны быть итерируемыми
    try:
        iter(a)
        iter(b)
    except TypeError:
        raise StopIteration("Один из аргументов не итерируем")

    # Проверка 2: элементы должны быть "однородны"
    a_types = {type(x) for x in a}
    b_types = {type(x) for x in b}
    if len(a_types | b_types) > 1:
        raise TypeError("Аргументы содержат неоднородные данные")

    # Проверка 3: оба аргумента должны быть отсортированы
    if any(a[i] > a[i + 1] for i in range(len(a) - 1)) or any(b[i] > b[i + 1] for i in range(len(b) - 1)):
        raise ValueError("Аргументы не отсортированы")

    # Слияние двух отсортированных итерируемых объектов
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
