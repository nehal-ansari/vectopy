"""
Test cases for VectoPyArray arithmetic operations and dot product.
"""

import vectopy as vp
import math
import pytest
from vectopy.core._internals import ShapeError

def test_addition_arrays():
    """Test array + array."""
    arr1 = vp.array([1, 2, 3])
    arr2 = vp.array([4, 5, 6])
    result = arr1 + arr2
    assert result.data == [5, 7, 9]
    assert result.dtype == int

def test_addition_scalar():
    """Test array + scalar."""
    arr = vp.array([1, 2, 3])
    result = arr + 5
    assert result.data == [6, 7, 8]

def test_subtraction():
    """Test array subtraction."""
    arr1 = vp.array([10, 20, 30])
    arr2 = vp.array([1, 2, 3])
    result = arr1 - arr2
    assert result.data == [9, 18, 27]

def test_multiplication():
    """Test array multiplication."""
    arr1 = vp.array([1, 2, 3])
    arr2 = vp.array([4, 5, 6])
    result = arr1 * arr2
    assert result.data == [4, 10, 18]

def test_division():
    """Test array division."""
    arr1 = vp.array([10, 20, 30])
    arr2 = vp.array([2, 4, 5])
    result = arr1 / arr2
    assert result.data == [5.0, 5.0, 6.0]
    assert result.dtype == float

def test_mixed_type_operations():
    """Test operations between int and float arrays."""
    int_arr = vp.array([1, 2, 3])
    float_arr = vp.array([1.5, 2.5, 3.5])
    result = int_arr + float_arr
    assert result.dtype == float
    assert result.data == [2.5, 4.5, 6.5]

def test_dot_product():
    arr_a = vp.array([1, 2 ,3])
    arr_b = vp.array([4, 3, 2])
    result = arr_a.dot(arr_b)
    assert result == 16
    assert isinstance(result, int)

    arr_a = vp.array([1.5, 2.5, 3.5])
    arr_b = vp.array([0.5, 1.5, 2.5])
    expected = 1.5*0.5 + 2.5*1.5 + 3.5*2.5
    result = arr_a.dot(arr_b)
    assert math.isclose(result, expected)
    assert isinstance(result, float)

    arr_a = vp.array([1, 2, 3])
    arr_b = vp.array([1.5, 2.5, 3.5])
    expected = 1*1.5 + 2*2.5 + 3*3.5
    result = arr_a.dot(arr_b)
    assert math.isclose(result, expected)
    assert isinstance(result, float)

    arr_a = vp.array([1, 2, 3])
    arr_b = vp.array([1, 2])
    with pytest.raises(ShapeError):
        arr_a.dot(arr_b)