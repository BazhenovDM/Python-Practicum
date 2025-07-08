# A+B+...
from sys import stdin


def main() -> None:
    print(sum([int(number) for line in stdin.readlines() for number in line.rstrip("\n").split()]))


if __name__ == '__main__':
    main()
