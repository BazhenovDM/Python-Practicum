# Цифровая сумма

def main() -> None:
    number = int(input())
    sum_of_digits = 0
    while number > 0:
        sum_of_digits += number % 10
        number = number // 10
    print(sum_of_digits)


if __name__ == '__main__':
    main()