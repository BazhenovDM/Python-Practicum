# Азбука

def main() -> None:
    for i in range(int(input())):
        if input()[0] not in ("а", "б", "в"):
            print("NO")
            break
    else:
        print("YES")


if __name__ == '__main__':
    main()