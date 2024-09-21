name = input()
number = int(input())

group = number // 100
position = number % 10
bed = (number % 100) // 10

print(f'Группа №{group}.')
print(f'{position}. {name}.',)
print(f'Шкафчик: {number}.')
print(f'Кроватка: {bed}.')
