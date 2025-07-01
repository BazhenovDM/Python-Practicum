# Зайка — 9

def main() -> None:
    locker = {}
    while (answer := input()):
        for i in answer.split():
            if i in locker:
                locker[i] += 1
            else:
                locker[i] = 1
    print(*(f"{key} {value}" for key, value in locker.items()), sep="\n")


if __name__ == '__main__':
    main()