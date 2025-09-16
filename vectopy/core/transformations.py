"""
Data transformation operations for VectoPyArray.
"""

from .arrays import VectoPyArray

def normalize(self):
    """Normalize the vector to have mean 0 and standard deviation 1."""
    # This is a unique VectoPy method!
    if len(self._data) < 2:
        raise ValueError("Normalization requires at least two elements.")
    mu = self.mean()
    sigma = self.std()
    if sigma == 0:
        return VectoPyArray(self.shape, dtype=float, buffer=[0.0] * self._size)
    normalized_data = [(x - mu) / sigma for x in self._data]
    return VectoPyArray(self.shape, dtype=float, buffer=normalized_data)

def clip(self, min_val, max_val):
    """Clip the values in the array to be between min_val and max_val."""
    clipped_data = [max(min_val, min(x, max_val)) for x in self._data]
    return VectoPyArray(self.shape, dtype=self._dtype, buffer=clipped_data)

def reverse(self):
    """Return a reversed copy of the array."""
    return VectoPyArray(self.shape, dtype=self._dtype, buffer=list(reversed(self._data)))

def minmax_scale(self):
    """Scale array to [0, 1] range."""
    if not self._data:
        raise ValueError("Cannot scale empty array.")
    min_val = self.min()
    max_val = self.max()
    if min_val == max_val:
        return VectoPyArray(self.shape, dtype=float, buffer=[0.5] * self._size)
    scaled_data = [(x - min_val) / (max_val - min_val) for x in self._data]
    return VectoPyArray(self.shape, dtype=float, buffer=scaled_data)

# Attach methods to VectoPyArray
VectoPyArray.normalize = normalize
VectoPyArray.clip = clip
VectoPyArray.reverse = reverse
VectoPyArray.minmax_scale = minmax_scale

