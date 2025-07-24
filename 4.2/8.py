# Странный рост

def grow(*args, **kwargs):
    locker = []
    for num in args:
        result = num
        for k, v in kwargs.items():
            if num % len(k) == 0:
                result += v
        locker.append(result)
    return tuple(locker)
