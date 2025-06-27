# Властелин Чисел: Две Башни

def main() -> None:
    number = int("".join(sorted(input())))
    str(number // 100)
    first_half = str(number // 100) + str(number // 10 % 10) if str(number // 100) != "0" else str(
        number // 10 % 10) + str(number // 100)
    second_half = str(number % 10) + str(number // 10 % 10)
    print(first_half, second_half)


if __name__ == '__main__':
    main()
