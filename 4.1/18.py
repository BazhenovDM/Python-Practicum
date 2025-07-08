# Слияние

def merge(locker1: tuple, locker2: tuple):
    locker = list(locker1 + locker2)
    for i in range(len(locker)):
        for j in range(i, len(locker)):
            if locker[i] > locker[j]:
                locker[i], locker[j] = locker[j], locker[i]
    return tuple(locker)
