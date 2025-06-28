# Редизайн таблицы умножения

def main() -> None:
    number, width = int(input()), int(input())
    for i in range(1, number + 1):
        for j in range(1, number + 1):
            print(f" {i * j:^{width - 2}} ", end="|" if j != number else "\n")
        print("-" * (number * width + (number - 1)) if i != number else "")

if __name__ == '__main__':
    main()
