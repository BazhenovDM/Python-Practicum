# Очистка данных

def main() -> None:
    while (answer := input()):
        if answer[-3:-1] != "@@":
            print(answer[2:] if answer[:2] == "##" else answer)

if __name__ == '__main__':
    main()