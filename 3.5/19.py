# Это будет наш секрет

def main() -> None:
    number = int(input())
    alphabet = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
    with open("public.txt", "r", encoding="UTF-8") as f:
        locker = f.read()

    result = ""

    for word in locker:
        if word.isalpha():
            if word.isupper():
                result += alphabet[(alphabet.index(word) + number) % 26]
            else:
                result += alphabet[(alphabet.index(word.upper()) + number) % 26].lower()
        else:
            result += word

    with open("private.txt", "w") as f:
        f.write(result)


if __name__ == '__main__':
    main()
