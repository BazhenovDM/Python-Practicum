# Массовое возведение в степень 2.0

def main() -> None:
    locker = map(int, input().split())
    power = int(input())
    print(*[i ** power for i in locker])

if __name__ == '__main__':
    main()
