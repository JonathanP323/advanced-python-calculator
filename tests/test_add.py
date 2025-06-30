import pytest
from commands import add

def test_add_positive_numbers():
    assert add.run(3, 5) == 8

def test_add_negative_numbers():
    assert add.run(-3, -2) == -5

def test_add_zero():
    assert add.run(0, 5) == 5
    assert add.run(5, 0) == 5

def test_add_mixed_sign_numbers():
    assert add.run(-3, 3) == 0
