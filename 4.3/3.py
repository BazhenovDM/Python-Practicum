# Многочлен N-ой степени

def make_equation(*args):
    if len(args) == 1:
        return args[0]
    return f"({make_equation(*args[:-1])}) * x + {args[-1]}"
