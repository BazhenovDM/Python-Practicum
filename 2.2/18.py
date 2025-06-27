# Территория зла

def main() -> None:
    a, b, c = sorted(map(int, (input() for _ in range(3))))
    if c ** 2 == a ** 2 + b ** 2:
        print("100%")
    elif c ** 2 > a ** 2 + b ** 2:
        print("велика")
    else:
        print("крайне мала")


if __name__ == '__main__':
    main()
