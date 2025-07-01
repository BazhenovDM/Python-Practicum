# Однофамильцы

def main() -> None:
    locker = {}

    for i in range(int(input())):
        name = input()
        if name in locker:
            locker[name] += 1
        else:
            locker[name] = 1

    count = 0

    for value in locker.values():
        if value > 1:
            count += value

    print(count)


if __name__ == '__main__':
    main()
