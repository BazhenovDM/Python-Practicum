# А роза упала на лапу Азора 4.0

def main() -> None:
    answer = input()
    print("YES" if answer == answer[::-1] else "NO", end="")

if __name__ == '__main__':
    main()