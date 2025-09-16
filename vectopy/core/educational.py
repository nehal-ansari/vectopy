"""
Educational methods for VectoPyArray.
"""

from .arrays import VectoPyArray

def explain(self):
    """Explain the array's properties and internals."""
    itemsize = 8 if self._dtype is float else 4
    print(f"NDArray1D Metadata Explanation:")
    print(f"  • Shape: {self.shape} - A 1-dimensional array with {self._size} elements.")
    print(f"  • Dtype: {self._dtype} - Elements are Python {self._dtype.__name__} objects.")
    print(f"  • Strides: ({itemsize},) - To move to the next element, step {itemsize} bytes in memory (simulated).")
    print(f"  • Base: None - This array owns its data (simulated).")
    print(f"  • Underlying Data: {self._data}")
    print(f"  • Memory Size: {self._size * itemsize} bytes (simulated)")

def visualize(self):
    """Simple ASCII visualization of the array."""
    if not self._data:
        print("Empty array")
        return
    
    max_val = max(self._data)
    min_val = min(self._data)
    range_val = max_val - min_val
    
    if range_val == 0:
        # All values are the same
        for _ in self._data:
            print("█", end="")
        print()
    else:
        # Scale values to 0-10 range for visualization
        for value in self._data:
            scaled = int(((value - min_val) / range_val) * 10)
            bar = "█" * (scaled + 1)
            print(f"{bar:<10} ({value})")

def benchmark(self, operation, *args):
    """Time an operation for educational purposes."""
    import time
    start = time.time()
    result = operation(self, *args)
    end = time.time()
    print(f"Operation {operation.__name__} took {end - start:.6f} seconds")
    return result

# Attach methods to NDArray1D
VectoPyArray.explain = explain
VectoPyArray.visualize = visualize
VectoPyArray.benchmark = benchmark