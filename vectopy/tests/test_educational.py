"""
Test cases for VectoPyArray algorithms operations.
"""

import vectopy as vp

def test_explain_int_array(capsys):
    """Test explain with integer array."""
    arr = vp.array([10, 20, 30])
    arr.explain()
    
    captured = capsys.readouterr()
    output = captured.out
    
    # Check key information
    assert "Shape: (3,)" in output
    assert "Dtype: <class 'int'>" in output
    assert "Strides: (4,)" in output
    assert "Underlying Data: [10, 20, 30]" in output
    assert "Memory Size: 12 bytes" in output


def test_explain_float_array(capsys):
    """Test explain with float array."""
    arr = vp.array([1.5, 2.5, 3.5])
    arr.explain()
    
    captured = capsys.readouterr()
    output = captured.out
    
    assert "Shape: (3,)" in output
    assert "Dtype: <class 'float'>" in output
    assert "Strides: (8,)" in output  # 8 bytes for float
    assert "Memory Size: 24 bytes" in output  # 3 * 8 = 24