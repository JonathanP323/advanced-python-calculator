import pytest
from commands import subtract

def test_subtract_positive_numbers():
    assert subtract.run(10, 5) == 5

def test_subtract_negative_numbers():
    assert subtract.run(-3, -2) == -1

def test_subtract_zero():
    assert subtract.run(5, 0) == 5
    assert subtract.run(0, 5) == -5

def test_subtract_mixed_sign_numbers():
    assert subtract.run(-3, 3) == -6
