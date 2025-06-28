# Сильная цифра

def main() -> None:
    number = int(input())
    max_digit = - 10 ** 20
    while number > 0:
        max_digit = max(max_digit, number % 10)
        number = number // 10
    print(max_digit)


if __name__ == '__main__':
    main()