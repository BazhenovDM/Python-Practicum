# Модернизация системы вывода

__phrases = []


def modern_print(text):
    if text not in __phrases:
        print(text)
        __phrases.append(text)
