# Кто быстрее на этот раз?

def main() -> None:
    first, second, third = map(int, (input() for i in range(3)))

    if first > second and first > third:
        print("Петя")
    elif second > first and second > third:
        print("Вася")
    else:
        print("Толя")


if __name__ == '__main__':
    main()