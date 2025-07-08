# Поиск гор 2

def find_mountains(data):
    locker = []
    for i in range(1, len(data) - 1):
        for j in range(1, len(data[i]) - 1):
            f1 = data[i - 1][j - 1] < data[i][j] > data[i + 1][j + 1]
            f2 = data[i - 1][j] < data[i][j] > data[i + 1][j]
            f3 = data[i][j - 1] < data[i][j] > data[i][j + 1]
            f4 = data[i + 1][j - 1] < data[i][j] > data[i - 1][j + 1]
            if f1 and f2 and f3 and f4:
                locker.append((i + 1, j + 1))
    return tuple(locker)
