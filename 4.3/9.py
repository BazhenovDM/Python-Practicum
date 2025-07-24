# Циклический генератор

def cycle(locker: list):
    while True:
        for i in locker:
            yield i