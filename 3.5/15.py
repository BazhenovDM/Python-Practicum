# Поставь себя на моё место
import json
from sys import stdin


def main() -> None:
    locker = stdin.read().split()
    with open("scoring.json", "r") as f:
        data = json.load(f)

    sum_of_points = 0
    for group in data:
        count = 0
        for test in group["tests"]:
            if test["pattern"] in locker:
                count += 1
        sum_of_points += group["points"] * count // len(group["tests"])

    print(sum_of_points)


if __name__ == '__main__':
    main()
