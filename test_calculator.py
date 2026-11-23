import pytest

from calculator import add, subtract, multiply, divide, power, square_root

# Basic and edge-case unit tests
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (-5, -5, -10),
    (2.5, 2.5, 5.0),
])

def test_addition(a, b, expected):
    assert add(a, b) == expected

def test_subtraction():
    assert subtract(10, 4) == 6
    assert subtract(4, 10) == -6

def test_multiplication():
    assert multiply(3, 4) == 12
    assert multiply(5, 0) == 0
    assert multiply(-2, 3) == -6

def test_division():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5

def test_division_by_zero():
    with pytest.raises(ValueError, match="Division by zero is not possible"):
        divide(10, 0)

# Funcionalities developed on TDD
def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1

def test_square_root():
    assert square_root(9) == 3
    assert square_root(0) == 0

def test_square_root_negative():
    with pytest.raises(ValueError, match="There is not real square root for a negative number"):
        square_root(-4)