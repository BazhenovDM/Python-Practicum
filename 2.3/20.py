# Хайпанём немножечко!

def main() -> None:
    n = int(input())
    prev = 0
    for i in range(n):
        b = int(input())
        m = b // (256 ** 2)
        r = (b // 256) % 256
        h = b % 256
        if h != 37 * (m + r + prev) % 256 or h >= 100:
            print(i)
            break
        prev = h
    else:
        print(-1)


if __name__ == '__main__':
    main()
