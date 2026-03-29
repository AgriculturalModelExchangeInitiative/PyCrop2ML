"""
Test CyML modulo operation examples

These are simple CyML code examples that demonstrate modulo usage
"""

# Example 1: Basic modulo operation
def modulo_basic(int a, int b):
    """Calculate remainder of a divided by b"""
    cdef int remainder
    remainder = a % b
    return remainder


# Example 2: Check if number is even
def is_even(int n):
    """Check if a number is even using modulo"""
    cdef bool result
    result = (n % 2 == 0)
    return result


# Example 3: Check if number is odd
def is_odd(int n):
    """Check if a number is odd using modulo"""
    return n % 2 != 0


# Example 4: Get last digit
def get_last_digit(int number):
    """Get the last digit of a number"""
    cdef int digit
    digit = number % 10
    return digit


# Example 5: Modulo in loop with continue
def sum_non_multiples(int n, int divisor):
    """Sum numbers from 0 to n that are not multiples of divisor"""
    cdef int i, total = 0
    for i in range(n):
        if i % divisor == 0:
            continue
        total += i
    return total


# Example 6: Modulo with conditional
def categorize_number(int n):
    """Categorize number based on remainder when divided by 3"""
    cdef int category
    if n % 3 == 0:
        category = 0
    elif n % 3 == 1:
        category = 1
    else:
        category = 2
    return category


# Example 7: Modulo in complex expression
def complex_modulo(int x, int y):
    """Complex expression with modulo"""
    cdef int result
    result = (x % y + y) % y  # Ensure positive remainder
    return result


# Example 8: Modulo with augmented assignment
def process_with_modulo(int value, int mod):
    """Process value using modulo with augmented assignment"""
    cdef int result = value
    result %= mod
    return result
