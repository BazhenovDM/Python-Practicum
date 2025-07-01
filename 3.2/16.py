# Зайка — 10

def main() -> None:
    locker = set()
    while (answer := input()):
        string = answer.split()
        while string:
            if "зайка" in string and len(string) > 1:
                n = string.index("зайка")
                locker.add(string[n - 1]) if n - 1 > -1 else ...
                locker.add(string[n + 1]) if n + 1 < len(string) else ...
                string = string[n + 1:]
            else:
                break
    print(*locker, sep="\n")


if __name__ == '__main__':
    main()
