"""
Test cases for VectoPyArray transformation operations.
"""

import vectopy as vp

# Test normalize method
def test_basic_normalization():
    """Test normalizing simple numbers."""
    arr = vp.array([1, 2, 3, 4, 5])
    result = arr.normalize()
    print(result)
    print("Hello")
    # After normalization, mean should be 0, std should be 1
    assert abs(result.mean()) < 0.0001  # Almost 0
    assert abs(result.std() - 1) < 0.0001  # Almost 1

def test_all_same_numbers():
    """Test when all numbers are identical."""
    arr = vp.array([5, 5, 5, 5, 5])
    result = arr.normalize()
    # All should become 0.0 (since no variation)
    assert result.data == [0.0, 0.0, 0.0, 0.0, 0.0]
    assert result.dtype == float

def test_two_elements():
    """Test with minimum required elements (2)."""
    arr = vp.array([10, 20])
    result = arr.normalize()
    # Should have mean ~0 and std ~1
    assert abs(result.mean()) < 0.0001
    assert abs(result.std() - 1) < 0.0001

def test_single_element_error():
    """Test that single element raises error."""
    arr = vp.array([42])
    try:
        result = arr.normalize()
        assert False, "Should have raised an error!"
    except ValueError as e:
        assert "at least two elements" in str(e)

def test_negative_numbers():
    """Test normalization with negative numbers."""
    arr = vp.array([-2, -1, 0, 1, 2])
    result = arr.normalize()
    # Should still have mean 0 and std 1
    assert abs(result.mean()) < 0.0001
    assert abs(result.std() - 1) < 0.0001

def test_float_numbers():
    """Test with decimal numbers."""
    arr = vp.array([1.5, 2.5, 3.5, 4.5])
    result = arr.normalize()
    # Should work with floats too
    assert abs(result.mean()) < 0.0001
    assert abs(result.std() - 1) < 0.0001
    assert result.dtype == float


# Test minmax_scale method
def test_basic_minmax_scale():
    """Test basic minmax scaling."""
    arr = vp.array([10, 20, 30, 40, 50])
    result = arr.minmax_scale()   
    # Should become [0.0, 0.25, 0.5, 0.75, 1.0]
    expected = [0.0, 0.25, 0.5, 0.75, 1.0]
    for i in range(len(result.data)):
        assert abs(result.data[i] - expected[i]) < 0.001
    assert result.dtype == float

def test_all_same_minmax():
    """Test when all numbers are identical."""
    arr = vp.array([7, 7, 7, 7, 7])
    result = arr.minmax_scale()
    # All should become 0.5 (middle point)
    assert result.data == [0.5, 0.5, 0.5, 0.5, 0.5]
    assert result.dtype == float

def test_negative_minmax():
    """Test scaling with negative numbers."""
    arr = vp.array([-10, 0, 10])
    result = arr.minmax_scale()
    # Should become [0.0, 0.5, 1.0]
    expected = [0.0, 0.5, 1.0]
    for i in range(len(result.data)):
        assert abs(result.data[i] - expected[i]) < 0.001

def test_single_element():
    """Test with single element."""
    arr = vp.array([42])
    result = arr.minmax_scale()
    # Single element becomes 0.5 (middle)
    assert result.data == [0.5]
    assert result.dtype == float

def test_decimal_minmax():
    """Test with decimal numbers."""
    arr = vp.array([1.5, 3.0, 4.5])
    result = arr.minmax_scale()
    # Should become [0.0, 0.5, 1.0]
    expected = [0.0, 0.5, 1.0]
    for i in range(len(result.data)):
        assert abs(result.data[i] - expected[i]) < 0.001


# Test clip method
def test_basic_clip():
    """Test basic clipping functionality."""
    arr = vp.array([-5, 0, 50, 100, 150])
    result = arr.clip(0, 100)
    assert result.data == [0, 0, 50, 100, 100]  # -5→0, 150→100
    assert result.dtype == int  # Should keep original dtype

def test_no_clip_needed():
    """Test when no values need clipping."""
    arr = vp.array([10, 20, 30, 40])
    result = arr.clip(0, 100)
    assert result.data == [10, 20, 30, 40]  # All unchanged

def test_float_clip():
    """Test clipping with decimal numbers."""
    arr = vp.array([-2.5, 0.5, 3.5, 5.5])
    result = arr.clip(0.0, 5.0)
    assert result.data == [0.0, 0.5, 3.5, 5.0]  # -2.5→0.0, 5.5→5.0

def test_extreme_clip():
    """Test with very wide range."""
    arr = vp.array([-1000, 0, 500, 1000])
    result = arr.clip(-10, 10)
    assert result.data == [-10, 0, 10, 10]  # All clipped to ±10

def test_same_min_max():
    """Test when min and max are the same."""
    arr = vp.array([1, 2, 3, 4, 5])
    result = arr.clip(3, 3)  # Force all to be 3
    assert result.data == [3, 3, 3, 3, 3]  # Everything becomes 3


# Test reverse method
def test_basic_reverse():
    """Test basic array reversal."""
    arr = vp.array([1, 2, 3, 4, 5])
    result = arr.reverse()
    assert result.data == [5, 4, 3, 2, 1]  # Completely reversed
    assert result.dtype == int  # Should keep original dtype

def test_single_element_reverse():
    """Test reversing a single element array."""
    arr = vp.array([42])
    result = arr.reverse()
    assert result.data == [42]  # Stays the same (only one element)
    assert result.dtype == int

def test_float_reverse():
    """Test reversing float numbers."""
    arr = vp.array([1.1, 2.2, 3.3, 4.4])
    result = arr.reverse()
    assert result.data == [4.4, 3.3, 2.2, 1.1]  # Decimals reversed
    assert result.dtype == float