# Частотный анализ на минималках

def main() -> None:
    max_value, letter = 0, ""
    letter_lock = ""
    while (answer := input()) != "ФИНИШ":
        letter_lock += answer.lower()
    for i in letter_lock:
        if max_value < letter_lock.count(i):
            max_value = letter_lock.count(i)
            letter = i
    print(letter)

if __name__ == '__main__':
    main()