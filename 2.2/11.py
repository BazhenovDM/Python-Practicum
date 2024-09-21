a = input()
a = sorted(a)
if int(a[0]) + int(a[2]) == int(a[1]) * 2:
    print('YES')
else:
    print('NO')