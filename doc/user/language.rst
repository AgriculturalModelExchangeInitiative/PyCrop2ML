CyML Language Specification
===========================

This document specifies the CyML language, an extended Cython subset supported by PyCrop2ML 
for crop model development and transpilation.

.. highlight:: Cython


.. _language-file:
Cython file types
-----------------

* The implementation files, carrying a ``.pyx`` suffix.
* CyML is a subset of Cython with additional constraints to ensure transpilability across multiple languages.


.. _basic-types:

Basic Types
-----------

The following basic types are supported:

- ``bool`` - Boolean values (True/False)
- ``int`` - Integer values
- ``float`` - Single precision floating point
- ``double`` - Double precision floating point (treated as float in CyML)
- ``str`` - String values

.. _complex-types:

Complex Types
------------

The following complex types are supported:

- ``list`` - Dynamic list container (e.g., ``intlist`` for int list, ``floatlist`` for float list)
- ``array`` - Fixed-size array container (e.g., ``intarray``, ``floatarray``)
- ``tuple`` - Immutable sequence of elements
- ``dict`` - Dictionary/hash map (key-value pairs)
- ``datetime`` - Date and time values
- ``struct`` - User-defined composite types (C-like structures)
- ``enum`` - Enumeration types


.. _declarations:

Variable Declarations
---------------------

Variables must be declared with type annotations using ``cdef``:

::

    cdef int x
    cdef float temperature = 25.5
    cdef str name = "model"
    cdef bool is_valid = True
    cdef intlist values
    cdef floatarray[10] temperatures

Arrays can be declared with or without size specification:

::

    cdef float array1[]           # Dynamic size
    cdef int array2[100]          # Fixed size
    cdef floatarray data[n]       # Size from variable


.. _imports:

Import Statements
-----------------

CyML supports importing modules and functions:

::

    import math
    from math import sin, cos, pi
    from datetime import datetime

Supported import namespaces include ``math``, ``datetime``, and ``typing``.


.. _conditional-statements:

Conditional Statements
----------------------

CyML supports standard conditional statements:

**IF Statement**

::

    if condition:
        # code block

**IF/Else Statement**

::

    if condition:
        # code block
    else:
        # alternative code block

**IF/ElseIf/Else Statement**

::

    if condition1:
        # code block 1
    elif condition2:
        # code block 2
    else:
        # code block 3

The ``elif`` and ``else`` clauses are optional. An ``if`` statement can appear
anywhere that a normal statement or declaration can appear.

**Conditional Expressions (Ternary Operator)**

CyML also supports inline conditional expressions:

::

    result = true_value if condition else false_value


.. _loops:

Loops
-----

Integer For Loops
^^^^^^^^^^^^^^^^^

CyML recognises the usual Python for-in-range integer loop pattern::


    for i in range(n):
        ...

    for i in range(f, n):
        ...

    for i in range(f, n, s):
        ...

Where ``f`` is the start value, ``n`` is the end value (exclusive), and ``s`` is the step.

**For-in Loop**

Iterate over sequences (lists, arrays, tuples):

::

    for item in my_list:
        # process item

**For Loop with Index**

Use ``enumerate()`` to get both index and value:

::

    for index, value in enumerate(my_list):
        # process index and value


While Loop
^^^^^^^^^^

Standard Python-style while loop:

::

    while condition:
        # code block

Like other Python looping statements, ``break`` and ``continue`` may be used in the
body, without ``else`` clause statement.

**Break Statement**

Exit the loop immediately:

::

    while True:
        if condition:
            break

**Continue Statement**

Skip to the next iteration:

::

    for i in range(10):
        if i % 2 == 0:
            continue
        # process odd numbers only


.. _comprehensions:

List Comprehensions
-------------------

CyML supports list comprehensions for creating lists from iterables:

::

    squares = [x**2 for x in range(10)]
    evens = [x for x in range(20) if x % 2 == 0]
    

.. _functions:

Function Definitions
--------------------

Functions are defined with typed parameters and can return values:

::

    def calculate_sum(int a, int b):
        cdef int result
        result = a + b
        return result

**Parameters**

- All parameters must have type annotations
- Default values are supported for optional parameters

