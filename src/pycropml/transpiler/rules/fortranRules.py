from pycropml.transpiler.rules.generalRule import GeneralRule
from pycropml.transpiler.pseudo_tree import Node
class FortranRules(GeneralRule):
    def __init__(self):
        GeneralRule.__init__(self)
        
    binary_op = {"and":".AND.",
                "or":".OR.",
                "not": ".NOT..",
                "<":".LT.",
                ">":".GT.",
                "==":".EQ.",
                "+":"+",
                "-":"-",
                "*":"*",
                "/":"/",
                "<=":".LE.",
                ">=":".GE.",
                "!=":".NE.",
                '**':'**'
            }
    unary_op = {
        'not':'.NOT. ',
        '+': '+', 
        '-': '-',
        '~': '~'
        }
    
    types={
           "int": "INTEGER",
           "float":"REAL",
           "bool":"LOGICAL",
           "str":"CHARACTER(65)",
           "list": "%s,DIMENSION (:), ALLOCATABLE::"
           }
    
    functions = {
            'math': {
                'ln':          'LOG',
                'log':         'LOG',
                'tan':         'TAN',
                'sin':         'SIN',
                'cos':         'COS',
                'asin':        'ASIN',
                'acos':        'ACOS',
                'atan':         'ATAN',
                'sqrt':         'SQRT',
                'exp' :         'EXP',
                'ceil':          lambda node: Node("call", function="REAL", args=Node("call", function='CEILING', args=node.args, pseudo_type="FLOAT"), pseudo_type="FLOAT")
            },
            'system': {
                    'min': 'MIN',
                    'max': 'MAX',
                    'abs':'ABS',
                    'round': 'Round',
                    'pow':         lambda node: Node("call", function=" ",args=Node("binary_op", op = "**", left = node.args[0], right=node.args[1]), pseudo_type="boolean")
                    },
            
            }

    methods = {
            
            'int':{
                    'float':'REAL'                    
                    },
            'float':{
                    'int':'INT'
                    },
            'str':{
                    'int':'INT',
                    'find':lambda node: Node("subroutine",receiver = node.receiver, function="index", args=node.args, pseudo_type=node.pseudo_type)
                    },
            'list':{
                    'len':'SIZE',
                    'append':lambda node: Node("subroutine",receiver = node.receiver, function="call Add", args=node.args, pseudo_type=node.pseudo_type),
                    'sum':'sum',
                    'pop':'.RemoveAt',
                    'contains?':lambda node: Node("call", function="ANY", args=Node(type="binary_op", op="==", right =node.args, left = node.receiver), 
                                                 pseudo_type=node.pseudo_type),
                    'not contains?':lambda node: Node("call", function="ALL", args=Node(type="binary_op", op="!=", right =node.args, left = node.receiver), 
                                                 pseudo_type=node.pseudo_type),
                    'index':lambda node: Node("subroutine",receiver = node.receiver, function="indice", args=node.args, pseudo_type=node.pseudo_type)
                    
                    },
            'dict':{
                    'len':'SIZE'
                    }
            }
            
    """dependencies = {

        'list': {
            'index': 'list_sub',
            'append': 'list_sub'
        }
    }"""

    


