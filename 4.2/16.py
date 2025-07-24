# Обратная связь

def login(name, password, call1, call2):
    corr = hex(sum([ord(i) for i in name]) * len(name))
    if corr[2:].upper() == password[::-1]:
        call1(name)
    else:
        call2(name)
