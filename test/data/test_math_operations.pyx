"""
Test CyML arithmetic and mathematical operations
"""
from math import sin, cos, tan, sqrt, exp, log, abs, ceil, floor, round, pi


def arithmetic_operations(float a, float b):
    """Test all basic arithmetic operations"""
    cdef float add, sub, mul, div, power
    
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    power = a ** b
    
    return add


def unary_operations(float x):
    """Test unary operations"""
    cdef float pos, neg
    cdef bool not_val
    
    pos = +x
    neg = -x
    not_val = not (x > 0.0)
    
    return neg


def augmented_assignments(float value):
    """Test augmented assignment operators"""
    cdef float result = value
    
    result += 10.0
    result -= 5.0
    result *= 2.0
    result /= 3.0
    
    return result


def trigonometric_functions(float angle):
    """Test trigonometric functions"""
    cdef float sine, cosine, tangent
    
    sine = sin(angle)
    cosine = cos(angle)
    tangent = tan(angle)
    
    return sine


def exponential_logarithmic(float x):
    """Test exponential and logarithmic functions"""
    cdef float exponential, logarithm, square_root, power
    
    exponential = exp(x)
    logarithm = log(x)
    square_root = sqrt(x)
    power = pow(x, 2.0)
    
    return exponential


def rounding_functions(float x):
    """Test rounding and numeric functions"""
    cdef float absolute, rounded
    cdef int ceiling, floored
    
    absolute = abs(x)
    rounded = round(x)
    ceiling = ceil(x)
    floored = floor(x)
    
    return rounded


def min_max_operations(float a, float b):
    """Test min and max functions"""
    cdef float minimum, maximum
    
    minimum = min(a, b)
    maximum = max(a, b)
    
    return maximum


def aggregate_list_operations():
    """Test aggregate operations on lists"""
    cdef floatlist values = [1.5, 2.7, 3.2, 4.8, 5.1]
    cdef float total, average, minimum, maximum
    cdef int count
    
    total = sum(values)
    count = len(values)
    minimum = min(values)
    maximum = max(values)
    
    return total


def use_pi_constant():
    """Test using mathematical constant pi"""
    cdef float circumference, radius = 5.0
    
    circumference = 2.0 * pi * radius
    
    return circumference


def complex_math_expression(float x, float y):
    """Test complex mathematical expression"""
    cdef float result
    
    result = sqrt(x**2 + y**2) + sin(x) * cos(y) + log(abs(x) + 1.0)
    
    return result
