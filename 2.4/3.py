# Новогоднее настроение

def main() -> None:
    max_number = int(input())
    row, col, number = 1, 1, 1
    while number <= max_number:
        while col <= row and number <= max_number:
            print(number, end=" ")
            col += 1
            number += 1
        print("")
        col = 1
        row += 1


if __name__ == '__main__':
    main()
