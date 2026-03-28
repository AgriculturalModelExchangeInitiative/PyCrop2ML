# CyML Unit Tests

This directory contains comprehensive unit tests for the CyML language transpiler.

## Test Files

### Test Suite
- **test_cyml_operations.py** - Main test suite with comprehensive tests for all CyML language features

### Test Data (CyML Examples)
Located in `test/data/`:

- **test_modulo.pyx** - Examples and tests for modulo operation (%)
- **test_math_operations.pyx** - Mathematical functions and operations
- **test_control_flow.pyx** - Control flow structures (if, for, while, break, continue)
- **test_data_structures.pyx** - Lists, arrays, tuples, dictionaries
- **test_advanced_features.pyx** - Structs, enums, type conversions, and advanced features

## Running Tests

### Run all tests
```bash
cd /mnt/d/Docs/PyCropML_Old
python -m pytest test/test_cyml_operations.py -v
```

### Run specific test class
```bash
python -m pytest test/test_cyml_operations.py::TestCyMLOperations -v
```

### Run specific test for modulo
```bash
python -m pytest test/test_cyml_operations.py::TestCyMLModuloSpecific -v
```

### Run using unittest
```bash
python test/test_cyml_operations.py
```

## Test Coverage

The test suite covers:

### Basic Operations
- ✓ Arithmetic operations (+, -, *, /, **, %)
- ✓ Modulo operation (% operator and modulo() function)
- ✓ Comparison operators (==, !=, <, <=, >, >=)
- ✓ Boolean operators (and, or, not)
- ✓ Augmented assignment (+=, -=, *=, /=)
- ✓ Unary operators (+, -, not, ~)
- ✓ Membership operators (in, not in)
- ✓ Identity operators (is, is not)

### Control Flow
- ✓ If/elif/else statements
- ✓ Conditional expressions (ternary operator)
- ✓ For loops with range()
- ✓ For loops with enumerate()
- ✓ For-in loops
- ✓ While loops
- ✓ Break and continue statements

### Data Structures
- ✓ Lists (creation, indexing, slicing, methods)
- ✓ Arrays (fixed-size arrays)
- ✓ Tuples (creation, indexing, unpacking)
- ✓ Dictionaries (creation, access, methods)
- ✓ List comprehensions

### Functions
- ✓ Function definitions with typed parameters
- ✓ Return statements
- ✓ Multiple return values (tuples)
- ✓ Default parameters
- ✓ Recursive functions

### Advanced Features
- ✓ Struct definitions
- ✓ Enum definitions
- ✓ Type conversions (int, float, str)
- ✓ None type and checking
- ✓ Comments (single-line, inline)

### Mathematical Functions
- ✓ Trigonometric (sin, cos, tan, asin, acos, atan)
- ✓ Hyperbolic (sinh, cosh, tanh)
- ✓ Exponential and logarithmic (exp, log, sqrt, pow)
- ✓ Rounding (abs, ceil, floor, round)
- ✓ Aggregate (min, max, sum)
- ✓ Constants (pi)
- ✓ Special functions (isnan)

### String Operations
- ✓ String indexing
- ✓ String methods (index)
- ✓ String conversions

### Slicing and Indexing
- ✓ Index access (positive and negative)
- ✓ Slice operations (start:end, :end, start:, :)

## Test Data Files

Each `.pyx` file in `test/data/` contains multiple examples demonstrating specific CyML features:

### test_modulo.pyx
Contains 9 examples of modulo usage:
1. Basic modulo operation
2. Check if number is even
3. Check if number is odd
4. Get last digit of a number
5. Sum non-multiples in a loop
6. Categorize numbers by remainder
7. Complex modulo expressions
8. Modulo as function call
9. Modulo with augmented assignment

These files can be used for:
- Manual testing of transpilation
- Documentation examples
- Regression testing
- Learning CyML syntax

## Adding New Tests

To add new tests:

1. **Add test method to test_cyml_operations.py**:
   ```python
   def test_my_feature(self):
       """Test description"""
       code = """
   def my_function(int x):
       cdef int result
       result = x + 1
       return result
   """
       result = self._transpile_code(code)
       self.assertIsNotNone(result)
   ```

2. **Add example to appropriate .pyx file** in `test/data/`

3. **Run tests** to verify

## Known Issues

- Some complex cases may require adjustment based on transpiler capabilities
- File I/O tests are limited due to CyML constraints
- Class-based OOP is not fully supported (use structs instead)

## Notes

- Tests use both direct AST parsing and transpilation approaches
- The test suite is designed to validate that CyML constructs are properly recognized and transpiled
- Tests focus on syntax correctness rather than semantic execution
