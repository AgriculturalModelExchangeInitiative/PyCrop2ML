CyML Language Specification
===========================

This document specifies the CyML language, an extended Cython subset supported.

.. highlight:: Cython


CyML Language Specification
===========================

This document specifies the CyML language, an extended Cython subset supported.


.. _language-file:
Cython file types
-----------------

* The implementation files, carrying a ``.pyx`` suffix.


.. _basic-types:

Basic Types
-----------

The following basic types are supported

- ``bool``
- ``int``
- ``float``
- ``double``
- ``string``

.. _complex-types:

Complex Types
------------

The following complex types are supported

- ``array``
- ``list``
- ``datetime``


.. _conditional-statements:

Conditional Statements
----------------------

- IF
- IF/Else
- IF/ElseIf/Else

The ``ELIF`` and ``ELSE`` clauses are optional. An ``IF`` statement can appear
anywhere that a normal statement or declaration can appear

Integer For Loops
-----------------
CyML recognises the usual Python for-in-range integer loop pattern::

    for i in range(n):
        ...

Like other Python looping statements, break and continue may be used in the
body, without the loop that have an else clause.


While Loop
-----------------
- Like Python While loop


Function
--------
- Parameters with declaration 
- Default value is possible

Return Statement
----------------
- A function needs to return the same data type. 

The following code is valid: 

::

    def fibonacci(int n):
        if n <= 2:
            return 1
        else:
            return fibonacci(n-1)+fibonacci(n-2)

Call functions
--------------
- Call to CyML functions are supported if the function

- is accessible on the module

- is accessible from import statement


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
========== =========

**Binary operators**

========== =========
Add        ``a + b``
Sub        ``a - b``
Mult       ``a * b``
Div        ``a / b``
Pow        ``a ** b``
Mod        ``a % b``
BitOr      ``a | b``
BitAnd     ``a & b``
========== =========

**Augmented assign statements**

=========== ===========
AugAdd      ``a += b``
AugSub      ``a -= b``
AugMult     ``a *= b``
AugDiv      ``a /= b``
=========== ===========

**Comparison Operators**

=========== =========
Eq          ``a == b``
NotEq       ``a != b``
Lt          ``a < b``
LtE         ``a <= b``
Gt          ``a > b``
GtE         ``a >= b``
=========== =========

**Bool Operators**

==== ============
&&   ``a and b``
||   ``a or b``
==== ============


Array routines
-----------------------------

============================= =======================================================================================
``   ``                        Return a new array of given shape and type, without initializing entries.
``   ``                        Return a new array of given shape and type, filled with ones.
``   ``                        Return a new array of given shape and type, filled with zeros.
============================= =======================================================================================

Mathematical functions
----------------------------

**Trigonometric functions**

============================= =======================================================================================
``sin(x)``                    Trigonometric sine, element-wise.
``cos(x)``                    Cosine elementwise.
``tan(x)``                    Compute tangent element-wise.
``arcsin(x)``                 Inverse sine, element-wise.
``arccos(x)``                 Trigonometric inverse cosine, element-wise.
``arctan(x)``                 Trigonometric inverse tangent, element-wise.
============================= =======================================================================================

**Hyperbolic functions**

============================= =======================================================================================
``sinh(x)``                   Hyperbolic sine, element-wise.
``cosh(x)``                   Hyperbolic cosine, element-wise.
``tanh(x)``                   Compute hyperbolic tangent element-wise.
============================= =======================================================================================


