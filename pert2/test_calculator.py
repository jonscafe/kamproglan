import pytest
from calc import add, subtract, multiply, divide  # Assume the functions are in calculator.py

def test_add():
    assert add(5, 3) == 8
    assert add(5, -3) == 2
    assert add(0, 5) == 5

def test_subtract():
    assert subtract(8, 5) == 3
    assert subtract(5, 8) == -3
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(-4, 3) == -12

def test_divide():
    assert divide(8, 2) == 4.0
    assert divide(-8, -2) == 4.0
    assert divide(8, 0) == "Error: Division by zero is undefined."
