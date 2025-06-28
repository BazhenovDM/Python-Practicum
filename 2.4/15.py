# Числовая змейка 2.0

def main() -> None:
    width, length = int(input()), int(input())
    flag = False
    for i in range(1, width + 1):
        for j in range(0, length):
            print(f"{(j + 1) * width - i + 1 if flag else i + j * width:>{len(str(width * length))}}", end=" ")
            flag = not flag
        flag = False
        print("")


if __name__ == '__main__':
    main()
