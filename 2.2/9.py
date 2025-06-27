# Первому игроку приготовиться

def main() -> None:
    first, second, third = input(), input(), input()
    if first < second and first < third:
        print(first)
    elif second < first and second < third:
        print(second)
    else:
        print(third)


if __name__ == '__main__':
    main()