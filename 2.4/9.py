#

def main() -> None:
    result = 0
    for i in range(n := int(input())):
        biggest_digit = 0
        number = int(input())
        while number:
            biggest_digit = max(biggest_digit, number % 10)
            number //= 10
        result += biggest_digit * 10 ** (n - i - 1)
    print(result)


if __name__ == '__main__':
    main()
