"""
Educational methods for VectoPyArray.
"""

from .arrays import VectoPyArray

def explain(self):
    """Explain the array's properties and internals."""
    itemsize = 8 if self._dtype is float else 4
    print(f"VectoPyArray Metadata Explanation:")
    print(f"  • Shape: {self.shape} - A 1-dimensional array with {self._size} elements.")
    print(f"  • Dtype: {self._dtype} - Elements are Python {self._dtype.__name__} objects.")
    print(f"  • Strides: ({itemsize},) - To move to the next element, step {itemsize} bytes in memory (simulated).")
    print(f"  • Base: None - This array owns its data (simulated).")
    print(f"  • Underlying Data: {self._data}")
    print(f"  • Memory Size: {self._size * itemsize} bytes (simulated)")

# Attach methods to NDArray1D
VectoPyArray.explain = explain
