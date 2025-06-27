# А роза упала на лапу Азора

def main() -> None:
    number = int(input())
    print("YES" if number % 100 == number // 1000 + number // 100 % 10 * 10 else "NO")


if __name__ == '__main__':
    main()