::

    def greet(str name, str prefix = "Hello"):
        return prefix + " " + name

**Return Statements**

Functions can return single or multiple values:

::

    def fibonacci(int n):
        if n <= 2:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

**Multiple Return Values (Tuples)**

::

    def get_min_max(floatlist values):
        cdef float min_val, max_val
        min_val = min(values)
        max_val = max(values)
        return min_val, max_val
    
    # Usage with tuple unpacking
    cdef float low, high
    low, high = get_min_max(data)


.. _function-calls:

Call Functions
--------------

- Calls to CyML functions are supported if the function:
  - is defined in the same module
  - is accessible from import statement

::

    cdef float result
    result = calculate_sum(10, 20)


.. _structs-enums:

Structures and Enumerations
----------------------------

**Structures (Records)**

Define composite types using C-style structs:

::

    cdef struct Point:
        float x
        float y
        float z

    # Usage
    cdef Point p
    p.x = 1.0
    p.y = 2.0
    p.z = 3.0

**Enumerations**

Define enumeration types:

::

    cdef enum Color:
        RED = 0
        GREEN = 1
        BLUE = 2
    
    # Or with automatic numbering
    cdef enum Status:
        PENDING
        RUNNING
        COMPLETED


.. _none-type:

None Type
---------

CyML supports None values and checking for None:

::

    cdef object value = None
    
    if value is None:
        # handle None case
    
    if value is not None:
        # value is not None


.. _operators:

Operators
---------

**Assignment**

========== =========
Assign     ``b = a``
========== =========

**Unary operators**

========== =========
UAdd       ``+a``
USub       ``-a``
Not        ``not a``
Invert     ``~a``
========== =========

**Binary operators**

============ ============
Add          ``a + b``
Sub          ``a - b``
Mult         ``a * b``
Div          ``a / b``
Pow          ``a ** b``
Mod          ``a % b``   (integers only)
BitOr        ``a | b``
BitAnd       ``a & b``
============ ============

.. note::
   The modulo operator ``%`` only works with integer operands. For floating-point modulo,
   you must convert to integers first or use a different approach.

**Augmented assign statements**

=========== ===========
AugAdd      ``a += b``
AugSub      ``a -= b``
AugMult     ``a *= b``
AugDiv      ``a /= b``
=========== ===========

**Comparison Operators**

=========== ===========
Eq          ``a == b``
NotEq       ``a != b``
Lt          ``a < b``
LtE         ``a <= b``
Gt          ``a > b``
GtE         ``a >= b``
Is          ``a is b``
IsNot       ``a is not b``
=========== ===========

**Boolean Operators**

=========== ============
And         ``a and b``
Or          ``a or b``
Not         ``not a``
=========== ============

**Membership Operators**

=========== ======================
In          ``item in collection``
NotIn       ``item not in collection``
=========== ======================


.. _indexing-slicing:

Indexing and Slicing
--------------------

**Index Access**

Access elements by index (0-based):

::

    cdef intlist values = [1, 2, 3, 4, 5]
    cdef int first = values[0]
    cdef int last = values[4]
    
    # Negative indexing supported
    cdef int from_end = values[-1]  # Last element

**Slice Access**

Extract subsequences using slice notation:

::

    cdef intlist numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # Slice from index to end
    cdef intlist tail = numbers[5:]     # [5, 6, 7, 8, 9]
    
    # Slice from start to index
    cdef intlist head = numbers[:5]     # [0, 1, 2, 3, 4]
    
    # Slice with start and end
    cdef intlist middle = numbers[2:7]  # [2, 3, 4, 5, 6]
    
    # Full slice (copy)
    cdef intlist copy = numbers[:]      # All elements

**Dictionary Access**

::

    cdef dict[str, int] ages = {"Alice": 30, "Bob": 25}
    cdef int alice_age = ages["Alice"]
    cdef int bob_age = ages.get("Bob")


.. _collections:

Collection Operations
---------------------

**Lists**

::

    cdef intlist numbers = []
    cdef floatlist values = [1.0, 2.5, 3.7]
    
    # List operations
    numbers.append(5)           # Add element
    values.extend([4.2, 5.8])   # Add multiple elements
    cdef int last = numbers.pop()  # Remove and return last element
    cdef int length = len(numbers) # Get length
    cdef float total = sum(values) # Sum all elements
    
    # Check membership
    if 5 in numbers:
        # element found
    
    if 10 not in numbers:
        # element not found
    
    # Find index
    cdef int idx = numbers.index(5)

