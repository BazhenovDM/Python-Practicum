# Красота спасёт мир

def main() -> None:
    number = input()
    if (a := int("".join(sorted(number)))) // 100 + a % 10 == a // 10 % 10 * 2:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()