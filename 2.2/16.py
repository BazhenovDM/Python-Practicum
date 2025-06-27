# Легенды велогонок возвращаются: кто быстрее?

def main() -> None:
    first, second, third = map(int, (input() for _ in range(3)))

    if first > second > third:
        print(f"{"Петя":^24}\n{"Вася":^8}\n{"Толя":>22}\n   II      I      III   ")
    elif first > third > second:
        print(f"{"Петя":^24}\n{"Толя":^8}\n{"Вася":>22}\n   II      I      III   ")
    elif second > first > third:
        print(f"{"Вася":^24}\n{"Петя":^8}\n{"Толя":>22}\n   II      I      III   ")
    elif second > third > first:
        print(f"{"Вася":^24}\n{"Толя":^8}\n{"Петя":>22}\n   II      I      III   ")
    elif third > second > first:
        print(f"{"Толя":^24}\n{"Вася":^8}\n{"Петя":>22}\n   II      I      III   ")
    else:
        print(f"{"Толя":^24}\n{"Петя":^8}\n{"Вася":>22}\n   II      I      III   ")


if __name__ == '__main__':
    main()
