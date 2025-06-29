# Меню питания

def main() -> None:
    menu = ("Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая")
    print(*[*menu * (n := int(input()))][:n], sep="\n")


if __name__ == '__main__':
    main()
