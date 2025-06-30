import pytest
from commands import divide

def test_divide_positive_numbers():
    assert divide.run(10, 2) == 5

def test_divide_negative_numbers():
    assert divide.run(-9, -3) == 3

def test_divide_mixed_sign_numbers():
    assert divide.run(-12, 3) == -4

def test_divide_by_one():
    assert divide.run(5, 1) == 5

def test_divide_by_self():
    assert divide.run(7, 7) == 1

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide.run(10, 0)
