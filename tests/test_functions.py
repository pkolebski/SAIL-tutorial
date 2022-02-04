"""Tests for simple calculator functions."""
import pytest as pytest

from tutorial.functions import add, divide, multiply, subtract


def test_add():
    """Test add function."""
    assert add(1, 1) == 2


def test_subtract():
    """Test subtract function."""
    assert subtract(10, 1) == 9


def test_multiply():
    """Test multiply function."""
    assert multiply(2, 2) == 4


def test_divide():
    """Test divide function."""
    assert divide(10, 2) == 5
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
