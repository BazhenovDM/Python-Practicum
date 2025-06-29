# Массовое возведение в степень

def main() -> None:
    locker = []

    for i in range(int(input())):
        locker.append(int(input()))

    power = int(input())
    for i in locker:
        print(i ** power)


if __name__ == '__main__':
    main()
