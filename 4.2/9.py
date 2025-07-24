# Странное произведение

def product(*args, **kwargs):
    locker = []
    for name in args:
        result = 1
        flag = False
        for k, v in kwargs.items():
            if k in name:
                result *= v
                flag = True
        locker.append(result) if flag else ...
    return tuple(locker)