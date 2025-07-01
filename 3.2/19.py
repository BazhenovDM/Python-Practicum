# Частная собственность

def main() -> None:
    toys = {}

    for i in range(int(input())):
        answer = (input().split(": ")[1]).split(", ")
        for j in set(answer):
            if j in toys.keys():
                toys[j] += 1
            else:
                toys[j] = 1

    print(*(f"{toy}" for toy, count in sorted(toys.items()) if count == 1), sep="\n")

if __name__ == '__main__':
    main()
