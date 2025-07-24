# "Выпрямление" списка

def make_linear(locker: list) -> list:
    new_locker = []
    for el in locker:
        if not isinstance(el, list):
            new_locker.append(el)
        else:
            new_locker += make_linear(el)
    return new_locker
