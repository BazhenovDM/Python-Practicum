# Средний рост
from sys import stdin


def main() -> None:
    locker = [int(param[2]) - int(param[1]) for param in [line.rstrip("\n").split() for line in stdin.readlines()]]
    print(round(sum(locker) / len(locker)))


if __name__ == '__main__':
    main()
