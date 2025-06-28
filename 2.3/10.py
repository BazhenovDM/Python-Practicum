# Маршрут построен

def main() -> None:
    x, y = 0, 0
    while (route := input()) != "СТОП":
        coordinate = int(input())
        x = x + coordinate if route == "ВОСТОК" else x - coordinate if route == "ЗАПАД" else x + 0
        y = y + coordinate if route == "СЕВЕР" else y - coordinate if route == "ЮГ" else y + 0
    print(y, x, sep="\n")


if __name__ == '__main__':
    main()
