# Властелин Чисел: Возвращение Цезаря


def main() -> None:
    a, b, c, d = sorted(map(int, input() + input()))
    number = d * 100 + (b + c) % 10 * 10 + a
    print(number)


if __name__ == '__main__':
    main()
