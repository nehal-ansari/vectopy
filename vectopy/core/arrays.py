from ._internals import ShapeError, DtypeError, _check_same_shape

class VectoPyArray:
  """The core 1-dimensional array object."""

  def __init__(self, shape, dtype=float, buffer=None):
    if len(shape) != 1:
      raise ShapeError("VectoPyArray only supports 1-dimensional arrays.")
    self._shape = tuple(shape)
    self._dtype = dtype
    self._size = shape[0]
    self._data = list(buffer) if buffer is not None else [dtype(0)] * self._size

  @property
  def shape(self):
    return self._shape
  
  @property
  def dtype(self):
    return self._dtype
  
  @property
  def data(self):
    """Direct access to the underlying Python list. For educational purposee."""
    return self._data
  
  def __str__(self):
    return f"VectoPyArray({self._data}, dtype={self._dtype})"
  
  def __repr__(self):
    return self.__str__()
  
  def __len__(self):
    return self._size
  
  def __getitem__(self, index):
    if isinstance(index, slice):
      # Return a new VectoPyArray for slices
      return VectoPyArray((len(self._data[index]),), self._data, buffer=self._data[index])
    return self._data[index]
  
  def __eq__(self, other):
    if not isinstance(other, VectoPyArray):
      return False
    return self._data == other.data and self._dtype == other.dtype
  
  def _element_wise_operation(self, other, op):
    """Helper for element-wise operations."""
    if isinstance(other, (int, float)):
      result_data = [op(x, other) for x in self._data]
      # Determine appropriate dtype for result
      result_dtype = float if(isinstance(other, float) or self._dtype is float) else self._dtype
      return VectoPyArray(self.shape, dtype=result_dtype, buffer=result_data)
    elif isinstance(other, VectoPyArray):
      _check_same_shape(self, other)
      result_data = [op(x, y) for x, y in zip(self._data, other.data)]
      #Determinig the resulting dtype: float if eaither operand is float
      result_dtype = float if (self._dtype is float or other.dtype is float) else self._dtype
      return VectoPyArray(self.shape, dtype=result_dtype, buffer=result_data)
    else:
      raise TypeError(f"Unsupported operand type(s): 'VectoPyArray' and '{type(other).__name__}'")
    
  def __add__(self, other):
    return self._element_wise_operation(other, lambda x, y: x + y)
  
  def __sub__(self, other):
    return self._element_wise_operation(other, lambda x, y: x - y)
  
  def __mul__(self, other):
    return self._element_wise_operation(other, lambda x, y: x * y)
  
  def __truediv__(self, other):
    return self._element_wise_operation(other, lambda x, y: x / y)
  
  def dot(self, other):
    """Dot product of two arrays."""
    _check_same_shape(self, other)
    return sum(x * y for x, y in zip(self._data, other.data))