"""
Test cases for VectoPyArray statistical operations.
"""

import vectopy as vp
import math

# Test sum() method
def test_sum_op():
    arr = vp.array([1, 2, 3, 4, 5])
    assert arr.sum() == 15
    assert isinstance(arr.sum(), int)

    arr = vp.array([1.5, 2.5, 3.5, 4.5, 5.5])
    assert arr.sum() == 17.5
    assert isinstance(arr.sum(), float)

    arr = vp.array([-5, -3, -1, 2, 4])
    assert arr.sum() == -3
    assert isinstance(arr.sum(), int)

    arr = vp.array([-2, -1, 0, 1, 2])
    assert arr.sum() == 0
    assert isinstance(arr.sum(), int)

    arr = vp.array([42])
    assert arr.sum() == 42
    assert isinstance(arr.sum(), int)

    arr = vp.array([-2, -1, 0, 1, 2.3])
    assert round(arr.sum(), 1) == 0.3
    assert isinstance(arr.sum(), float)

# Test max method
def test_max_op():
    arr = vp.array([1, 2, 3, 4, 5])
    result = arr.max()
    assert result == 5

    arr = vp.array([1.5, 2.5, 3.5, 4.5, 5.5])
    assert arr.max() == 5.5

    arr = vp.array([-5, -3, -1, 2, 4])
    assert arr.max() == 4

    arr = vp.array([42])
    assert arr.max() == 42

    arr = vp.array([-2, -1, 0, 1, 2.3])
    assert arr.max() == 2.3
    
# Test min method
def test_min_op():
    arr = vp.array([1, 2, 3, 4, 5])
    result = arr.min()
    assert result == 1

    arr = vp.array([1.5, 2.5, 3.5, 4.5, 5.5])
    assert arr.min() == 1.5

    arr = vp.array([-5, -3, -1, 2, 4])
    assert arr.min() == -5

    arr = vp.array([42])
    assert arr.min() == 42

    arr = vp.array([-2, -1, 0, 1, 2.3])
    assert arr.min() == -2

# Test mean method
def test_mean_op():
    arr = vp.array([1, 2, 3, 4, 5])
    result = arr.mean()
    assert result == 3

    arr = vp.array([1.5, 2.5, 3.5, 4.5, 5.5])
    assert arr.mean() == 3.5

    arr = vp.array([-5, -3, -1, 2, 4])
    assert arr.mean() == -0.6

    arr = vp.array([42])
    assert arr.mean() == 42.0

    arr = vp.array([-2, -1, 0, 1, 2])
    assert arr.mean() == 0.0

# Test std method
def test_std_op():
    arr = vp.array([1, 2, 3, 4, 5])
    expected_std = math.sqrt(sum((x - 3) ** 2 for x in [1, 2, 3, 4, 5]) / 5)
    assert math.isclose(arr.std(), expected_std)

    arr = vp.array([1.5, 2.5, 3.5, 4.5, 5.5])
    expected_std = math.sqrt(sum((x - 3.5) ** 2 for x in [1.5, 2.5, 3.5, 4.5, 5.5]) / 5)
    assert math.isclose(arr.std(), expected_std)  

    arr = vp.array([42])
    assert arr.std() == 0.0

    arr = vp.array([5, 5, 5, 5, 5])
    assert arr.std() == 0.0

# Test median() method
def test_median_op():
    arr = vp.array([1, 2, 3, 4, 5])
    assert arr.median() == 3

    arr = vp.array([1, 2, 3, 4, 5, 6])
    assert arr.median() == 3.5

    arr = vp.array([5, 1, 3, 2, 4])
    assert arr.median() == 3

    arr = vp.array([-5, -3, -1, 2, 4])
    assert arr.median() == -1

    arr = vp.array([42])
    assert arr.median() == 42

# Test mode() method
def test_mode_op():
    arr = vp.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
    assert arr.mode() == 4

    arr = vp.array([1, 1, 2, 2, 3, 3])
    modes = arr.mode()
    assert isinstance(modes, list)
    assert set(modes) == {1, 2, 3}
    assert len(modes) == 3

    arr = vp.array([1, 2, 3, 4, 5])
    modes = arr.mode()
    assert isinstance(modes, list)
    assert set(modes) == {1, 2, 3, 4, 5}
    assert len(modes) == 5

    arr = vp.array([42])
    assert arr.mode() == 42

    arr = vp.array([0, 0, 1, 2, 3])
    assert arr.mode() == 0

    
def test_methods_attached_to_class():
    int_array = vp.array([1, 2, 3, 4, 5])
    assert hasattr(int_array, 'sum')
    assert hasattr(int_array, 'max')
    assert hasattr(int_array, 'min')
    assert hasattr(int_array, 'mean')
    assert hasattr(int_array, 'std')
    assert hasattr(int_array, 'median')
    assert hasattr(int_array, 'mode')
    
    assert callable(int_array.sum)
    assert callable(int_array.max)
    assert callable(int_array.min)
    assert callable(int_array.mean)
    assert callable(int_array.std)
    assert callable(int_array.median)
    assert callable(int_array.mode)