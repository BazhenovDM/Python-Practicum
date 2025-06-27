# Список победителей

def main() -> None:
    first, second, third = map(int, (input() for _ in range(3)))

    if first > second > third:
        print("1. Петя\n2. Вася\n3. Толя")
    elif first > third > second:
        print("1. Петя\n2. Толя\n3. Вася")
    elif second > first > third:
        print("1. Вася\n2. Петя\n3. Толя")
    elif second > third > first:
        print("1. Вася\n2. Толя\n3. Петя")
    elif third > first > second:
        print("1. Толя\n2. Петя\n3. Вася")
    else:
        print("1. Толя\n2. Вася\n3. Петя")


if __name__ == '__main__':
    main()
