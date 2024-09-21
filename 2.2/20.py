a = input()
b = input()
c = input()

d = sorted([a, b, c])
for i in d:
    if 'зайка' in i:
        print(i, len(i))
        break
