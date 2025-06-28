# Считалочка 2.0

def main() -> None:
    start, end = int(input()), int(input())
    step = 1 if start < end else -1
    end = end + 1 if start < end else end - 1
    print(*[i for i in range(start, end, step)])

if __name__ == '__main__':
    main()