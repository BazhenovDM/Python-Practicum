# Числовой прямоугольник

def main() -> None:
    width, length = int(input()), int(input())
    counter = 0
    while counter != width * length:
        counter += 1
        print(f"{counter:>{len(str(width * length))}}", end=" ")
        if counter % length == 0:
            print("")


if __name__ == '__main__':
    main()
