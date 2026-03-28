"""
Test CyML language constructs and operations

This test suite validates that CyML properly supports various language
features including arithmetic operations, comparisons, control flow, etc.
"""
from __future__ import absolute_import
from __future__ import print_function
import unittest
import tempfile
import os
from unittest.main import main
from pycropml.transpiler.main import Main


class TestCyMLOperations(unittest.TestCase):
    """Test suite for CyML language operations"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.temp_dir = tempfile.mkdtemp()
        self.test_files = {}
    
    def tearDown(self):
        """Clean up test files"""
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
    
    def _create_test_file(self, name, content):
        """Helper to create a test .pyx file"""
        filepath = os.path.join(self.temp_dir, name)
        with open(filepath, 'w') as f:
            f.write(content)
        return filepath
    
    def _transpile_code(self, code, target_lang='py'):
        """Helper to transpile CyML code to target language"""
        try:
            # Pass code directly to Main, not a file path
            cst = Main(code, target_lang)
            result = cst.parse()
            p = cst.to_ast(code)  # convert to ast
            return p
        except Exception as e:
            self.fail(f"Transpilation failed: {e}")
    
    def test_modulo_operation(self):
        """Test modulo operation (%) is properly supported"""
        code = """
def test_modulo(int a, int b):
    cdef int result
    result = a % b
    return result
"""
        result = self._transpile_code(code)
        self.assertIsNotNone(result)
        # Successful transpilation confirms modulo is supported
    
    def test_arithmetic_operations(self):
        """Test basic arithmetic operations"""
        code = """
def test_arithmetic(float a, float b):
    cdef float add_result, sub_result, mul_result, div_result, pow_result
    add_result = a + b
    sub_result = a - b
    mul_result = a * b
    div_result = a / b
    pow_result = a ** b
    return add_result
"""
        result = self._transpile_code(code)
        self.assertIsNotNone(result)
    
    def test_comparison_operations(self):
        """Test comparison operators"""
        code = """
def test_comparison(int a, int b):
    cdef bool eq, neq, lt, lte, gt, gte
    eq = (a == b)
    neq = (a != b)
    lt = (a < b)
    lte = (a <= b)
    gt = (a > b)
    gte = (a >= b)
    return eq
"""
        result = self._transpile_code(code)
        self.assertIsNotNone(result)
    
    def test_boolean_operations(self):
        """Test boolean operators (and, or, not)"""
        code = """
def test_boolean(bool a, bool b):
    cdef bool and_result, or_result, not_result
    and_result = a and b
    or_result = a or b
    not_result = not a
    return and_result
"""
        result = self._transpile_code(code)
        self.assertIsNotNone(result)
    
    def test_augmented_assignment(self):
        """Test augmented assignment operators (+=, -=, *=, /=)"""
        code = """
def test_augmented(float x):
    cdef float result = x
    result += 5.0
    result -= 2.0
    result *= 3.0
    result /= 2.0
    return result
"""
        result = self._transpile_code(code)
        self.assertIsNotNone(result)
    
    def test_if_statement(self):
        """Test if/elif/else statements"""
        code = """
def test_if(int value):
    cdef int result
    if value > 10:
        result = 1
    elif value > 5:
        result = 2
    else:
        result = 3
    return result
"""
        result = self._transpile_code(code)
        self.assertIsNotNone(result)
    
    def test_for_loop_range(self):
        """Test for loop with range"""
        code = """
def test_for(int n):
    cdef int i, sum = 0
    for i in range(n):
        sum += i
    return sum
"""
        result = self._transpile_code(code)
        self.assertIsNotNone(result)
    
    def test_for_loop_range_step(self):
        """Test for loop with range and step"""
        code = """
def test_for_step(int start, int end, int step):
    cdef int i, count = 0
    for i in range(start, end, step):
        count += 1
    return count
"""
        result = self._transpile_code(code)
        self.assertIsNotNone(result)
    
    def test_while_loop(self):
        """Test while loop"""
        code = """
def test_while(int n):
    cdef int count = 0
    while count < n:
        count += 1
    return count
