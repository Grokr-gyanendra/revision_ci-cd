from main import add, sub, mul, div
import pytest

def test_add():
    assert add(10,2) == 12

def test_mul():
    assert mul(10, 2) == 20

def test_sub():
    assert sub(10, 2) == 8

def test_div():
    assert div(10, 2) == 5
    with pytest.raises(ValueError):
        div(10, 0)