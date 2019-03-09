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
                "<=":"<="
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
           "str":"string"       
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
                'exp' :         'Math.Exp'
                    
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
                    'int':'(int)'
                    },
            'list':{
                    'len':lambda node: Node("method_call", receiver =node.receiver, message=".Count()", args=[], pseudo_type=node.pseudo_type),
                    'append':'.Add',
                    'sum':lambda node: Node("method_call", receiver =node.receiver, message=".Sum()", args=[], pseudo_type=node.pseudo_type),
                    'pop':'.RemoveAt'
                    }
            }
    
    


