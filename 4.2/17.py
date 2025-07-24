# Фильтрация словаря

lambda x: isinstance(x[1], list) and len([i for i in x[1] if int(i) % 2 == 0]) > 0,
