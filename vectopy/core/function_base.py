from .arrays import VectoPyArray

def array(obj, dtype=None):
  """Create an VectoPyArray from a sequence."""
  if not hasattr(obj, '__len__'):
    raise TypeError("Input object must be a sequence.")
  if not obj:
    raise ValueError("Cannot create an array from an empty sequence.")
  if dtype is None:
    # Make whole list of type float if any element of list is float
    dtype = float if any(isinstance(x, float) for x in obj) else int
    # Convert all elements to the chosen dtype
    converted_data = [dtype(x) for x in obj]
  return VectoPyArray((len(obj),), dtype=dtype, buffer=converted_data)

def zeros(shape, dtype=float):
  """Return a new array of given shape and type, filled with zeros."""
  return VectoPyArray((shape,), dtype=dtype)

def ones(shape, dtype=float):
  """Return a new array of given shape and type, filled with ones"""
  return VectoPyArray((shape,), dtype=dtype, buffer=[dtype(1)] * shape)
  
def full(shape, fill_value, dtype=None):
  """Return a new array of given shape and type, filled with 'fill_value'"""
  dtype = type(fill_value) if dtype is None else dtype
  return VectoPyArray((shape,), dtype=dtype, buffer=[dtype(fill_value)] * shape)

def arange(start, stop=None, step=1, dtype=None):
  """Return evenly spaced value within a given interval."""
  if stop is None:
    start, stop = 0, start
  data = list(range(start, stop, step))
  if not data:
    raise ValueError("arange: empty range for given start, stop, and step")
  if dtype is None:
    dtype = type(data[0])
  return VectoPyArray((len(data),), dtype=dtype, buffer=data) 