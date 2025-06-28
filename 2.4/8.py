# Максимальная сумма

def main() -> None:
    max_sum, winner_name = 0, ""
    for i in range(int(input())):
        name, number = input(), int(input())
        sum_of_digits = 0
        while number:
            sum_of_digits += number % 10
            number //= 10
        if max_sum <= sum_of_digits:
            max_sum = sum_of_digits
            winner_name = name
    print(winner_name)


if __name__ == '__main__':
    main()
