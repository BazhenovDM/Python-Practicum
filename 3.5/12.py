# Разделяй и властвуй

def main() -> None:
    with open(input(), "r") as file:
        locker = file.readlines()
    print(locker)
    even, odd, eq = "", "", ""

    for line in locker:
        for number in line.split():
            even_count = len([n for n in number if int(n) % 2 == 0])
            odd_count = len([n for n in number if int(n) % 2 != 0])
            if even_count > odd_count:
                even += number + " "
            elif even_count < odd_count:
                odd += number + " "
            else:
                eq += number + " "
        even, odd, eq = even + "\n", odd + "\n", eq + "\n"

    with open(input(), "w") as file1:
        file1.write(even)
    with open(input(), "w") as file1:
        file1.write(odd)
    with open(input(), "w") as file1:
        file1.write(eq)


if __name__ == '__main__':
    main()
