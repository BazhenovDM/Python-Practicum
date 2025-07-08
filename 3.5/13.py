# Обновление данных
import json
from sys import stdin


def main() -> None:
    file_name = input()
    locker = [line.rstrip("\n").split(" == ") for line in stdin.readlines()]
    with open(file_name, "r") as file:
        data = json.load(file)
    for k, v in locker:
        data[k] = v
    with open(file_name, "w") as file:
        json.dump(data, file, ensure_ascii=False)


if __name__ == '__main__':
    main()
