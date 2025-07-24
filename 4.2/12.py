# В эфире рубрика «Эксперименты»

locker = []


def enter_results(*args) -> None:
    cup = []
    for i in range(len(args)):
        if i % 2 == 0:
            cup = [args[i]]
        else:
            cup.append(args[i])
            locker.append(cup)
            cup = []


def get_sum() -> tuple:
    first, second = 0, 0
    for i, j in locker:
        first += i
        second += j
    return round(first, 2), round(second, 2)


def get_average() -> tuple:
    return round(get_sum()[0] / len(locker), 2), round(get_sum()[1] / len(locker), 2)
