# Дед Мороз и конфеты

N, M = int(input()), int(input())

candy_for_kids = M // N
candy_for_santa = M % N

print(candy_for_kids, candy_for_santa, sep="\n")