# А роза упала на лапу Азора 3.0

def main() -> None:
    count = 0
    for i in range(int(input())):
        number = int(input())
        reversed_number = 0
        while reversed_number < number:
            reversed_number = reversed_number * 10 + number % 10
            number //= 10
        count += 1 if reversed_number == number or reversed_number // 10 == number else 0
    print(count)


if __name__ == '__main__':
    main()
