# Транслитерация 2.0


def main() -> None:
    alphabet = {
        "А": "A",
        "Б": "B",
        "В": "V",
        "Г": "G",
        "Д": "D",
        "Е": "E",
        "Ё": "E",
        "Ж": "ZH",
        "З": "Z",
        "И": "I",
        "Й": "I",
        "К": "K",
        "Л": "L",
        "М": "M",
        "Н": "N",
        "О": "O",
        "П": "P",
        "Р": "R",
        "С": "S",
        "Т": "T",
        "У": "U",
        "Ф": "F",
        "Х": "KH",
        "Ц": "TC",
        "Ч": "CH",
        "Ш": "SH",
        "Щ": "SHCH",
        "Ы": "Y",
        "Э": "E",
        "Ю": "IU",
        "Я": "IA",
        "Ь": "",
        "Ъ": "",
    }
    with open("cyrillic.txt") as file:
        locker = list(file.read())

    result = ""
    for k, w in enumerate(locker):
        if w.isalpha() and w.upper() in alphabet:
            result += alphabet[w].capitalize() if w.isupper() else alphabet[w.upper()].lower()
            continue
        result += w

    with open("transliteration.txt", mode="w") as file:
        file.write(result)


if __name__ == '__main__':
    main()
