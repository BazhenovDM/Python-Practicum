# Автоматизация игры

number = int(input())

a = number // 1000
b = number // 100 % 10
c = number // 10 % 10
d = number % 10
new_number = b * 1000 + a * 100 + d * 10 + c

print(new_number)

# Мерзкая, неэлегантная реализация, но просили мат. операциями, значит надо