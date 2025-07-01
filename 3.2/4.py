# Кашееды

def main() -> None:
    n, m = int(input()), int(input())
    n_set, m_set = set(), set()

    for i in range(n):
        n_set.add(input())
    for j in range(m):
        m_set.add(input())

    print(len(n_set & m_set) if n_set & m_set else "Таких нет")


if __name__ == '__main__':
    main()