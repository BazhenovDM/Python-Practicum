# Простая задача

def main() -> None:
    number = int(input())
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print("NO")
            break
    else:
        print("YES" if number > 2 else "NO")

if __name__ == '__main__':
    main()