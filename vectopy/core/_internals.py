class ShapeError(Exception):
    """Raised for operations involving incompatible shapes."""
    pass

class DtypeError(Exception):
    """Raised for operations involving incompatible data types."""
    pass

def _check_same_shape(a, b):
    """Helper function to check if two arrays have the same shape."""
    if a.shape != b.shape:
        raise ShapeError(f"Operands must have the same shape. Got {a.shape} and {b.shape}.")
    
