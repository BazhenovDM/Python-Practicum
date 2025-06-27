# Зайка — 2

def main() -> None:
    first, second, third = input(), input(), input()
    rabbits = sorted(word + f" {len(word)}" for word in (first, second, third) if "зайка" in word)
    print(rabbits[0])

if __name__ == '__main__':
    main()