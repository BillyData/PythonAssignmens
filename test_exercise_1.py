# filename : test_exercise_1.py

import pytest
from lab3 import binary_search


def test_binary_search():
    assert binary_search(10) == 4
    assert binary_search(4) == 2
    assert binary_search(8) == 3
