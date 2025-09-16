"""
Time series operations for NDArray1D.
"""

from .arrays import VectoPyArray

def moving_average(self, window):
    """Calculate moving average with given window size."""
    if window <= 0:
        raise ValueError("Window size must be positive.")
    if window > len(self._data):
        raise ValueError("Window size cannot be larger than array size.")
    
    result = []
    for i in range(len(self._data) - window + 1):
        window_data = self._data[i:i + window]
        window_avg = sum(window_data) / window
        result.append(window_avg)
    
    return VectoPyArray((len(result),), dtype=float, buffer=result)

def diff(self):
    """Calculate differences between consecutive elements."""
    if len(self._data) < 2:
        raise ValueError("Need at least 2 elements for differences.")
    differences = [self._data[i + 1] - self._data[i] for i in range(len(self._data) - 1)]
    return VectoPyArray((len(differences),), dtype=self._dtype, buffer=differences)

def cumulative_sum(self):
    """Calculate cumulative sum (prefix sum)."""
    result = []
    current_sum = self._dtype(0)
    for item in self._data:
        current_sum += item
        result.append(current_sum)
    return VectoPyArray(self.shape, dtype=self._dtype, buffer=result)

def shift(self, periods=1):
    """Shift array elements by periods."""
    if periods == 0:
        return VectoPyArray(self.shape, dtype=self._dtype, buffer=self._data.copy())
    
    shifted_data = [self._dtype(0)] * len(self._data)
    if periods > 0:
        shifted_data[periods:] = self._data[:-periods]
    else:
        shifted_data[:periods] = self._data[-periods:]
    
    return VectoPyArray(self.shape, dtype=self._dtype, buffer=shifted_data)

# Attach methods to VectoPyArray
VectoPyArray.moving_average = moving_average
VectoPyArray.diff = diff
VectoPyArray.cumulative_sum = cumulative_sum
VectoPyArray.shift = shift