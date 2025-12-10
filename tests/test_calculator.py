import pytest
from src import calculator

def test_add():
    assert calculator.add(2, 3) == 5


def test_sub():
    assert calculator.sub(5, 2) == 3


def test_mul():
    assert calculator.mul(2, 3) == 6


def test_div():
    assert calculator.div(6, 3) == 2
    with pytest.raises(ZeroDivisionError):
        calculator.div(1, 0)
