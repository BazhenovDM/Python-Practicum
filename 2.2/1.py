# Просто здравствуй, просто как дела

def main() -> None:
    name = input("Как Вас зовут? ")
    print(f"\nЗдравствуйте, {name}!")
    answer = input("Как дела? ")
    print("\nЯ за Вас рада!" if answer == "хорошо" else "\nВсё наладится!" if answer == "плохо" else None)

if __name__ == '__main__':
    main()