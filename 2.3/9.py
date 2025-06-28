# Факториал

def main() -> None:
    number = int(input())
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print(factorial)

if __name__ == '__main__':
    main()