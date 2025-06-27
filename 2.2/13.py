# Властелин Чисел: Братство общей цифры

def main() -> None:
    elves, dwarves, humans = map(int, (input() for _ in range(3)))
    if elves % 10 == dwarves % 10 == humans % 10:
        print(elves % 10)
    elif elves // 10 % 10 == dwarves // 10 % 10 == humans // 10 % 10:
        print(elves // 10 % 10)

if __name__ == '__main__':
    main()
