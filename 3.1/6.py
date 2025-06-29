# Зайка — 6

def main() -> None:
    count = 0
    for i in range(int(input())):
        count += input().count("зайка")
    print(count)

if __name__ == '__main__':
    main()