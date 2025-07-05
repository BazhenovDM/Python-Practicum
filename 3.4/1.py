# Автоматизация списка

def main() -> None:
    for ind, word in enumerate(input().split(), 1):
        print(f"{ind}. {word}")


if __name__ == '__main__':
    main()