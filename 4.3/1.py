# Рекурсивный сумматор

def recursive_sum(*args) -> int:
    args = list(args)
    if len(args) < 1:
        return 0
    return args.pop() + recursive_sum(*args)
