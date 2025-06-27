# Интересное сложение

first_number, second_number = int(input()), int(input())

hundreds = (first_number // 100 + second_number // 100) % 10
dozens = (first_number // 10 + second_number // 10) % 10
units = (first_number + second_number) % 10
result = hundreds * 100 + dozens * 10 + units

print(result)