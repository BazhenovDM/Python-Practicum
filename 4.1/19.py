# Обмен содержимым

def swap(a, b):
    a[:], b[:] = b[:], a[:]


a = b = [1, 2]
c = d = [2, 1]
print(a, b, c, d)
swap(a, c)
print(a, b, c, d)
