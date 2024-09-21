a = input()
a = sorted(a)
b = a[-1] + a[-2]
if a[0] != '0':
    c = a[0] + a[1]
else: 
    c = a[1] + a[0]
print(c, b)