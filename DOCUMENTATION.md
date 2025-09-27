# VectoPy - A Python Library (Documentation)

## 🔧 Array Creation

### `vp.array(data, dtype=None)`

Create a VectoPyArray from a list, tuple, range or vectopy itself.

```python
# From list
arr1 = vp.array([1, 2, 3, 4, 5])

# From tuple  
arr2 = vp.array((1, 2, 3))

# From range
arr3 = vp.array(range(2,10,2))

# From VectoPy
arr4 = vp.array((1, 2, 3))
arr5 = vp.array(arr) 

# With specific data type
arr6 = vp.array([1.5, 2.5, 3.5], dtype=float)
```

**Important Note:** You cannot create empty vector arrays using 'vp.array()' or 'vp.array([])' with empty Python lists. You must have atleat one element while creating the array. Also VectoPyArray can have elements of either float dtype or int dtype, can't be mixed.

### `vp.zeros(shape, dtype=float)`
Create an array filled with zeros.
```python
zeros_arr = vp.zeros(5)  # [0, 0, 0, 0, 0]
```

### `vp.ones(shape, dtype=float)`
Create an array filled with ones.

```python
ones_arr = vp.ones(3)  # [1, 1, 1]
```

### `vp.full(shape, fill_value, dtype=None)`
Create an array filled with a specific value.

```python
full_arr = vp.full(4, 7)  # [7, 7, 7, 7]
```

### `vp.arange(stop) or vp.arange(start, stop, step=1, dtype=None)`
Create an array with a range of values.

```python
arr1 = vp.arange(5)      # [0, 1, 2, 3, 4]
arr2 = vp.arange(1, 10, 2)  # [1, 3, 5, 7, 9]
```

## ➕ Basic Operations

### Element-wise Arithmetic `+-/*`
VectoPyArray supports element-wise operations with other arrays or scalars.

```python
a = vp.array([10, 20, 30])
b = vp.array([2, 4, 5])

print(a + b)   # [12, 24, 35] - Element-wise addition
print(a - b)   # [8, 16, 25]  - Element-wise subtraction  
print(a * b)   # [20, 80, 150] - Element-wise multiplication
print(a / b)   # [5.0, 5.0, 6.0] - Element-wise division (always returns float)

print(a + 2)   # [12, 22, 32] - Scalar addition
print(a * 3)   # [30, 60, 90] - Scalar multiplication
```
**Note:** For element-wise operations, both the operands must be of same size. 

### Dot Product - `array.dot(other)`
Calculate the dot product of two arrays.

```python
a = vp.array([1, 2, 3])
b = vp.array([4, 5, 6])
dot_result = a.dot(b)  # 1*4 + 2*5 + 3*6 = 32
```

### Slicing and Indexing `[]`
Access elements using Python slicing syntax.

```python
arr = vp.array([5, 10, 15, 20, 25])

print(arr[2])       # 15 - Single element
print(arr[1:4])     # [10, 15, 20] - Slice
print(arr[::-1])    # [25, 20, 15, 10, 5] - Reverse
```

## 📊 Statistical Methods

### `array.sum()`
Calculate the sum of all elements.

```python
arr = vp.array([1, 2, 3, 4, 5])
total = arr.sum()  # 15
```

### `array.mean()`
Calculate the arithmetic mean.

```python
arr = vp.array([1, 2, 3, 4, 5])
average = arr.mean()  # 3.0
```

### `array.min()` and `array.max()`
Find the minimum and maximum values.

```python
arr = vp.array([5, 2, 8, 1, 9])
print(arr.min())  # 1
print(arr.max())  # 9
```

### `array.std()`
Calculate the standard deviation (measure of spread).

```python
arr = vp.array([1, 2, 3, 4, 5])
std_dev = arr.std()  # ≈1.41
```
### `array.median()`
Calculate the median (middle value) of the array elements.

```python
arr = vp.array([1, 3, 5, 7, 9])
median_val = arr.median()  # 5

arr_even = vp.array([1, 2, 3, 4, 5, 6])
median_even = arr_even.median()  # (3 + 4) / 2 = 3.5
```

### `array.mode()`
Find the most frequent value(s).

```python
arr = vp.array([5, 10, 15, 20, 25, 5, 10])
mode_val = arr.mode()  # [5, 10] (bimodal)
```

## 🧮 Advanced Operations

### `array.normalize()`
Normalize the array to have mean 0 and standard deviation 1 (Z-score normalization).

