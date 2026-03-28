"""
Test CyML data structures: lists, arrays, tuples, dictionaries
"""


def list_operations_basic():
    """Test basic list operations"""
    cdef intlist numbers = [1, 2, 3, 4, 5]
    cdef int length, first, last
    
    length = len(numbers)
    first = numbers[0]
    last = numbers[4]
    
    return length


def list_append_extend():
    """Test list append and extend"""
    cdef intlist numbers = [1, 2, 3]
    cdef intlist more = [4, 5]
    
    numbers.append(4)
    numbers.extend(more)
    
    return len(numbers)


def list_pop_operation():
    """Test list pop operation"""
    cdef intlist numbers = [1, 2, 3, 4, 5]
    cdef int last
    
    last = numbers.pop(-1)
    
    return last


def list_index_operation():
    """Test list index method"""
    cdef intlist numbers = [10, 20, 30, 40, 50]
    cdef int idx
    
    idx = numbers.index(30)
    
    return idx


def list_membership():
    """Test membership operators with lists"""
    cdef intlist numbers = [1, 2, 3, 4, 5]
    cdef bool found, not_found
    
    if 3 in numbers:
        found = True
    
    if 10 not in numbers:
        not_found = True
    
    return found


def list_slicing():
    """Test list slicing operations"""
    cdef intlist numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    cdef intlist head, tail, middle, full
    
    head = numbers[:5]      # First 5 elements
    tail = numbers[5:]      # From index 5 to end
    middle = numbers[2:7]   # Elements 2 to 6
    full = numbers[:]       # Full copy
    
    return len(middle)


def list_aggregate_functions():
    """Test aggregate functions on lists"""
    cdef floatlist values = [1.5, 2.3, 3.7, 4.2, 5.1]
    cdef float total, minimum, maximum
    
    total = sum(values)
    minimum = min(values)
    maximum = max(values)
    
    return total


def list_comprehension_basic():
    """Test basic list comprehension"""
    cdef intlist squares
    cdef int x
    
    squares = [x**2 for x in range(10)]
    
    return sum(squares)


def list_comprehension_condition():
    """Test list comprehension with condition"""
    cdef intlist evens
    cdef int x
    
    evens = [x for x in range(20) if x % 2 == 0]
    
    return len(evens)


def array_declaration():
    """Test array declaration and usage"""
    cdef floatarray[10] temperatures
    cdef int size
    
    size = len(temperatures)
    
    return size


def array_initialization():
    """Test array initialization with values"""
    cdef intarray values
    cdef int total
    
    values = array('i', [1, 2, 3, 4, 5])
    total = sum(values)
    
    return total


def tuple_operations():
    """Test tuple operations"""
    cdef tuple coords = (1.0, 2.0, 3.0)
    cdef float x, y, z
    cdef int length
    
    x = coords[0]
    y = coords[1]
    z = coords[2]
    length = len(coords)
    
    return x


def tuple_unpacking():
    """Test tuple unpacking"""
    cdef tuple point = (10, 20, 30)
    cdef int x, y, z
    
    x, y, z = point
    
    return x + y + z


def multiple_return_values():
    """Test function returning multiple values (tuple)"""
    return 1, 2, 3


def use_multiple_returns():
    """Test using multiple return values"""
    cdef int a, b, c
    
    a, b, c = multiple_return_values()
    
    return a + b + c


def dict_basic_operations():
    """Test basic dictionary operations"""
    cdef dict[str, int] ages = {"Alice": 30, "Bob": 25, "Charlie": 35}
    cdef int alice_age, bob_age
    cdef int length
    
    alice_age = ages["Alice"]
    bob_age = ages.get("Bob")
    length = len(ages)
    
    return alice_age


def dict_keys_operation():
    """Test dictionary keys operation"""
    cdef dict[str, float] data = {"temp": 25.5, "humidity": 60.0}
    cdef list keys
    
    keys = data.keys()
    
    return len(keys)


def dict_update():
    """Test dictionary update/add"""
    cdef dict[str, int] scores = {"test1": 85, "test2": 90}
    
    scores["test3"] = 95  # Add new entry
    scores["test1"] = 88  # Update existing
    
    return scores["test3"]


def empty_list():
    """Test empty list creation"""
    cdef intlist numbers
    
    numbers.append(1)
    numbers.append(2)
    
    return len(numbers)


def empty_dict():
    """Test empty dictionary creation"""
    cdef dict[str, int] data
    
    data["key1"] = 10
    data["key2"] = 20
    
    return len(data)


def nested_list():
    """Test nested data structures"""
    cdef intlist list1 = [1, 2, 3]
    cdef intlist list2 = [4, 5, 6]
    cdef int sum1, sum2
    
    sum1 = sum(list1)
    sum2 = sum(list2)
    
    return sum1 + sum2
