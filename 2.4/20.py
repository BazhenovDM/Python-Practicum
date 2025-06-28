# Математическая выгода

def main() -> None:
    number = int(input())
    max_value, max_system = 0, 10
    for i in range(2, 10 + 1):
        sum_of_digits, number_copy = 0, number
        while number_copy:
            sum_of_digits += number_copy % i
            number_copy //= i
        if sum_of_digits > max_value:
            max_value = sum_of_digits
            max_system = i
    print(max_system)


if __name__ == '__main__':
    main()
