# coding: utf8
from pycropml.transpiler.rules.generalRule import GeneralRule
from pycropml.transpiler.pseudo_tree import Node


def translateNotContains(node):
    return Node("call", function="!", args=[Node("simpleCall", op='%in%', value=node.args, sequence=node.receiver, pseudo_type='Boolean')])

def translateDictkeys(node): return Node("method_call", receiver=node.receiver, message=".keys()", args=[], pseudo_type=node.pseudo_type)

def translatePrint(node): return Node(type="ExprStatNode", expr=Node(type="custom_call", function="print", args= node.args if "elements" not in dir(node.args[0]) else [arg for arg in node.args[0].elements]))

def translateModulo(node): return Node(type="binary_op", op="%", left=node.args[0], right=node.args[1])

def translatePow(node): return Node(type="binary_op", op="**", left=node.args[0], right=node.args[1])

def translateCopy(node):
    return Node("local", name = node.args.name)

def translateAllocate(node):
    typ = node.pseudo_type[-1]
    newtyp = changetyp(typ)
    return Node("assignment", target = node.receiver, value=Node("call", function = "vector", args=[Node("empty"),node.args]), pseudo_type=node.pseudo_type)

def translateIsNot(node):
    return Node("call", function="!is.null", args=[node.left])

class RRules(GeneralRule):

    def __init__(self):
        GeneralRule.__init__(self)

    binary_op = {"and": "&&",
                 "or": "||",
                 "not": "!",
                 "<": "<",
                 ">": ">",
                 "==": "==",
                 "+": "+",
                 "-": "-",
                 "*": "*",
                 "/": "/",
                 ">=": ">=",
                 "<=": "<=",
                 "!=": "!=",
                 "%":"%%",
                 "**":"^",
                 "is_not":translateIsNot
                 }

    unary_op = {
        'not': '!',
        '+': '+',
        '-': '-',
        '~': '~'
    }

    types = {
        "int": "int",
        "float": "float",
        "bool": "bool",
        "list": "vector",
        "str": "str",
        "datetime":"str"
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
            'ceil':         'ceiling',
            'round':        'round',
            'exp':         'exp',
            'floor':'floor',
            "isnan":"is.nan"

        },
       'io': {
            'print':    translatePrint,
            'read':       'read',
            'read_file':  'File.ReadAllText',
            'write_file': 'File.WriteAllText'
        },
        'system': {
            'min': 'min',
            'max': 'max',
            'abs': 'abs',
            'pow': translatePow,
            'modulo': translateModulo,
            "copy":translateCopy,
            "integr":lambda node: Node("call", function="c", args=node.args),
            "round": 'round'
        },
        'datetime':{
            'datetime':  lambda node : Node(type="str", value=argsToStr(node.args)),
        }
    }
    constant = {
            
        'math':{
                
            'pi': 'pi'
                
                }            
    }

    methods = {

        'int': {
            'float': 'as.double'
        },
        'float': {
            'int': 'as.integer'
        },
        'str': {
            'int': 'as.character',
            'find': '.index'
        },
        'list': {
            'len': 'length',
            'append': lambda node: Node(type="assignment", target=node.receiver, value=Node(type="call", function="c", args=[node.receiver,node.args])),
            'sum': 'sum',
            'pop': '.pop',
            'contains?': lambda node: Node("simpleCall", op='%in%', value=node.args, sequence=node.receiver, pseudo_type='Boolean'),
            'not contains?': translateNotContains,
            'index': lambda node: Node("call", function="which", \
                args=[Node("simpleCall", op='%in%', value=node.receiver, \
                    sequence=node.args, pseudo_type='Boolean')]),
            'allocate': translateAllocate
        },
        'datetime':{
            'datetime': lambda node : Node(type="str", value=argsToStr(node.args)),
            'day':'day'
        },
        'array': {
            'len': 'length',
            'append': '.append',
            'sum':'sum',
            'allocate': translateAllocate
        },
        'dict': {
			'len': 'len',
			'keys': translateDictkeys,
			'get' : '.get'

        }

    }

def argsToStr(args):
    t=[]
    for arg in args:
        t.append(arg.value)
    return "%s"%('/'.join(t))

def changetyp(typ):
    if typ in ("float", "int", "double"):
        newtyp = "numeric"
    elif typ == "bool":
        newtyp = "logical"
    elif typ == "str":
        newtyp = "character"
    return newtyp
