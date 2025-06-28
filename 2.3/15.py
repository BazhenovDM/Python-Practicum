# Зайка - 4

def main() -> None:
    n = int(input())
    count = 0
    for i in range(n):
        count = count + 1 if "зайка" in input() else count
    print(count)


if __name__ == '__main__':
    main()