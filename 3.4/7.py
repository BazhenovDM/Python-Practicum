# Игровая сетка
from itertools import combinations


def main() -> None:
    n = int(input())
    locker = []
    for i in range(n):
        locker.append(input())
    print(*[f"{i} - {j}" for i, j in combinations(locker, 2)], sep="\n")


if __name__ == '__main__':
    main()
