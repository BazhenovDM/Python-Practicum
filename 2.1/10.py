# Детский сад — штаны на лямках

child_name = input()
locker_number = int(input())

group_number = locker_number // 100
bed_number = locker_number // 10 % 10
child_number = locker_number % 10

message = f"""Группа №{group_number}.
{child_number}. {child_name}.
Шкафчик: {locker_number}.
Кроватка: {bed_number}."""

print(message)
