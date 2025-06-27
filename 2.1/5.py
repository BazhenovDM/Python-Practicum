# Магазин

price, weight, money = map(int, (input() for i in range(3)))

print(f"{money - price * weight:.0f}")