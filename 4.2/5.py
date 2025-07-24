# Подготовка данных

def to_string(*args, sep: str = " ", end: str = "\n") -> str:
    return sep.join(map(str, args)) + end
