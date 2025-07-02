# Обобщение

def main() -> None:
    {tuple(sorted([i, j])) for i in text.split() for j in text.split() if i != j and len(set(i) & set(j)) >= 3}


if __name__ == '__main__':
    main()