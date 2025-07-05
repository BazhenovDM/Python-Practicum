# Сборы на прогулку

def main() -> None:
    print(*[f"{i} - {j}" for i, j in zip(input().split(", "), input().split(", "))], sep="\n")


if __name__ == '__main__':
    main()