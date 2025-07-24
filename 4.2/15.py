# Повторюшка

def get_repeater(func, count):
    def repeated(x):
        for _ in range(count):
            x = func(x)
        return x
    return repeated