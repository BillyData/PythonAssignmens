# filename: test_days_converter.py

import pytest
from days_converter import convert_days_to_years_weeks_days


def test_convert_days_to_years_weeks_days():
    # Test case 1: Valid input
    assert convert_days_to_years_weeks_days(
        1532) == "1532 days = 4 years + 10 weeks + 2 days."

    # Test case 2: Input is 0 days
    assert convert_days_to_years_weeks_days(
        0) == "0 days = 0 years + 0 weeks + 0 days."

    # Test case 3: Input is a negative number
    assert convert_days_to_years_weeks_days(
        -100) == "Error: Input must be a non-negative integer."

    # Test case 4: Input is a float
    assert convert_days_to_years_weeks_days(
        365.5) == "Error: Input must be a non-negative integer."


if __name__ == "__main__":
    pytest.main()