"""
        result = self._transpile_code(code)
        self.assertIsNotNone(result)
    
    def test_break_continue(self):
        """Test break and continue statements"""
        code = """
def test_break_continue(int n):
    cdef int i, sum = 0
    for i in range(n):
        if i % 2 == 0:
            continue
        if i > 10:
            break
        sum += i
    return sum
"""
        result = self._transpile_code(code)
        self.assertIsNotNone(result)
    
    def test_list_operations(self):
        """Test list operations"""
        code = """
def test_list():
    cdef intlist numbers = [1, 2, 3, 4, 5]
    cdef int length, total
    length = len(numbers)
    total = sum(numbers)
    numbers.append(6)
    return total
"""
        result = self._transpile_code(code)
        self.assertIsNotNone(result)
    
    def test_array_declaration(self):
        """Test array declarations"""
        code = """
def test_array():
    cdef float temps[10] # declare a C-style array of 10 floats
    cdef int size
    size = len(temps)
    return size
"""
        result = self._transpile_code(code)
        self.assertIsNotNone(result)
    
    def test_tuple_operations(self):
        """Test tuple operations and unpacking"""
        code = """
def get_values():
    return 1, 2, 3

def test_tuple():
    cdef int a, b, c
    a, b, c = get_values()
    return a + b + c
"""
        result = self._transpile_code(code)
        self.assertIsNotNone(result)
    
    def test_dict_operations(self):
        """Test dictionary operations"""
        code = """
def test_dict():
    cdef dict[str, int] ages = {"Alice": 30, "Bob": 25}
    cdef int alice_age
    alice_age = ages["Alice"]
    return alice_age
"""
        result = self._transpile_code(code)
        self.assertIsNotNone(result)
    
    def test_math_functions(self):
        """Test mathematical functions"""
        code = """
from math import sin, cos, sqrt, exp, log, abs, ceil, floor

def test_math(float x):
    cdef float result
    result = sin(x) + cos(x)
    result = sqrt(x)
    result = exp(x)
    result = log(x)
    result = abs(x)
    return result
"""
        result = self._transpile_code(code)
        self.assertIsNotNone(result)
    
    def test_min_max_functions(self):
        """Test min and max functions"""
        code = """
def test_minmax(float a, float b):
    cdef float minimum, maximum
    minimum = min(a, b)
    maximum = max(a, b)
    return maximum
"""
        result = self._transpile_code(code)
        self.assertIsNotNone(result)
    
    def test_struct_definition(self):
        """Test struct/record definition"""
        code = """
cdef struct Point:
    float x
    float y
    float z

def test_struct():
    cdef Point p
    p.x = 1.0
    p.y = 2.0
    p.z = 3.0
    return p.x
"""
        result = self._transpile_code(code)
        print(result, flush=True)  # Debug print to check struct handling   
        self.assertIsNotNone(result)
    
    def test_enum_definition(self):
        """Test enum definition"""
        code = """
cdef enum Color:
    RED = 0
    GREEN = 1
    BLUE = 2

def test_enum():
    cdef int g
    g = Color.GREEN
    return g
"""
        result = self._transpile_code(code)
        self.assertIsNotNone(result)
    
    def test_conditional_expression(self):
        """Test ternary/conditional expression"""
        code = """
def test_ternary(int x):
    cdef int result
    result = 1 if x > 0 else -1
    return result
"""
        result = self._transpile_code(code)
        self.assertIsNotNone(result)
    
    def test_list_comprehension(self):
        """Test list comprehension"""
        code = """
def test_comprehension():
    cdef intlist squares
    cdef int x
    squares = [x**2 for x in range(10)]
    return sum(squares)
"""
        result = self._transpile_code(code)
        self.assertIsNotNone(result)
    
    def test_none_type(self):
        """Test None type and is/is not operators"""
        code = """
cdef struct Point:
    float x
    float y
    float z

def test_none(Point value):
    cdef bool is_none
    if value.x is None:
        is_none = True
    else:
        is_none = False
    return is_none
"""
        result = self._transpile_code(code)
        self.assertIsNotNone(result)
    
    def test_string_operations(self):
        """Test string operations"""
        code = """
