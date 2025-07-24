# Рекурсивный сумматор цифр

def recursive_digit_sum(digit: int) -> int:
    if digit < 10:
        return digit
    return digit % 10 + recursive_digit_sum(digit // 10)
