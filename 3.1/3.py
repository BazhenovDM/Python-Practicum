# Анонс новости

def main() -> None:
    length, n = int(input()), int(input())
    for i in range(n):
        answer = input()
        print(answer[:length - 3] + "..." if len(answer) > length else answer)

if __name__ == '__main__':
    main()