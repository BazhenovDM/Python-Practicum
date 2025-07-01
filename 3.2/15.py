# Двоичная статистика!

def main() -> None:
    answer = list(map(int, input().split()))
    locker = list({
        "digits": 0,
        "units": 0,
        "zeros": 0
    } for _ in range(len(answer)))

    for i in range(len(answer)):
        bin_num = bin(answer[i])[2:]
        locker[i]["digits"] = len(bin_num)
        locker[i]["units"] = bin_num.count("1")
        locker[i]["zeros"] = bin_num.count("0")

    print(locker)



if __name__ == '__main__':
    main()
