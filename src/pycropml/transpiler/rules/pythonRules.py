# coding: utf8
from pycropml.transpiler.rules.generalRule import GeneralRule
from pycropml.transpiler.pseudo_tree import Node


def translateNotContains(node):
    return Node("simpleCall", op='not in', value=node.args, sequence=node.receiver, pseudo_type='Boolean')

def translateDictkeys(node): return Node("method_call", receiver=node.receiver, message=".keys()", args=[], pseudo_type=node.pseudo_type)



class PythonRules(GeneralRule):

    def __init__(self):
        GeneralRule.__init__(self)

    binary_op = {"and": "and",
                 "or": "or",
                 "not": "not",
                 "<": "<",
                 ">": ">",
                 "==": "==",
                 "+": "+",
                 "-": "-",
                 "*": "*",
                 "/": "/",
                 ">=": ">=",
                 "<=": "<=",
                 "!=": "!="
                 }

    unary_op = {
        'not': 'not ',
        '+': '+',
        '-': '-',
        '~': '~'
    }

    types = {
        "int": "int",
        "float": "float",
        "bool": "bool",
        "list": "list",
        "tuple": "tuple",
        "str": "str",
        "dict": "dict"
    }

    functions = {
        'math': {
            'ln':          'log',
            'log':         'log',
            'tan':         'tan',
            'sin':         'sin',
            'cos':         'cos',
            'asin':        'asin',
            'acos':        'acos',
            'atan':         'atan',
            'sqrt':         'sqrt',
            'ceil':         'ceil',
            'round':        'round',
            'exp':         'exp'

        },
        'system': {
            'min': 'min',
            'max': 'max',
            'abs': 'abs',
            'pow': 'pow'}
    }

    methods = {

        'int': {
            'float': 'float'
        },
        'float': {
            'int': 'int'
        },
        'str': {
            'int': 'int',
            'find': '.index'
        },
        'list': {
            'len': 'len',
            'append': '.append',
            'sum': 'sum',
            'pop': '.pop',
            'contains?': lambda node: Node("simpleCall", op='in', value=node.args, sequence=node.receiver, pseudo_type='Boolean'),
            'not contains?': translateNotContains,
            'index': '.index'
        },
        'array': {
            'len': 'len'
        },
        'dict': {
			'len': 'len',
			'keys': translateDictkeys,
			'get' : '.get'

        }

    }
