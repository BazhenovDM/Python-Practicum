# Мы делили апельсин

def main() -> None:
    value = int(input())
    print("А Б В")
    for i in range(1, value - 1):
        for j in range(1, value - i):
            k = value - i - j
            if k >= 1:
                print(i, j, k)

if __name__ == '__main__':
    main()
