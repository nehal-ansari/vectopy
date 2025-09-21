"""
Test cases for VectoPyArray time series operations.
"""

import vectopy as vp

# Test moving_average method
def test_basic_moving_average():
    """Test basic moving average calculation."""
    arr = vp.array([1, 2, 3, 4, 5])
    result = arr.moving_average(3)
    # Windows: [1,2,3]=2.0, [2,3,4]=3.0, [3,4,5]=4.0
    expected = [2.0, 3.0, 4.0]
    assert result.data == expected
    assert result.dtype == float

def test_window_size_1():
    """Test moving average with window size 1."""
    arr = vp.array([10, 20, 30])
    result = arr.moving_average(1)
    # Each window is just one number: [10], [20], [30]
    assert result.data == [10.0, 20.0, 30.0]  # Same as original

def test_full_window():
    """Test when window equals array size."""
    arr = vp.array([5, 10, 15])
    result = arr.moving_average(3)
    # Only one window: [5,10,15] = 10.0
    assert result.data == [10.0]  # Single average value

def test_window_too_large():
    """Test error when window is larger than array."""
    arr = vp.array([1, 2, 3])
    try:
        result = arr.moving_average(5)
        assert False, "Should have raised an error!"
    except ValueError as e:
        assert "larger than array" in str(e)

def test_zero_window():
    """Test error when window size is zero."""
    arr = vp.array([1, 2, 3])
    try:
        result = arr.moving_average(0)
        assert False, "Should have raised an error!"
    except ValueError as e:
        assert "positive" in str(e)

def test_negative_numbers():
    """Test moving average with negative numbers."""
    arr = vp.array([-2, -1, 0, 1, 2])
    result = arr.moving_average(3)
    # Windows: [-2,-1,0]=-1.0, [-1,0,1]=0.0, [0,1,2]=1.0
    assert result.data == [-1.0, 0.0, 1.0]

    
# Test diff method
def test_basic_diff():
    """Test basic difference calculation."""
    arr = vp.array([1, 3, 5, 7, 9])
    result = arr.diff()
    # Differences: [3-1=2, 5-3=2, 7-5=2, 9-7=2]
    assert result.data == [2, 2, 2, 2]  # All differences are 2
    assert result.dtype == int

def test_mixed_diff():
    """Test with increasing and decreasing values."""
    arr = vp.array([10, 15, 12, 18, 20])
    result = arr.diff()
    # Differences: [15-10=5, 12-15=-3, 18-12=6, 20-18=2]
    assert result.data == [5, -3, 6, 2]

def test_single_element_error():
    """Test error with single element."""
    arr = vp.array([42])
    try:
        result = arr.diff()
        assert False, "Should have raised an error!"
    except ValueError as e:
        assert "at least 2 elements" in str(e)

def test_negative_diff():
    """Test differences with negative numbers."""
    arr = vp.array([5, 0, -5, -10])
    result = arr.diff()
    # Differences: [0-5=-5, -5-0=-5, -10-(-5)=-5]
    assert result.data == [-5, -5, -5]

def test_two_elements_diff():
    """Test with minimum required elements (2)."""
    arr = vp.array([10, 25])
    result = arr.diff()
    # Only one difference: 25-10=15
    assert result.data == [15]
    assert len(result) == 1


# Test cumulative_sum method
def test_basic_cumsum():
    """Test basic cumulative sum calculation."""
    arr = vp.array([1, 2, 3, 4, 5])
    result = arr.cumulative_sum()
    # Cumulative: [1, 1+2=3, 3+3=6, 6+4=10, 10+5=15]
    assert result.data == [1, 3, 6, 10, 15]
    assert result.dtype == int

def test_single_element_cumsum():
    """Test cumulative sum with single element."""
    arr = vp.array([42])
    result = arr.cumulative_sum()
    # Only one element: cumulative sum is itself
    assert result.data == [42]
    assert result.dtype == int

def test_negative_cumsum():
    """Test cumulative sum with negative numbers."""
    arr = vp.array([10, -5, 3, -2, 8])
    result = arr.cumulative_sum()
    # Cumulative: [10, 10-5=5, 5+3=8, 8-2=6, 6+8=14]
    assert result.data == [10, 5, 8, 6, 14]

def test_mixed_cumsum():
    """Test cumulative sum with mixed numbers."""
    arr = vp.array([2, -3, 5, -1, 4])
    result = arr.cumulative_sum()   
    # Cumulative: [2, 2-3=-1, -1+5=4, 4-1=3, 3+4=7]
    assert result.data == [2, -1, 4, 3, 7]


# Test shift method
def test_shift_right():
    """Test shifting elements to the right."""
    arr = vp.array([1, 2, 3, 4, 5])
    result = arr.shift(1)  # Shift right by 1
    # [1,2,3,4,5] → [0,1,2,3,4]
    assert result.data == [0, 1, 2, 3, 4]
    assert result.dtype == int

def test_shift_left():
    """Test shifting elements to the left."""
    arr = vp.array([1, 2, 3, 4, 5])
    result = arr.shift(-1)  # Shift left by 1
    # [1,2,3,4,5] → [2,3,4,5,0]
    assert result.data == [2, 3, 4, 5, 0]

def test_no_shift():
    """Test with zero shift (should return copy)."""
    arr = vp.array([1, 2, 3])
    result = arr.shift(0)
    # Should be identical copy
    assert result.data == [1, 2, 3]
    assert result is not arr  # Should be different object

def test_shift_right_multiple():
    """Test shifting right by multiple positions."""
    arr = vp.array([1, 2, 3, 4, 5])
    result = arr.shift(2)  # Shift right by 2
    # [1,2,3,4,5] → [0,0,1,2,3]
    assert result.data == [0, 0, 1, 2, 3]

def test_shift_left_multiple():
    """Test shifting left by multiple positions."""
    arr = vp.array([1, 2, 3, 4, 5])
    result = arr.shift(-2)  # Shift left by 2
    # [1,2,3,4,5] → [3,4,5,0,0]
    assert result.data == [3, 4, 5, 0, 0]

def test_float_shift():
    """Test shifting with float array."""
    arr = vp.array([1.5, 2.5, 3.5])
    result = arr.shift(1)
    # [1.5,2.5,3.5] → [0.0,1.5,2.5]
    assert result.data == [0.0, 1.5, 2.5]
    assert result.dtype == float

def test_full_shift():
    """Test shifting by array length."""
    arr = vp.array([1, 2, 3, 4, 5])
    result = arr.shift(5)  # Shift right by full length
    # [1,2,3,4,5] → [0,0,0,0,0] (all elements shifted out)
    assert result.data == [0, 0, 0, 0, 0]