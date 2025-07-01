# Однофамильцы — 2

def main() -> None:
    locker = {}

    for i in range(int(input())):
        name = input()
        if name in locker:
            locker[name] += 1
        else:
            locker[name] = 1

    flag = False

    for key, value in sorted(locker.items()):
        if value > 1:
            print(f"{key} - {value}")
            flag = True

    print("Однофамильцев нет") if not flag else ...

if __name__ == '__main__':
    main()
