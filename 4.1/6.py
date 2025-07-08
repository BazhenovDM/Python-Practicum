# Странная игра

__count = 0


def move(player, number):
    global __count
    __count += number if player == "Петя" else (-number)


def game_over():
    return "Петя" if __count > 0 else "Ваня" if __count < 0 else "Ничья"
