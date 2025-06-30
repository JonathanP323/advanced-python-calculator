import pytest
from commands.divide import run

def test_divide_by_zero():
    with pytest.raises(ValueError):
        run(10, 0)

