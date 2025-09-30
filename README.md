# VectoPy - Pure Python Vector Operations Library

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Issues](https://img.shields.io/github/issues/nehalAnsari2000/vectopy)](https://github.com/nehalAnsari2000/vectopy/issues)

## What is VectoPy?

**Vectopy** is an educational vector operations library written in pure Python. It provides 1D array/vector functionality supporting only integer and float data types. This library is designed specifically for educational purposes to help understand how numerical computing libraries like NumPy are built from the ground up.

### Key Characteristics:
- 🎓 **Educational Focus**: Learn how numerical libraries are implemented
- 🐍 **Pure Python**: Written entirely in Python (no C extensions)
- ⚡ **1D Arrays Only**: Supports only 1-dimensional vectors/arrays
- 🔢 **Limited Data Types**: Only supports int and float elements
- 📚 **Thorough Testing**: Comprehensive test cases covering edge cases
- 🏎️ **Slower but Clear**: Prioritizes readability over performance

## Motivation

I've always been curious about how popular scientific computing libraries like NumPy and scikit-learn are implemented. This curiosity drove me to build **vectopy** from scratch to deeply understand:

- How array operations are implemented internally
- How to create a consistent API similar to production libraries
- How to write comprehensive test cases for numerical operations

While vectopy is slower than optimized libraries, it provides transparent, readable code that helps learners understand the fundamentals of numerical computing.

## Features

- **Vector Operations**: Addition, subtraction, multiplication, division, Dot product
- **Array Creations**: array(), ones(), zeros(), full(), arange(), slicing operators
- **Statistical Functions**: Sum, Max, Min, Mean, median, mode, variance, standard deviation
- **Time Series**: Moving Average, Diff(Difference between consecutive elements), Cumulative Sum(Prefix sum), Shift
- **Transformation**: Normalization(mean=0, std=1), Clip, Reverse, MinMax Scale[0, 1]
- **Algorithms**: Majority Element(Boyer-Moore algorithm), IsMonotonic, Unique
- **Educational Utilities**: Step-by-step operation explanations, explain() method
- **Comprehensive Testing**: Thorough test coverage for edge cases

- **📚 For detailed documentation, please check [DOCUMENTATION.md](DOCUMENTATION.md)**

## Installation

### Method 1: Install from GitHub (Recommended)

```bash
# Create and activate virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# OR
venv\Scripts\activate     # Windows

# Install vectopy directly from GitHub
pip install git+https://github.com/nehal-ansari/vectopy.git

# Verify installation:
python -c "import vectopy; print('vectopy imported successfully!')"
```

### Method 2: Clone and Install Locally
```bash
# Clone the repository
git clone https://github.com/nehal-ansari/vectopy.git
cd vectopy

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# OR
venv\Scripts\activate     # Windows

# Install dependencies and package
pip install -r requirements.txt
pip install -e .

# Verify installation:
python -c "import vectopy; print('vectopy imported successfully!')"
```


## Quick Start
```python
import vectopy as vp

# Create vectors
v1 = vp.array([1, 2, 3, 4, 5])
v2 = vp.array([6, 7, 8, 9, 10])

# Basic arithmetic operations
result_add = v1 + v2        # Vector addition
result_sub = v1 - v2        # Vector subtraction
result_mul = v1 * 2         # Scalar multiplication
result_div = v1 / 2         # Scalar division

# Mathematical operations
dot_product = v1.dot(v2)    # Dot product
normalized = v1.normalize() # Unit vector

# Display results
print(f"Addition: {result_add}")
print(f"Dot product: {dot_product}")
```

## Usage Examples
- Explore the **examples/** directory for comprehensive usage examples:
```bash
# Run basic usage example
python examples/01_basic_usage.py

# Run all examples
python examples/*.py
```

## Running Tests
- vectopy includes comprehensive tests to ensure reliability:
```bash
# Run all tests
python -m pytest vectory/tests/ -v

# Run specific test modules
python -m pytest vectopy/tests/test_array_creation.py -v
python -m pytest vectopy/tests/test_statistics.py -v
python -m pytest vectopy/tests/test_algorithms.py -v

# Run tests with coverage report
python -m pytest vectory/tests/ --cov=vectopy
```

## Requirements Management
The **requirements.txt** file contains all necessary dependencies:
```
build==1.3.0
colorama==0.4.6
iniconfig==2.1.0
packaging==25.0
pluggy==1.6.0
Pygments==2.19.2
pyproject_hooks==1.2.0
pytest==8.4.2
```

To freeze your current environment's requirements:
```bash
pip freeze > requirements.txt
```  
To install from requirements:
```bash
pip install -r requirements.txt
```

## Performance Note
⚠️ **Important:** vectopy is written in pure Python for educational purposes and is slower than optimized libraries like NumPy. It is not recommended for production use or large-scale computations. The focus is on code readability and educational value, not performance optimization.

## Contributing
I welcome contributions from fellow learners and educators! If you'd like to contribute:
1. Fork the repository
2. Create a feature branch  
   `git checkout -b feature/amazing-feature`
3. Commit your changes  
   `git commit -m 'Add amazing feature'`
4. Push to the branch  
   `git push origin feature/amazing-feature`
5. Open a Pull Request

Please ensure your code includes:
- ✅ Proper docstrings
- ✅ Comprehensive test cases 
- ✅ Educational comments where appropriate

## Learning Resources
If you're using vectopy to learn about library development:

1. Study the `VectoPyArray` class in `vectopy/core/arrays.py`
2. Look at how operator overloading is implemented (`__add__`, `__sub__`, etc.)
3. Examine the test cases to understand edge case handling
4. Read the educational functions to see how concepts are explained

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support
If you have questions, issues, or want to discuss library implementation:

- 📋 Open an issue on [GitHub Issues](https://github.com/nehal-ansari/vectopy/issues)
- 📧 Email me at: nehalansari3112@gmail.com
- 💬 Use vectopy as a learning resource for your own educational projects

## Acknowledgments
This project was inspired by:

- NumPy: For the API design and functionality reference. For understanding how to build libraries in python.
- Python's educational ecosystem: For promoting learning through building
- The open-source community: For making learning resources accessible

### Happy Learning! 🚀
*Remember: The goal isn't to build the fastest library, but to understand how libraries are built!*
