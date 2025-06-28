# Первому игроку приготовиться 2.0

def main() -> None:
    n = int(input())
    min_value = "я" * 1000
    for i in range(n):
        name = input()
        min_value = min(min_value, name)
    print(min_value)




if __name__ == '__main__':
    main()