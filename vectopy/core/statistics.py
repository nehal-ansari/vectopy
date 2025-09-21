"""
Statistical operations for VectoPyArray.
"""

from .arrays import VectoPyArray
from collections import Counter
import math
import builtins


def sum(self):
    """Sum of array elements."""
    total = self._dtype(0)
    for item in self._data:
        total += item
    return total

def max(self):
    """Maximum value of the array."""
    mx = self._data[0]  
    for item in self._data:
        if item > mx:
            mx = item 
    return mx

def min(self):
    """Minimum value of the array."""
    mn = self._data[0]  
    for item in self._data:
        if item < mn:
            mn = item 
    return mn

def mean(self):
    """Mean of the array elements."""
    return self.sum() / len(self._data)

def std(self):
    """Standard deviation of the array elements."""
    m = self.mean()
    mean_sqr = ((x - m) ** 2 for x in self._data)
    sm = 0
    for val in mean_sqr:
        sm += val
    variance = sm / len(self._data)
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
    
def mode(self):
    """Find the most frequent element(s)."""
    if not self._data:
        raise ValueError("Cannot find mode of empty array.")
    
    counter = Counter(self._data)
    max_count = builtins.max(counter.values())
    modes = [item for item, count in counter.items() if count == max_count]
    
    if len(modes) == 1:
        return modes[0]
    else:
        return modes
    
# Attach methods to VectoPyArray
VectoPyArray.sum = sum
VectoPyArray.max = max
VectoPyArray.min = min
VectoPyArray.mean = mean
VectoPyArray.std = std
VectoPyArray.median = median
VectoPyArray.mode = mode