# Польский калькулятор

def main() -> None:
    answer = input().split()
    digit_stack = []
    for i in answer:
        if i.isdigit():
            digit_stack.append(int(i))
        elif i == "+":
            digit_stack.append(digit_stack.pop(-2) + digit_stack.pop(-1))
        elif i == "-":
            digit_stack.append(digit_stack.pop(-2) - digit_stack.pop(-1))
        elif i == "*":
            digit_stack.append(digit_stack.pop(-2) * digit_stack.pop(-1))
    print(*digit_stack)





if __name__ == '__main__':
    main()
