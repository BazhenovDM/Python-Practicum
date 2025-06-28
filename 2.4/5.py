# Зайка — 5

def main() -> None:
    count = 0
    is_new_route = True
    for i in range(int(input())):
        while (answer := input()) != "ВСЁ":
            if answer == "зайка" and is_new_route:
                count += 1
                is_new_route = False
        is_new_route = True
    print(count)



if __name__ == '__main__':
    main()