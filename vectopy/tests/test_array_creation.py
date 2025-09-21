"""
Test cases for VectoPyArray array creation.
"""

import pytest
import vectopy as vp

def test_array_from_list():
    """Test creating array from list."""
    arr = vp.array([1, 2, 3])
    assert arr.data == [1, 2, 3]
    assert arr.dtype == int

def test_array_from_tuple():
    """Test creating array from tuple."""
    arr = vp.array((1, 2, 3))
    assert arr.data == [1, 2, 3]
    assert arr.dtype == int

def test_array_from_vectopy_obj():
    """Test creating array from VectoPyArray object."""
    arr = vp.array((1, 2, 3))
    arr2 = vp.array(arr)    
    assert arr2.data == [1, 2, 3]
    assert arr.dtype == int

def test_array_from_range_or_any_iterables():
    """Test creating array from range() fn or any other iterables which contains __list__ attribute."""
    arr = vp.array(range(2,10,2))
    assert arr.data == [2, 4, 6, 8]
    assert arr.dtype == int

def test_zeros_creation():
    """Test zeros() function."""
    arr = vp.zeros(3)
    assert arr.data == [0.0, 0.0, 0.0]
    assert arr.dtype == float

def test_ones_creation():
    """Test ones() function."""
    arr = vp.ones(3, dtype=int)
    assert arr.data == [1, 1, 1]
    assert arr.dtype == int

def test_full_creation():
    """Test full() function."""
    arr = vp.full(3, 7)
    assert arr.data == [7, 7, 7]
    assert arr.dtype == int

def test_arange_creation():
    """Test arange() function."""
    arr = vp.arange(5)
    arr2 = vp.arange(1,9,2)
    assert arr.data == [0, 1, 2, 3, 4]
    assert arr.dtype == int
    assert arr2.data == [1, 3, 5, 7]

def test_empty_array_error():
    """Test error for empty input."""
    with pytest.raises(ValueError):
        vp.array([])