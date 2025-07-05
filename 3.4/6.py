# Колода карт
from itertools import product


def main() -> None:
    suit = ["пик", "треф", "бубен", "червей"]
    value = [i for i in range(2, 11)] + ["валет", "дама", "король", "туз"]
    answer = input()
    suit.remove(answer)
    for i in product(value, suit):
        print(*i, sep=" ")


if __name__ == '__main__':
    main()
