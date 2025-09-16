"""
Statistical operations for VectoPyArray.
"""

from .arrays import VectoPyArray
import math

# mode

def sum(self):
    """Sum of array elements."""
    total = self._dtype(0)
    for item in self._data:
        total += item
    return total

def max(self):
    """Maximum value of the array."""
    return max(self._data)

def min(self):
    """Minimum value of the array."""
    return min(self._data)

def mean(self):
    """Mean of the array elements."""
    return self.sum() / len(self._data)

def std(self):
    """Standard deviation of the array elements."""
    m = self.mean()
    variance = sum((x - m) ** 2 for x in self._data) / len(self._data)
    return math.sqrt(variance)

def median(self):
    """Median of the array elements."""
    if not self._data:
        raise ValueError("Cannot compute median of empty array.")
    sorted_data = sorted(self._data)
    n = len(sorted_data)
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    
# Attach methods to VectoPyArray
VectoPyArray.sum = sum
VectoPyArray.max = max
VectoPyArray.min = min
VectoPyArray.mean = mean
VectoPyArray.std = std
VectoPyArray.median = median