# Числовое фрагментирование
def fragments(numbers):
    if not numbers:
        return []

    result = []
    current = [numbers[0]]

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            current.append(numbers[i])
        else:
            result.append(current)
            current = [numbers[i]]

    result.append(current)
    return result
