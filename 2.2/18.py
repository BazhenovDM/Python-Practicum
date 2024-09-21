a = int(input())
b = int(input())
c = int(input())

d = sorted([a, b, c])
if d[-1] ** 2 > d[-2] ** 2 + d[-3] ** 2:
    print('велика')
elif d[-1] ** 2 < d[-2] ** 2 + d[-3] ** 2:
    print('крайне мала')
else:
    print('100%')