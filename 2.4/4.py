# Суммарная сумма

def main() -> None:
    n = int(input())
    sum_of_digits = 0

    for i in range(n):
        number = int(input())
        while number:
            sum_of_digits += number % 10
            number //= 10
    print(sum_of_digits)



if __name__ == '__main__':
    main()