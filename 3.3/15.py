# Буквенная статистика

def main() -> None:
    {i: j for i, j in sorted([(k.lower(), text.lower().count(k.lower())) for k in sorted(text) if k.isalpha()])}


if __name__ == '__main__':
    main()