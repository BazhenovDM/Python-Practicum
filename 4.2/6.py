# Арифметический помощник

def get_operator(operator: str):
    match operator:
        case "+":
            return lambda a, b: a + b
        case "-":
            return lambda a, b: a - b
        case "*":
            return lambda a, b: a * b
        case "//":
            return lambda a, b: a // b
        case "**":
            return lambda a, b: a ** b
    return None
