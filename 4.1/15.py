# Словарная строка

def get_dict(text: str):
    return {k: v for k, v in [string.split("=") for string in text.split(";")]}
