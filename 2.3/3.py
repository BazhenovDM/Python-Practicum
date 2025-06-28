# Считалочка

def main() -> None:
    start, end = int(input()), int(input())
    print(*[i for i in range(start, end + 1)])


if __name__ == '__main__':
    main()
