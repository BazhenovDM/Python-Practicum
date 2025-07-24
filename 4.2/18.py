# Преобразование словаря


lambda x: ("".join([i.lower() for i in x[0] if i.isalpha()]), sum(x[1])) if isinstance(x[1], list) or isinstance(
    x[1], tuple) else ("".join([i.lower() for i in x[0] if i.isalpha()]), x[1])
