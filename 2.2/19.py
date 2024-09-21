x = float(input())
y = float(input())


def parab(x, y):
    if y <= 0:
        if y < (0.25 * (x ** 2)) + (0.5 * x) + 8.75:
            return False
    return True


def pram(x, y):
    if x <= 0 and y >= 0:
        if y < (5 / 3 * x + 35 / 3):
            return False
    return True


def red_cir(x, y):
    if x >= 0 and y >= 0:
        if (x) ** 2 + y ** 2 < 25:
            return False
    return True


def zel_cir(x, y):
    if (x) ** 2 + y ** 2 < 100:
        return True
    return False


def check_red(x, y):
    if y <= 0:
        if not (parab(x, y)):
            return True
        return False
    if x <= 0 and y >= 0:
        if not (pram(x, y)):
            return True
        return False
    if x >= 0 and y >= 0:
        if not (red_cir(x, y)):
            return True
        return False
    

if not (check_red(x, y)):
    if zel_cir(x, y):
        print('Зона безопасна. Продолжайте работу.')
    else:
        print('Вы вышли в море и рискуете быть съеденным акулой!')
else:
    print('Опасность! Покиньте зону как можно скорее!')