**Arrays**

Arrays are similar to lists but fixed-size:

::

    cdef floatarray[10] temps
    cdef int size = len(temps)
    temps.append(23.5)

**Tuples**

Immutable sequences:

::

    cdef tuple coords = (1.0, 2.0, 3.0)
    cdef float x = coords[0]
    cdef int tuple_len = len(coords)

**Dictionaries**

Key-value mappings:

::

    cdef dict[str, float] data = {"temp": 25.5, "humidity": 60.0}
    
    # Dictionary operations
    cdef int dict_len = len(data)
    cdef list keys = data.keys()
    cdef float temp = data.get("temp")
    
    # Adding/updating entries
    data["pressure"] = 1013.25


.. _type-conversions:

Type Conversions
----------------

CyML supports explicit type conversions between basic types:

::

    cdef float x = 3.14
    cdef int i = int(x)        # Convert float to int (truncation)
    
    cdef int y = 42
    cdef float f = float(y)    # Convert int to float
    cdef float d = double(y)   # Convert int to double (treated as float)
    
    cdef str s = "123"
    cdef int n = int(s)        # Parse string to int

**String Methods**

::

    cdef str text = "Hello World"
    cdef int pos = text.index("World")  # Find substring position
    cdef int n = int(text)              # Convert to int (if valid)


.. _math-functions:

Mathematical Functions
----------------------

**Constants**

============================ ===========================================
``pi``                       Mathematical constant π (3.14159...)
============================ ===========================================

To use mathematical constants, import from math:

::

    from math import pi
    cdef float circumference = 2 * pi * radius


**Trigonometric Functions**

All trigonometric functions work with radians:

============================= =======================================================================================
``sin(x)``                    Trigonometric sine, element-wise.
``cos(x)``                    Cosine element-wise.
``tan(x)``                    Compute tangent element-wise.
``asin(x)``                   Inverse sine (arcsin), element-wise. Returns value in [-π/2, π/2].
``acos(x)``                   Inverse cosine (arccos), element-wise. Returns value in [0, π].
``atan(x)``                   Inverse tangent (arctan), element-wise. Returns value in [-π/2, π/2].
============================= =======================================================================================

**Hyperbolic Functions**

============================= =======================================================================================
``sinh(x)``                   Hyperbolic sine, element-wise.
``cosh(x)``                   Hyperbolic cosine, element-wise.
``tanh(x)``                   Hyperbolic tangent element-wise.
============================= =======================================================================================

**Exponential and Logarithmic Functions**

============================= =======================================================================================
``exp(x)``                    Exponential function (e^x).
``log(x)``                    Natural logarithm (base e).
``ln(x)``                     Natural logarithm (alias for log).
``sqrt(x)``                   Square root.
``pow(x, y)``                 Power function (x^y). Can also use ``x ** y``.
============================= =======================================================================================

**Rounding and Numeric Functions**

============================= =======================================================================================
``abs(x)``                    Absolute value.
``ceil(x)``                   Ceiling function (smallest integer ≥ x).
``floor(x)``                  Floor function (largest integer ≤ x).
``round(x)``                  Round to nearest integer.
``isnan(x)``                  Check if value is NaN (Not a Number).
============================= =======================================================================================

**Aggregate Functions**

============================= =======================================================================================
``min(a, b)``                 Minimum of two values.
``max(a, b)``                 Maximum of two values.
``min(list)``                 Minimum value in a list/array (when used as method).
``max(list)``                 Maximum value in a list/array (when used as method).
``sum(list)``                 Sum of all elements in list/array.
``mean(list)``                Mean (average) of all elements in list/array.
``count(list)``               Count of elements in list/array.
============================= =======================================================================================

**Example Usage**

