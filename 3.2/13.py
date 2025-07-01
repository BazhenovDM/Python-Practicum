# Дайте чего-нибудь новенького!

def main() -> None:
    today_food = set()
    week_food = set()
    for i in range(int(input())):
        today_food.add(input())

    for j in range(int(input())):
        for k in range(int(input())):
            week_food.add(input())

    print(*sorted(today_food ^ week_food), sep="\n") if today_food ^ week_food else print("Готовить нечего")


if __name__ == '__main__':
    main()
