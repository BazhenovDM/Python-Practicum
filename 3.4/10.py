# Мы делили апельсин 2.0
from itertools import product


def main() -> None:
    print("А Б В")
    for a, b, c in product(range(1, (n := int(input())) + 1), repeat=3):
        print(a, b, c) if a + b + c == n else ...


if __name__ == '__main__':
    main()
