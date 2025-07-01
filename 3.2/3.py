# Зайка — 8

def main() -> None:
    places = set()
    for i in range(int(input())):
        places |= set(input().split())
    print(*(place for place in places), sep="\n")


if __name__ == '__main__':
    main()