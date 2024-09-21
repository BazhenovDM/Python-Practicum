a = input()
b = input()
c = sorted(a + b)
d = c[-1] + str((int(c[-2]) + int(c[-3])) % 10) + c[-4]
print(d)