a = f"{input():0>3}"
b = f"{input():0>3}"

c = str((int(a[0]) + int(b[0])) % 10) + str((int(a[1]) + int(b[1])) % 10) + str((int(a[2]) + int(b[2])) % 10) 
print(c)