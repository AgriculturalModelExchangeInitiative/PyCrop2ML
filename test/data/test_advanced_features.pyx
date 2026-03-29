"""
Test CyML advanced features: structs, enums, type conversions
"""
from math import *

# Test struct definition
cdef struct Point2D:
    float x
    float y


cdef struct Point3D:
    float x
    float y
    float z


cdef struct Person:
    str name
    int age
    float height


def struct_basic_usage():
    """Test basic struct usage"""
    cdef Point2D p
    
    p.x = 10.0
    p.y = 20.0
    
    return p.x


def struct_3d_point():
    """Test 3D point struct"""
    cdef Point3D point
    cdef float distance
    
    point.x = 3.0
    point.y = 4.0
    point.z = 5.0
    
    # Calculate distance from origin
    distance = sqrt(point.x**2 + point.y**2 + point.z**2)
    
    return distance


def struct_with_mixed_types():
    """Test struct with mixed types"""
    cdef Person person
    
    person.name = "Alice"
    person.age = 30
    person.height = 1.65
    
    return person.age


# Test enum definition
cdef enum Color:
    RED = 0
    GREEN = 1
    BLUE = 2


cdef enum Status:
    PENDING = 0
    RUNNING = 1
    COMPLETED = 2
    FAILED = 3


def enum_basic_usage():
    """Test basic enum usage"""
    cdef Color c
    
    c = RED
    
    return c


def enum_in_conditional():
    """Test enum in conditional statement"""
    cdef int status
    cdef str message
    
    if status == PENDING:
        message = "Waiting"
    elif status == RUNNING:
        message = "Processing"
    elif status == COMPLETED:
        message = "Done"
    else:
        message = "Error"
    
    return message


def type_conversion_int_float():
    """Test int to float and float to int conversions"""
    cdef int i = 42
    cdef float f = 3.14
    cdef float f_from_i
    cdef int i_from_f
    
    f_from_i = float(i)
    i_from_f = int(f)
    
    return i_from_f


def type_conversion_string_int():
    """Test string to int conversion"""
    cdef str s = "123"
    cdef int n
    
    n = int(s)
    
    return n


def type_conversion_string_float():
    """Test string to float conversion"""
    cdef str s = "3.14"
    cdef float f
    
    f = float(s)
    
    return f


def none_type_checking():
    """Test None type checking (using bool flag pattern)"""
    cdef bool has_value = False
    cdef bool is_none
    
    if not has_value:
        is_none = True
    else:
        is_none = False
    
    return is_none


def none_type_is_not():
    """Test is not None checking (using bool flag pattern)"""
    cdef bool has_value = True
    cdef bool is_not_none
    
    if has_value:
        is_not_none = True
    else:
        is_not_none = False
    
    return is_not_none


def string_index_method():
    """Test string index method"""
    cdef str text = "Hello World"
    cdef int pos
    
    pos = text.index("World")
    
    return pos


def comparison_operators(int a, int b):
    """Test all comparison operators"""
    cdef bool eq, neq, lt, lte, gt, gte
    
    eq = (a == b)
    neq = (a != b)
    lt = (a < b)
    lte = (a <= b)
    gt = (a > b)
    gte = (a >= b)
    
    return eq


def boolean_operators(bool a, bool b):
    """Test boolean operators"""
    cdef bool and_result, or_result, not_result
    
    and_result = a and b
    or_result = a or b
    not_result = not a
    
    return and_result


def bitwise_operators(int a, int b):
    """Test bitwise operators"""
    cdef int bit_or, bit_and
    
    bit_or = a | b
    bit_and = a & b
    
    return bit_or


def comments_test():
    """Test that comments are properly handled"""
    # This is a single-line comment
    cdef int x = 5  # Inline comment
    
    # Multiple comment lines
    # can be used
    
    return x


def default_parameters(int value, float multiplier = 2.0):
    """Test function with default parameters"""
    cdef float result
    
    result = float(value) * multiplier
    
    return result


def recursive_function(int n):
    """Test recursive function (Fibonacci)"""
    if n <= 1:
        return n
    else:
        return recursive_function(n-1) + recursive_function(n-2)


def function_with_multiple_params(int a, int b, int c, int d):
    """Test function with multiple parameters"""
    cdef int sum
    
    sum = a + b + c + d
    
    return sum


def complex_expression(int x, int y, int z):
    """Test complex expression with multiple operators"""
    cdef int result
    
    result = (x + y) * z - (x % y) + (y / z if z != 0 else 0)
    
    return result


def nan_check():
    """Test NaN checking"""
    cdef float invalid = 0.0 / 0.0
    cdef bool is_invalid
    
    if isnan(invalid):
        is_invalid = True
    else:
        is_invalid = False
    
    return is_invalid
