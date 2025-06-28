# НОК

def main() -> None:
    a, b = map(int, (input() for _ in range(2)))
    first_a, first_b = a, b
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    nok = abs(first_a * first_b) // a
    print(nok)

if __name__ == '__main__':
    main()