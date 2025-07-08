# Найдётся всё 2.0
from sys import stdin


def main() -> None:
    locker = [line.rstrip("\n") for line in stdin.readlines()]
    phrase = locker.pop()
    result = [line for line in locker if phrase.lower() in line.lower()]
    print(*result, sep="\n")


if __name__ == '__main__':
    main()
