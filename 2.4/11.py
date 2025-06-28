# Простая задача 3.0

def main() -> None:
    count = 0
    for i in range(int(input())):
        number = int(input())
        for j in range(2, int(number ** 0.5) + 1):
            if number % j == 0:
                break
        else:
            count += 1 if number > 1 else 0
    print(count)

if __name__ == '__main__':
    main()
