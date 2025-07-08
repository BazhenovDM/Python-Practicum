# Шахматный «обед»

def can_eat(horse, other):
    return abs(horse[0] - other[0]) + abs(horse[1] - other[1]) == 3
