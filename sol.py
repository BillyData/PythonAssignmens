import pytest

# Exercise 1.1


def perform_arithmetic_operations(num1, num2):
    try:
        addition = num1 + num2
        subtraction = num1 - num2
        multiplication = num1 * num2
        division = round(num1 / num2, 2)
        return addition, subtraction, multiplication, division
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero.")

# Test function for Exercise 1


def test_perform_arithmetic_operations():
    assert perform_arithmetic_operations(5, 2) == (7, 3, 10, 2.5)
    with pytest.raises(ValueError):
        perform_arithmetic_operations(5, 0)
