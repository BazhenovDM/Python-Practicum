name = input()
price = int(input())
weight = int(input())
money = int(input())
cost = weight * price
print(f'{'Чек':=^35}')
print(f'Товар:{name:>29}')
s = f'{weight}кг * {price}руб/кг'
print(f'Цена:{s:>30}')
print(f'Итого:{cost:>26}руб')
print(f'Внесено:{money:>24}руб')
print(f'Сдача:{money - cost:>26}руб')
print('=' * 35)

