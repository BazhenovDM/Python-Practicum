# Зайка — 3

def main() -> None:
    count = 0
    while (answer := input()) != "Приехали!":
        count += 1 if "зайка" in answer else 0
    print(count)


if __name__ == '__main__':
    main()
