# Exercise 1.3


def is_leap_year(year):
    # Leap year logic: divisible by 4, but not divisible by 100 unless also divisible by 400
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def get_days_in_month(month, year):
    days_in_month = {
        "January": 31,
        "February": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31,
    }

    month = month.capitalize()
    if month in days_in_month:
        if month == "February" and is_leap_year(year):
            return 29
        else:
            return days_in_month[month]
    else:
        return "Invalid month"


user_month = input("Enter a month: ")
user_year = int(input("Enter a year: "))
result = get_days_in_month(user_month, user_year)
print(result)


def test_get_days_in_month():
    # Test case 1: Valid month with a non-leap year
    assert get_days_in_month("January", 2023) == 31

    # Test case 2: Valid month with a leap year
    assert get_days_in_month("February", 2024) == 29
