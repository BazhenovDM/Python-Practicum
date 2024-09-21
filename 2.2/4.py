a = int(input())
b = int(input())
c = int(input())

if a > b and b > c: 
    print('1. Петя')
    print('2. Вася')
    print('3. Толя')
elif a > b and c > b and a > c:
    print('1. Петя')
    print('2. Толя')
    print('3. Вася')
elif b > a and a > c:
    print('1. Вася')
    print('2. Петя')
    print('3. Толя')
elif b > a and c > a and b > c:
    print('1. Вася')
    print('2. Толя')
    print('3. Петя')
elif c > b and b > a:
    print('1. Толя')
    print('2. Вася')
    print('3. Петя')
elif c > b and a > b and c > a:
    print('1. Толя')
    print('2. Петя')
    print('3. Вася')
