"""
Algorithm implementations for VectoPyArray.
"""

from .arrays import VectoPyArray
from collections import Counter

def majority_element(self):
    """Find majority element using Boyer-Moore algorithm."""
    if not self._data:
        raise ValueError("Cannot find majority element in empty array.")
    
    candidate = None
    count = 0
    
    for num in self._data:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    
    # Verify if candidate is actually majority
    if self._data.count(candidate) > len(self._data) // 2:
        return candidate
    else:
        raise ValueError("No majority element found.")

def unique(self):
    """Return unique elements in array."""
    unique_data = list(set(self._data))
    return VectoPyArray((len(unique_data),), dtype=self._dtype, buffer=unique_data)

def is_monotonic(self):
    """Check if array is monotonic (non-decreasing or non-increasing)."""
    if len(self._data) <= 1:
        return True
    
    increasing = all(self._data[i] <= self._data[i + 1] for i in range(len(self._data) - 1))
    decreasing = all(self._data[i] >= self._data[i + 1] for i in range(len(self._data) - 1))
    
    return increasing or decreasing

def mode(self):
    """Find the most frequent element(s)."""
    if not self._data:
        raise ValueError("Cannot find mode of empty array.")
    
    counter = Counter(self._data)
    max_count = max(counter.values())
    modes = [item for item, count in counter.items() if count == max_count]
    
    if len(modes) == 1:
        return modes[0]
    else:
        return modes

# Attach methods to VectoPyArray
VectoPyArray.majority_element = majority_element
VectoPyArray.unique = unique
VectoPyArray.is_monotonic = is_monotonic
VectoPyArray.mode = mode