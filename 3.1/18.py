# RLE

def main() -> None:
    answer = input()
    first, count = answer[0], 1
    for i in answer[1:]:
        if first == i:
            count += 1
        else:
            print(first, count)
            count = 1
            first = i
    print(first, count)



if __name__ == '__main__':
    main()
