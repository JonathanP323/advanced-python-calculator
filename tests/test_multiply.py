import pytest
from commands import multiply

def test_multiply_positive_numbers():
    assert multiply.run(3, 4) == 12

def test_multiply_by_zero():
    assert multiply.run(0, 10) == 0
    assert multiply.run(5, 0) == 0

def test_multiply_negative_numbers():
    assert multiply.run(-2, -3) == 6

def test_multiply_mixed_sign_numbers():
    assert multiply.run(-2, 3) == -6
