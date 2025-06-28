# Раз, два, три! Ёлочка, гори!

def main() -> None:
    while (answer := input()) != "Три!":
        print("Режим ожидания...")
    print("Ёлочка, гори!")


if __name__ == '__main__':
    main()
