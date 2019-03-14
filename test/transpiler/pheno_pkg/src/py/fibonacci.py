import numpy
from math import *

def fibonacci_(n):
    #- Description:
    #            - Model Name: fibonacci function
    #            - Author: Pierre Martre
    #            - Reference:  to write in package
    #            - Institution: INRA Montpellier
    #            - Abstract: see documentation
    #- inputs:
    #            - name: n
    #                          - description : argument
    #                          - datatype : INT
    #                          - inputtype : variable
    #- outputs:
    #            - name: result
    #                          - description :  fibonacci number 
    #                          - datatype : INT
    result = 0
    b = 1
    for i in range(0 , n , 1):
        temp = result
        result = b
        b = temp + b
    return result