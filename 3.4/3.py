# Рациональная считалочка
from itertools import count


def main() -> None:
    start, stop, step = map(float, input().split())
    for value in count(start, step):
        if value <= stop:
            print(f"{value:.2f}")
        else:
            break


if __name__ == '__main__':
    main()
