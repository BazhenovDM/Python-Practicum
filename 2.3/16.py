# А роза упала на лапу Азора 2.0

def main() -> None:
    number = int(input())
    reversed_num = 0
    while number > reversed_num:
        reversed_num = reversed_num * 10 + number % 10
        number //= 10
    print("YES" if (reversed_num == number) or (reversed_num // 10 == number) else "NO")


if __name__ == '__main__':
    main()
