# Чётная чистота

def main():
    number = int(input())
    new_number, power = 0, 1
    while number:
        if number % 10 % 2 != 0:
            new_number += (number % 10) * power
            power *= 10
        number //= 10
    print(new_number)


if __name__ == '__main__':
    main()
