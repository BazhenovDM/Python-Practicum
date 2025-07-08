# Файловая статистика 2.0
import json


def main() -> None:
    numbers = []
    with open(input(), "r") as file:
        for line in file:
            numbers.extend([int(x) for x in line.split()])
    locker = {
        "count": len(numbers),
        "positive_count": len([x for x in numbers if x > 0]),
        "min": min(numbers),
        "max": max(numbers),
        "sum": sum(numbers),
        "average": round(sum(numbers) / len(numbers), 2),
    }
    with open(input(), "w") as file:
        json.dump(locker, file, ensure_ascii=False)


if __name__ == '__main__':
    main()
