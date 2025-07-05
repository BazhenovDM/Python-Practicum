# Меню питания 2.0
from itertools import cycle


def main() -> None:
    locker = []
    for i in range(int(input())):
        locker.append(input())
    limit = int(input())
    temp = []
    for i in cycle(locker):
        if len(temp) < limit:
            print(i)
            temp.append(i)
        else:
            break


if __name__ == '__main__':
    main()
