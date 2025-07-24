# Декор результата

def answer(func):
    def new_func(*args, **kwargs):
        return f"Результат функции: {func(*args, **kwargs)}"

    return new_func
