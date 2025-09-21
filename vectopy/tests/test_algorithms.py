"""
Test cases for VectoPyArray algorithms operations.
"""

import vectopy as vp

# Test majority_element method
def test_basic_majority():
    """Test basic majority element."""
    arr = vp.array([2, 2, 3, 2, 4, 2, 2])
    result = arr.majority_element()
    assert result == 2  # 2 appears 5/7 times

def test_no_majority():
    """Test when no majority exists."""
    arr = vp.array([1, 2, 3, 1, 2, 3])
    try:
        result = arr.majority_element()
        assert False, "Should have raised an error!"
    except ValueError as e:
        assert "No majority" in str(e)

def test_single_element():
    """Test with single element."""
    arr = vp.array([42])
    result = arr.majority_element()
    assert result == 42  # 1/1 is majority!

def test_exactly_half():
    """Test when element appears exactly half (no majority)."""
    arr = vp.array([1, 2, 1, 2])
    try:
        result = arr.majority_element()
        assert False, "Should have raised an error!"
    except ValueError as e:
        assert "No majority" in str(e)

def test_float_majority():
    """Test majority with float numbers."""
    arr = vp.array([1.5, 2.0, 1.5, 1.5, 3.0, 1.5, 1.5])
    result = arr.majority_element()
    assert result == 1.5  # 1.5 appears 5/7 times

def test_all_same():
    """Test when all elements are the same."""
    arr = vp.array([7, 7, 7, 7, 7])
    result = arr.majority_element()
    assert result == 7  # 5/5 is definitely majority!


# Test unique method
def test_basic_unique():
    """Test basic duplicate removal."""
    arr = vp.array([1, 2, 3, 2, 1, 4, 3])
    result = arr.unique()
    # Should contain [1, 2, 3, 4] in some order
    assert sorted(result.data) == [1, 2, 3, 4]
    assert result.dtype == int

def test_all_unique():
    """Test when all elements are already unique."""
    arr = vp.array([10, 20, 30, 40])
    result = arr.unique()
    # Should stay the same (order might change)
    assert sorted(result.data) == [10, 20, 30, 40]

def test_all_same():
    """Test when all elements are identical."""
    arr = vp.array([5, 5, 5, 5, 5])
    result = arr.unique()       
    # Should become just [5]
    assert result.data == [5]
    assert len(result) == 1

def test_single_element_unique():
    """Test with single element."""
    arr = vp.array([42])
    result = arr.unique()
    # Should stay [42]
    assert result.data == [42]
    assert len(result) == 1


# Test is_monotonic  
def test_strictly_increasing():
    """Test strictly increasing array."""
    arr = vp.array([1, 2, 3, 4, 5])
    assert arr.is_monotonic() == True

def test_strictly_decreasing():
    """Test strictly decreasing array."""
    arr = vp.array([5, 4, 3, 2, 1])
    assert arr.is_monotonic() == True

def test_non_decreasing():
    """Test non-decreasing with duplicates."""
    arr = vp.array([1, 1, 2, 3, 3, 4])
    assert arr.is_monotonic() == True

def test_non_increasing():
    """Test non-increasing with duplicates."""
    arr = vp.array([5, 5, 4, 3, 3, 2])
    assert arr.is_monotonic() == True

def test_all_same():
    """Test array with all same elements."""
    arr = vp.array([7, 7, 7, 7, 7])
    assert arr.is_monotonic() == True  # Technically monotonic!

def test_not_monotonic():
    """Test non-monotonic array."""
    arr = vp.array([1, 3, 2, 4])
    assert arr.is_monotonic() == False  # Up then down

def test_single_element():
    """Test single element array."""
    arr = vp.array([42])
    assert arr.is_monotonic() == True  # Always monotonic

def test_up_then_down():
    """Test array that increases then decreases."""
    arr = vp.array([1, 2, 3, 2, 1])
    assert arr.is_monotonic() == False  # Not monotonic