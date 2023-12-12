import math
import pytest


def exercise1():
    while (1):
        a = input("Input the first number : ")
        b = input("Input the second number : ")

        if (is_int(a) == False or is_int(b) == False):
            print("Please enter valid input")
            continue

        a = int(a)
        b = int(b)

        print_banner()
        print(sum2ints(a, b))
        print(mul2ints(a, b))
        s = div2ints(a, b)
        if (s == "Divided by 0, please enter a valid number" or s == "The number rounded up does not have 2 digits after decimal"):
            continue
        else:
            print(s)
        break


def print_banner():
    print(f"Welcome to the awesome calculator")
    print(f"Please make sure to provide two integers as inputs")


def sum2ints(first_num: int, second_num: int):
    assert str(first_num).isdigit() & str(second_num).isdigit()
    return first_num + second_num


def mul2ints(first_num: int, second_num: int):
    assert str(first_num).isdigit() & str(second_num).isdigit()
    return first_num * second_num


def div2ints(first_num: int, second_num: int):
    assert str(first_num).isdigit() & str(second_num).isdigit()
    try:
        first_num / second_num
    except ZeroDivisionError:
        print("Divided by 0, please enter a valid number")
        return "Divided by 0, please enter a valid number"
    result = str(round(first_num / second_num, 2))
    I = result.find(".")
    if len(result) - I - 1 != 2:
        print("The number rounded up does not have 2 digits after decimal")
        return "The number rounded up does not have 2 digits after decimal"
    else:
        return result


def is_int(num):
    assert num.isdigit()


def test_add():
    assert sum2ints(2, 3.6) == 5
    assert sum2ints(1, 0) == 1


def test_mul():
    assert mul2ints(1.1, 2.4)
    assert mul2ints(2, 4) == 8


def test_div():
    assert div2ints(1, 0)
    assert div2ints(1, 2)


exercise1()
