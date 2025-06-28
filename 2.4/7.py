# На старт! Внимание! Марш!

def main() -> None:
    for i in range(1, n := int(input()) + 1):
        for j in range(i + 2, 0, -1):
            print(f"До старта {j} секунд(ы)")
        print(F"Старт {i}!!!")

if __name__ == '__main__':
    main()