# Кашееды - 2

def main() -> None:
    n, m = int(input()), int(input())
    result = set()

    for i in range(n + m):
        answer = input()
        if answer in result:
            result.remove(answer)
        else:
            result.add(answer)

    print(len(result) if result else "Таких нет")


if __name__ == '__main__':
    main()