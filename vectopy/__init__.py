"""
VectoPy - A pure Python, educational implementation of a NumPy-like library for 1D vectors.
"""

from .core.arrays import VectoPyArray
from .core.function_base import array, zeros, ones, full, arange


__all__ = [
    'VectoPyArray', 'array', 'zeros', 'ones', 'arange', 'full'
]