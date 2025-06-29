# Зайка — 7

def main() -> None:
    for i in range(int(input())):
        answer = input()
        print(answer.find("зайка") + 1 if "зайка" in answer else "Заек нет =(")


if __name__ == '__main__':
    main()