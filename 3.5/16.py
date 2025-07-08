# Найдётся всё 3.0
from sys import stdin


def main() -> None:
    flag = False
    request = input()
    locker = [name.rstrip("\n") for name in stdin.readlines()]
    for i in range(len(locker)):
        with open(locker[i]) as file:
            text = file.read().lower()
            while "  " in text or "\n" in file:
                text = text.replace("  ", " ").replace("\n", " ")
            if request.lower() in text:
                print(locker[i])
                flag = True
    if not flag:
        print("404. Not Found")


if __name__ == '__main__':
    main()
