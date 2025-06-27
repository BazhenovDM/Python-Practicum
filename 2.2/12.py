# Музыкальный инструмент

def main() -> None:
    a, b, c = sorted(map(int, (input() for _ in range(3))))
    print("YES" if c < a + b else "NO")

if __name__ == '__main__':
    main()