def test_string():
    cdef str text = "Hello World"
    cdef int pos, n
    pos = text.index("He")
    n = int("123")
    return pos
"""
        result = self._transpile_code(code)
        self.assertIsNotNone(result)
    
    def test_type_conversions(self):
        """Test type conversion functions"""
        code = """
def test_conversions():
    cdef float x = 3.14
    cdef int i = int(x)
    cdef float f = float(42)
    cdef str s = "123"
    cdef int n = int(s)
    return i
"""
        result = self._transpile_code(code)
        self.assertIsNotNone(result)
    
    def test_enumerate(self):
        """Test enumerate in for loops"""
        code = """
def test_enumerate():
    cdef intlist values = [10, 20, 30, 40]
    cdef int index, value, sum = 0
    for index, value in enumerate(values):
        sum += index * value
    return sum
"""
        result = self._transpile_code(code)
        self.assertIsNotNone(result)
    
    def test_membership_operators(self):
        """Test membership operators (in, not in)"""
        code = """
def test_membership():
    cdef intlist numbers = [1, 2, 3, 4, 5]
    cdef bool found, not_found
    if 3 in numbers:
        found = True
    if 10 not in numbers:
        not_found = True
    return found
"""
        result = self._transpile_code(code)
        self.assertIsNotNone(result)
    
    def test_slicing(self):
        """Test slice operations"""
        code = """
def test_slicing():
    cdef intlist numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    cdef intlist head, tail, middle
    head = numbers[:5]
    tail = numbers[5:]
    middle = numbers[2:7]
    return len(middle)
"""
        result = self._transpile_code(code)
        self.assertIsNotNone(result)


class TestCyMLModuloSpecific(unittest.TestCase):
    """Specific detailed tests for modulo operation"""
    def _transpile_code(self, code, target_lang='py'):
        """Helper to transpile CyML code to target language"""
        try:
            # Pass code directly to Main, not a file path
            cst = Main(code, target_lang)
            result = cst.parse()
            p = cst.to_ast(code)  # convert to ast
            return p
        except Exception as e:
            self.fail(f"Transpilation failed: {e}")   
             
    def test_modulo_with_literals(self):
        """Test modulo with literal values"""
        code = """
def test_mod():
    cdef int result
    result = 17 % 5
    return result
"""
        r = self._transpile_code(code)
        # This should parse without errors
        self.assertIsNotNone(r)
    
    def test_modulo_with_variables(self):
        """Test modulo with variables"""
        code = """
def test_mod(int a, int b):
    cdef int remainder
    remainder = a % b
    return remainder
"""
        r = self._transpile_code(code)
        self.assertIsNotNone(r)

    def test_modulo_in_expression(self):
        """Test modulo in complex expression"""
        code = """
def is_even(int n):
    return n % 2 == 0
"""
        cst = Main(code, 'py')
        p = cst.parse()
        r = cst.to_ast(code)  # convert to ast
        self.assertIsNotNone(r)
    
    def test_modulo_function_call(self):
        """Test modulo as function call - modulo() doesn't exist in Python, expect error"""
        from pycropml.transpiler.errors import PseudoCythonNotTranslatableError
        
        # Note: modulo() is not a standard Python function
        # Python uses the % operator for modulo, not a function
        # This test verifies that calling undefined function gives clear error
        code = """
def test_mod_func(int dividend, int divisor):
    cdef int result
    result = modulo(dividend, divisor)
    return result
"""
        cst = Main(code, 'py')
        p = cst.parse()
        
        
        
        with self.assertRaises(PseudoCythonNotTranslatableError) as context:
            r = cst.to_ast(code)
        
        error_message = str(context.exception)
        # Verify error message is clear about undefined function
        self.assertIn('modulo', error_message, "Error should mention function name 'modulo'")
        self.assertIn('not defined', error_message, "Error should say 'not defined'")
        self.assertIn('test_mod_func', error_message, "Error should mention function name")
        self.assertIn('line', error_message, "Error should mention line number")
        
        # Print the error for demonstration
        print(f"\n✓ Undefined function error detected with clear message:")
        print(f"  {error_message}")
    
    def test_modulo_operator_works(self):
        """Test that modulo operator (%) works correctly"""
        code = """
def test_mod_func(int dividend, int divisor):
    cdef int result
    result = dividend % divisor
    return result
"""
        cst = Main(code, 'py')
        p = cst.parse()
        r = cst.to_ast(code)
        self.assertIsNotNone(r, "Modulo operator should work correctly")
    
    def test_modulo_type_error_detection(self):
        """Test that type errors in modulo operations are detected with clear messages"""
        from pycropml.transpiler.errors import PseudoCythonTypeCheckError
        
        # Test: assigning int result to float variable should raise clear error
        code = """
def test_mod(int a, int b):
    cdef float remainder
    remainder = a % b
    return remainder
"""
        cst = Main(code, 'py')
        p = cst.parse()
        
        with self.assertRaises(PseudoCythonTypeCheckError) as context:
            r = cst.to_ast(code)
        
        error_message = str(context.exception)
        # Verify error message contains key information
        self.assertIn('remainder', error_message, "Error should mention variable name")
        self.assertIn('test_mod', error_message, "Error should mention function name")
        self.assertIn('line', error_message, "Error should mention line number")
        self.assertIn('float', error_message, "Error should mention declared type")
        self.assertIn('int', error_message, "Error should mention assigned type")
        
        # Print the error for demonstration
        print(f"\n✓ Type error detected with clear message:")
        print(f"  {error_message}")


