# Это будет шедевр!

def main() -> None:
    recipes = {}
    products = set()
    flag = False
    for i in range(int(input())):
        products.add(input())

    for j in range(int(input())):
        recipe, count = input(), int(input())
        recipes[recipe] = set(input() for _ in range(count))

    for key, value in sorted(recipes.items()):
        if products >= value:
            print(key)
            flag = True
    print("Готовить нечего") if not flag else ...


if __name__ == '__main__':
    main()
