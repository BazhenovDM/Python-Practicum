# Наилучший выбор

def choice(*args, min=None, max=None):
    if min:
        locker = [min(i) for i in args]
        value = locker[0]
        for v in locker:
            if value > v:
                value = v
    elif max:
        locker = [max(i) for i in args]
        value = locker[0]
        for v in locker:
            if value < v:
                value = v
    return value