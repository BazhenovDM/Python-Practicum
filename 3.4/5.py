# Список покупок
from itertools import chain


def main() -> None:
    for i, v in enumerate(sorted(chain(input().split(", "), input().split(", "), input().split(", "))), 1):
        print(f"{i}. {v}")


if __name__ == '__main__':
    main()
