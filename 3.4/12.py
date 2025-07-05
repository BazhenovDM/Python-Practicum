# Список покупок 2.0
from itertools import chain


def main() -> None:
    n = int(input())
    for i, v in enumerate(sorted(chain(*[input().split(", ") for _ in range(n)])), 1):
        print(f"{i}. {v}")


if __name__ == '__main__':
    main()
