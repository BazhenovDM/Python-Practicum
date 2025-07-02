# Максимальное произведение

def main() -> None:
    max(sorted(numbers)[-1] * sorted(numbers)[-2], sorted(numbers)[0] * sorted(numbers)[1])

if __name__ == '__main__':
    main()