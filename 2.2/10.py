# Лучшая защита — шифрование

def main() -> None:
    password = int(input())

    first_half = password % 10 + password // 10 % 10
    second_half = password // 100 + password // 10 % 10

    print(str(first_half) + str(second_half) if first_half >= second_half else str(second_half) + str(first_half))


if __name__ == '__main__':
    main()
