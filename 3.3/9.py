# Преобразование в строку

def main() -> None:
    " - ".join([str(j) for j in sorted({i for i in numbers})])


if __name__ == '__main__':
    main()
