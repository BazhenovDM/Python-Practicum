# НОД 2.0

def main() -> None:
    n, first = int(input()), int(input())
    for i in range(n - 1):
        second = int(input())
        while first != second:
            if first > second:
                first -= second
            else:
                second -= first
        first = second
    print(first)


if __name__ == '__main__':
    main()
