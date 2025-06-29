# Без комментариев

def main() -> None:
    while (answer := input()):
        print(answer[:answer.index("#")] if "#" in answer else answer) if answer[0] != "#" else ...


if __name__ == '__main__':
    main()