# НОД

def main() -> None:
    a, b = map(int, (input() for _ in range(2)))
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    print(a)

if __name__ == '__main__':
    main()