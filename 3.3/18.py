# Делители

def main() -> None:
    {k: [i for i in range(1, k + 1) if k % i == 0] for k in numbers}


if __name__ == '__main__':
    main()