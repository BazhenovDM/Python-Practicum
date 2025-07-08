# А роза упала на лапу Азора 7.0

def is_palindrome(x: str | int | tuple | list):
    if isinstance(x, int):
        return str(x) == str(x)[::-1]
    return x == x[::-1]
