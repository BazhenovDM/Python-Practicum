# Внимание! Акция!

def main() -> None:
    sum_of_prices = 0
    while (product_price := float(input())) != 0:
        sum_of_prices = sum_of_prices + product_price if product_price < 500 else sum_of_prices + 0.9 * product_price
    print(sum_of_prices)


if __name__ == '__main__':
    main()
