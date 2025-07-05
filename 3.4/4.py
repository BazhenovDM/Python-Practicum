# Словарная ёлка

def main() -> None:
    answer = input().split()
    for i in range(len(answer)):
        print(*answer[:i + 1], sep=" ")

if __name__ == '__main__':
    main()