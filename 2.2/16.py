vl = int(input())
v2 = int(input())
v3 = int(input())
s = [vl, v2, v3]
vic = []
for i in range(3):
    if max(s) == vl:
        s.remove(vl)
        vic.append("Петя")
    elif max(s) == v2:
        s.remove(v2)
        vic.append("Вася")
    else:
        s.remove(v3)
        vic.append("Толя")
print(" " * 10 + f"{vic[0]}")
print(" " * 2 + f"{vic[1]}")
print(" " * 18 + f"{vic[2]}")
print(" " * 3 + "II" + ' ' * 6 + 'I' + " " * 6 + 'III')