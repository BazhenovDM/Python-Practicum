# Накопление результата

def result_accumulator(func):
    locker = []

    def wrapper(*args, **kwargs):
        nonlocal locker
        if "method" in kwargs.keys():
            if kwargs["method"] == "accumulate":
                del kwargs["method"]
                locker.append(func(*args, **kwargs))
                return None
            elif kwargs["method"] == "drop":
                del kwargs["method"]
                locker.append(func(*args, **kwargs))
                drop = locker[:]
                locker.clear()
                return drop
        else:
            locker.append(func(*args, **kwargs))
            return None

    return wrapper