```python
arr = vp.array([1, 2, 3, 4, 5])
normalized = arr.normalize()
# Result: [-1.41, -0.71, 0, 0.71, 1.41] (approximately)
# Mean ≈ 0, Standard Deviation ≈ 1
```
**Mathematical Formula:** (x - mean) / std_dev

### `array.minmax_scale()`
Scale array values to the range [0, 1].

```python
arr = vp.array([10, 20, 30, 40, 50])
scaled = arr.minmax_scale()
# Result: [0.0, 0.25, 0.5, 0.75, 1.0]
```
**Mathematical Formula:** (x - min) / (max - min)

### `array.moving_average(window)`
Calculate moving average with specified window size.

```python
prices = vp.array([100, 105, 110, 115, 120, 125])
ma = prices.moving_average(3)
# Windows: [100,105,110]=105, [105,110,115]=110, [110,115,120]=115, [115,120,125]=120
# Result: [105, 110, 115, 120]
```

### `array.diff()`
Calculate differences between consecutive elements.

```python
arr = vp.array([1, 3, 5, 7, 9])
differences = arr.diff()
# Differences: [3-1=2, 5-3=2, 7-5=2, 9-7=2]
# Result: [2, 2, 2, 2]
```

### `array.cumulative_sum()`
Calculate cumulative sum (running total).

```python
arr = vp.array([1, 2, 3, 4, 5])
cum_sum = arr.cumulative_sum()
# Cumulative: [1, 1+2=3, 3+3=6, 6+4=10, 10+5=15]
# Result: [1, 3, 6, 10, 15]
```

### `array.clip(min_val, max_val)`
Clip values to be within specified range.

```python
arr = vp.array([-5, 0, 50, 100, 150])
clipped = arr.clip(0, 100)
# Values below 0 become 0, above 100 become 100
# Result: [0, 0, 50, 100, 100]
```

## 🔄 Array Manipulation

### `array.unique()`
Return array with duplicate elements removed.

```python
arr = vp.array([1, 2, 3, 2, 1, 4, 3])
unique_arr = arr.unique()
# Result: [1, 2, 3, 4] (order not guaranteed)
```

### `array.reverse()`
Return a reversed copy of the array.

```python
arr = vp.array([1, 2, 3, 4, 5])
reversed_arr = arr.reverse()
# Result: [5, 4, 3, 2, 1]
```

### `array.shift(periods=1)`
Shift elements by specified number of periods.

```python
arr = vp.array([1, 2, 3, 4, 5])

# Shift right (positive periods)
shifted_right = arr.shift(1)  # [0, 1, 2, 3, 4]

# Shift left (negative periods)  
shifted_left = arr.shift(-1)  # [2, 3, 4, 5, 0]
```

## 🔍 Data Analysis

### `array.majority_element()`
Find the majority element (appears more than half the time) using Boyer-Moore algorithm.

```python
votes = vp.array([2, 2, 3, 2, 4, 2, 2])
winner = votes.majority_element()  # 2 (appears 5/7 times)

# If no majority element, raises ValueError
mixed = vp.array([1, 2, 3, 1, 2, 3])
# mixed.majority_element()  # Raises ValueError
```

### `array.is_monotonic()`
Check if array is monotonic (non-decreasing or non-increasing).

```python
increasing = vp.array([1, 2, 3, 4, 5])
decreasing = vp.array([5, 4, 3, 2, 1])  
mixed = vp.array([1, 3, 2, 4])

print(increasing.is_monotonic())  # True
print(decreasing.is_monotonic())  # True  
print(mixed.is_monotonic())       # False
```

## ℹ️ Utility Methods

### `array.explain()`
Display detailed information about the array's properties and internals.

```python
arr = vp.array([10, 20, 30])
arr.explain()

# Output:
# VectoPyArray Metadata Explanation:
#   • Shape: (3,) - A 1-dimensional array with 3 elements.
#   • Dtype: <class 'int'> - Elements are Python int objects.
#   • Strides: (4,) - To move to the next element, step 4 bytes in memory (simulated).
#   • Base: None - This array owns its data (simulated).
#   • Underlying Data: [10, 20, 30]
#   • Memory Size: 12 bytes (simulated)
```

### Array Properties
```python
arr = vp.array([1, 2, 3, 4, 5])

print(arr.shape)    # (5,) - Array shape
print(arr.dtype)    # <class 'int'> - Data type
print(arr.data)     # [1, 2, 3, 4, 5] - Underlying list
print(len(arr))     # 5 - Number of elements
```
