"""
Basic Usage Examples for VectoPy
=====================================
This file demonstrates the core functionality of VectoPyArray.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import vectopy as vp

def main():
    print("=" * 60)
    print("VectoPy Basic Usage Examples")
    print("=" * 60)
    
    # Example 1: Creating Arrays
    print("\n1. Creating Arrays:")
    print("-" * 40)
    
    # From list
    arr1 = vp.array([1, 2, 3, 4, 5])
    print(f"From list: {arr1}")

    # From tuple
    arr2 = vp.array((1, 2, 3, 4, 5))
    print(f"From tuple: {arr2}")
    
    # With specific dtype
    arr3 = vp.array([1.5, 2.5, 3.5])
    print(f"Float array: {arr3}")
    
    # Creating zeros element array
    arr4 = vp.zeros(4)
    print(f"Zeros array: {arr4}")

    # Creating ones element array
    arr5 = vp.ones(4)
    print(f"Ones array: {arr5}")
    
    # Creating array using full
    arr6 = vp.full(3, 7)
    print(f"Using full(): {arr6}")

    # Creating array using arange
    arr7 = vp.arange(5)
    arr8 = vp.arange(1,9,2)
    print(f"Using arange(5): {arr7}")
    print(f"Using arange(1,9,2): {arr8}")

    # Example 2: Basic Operations
    print("\n2. Basic Arithmetic Operations:")
    print("-" * 40)
    
    a = vp.array([10, 20, 30])
    b = vp.array([2, 4, 5])
    
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * b = {a * b}")
    print(f"a / b = {a / b}")
    print(f"a * 2 = {a * 2}")
    print(f"a + 2 = {a + 2}")
    print(f"a.b (dot) = {a.dot(b)}")

    # Example 3: Slicing Operations
    print("\n3. Slicing Operations:")
    print("-" * 40)
    data = vp.array([5, 10, 15, 20, 25])
    print(f"data[1:4]: {data[1:4]}")
    print(f"data[::-1]: {data[::-1]}")
    print(f"data[2:]: {data[2:]}")

    # Example 4: Statistical Operations
    print("\n4. Statistical Operations:")
    print("-" * 40)
    
    data = vp.array([5, 10, 15, 20, 25])
    print(f"Data: {data}")
    print(f"Sum: {data.sum()}")
    print(f"Mean: {data.mean()}")
    print(f"Min: {data.min()}")
    print(f"Max: {data.max()}")
    print(f"Std: {data.std():.2f}\n")
    data2 = vp.array([5, 10, 15, 20, 25, 5, 10])
    print(f"Data2: {data2}")
    print(f"Mode: {data2.mode()}")
    
    # Example 5: Advanced Operations
    print("\n5. Advanced Operations:")
    print("-" * 40)
    
    # Normalization
    values = vp.array([1, 2, 3, 4, 5])
    normalized = values.normalize()
    print(f"Original: {values}")
    print(f"Normalized: {normalized}")
    print(f"Normalized mean: {normalized.mean():.2f}")
    print(f"Normalized std: {normalized.std():.2f}\n")
    
    # Moving Average
    prices = vp.array([100, 105, 110, 115, 120, 125])
    ma = prices.moving_average(3)
    print(f"Prices: {prices}")
    print(f"3-day Moving Average: {ma}\n")

    # Difference between consecutive terms
    arr = vp.array([1, 3, 5, 7, 9])
    dif = arr.diff()
    print(f"array: {arr}")
    print(f"Difference between consecutive terms: {dif}\n")
    
    # Cumulative Sum
    arr = vp.array([1, 2, 3, 4, 5])
    csum = arr.cumulative_sum()
    print(f"array: {arr}")
    print(f"Cumulative sum: {csum}\n")

    # MinMax Scale [0, 1]
    arr = vp.array([10, 20, 30, 40, 50])
    mms = arr.minmax_scale()
    print(f"array: {arr}")
    print(f"MinMax Scale: {mms}\n")

    # Clip
    arr = vp.array([-5, 0, 50, 100, 150])
    cd = arr.clip(0, 100)
    print(f"array: {arr}")
    print(f"Clipped data: {cd}\n")

    # Example 6: Array Manipulation
    print("\n6. Array Manipulation:")
    print("-" * 40)
    
    arr = vp.array([1, 2, 3, 2, 1, 4, 3])
    print(f"Original: {arr}")
    print(f"Unique: {arr.unique()}")
    print(f"Reversed: {arr.reverse()}")
    print(f"Shifted right: {arr.shift(1)}")
    print(f"Shifted left: {arr.shift(-1)}")
    
    # Example 7: Data Analysis
    print("\n7. Data Analysis:")
    print("-" * 40)
    
    # Find majority element
    votes = vp.array([2, 2, 3, 2, 4, 2, 2])
    try:
        winner = votes.majority_element()
        print(f"Votes: {votes}")
        print(f"Winner (Majority element): {winner}\n")
    except ValueError as e:
        print(f"Votes: {votes}")
        print(f"No majority: {e}\n")
    
    # Check monotonic
    increasing = vp.array([1, 2, 3, 4, 5])
    decreasing = vp.array([5, 4, 3, 2, 1])
    mixed = vp.array([1, 3, 2, 4])
    
    print(f"Increasing array: {increasing} -> Monotonic: {increasing.is_monotonic()}")
    print(f"Decreasing array: {decreasing} -> Monotonic: {decreasing.is_monotonic()}")
    print(f"Mixed array: {mixed} -> Monotonic: {mixed.is_monotonic()}")
    
    # Example 8: Explain Functionality
    print("\n8. Array Explanation:")
    print("-" * 40)
    
    sample = vp.array([10, 20, 30])
    print(sample)
    print("Array explanation:")
    sample.explain()
    
    print("\n" + "=" * 60)
    print("End of Basic Usage Examples")
    print("=" * 60)

if __name__ == "__main__":
    main()