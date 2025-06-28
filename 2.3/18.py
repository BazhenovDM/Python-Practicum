# Простая задача 2.0

def main() -> None:
    number = int(input())
    while number:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                print(f"{i} * ", end="")
                number //= i
                break
        else:
            print(number, end="")
            break


if __name__ == '__main__':
    main()
