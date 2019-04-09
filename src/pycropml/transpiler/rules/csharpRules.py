from pycropml.transpiler.rules.generalRule import GeneralRule
from pycropml.transpiler.pseudo_tree import Node

class CsharpRules(GeneralRule):
    def __init__(self):
        GeneralRule.__init__(self)
    
    binary_op = {"and":"&&",
                "or":"||",
                "not": "!",
                "<":"<",
                ">":">",
                "==":"==",
                "+":"+",
                "-":"-",
                "*":"*",
                "/":"/",
                ">=":">=",
                "<=":"<=",
                "!=":"!="
            }
    
    unary_op = {
        'not':'!',
        '+': '+', 
        '-': '-',
        '~': '~'
        }
    
    types={
           "int": "int",
           "float":"double",
           "bool":"bool",
           "list":"List",
           "tuple":"Tuple",
           "str":"string",
           "dict":"Dictionary"
           }
    
    functions = {
            'math': {
                'ln':          'Math.Log',
                'log':         'Math.Log',
                'tan':         'Math.Tan',
                'sin':         'Math.Sin',
                'cos':         'Math.Cos',
                'asin':        'Math.Asin',
                'acos':        'Math.Acos',
                'atan':         'Math.Atan',
                'sqrt':         'Math.Sqrt',
                'ceil':         'Math.Ceiling',
                'round':        'Math.Round',
                'exp' :         'Math.Exp',
                'pow':          'Math.Pow'
                    
            },
            'system': {
                    'min': 'Math.Min',
                    'max': 'Math.Max',
                    'abs': 'Math.Abs',
                    'pow':'Math.Pow'}
        }
                    
    methods = {
            
            'int':{
                    'float':'(double)'                    
                    },
            'float':{
                    'int':'(int)'
                    },
            'str':{
                    'int':'(int)',
                    'find':'.IndexOf'
                    },
            'list':{
                    'len':lambda node: Node("method_call", receiver =node.receiver, message=".Count()", args=[], pseudo_type=node.pseudo_type),
                    'append':'.Add',
                    'sum':lambda node: Node("method_call", receiver =node.receiver, message=".Sum()", args=[], pseudo_type=node.pseudo_type),
                    'pop':'.RemoveAt',
                    'insert_at':".Insert",
                    'contains?':'.Contains',
                    'not contains?':lambda node: Node("unary_op", operator="not", value =Node("standard_method_call", receiver =node.receiver, message="contains?", args=node.args, pseudo_type=node.pseudo_type)),
                    'index':'.IndexOf'
                    },
            'dict':{
                    'len':lambda node: Node("method_call", receiver =node.receiver, message=".Count()", args=[], pseudo_type=node.pseudo_type)
                    }
            }
    
    


