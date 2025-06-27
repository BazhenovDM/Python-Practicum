# Чек

product_name = input()
price, weight, money = map(int, (input() for i in range(3)))
finale_price = price * weight
change = money - finale_price

message = f"""Чек\n{product_name} - {weight}кг - {price}руб/кг
Итого: {finale_price}руб\nВнесено: {money}руб\nСдача: {change}руб"""

print(message)
