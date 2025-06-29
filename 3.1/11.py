# Найдётся всё

def main() -> None:
    locker = []

    for i in range(n := int(input())):
        locker.append(input())

    answer = input().lower()
    for i in locker:
        if answer in i.lower():
            print(i)


if __name__ == '__main__':
    main()
