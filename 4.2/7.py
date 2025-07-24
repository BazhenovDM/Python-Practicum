# Подготовитель данных

def get_formatter(sep: str = " ", end: str = ""):
    return lambda *args: sep.join(map(str, args)) + end
