# Файловая разница

def main() -> None:
    name1, name2, name3 = (input() for _ in range(3))

    locker1, locker2 = set(), set()
    with open(name1) as f1:
        for line in f1.read().replace("\n", " ").split():
            locker1.add(line)

    with open(name2) as f2:
        for line in f2.read().replace("\n", " ").split():
            locker2.add(line)
    with open(name3, "w") as f3:
        f3.write("\n".join(sorted([i for i in locker1 ^ locker2])))


if __name__ == '__main__':
    main()
