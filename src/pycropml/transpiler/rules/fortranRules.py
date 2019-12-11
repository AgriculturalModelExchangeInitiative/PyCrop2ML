# coding: utf8


from pycropml.transpiler.rules.generalRule import GeneralRule
from pycropml.transpiler.pseudo_tree import Node


    
def translateCeil(node):  return Node("call", function="REAL", args=Node("call", function='CEILING', args=node.args, pseudo_type="FLOAT"), pseudo_type="FLOAT")
def translatePow(node):	return Node("call", function=" ",args=Node("binary_op", op = "**", left = node.args[0], right=node.args[1]), pseudo_type="boolean")
def translateFind(node): return  Node("custom_call",receiver = node.receiver, function="index", args=node.args, pseudo_type=node.pseudo_type)
def translateAppend(node):	return  Node("custom_call",receiver = node.receiver, function="call Add", args=node.args, pseudo_type=node.pseudo_type)
def translatePop(node):	return  Node("assignment",target =node.receiver, value=Node("tab",receiver=node.receiver, index=node.args), pseudo_type="Void")
def translateContains(node): return  Node("call", function="ANY", args=Node(type="binary_op", op="==", right =node.args, left = node.receiver),pseudo_type=node.pseudo_type)
def translateNotContains(node):	return  Node("call", function="ALL", args=Node(type="binary_op", op="!=", right =node.args, left = node.receiver), pseudo_type=node.pseudo_type)
def translateIndex(node): return  Node("custom_call",receiver = node.receiver, function="indice", args=node.args, pseudo_type=node.pseudo_type)




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
           "list": "%s,DIMENSION (:), ALLOCATABLE::",
           "array":"%s, DIMENSION(%s)",
           "datetime":"CHARACTER(65)"
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
                'ceil':          translateCeil,
				'pow' : translatePow
            },
            'system': {
                    'min': 'MIN',
                    'max': 'MAX',
                    'abs':'ABS',
                    'round': 'Round',
                    'pow': translatePow,
                    'modulo':   "modulo"

                    },
            'datetime':{
                   'datetime': lambda node : Node(type="str", value=argsToStr(node.args))

           }
            
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
                    'find': translateFind
                    },

           
            'list':{
                    'len':'SIZE',
                    'append': translateAppend,
                    'sum':'sum',
                    'pop': translatePop,
                    'contains?': translateContains,
                    'not contains?':translateNotContains,
                    'index': translateIndex
                    
                    },
			'array':{
					'len': 'SIZE',
					'append': lambda node: Node("assignment", target=Node("index", sequence=node.receiver, index=node.args, pseudo_type=node.pseudo_type[0]), value="", pseudo_type="Void")

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

    def method(self):
        pass

def argsToStr(args):
    t=[]
    for arg in args:
        t.append(arg.value)
    return "%s"%('/'.join(t))