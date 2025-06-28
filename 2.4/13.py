# Числовой прямоугольник 2.0

def main() -> None:
    width, length = int(input()), int(input())
    for i in range(1, width + 1):
        for j in range(0, length):
            print(f"{i + width * j:{len(str(width * length))}}", end=" ")
        print("")



if __name__ == '__main__':
    main()
