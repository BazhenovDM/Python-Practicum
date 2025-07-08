# А роза упала на лапу Азора 6.0
from sys import stdin


def main() -> None:
    data = stdin.read().replace("\n", " ").rstrip(" ").split(" ")
    locker = [w for w in data if w.lower() == w[::-1].lower()]
    print(*sorted(set(locker)), sep="\n")


if __name__ == '__main__':
    main()
