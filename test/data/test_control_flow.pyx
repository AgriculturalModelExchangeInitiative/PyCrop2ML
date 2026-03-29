"""
Test CyML control flow structures
"""


def if_statement_basic(int x):
    """Test basic if statement"""
    cdef int result
    
    if x > 0:
        result = 1
    
    return result


def if_else_statement(int x):
    """Test if-else statement"""
    cdef int result
    
    if x >= 0:
        result = 1
    else:
        result = -1
    
    return result


def if_elif_else_statement(int score):
    """Test if-elif-else statement"""
    cdef str grade
    
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    
    return grade


def nested_if_statements(int x, int y):
    """Test nested if statements"""
    cdef int result
    
    if x > 0:
        if y > 0:
            result = 1
        else:
            result = 2
    else:
        if y > 0:
            result = 3
        else:
            result = 4
    
    return result


def conditional_expression(int x):
    """Test ternary/conditional expression"""
    cdef int result
    
    result = 1 if x > 0 else -1
    
    return result


def for_loop_range(int n):
    """Test for loop with range"""
    cdef int i, sum = 0
    
    for i in range(n):
        sum += i
    
    return sum


def for_loop_range_start_end(int start, int end):
    """Test for loop with start and end"""
    cdef int i, product = 1
    
    for i in range(start, end):
        product *= i
    
    return product


def for_loop_range_step(int start, int end, int step):
    """Test for loop with step"""
    cdef int i, count = 0
    
    for i in range(start, end, step):
        count += 1
    
    return count


def for_loop_list():
    """Test for loop iterating over list"""
    cdef intlist numbers = [1, 2, 3, 4, 5]
    cdef int item, sum = 0
    
    for item in numbers:
        sum += item
    
    return sum


def for_loop_enumerate():
    """Test for loop with enumerate"""
    cdef intlist values = [10, 20, 30, 40, 50]
    cdef int index, value, sum = 0
    
    for index, value in enumerate(values):
        sum += index * value
    
    return sum


def while_loop_basic(int n):
    """Test basic while loop"""
    cdef int count = 0
    
    while count < n:
        count += 1
    
    return count


def while_loop_condition(int n):
    """Test while loop with complex condition"""
    cdef int i = 0, sum = 0
    
    while i < n and sum < 100:
        sum += i
        i += 1
    
    return sum


def loop_with_break(int n):
    """Test loop with break statement"""
    cdef int i, sum = 0
    
    for i in range(n):
        if sum > 50:
            break
        sum += i
    
    return sum


def loop_with_continue(int n):
    """Test loop with continue statement"""
    cdef int i, sum = 0
    
    for i in range(n):
        if i % 2 == 0:
            continue
        sum += i
    
    return sum


def loop_with_break_continue(int n):
    """Test loop with both break and continue"""
    cdef int i, sum = 0
    
    for i in range(n):
        if i % 3 == 0:
            continue
        if i > 20:
            break
        sum += i
    
    return sum


def nested_loops(int rows, int cols):
    """Test nested loops"""
    cdef int i, j, count = 0
    
    for i in range(rows):
        for j in range(cols):
            count += 1
    
    return count


def multiple_conditions(int x, int y):
    """Test multiple conditions with and/or"""
    cdef bool result
    
    if x > 0 and y > 0:
        result = True
    elif x < 0 or y < 0:
        result = False
    else:
        result = True
    
    return result
