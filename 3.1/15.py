# НОД 3.0

def main() -> None:
    locker = list(map(int, input().split()))
    first = locker.pop()
    for i in locker:
        second = i
        while first != second:
            if first > second:
                first -= second
            else:
                second -= first
        first = second
    print(first)

if __name__ == '__main__':
    main()
