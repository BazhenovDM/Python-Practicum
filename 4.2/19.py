# Ключевой секрет

def secret_replace(text, **kwargs):
    txt = [i for i in text]
    for key, value in kwargs.items():
        count = 0
        for i in range(len(txt)):
            if txt[i] == key:
                txt[i] = value[count % len(value)]
                count += 1
    return "".join(txt)
