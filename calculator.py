import pytest
from calculator import add, subtract, multiply, divide

def test_add():
  """Test the add function."""
  assert add(1, 2) == 3
  assert add(5, 10) == 15

def test_subtract():
  """Test the subtract function."""
  assert subtract(10, 5) == 5
  assert subtract(15, 20) == -5

def test_multiply():
  """Test the multiply function."""
  assert multiply(2, 2) == 4
  assert multiply(5, 10) == 50

def test_divide():
  """Test the divide function."""
  assert divide(10, 5) == 2
  assert divide(15, 20) == 0.75

# functionality tests to ensure that the app also handles adding negative numbers
# and cases like  divide-by-zero
def test_add_negative_numbers():
  """Test that the add function can correctly calculate the sum of two negative numbers."""
  assert add(-1, -2) == -3

def test_divide_by_zero():
  """Test that the divide function can correctly handle dividing by zero."""
  with pytest.raises(ZeroDivisionError):
    divide(10, 0)
