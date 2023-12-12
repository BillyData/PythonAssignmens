import math
import test_example


def exercise1():
    a = input("Input the first number : ")
    b = input("Input the second number : ")

    # print(is_int(a))
    # print(is_int(b))

    is_int(a)
    is_int(b)

    a = int(a)
    b = int(b)

    print(print_banner())
    print(sum2ints(a, b))
    print(mul2ints(a, b))
    s = str(div2ints(a, b))
    try:
        I = s.find(".")
        raise len(s) - I == 2
    except:
        print("The number rounded up does not have 2 digits after decimal")
    return


def print_banner():
    print(f"Welcome to the awesome calculator")
    print(f"Please make sure to provide two integers as inputs")
    return


def sum2ints(first_num: int, second_num: int):
    return first_num + second_num


def mul2ints(first_num: int, second_num: int):
    return first_num * second_num


def div2ints(first_num: int, second_num: int):
    if (second_num == 0):
        raise "Cannot divide by 0"
    return round(first_num / second_num, 2)


def is_int(num):
    assert num.isdigit()


# exercise1()
