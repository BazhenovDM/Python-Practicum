# Хвост

def main() -> None:
    name, number = input(), int(input())
    with open(name) as file:
        print(*file.readlines()[-number:], sep="")


if __name__ == '__main__':
    main()
