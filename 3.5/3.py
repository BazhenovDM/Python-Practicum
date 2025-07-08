# Без комментариев 2.0
from sys import stdin


def main() -> None:
    locker = [line[0: line.find("#")] for line in stdin.readlines() if line[0] != "#"]
    print(*locker, sep="\n")


if __name__ == '__main__':
    main()
