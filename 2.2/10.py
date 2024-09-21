a = input()
b = int(a[-1]) + int(a[-2])
c = int(a[-3]) + int(a[-2])
print(str(max(b, c)) + str(min(b, c)))