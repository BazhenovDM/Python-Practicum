# Кашееды — 4

def main() -> None:
    locker, result = {}, []

    for i in range(int(input())):
        answer = input().split()
        locker[answer[0]] = answer[1:]

    type_of_porridge = input()

    for key, value in locker.items():
        if type_of_porridge in value:
            result.append(key)

    if result:
        print(*sorted(result), sep="\n")
    else:
        print("Таких нет")


if __name__ == '__main__':
    main()
