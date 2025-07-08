# Прятки

def main() -> None:
    with open("public.txt", "r") as file:
        for symbol in file.read():
            print(chr(ord(symbol) % 128), end="")


if __name__ == '__main__':
    main()
