# Украшение чека

product_name = input()
price, weight, money = map(int, (input() for i in range(3)))

finale_price = price * weight
change = money - finale_price
finale_price_string_value = f"{weight}кг * {price}руб/кг"

message = f"""{"Чек":=^35}
Товар: {product_name:>28}
Цена: {finale_price_string_value:>29}
Итого: {finale_price:>25}руб
Внесено: {money:>23}руб
Сдача: {change:>25}руб
{"=" * 35}"""

print(message)