class TestCyMLDataFiles(unittest.TestCase):
    """Test suite for CyML data files in test/data/"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.test_data_dir = os.path.join(os.path.dirname(__file__), 'data')
        self.test_files = [
            'test_modulo.pyx',
            'test_math_operations.pyx',
            'test_control_flow.pyx',
            'test_data_structures.pyx',
            'test_advanced_features.pyx'
        ]
    
    def _transpile_file(self, filename, target_lang='py'):
        """Helper to transpile a .pyx file from test/data/"""
        filepath = os.path.join(self.test_data_dir, filename)
        if not os.path.exists(filepath):
            self.fail(f"Test file not found: {filepath}")
        
        try:
            # Read the file content first
            with open(filepath, 'r') as f:
                content = f.read()
            
            cst = Main(content, target_lang)
            p = cst.parse()
            result = cst.to_ast(content)  # convert to ast
            return result
        except Exception as e:
            self.fail(f"Transpilation failed for {filename}: {e}")
    
    def test_math_operations_file(self):
        """Test that test_math_operations.pyx transpiles successfully"""
        result = self._transpile_file('test_math_operations.pyx')
        self.assertIsNotNone(result, "test_math_operations.pyx should transpile successfully")
    
    def test_control_flow_file(self):
        """Test that test_control_flow.pyx transpiles successfully"""
        result = self._transpile_file('test_control_flow.pyx')
        self.assertIsNotNone(result, "test_control_flow.pyx should transpile successfully")
    
    def test_data_structures_file(self):
        """Test that test_data_structures.pyx transpiles successfully"""
        result = self._transpile_file('test_data_structures.pyx')
        self.assertIsNotNone(result, "test_data_structures.pyx should transpile successfully")
    
    def test_advanced_features_file(self):
        """Test that test_advanced_features.pyx transpiles successfully"""
        result = self._transpile_file('test_advanced_features.pyx')
        self.assertIsNotNone(result, "test_advanced_features.pyx should transpile successfully")
    
    def test_all_data_files_exist(self):
        """Verify all expected test data files exist"""
        for filename in self.test_files:
            filepath = os.path.join(self.test_data_dir, filename)
            self.assertTrue(os.path.exists(filepath), 
                          f"Test data file should exist: {filename}")
    
    def test_transpile_to_multiple_languages(self):
        """Test transpiling test_modulo.pyx to multiple target languages"""
        languages = ['py', 'cs', 'java', 'cpp', 'f90']
        for lang in languages:
            with self.subTest(language=lang):
                result = self._transpile_file('test_modulo.pyx', lang)
                self.assertIsNotNone(result, 
                                   f"test_modulo.pyx should transpile to {lang}")


if __name__ == '__main__':
    # Run tests
    unittest.main(verbosity=2)
