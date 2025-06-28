# Числовая змейка

def main() -> None:
    width, length = int(input()), int(input())
    flag = True
    for i in range(0, width):
        if flag:
            for j in range(1, length + 1):
                print(f"{j + length * i:>{len(str(width * length))}}", end=" ")
        else:
            for j in range(length, 0, -1):
                print(f"{j + length * i:>{len(str(width * length))}}", end=" ")
        flag = not flag
        print("")


if __name__ == '__main__':
    main()