::

    from math import sin, cos, pi, sqrt, exp, log
    
    cdef float angle = pi / 4
    cdef float x = sin(angle)
    cdef float y = cos(angle)
    
    cdef float hypotenuse = sqrt(3.0**2 + 4.0**2)
    cdef float logarithm = log(100.0)
    cdef float exponential = exp(2.0)
    
    cdef int absolute = abs(-42)
    cdef float rounded = round(3.7)
    cdef int ceiling = ceil(3.2)
    cdef int floored = floor(3.9)
    
    # Check for NaN
    cdef float invalid = 0.0 / 0.0
    if isnan(invalid):
        # Handle NaN value


.. _datetime-support:

DateTime Support
----------------

CyML supports datetime objects and operations:

::

    from datetime import datetime
    
    cdef datetime now = datetime(2024, 3, 15, 10, 30, 0)
    cdef int day = now.day


.. _utility-functions:

Utility Functions
-----------------

**System Functions**

============================= =======================================================================================
``copy(obj)``                 Create a copy of an object (for lists/arrays).
============================= =======================================================================================

**Example**

::

    cdef intlist original = [1, 2, 3, 4, 5]
    cdef intlist duplicate = copy(original)


.. _comments:

Comments
--------

CyML supports Python-style comments:

::

    # This is a single-line comment
    
    cdef int x = 5  # Inline comment
    
    """
    Multi-line comments can be used
    in function definitions and at
    module level as docstrings.
    """


.. _units-support:

Units Support
-------------

CyML has built-in support for physical units (experimental feature):

::

    cdef float temp = 25.5 * degC
    cdef float distance = 100.0 / m
    
    # Units are propagated through calculations
    cdef float result = temp + 5.0 * degC


.. _best-practices:

Best Practices and Limitations
-------------------------------

**Type Consistency**

- Once a variable is declared with a type, that type cannot be changed
- All function parameters must be explicitly typed
- Return types should be consistent with function signature

**Supported Features**

CyML is designed for transpilation, so it supports a subset of Cython/Python features:

- ✓ Basic types and operations
- ✓ Control flow (if/elif/else, for, while)
- ✓ Functions with typed parameters
- ✓ Lists, arrays, tuples, dictionaries
- ✓ Mathematical operations and functions
- ✓ Structures and enumerations
- ✓ List comprehensions
- ✓ Multiple return values (tuples)

**Limitations**

- Classes are not fully supported (use structs instead)
- Some advanced Python features are not available
- File I/O is limited
- Not all Python standard library modules are supported

**Code Organization**

- Keep functions focused and single-purpose
- Use meaningful variable names
- Add comments for complex logic


Testing CyML Code
-----------------

The PyCropML project includes comprehensive unit tests for CyML language features.

**Running Tests**

The test suite can be run using either pytest or unittest:

**Using pytest** (recommended for detailed output):

.. code-block:: bash

    # Run all tests in a file with verbose output
    python -m pytest test/test_cyml_operations.py -v
    
    # Run all tests in a specific test class
    python -m pytest test/test_cyml_operations.py::TestCyMLOperations -v
    
    # Run a single specific test
    python -m pytest test/test_cyml_operations.py::TestCyMLOperations::test_modulo_operation -v

**Using unittest** (built-in Python test framework):

.. code-block:: bash

    # Run all tests from the test directory
    cd test
    python -m unittest test_cyml_operations
    
    # Run tests in a specific class
    python -m unittest test_cyml_operations.TestCyMLOperations
    
    # Run a single specific test
    python -m unittest test_cyml_operations.TestCyMLOperations.test_modulo_operation

**Test Organization**

The test suite is organized into three main test classes:

- ``TestCyMLOperations``: Comprehensive tests for all CyML language features (30+ tests)
- ``TestCyMLModuloSpecific``: Detailed tests for modulo operations and error messages
- ``TestCyMLDataFiles``: Tests for transpiling complete .pyx files from test/data/

**Writing New Tests**

When adding new CyML features, write tests that verify:

1. **Successful transpilation**: Code transpiles without errors
2. **Type checking**: Type errors are caught and reported clearly
3. **Multiple languages**: Features work across target languages (py, cs, java, cpp, f90)

Example test structure:

.. code-block:: python

    def test_new_feature(self):
        """Test description of what feature does"""
        code = """
    def test_function():
        cdef int x = 42
        return x
    """
        result = self._transpile_code(code)
        self.assertIsNotNone(result)
- Declare all variables at the start of functions when possible