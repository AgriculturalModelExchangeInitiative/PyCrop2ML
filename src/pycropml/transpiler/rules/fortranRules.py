# coding: utf8


from pycropml.transpiler.rules.generalRule import GeneralRule
from pycropml.transpiler.pseudo_tree import Node


    
def translateCeil(node):  return Node("call", function='CEILING', args=node.args, pseudo_type="int")
def translatePow(node):	return Node("call", function=" ",args=Node("binary_op", op = "**", left = node.args[0], right=node.args[1]), pseudo_type="boolean")
def translateFind(node): return  Node("custom_call",receiver = node.receiver, function="index", args=node.args, pseudo_type=node.pseudo_type)
def translateAppend(node):	return  Node("custom_call",receiver = node.receiver, function="call Add", args=[node.receiver,node.args], pseudo_type=node.pseudo_type)
def translatePop(node):	return  Node("assignment",target =node.receiver, value=Node("tab",receiver=node.receiver, index=node.args), pseudo_type="Void")
def translateContains(node): return  Node("call", function="ANY", args=Node(type="binary_op", op="==", right =node.args, left = node.receiver),pseudo_type=node.pseudo_type)
def translateNotContains(node):	return  Node("call", function="ALL", args=Node(type="binary_op", op="!=", right =node.args, left = node.receiver), pseudo_type=node.pseudo_type)
def translateIndex(node): return  Node("custom_call",receiver = node.receiver, function="indice", args=[Node(type="local",name=node.receiver.name),node.args], pseudo_type=node.pseudo_type)
def translatePrint(node): return Node(type="combine", args=[Node("local", name="print *, "),\
                                                            node.args if "elements" not in dir(node.args[0]) else [arg for arg in node.args[0].elements]])

def translateLog(node):  return Node("binary_op", op = "/", left = Node("call", function='LOG', args=node.args[0]),right = Node("call", function='LOG', args=Node("call", function="REAL", args=node.args[1])), pseudo_type="float")

def translateCopy(node):
    return Node("local", name = node.args.name)
def translateMIN(node):
    args=[]
    if len(node.args)>=2:
        for i in range(len(node.args)):
            if node.args[i].pseudo_type!=node.pseudo_type:
                node.args[i] = Node(type="call", function=node.pseudo_type,args =node.args[i], pseudo_type=node.pseudo_type )
            args.append(node.args[i])
        node.type = "call"
        node.args = args
        node.function = "MIN"
    return node

def translateMAX(node):
    args=[]
    if len(node.args)>=2:
        for i in range(len(node.args)):
            if node.args[i].pseudo_type!=node.pseudo_type:
                node.args[i] = Node(type="call", function=node.pseudo_type,args =node.args[i], pseudo_type=node.pseudo_type )
            args.append(node.args[i])
        node.type = "call"
        node.args = args
    node.function = "MAX"
    return node

def translateList(node):
    if node.args.type == "standard_call":
        pass
    return

def translate_isnot(node): 
    print(node.y)
    if node.type=="array":
        return Node("assignment", op="!=",value=Node("int", value="0", pseudo_type="int"), target=Node("call", function="SIZE", args=Node(type=node.type, left = node.name,pseudo_type=node.pseudo_type)))    
        #return Node("call", function="SIZE", args=Node(type=node.type, left = node.name,pseudo_type=node.pseudo_type))
    return  Node("call", function="ALLOCATED", args=Node(type=node.type, left = node.name,pseudo_type=node.pseudo_type))

def translate_isnan(node):
    return Node("binary_op", op="!=", left=node.args, right=node.args, pseudo_type=node.pseudo_type)

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
                '**':'**',
                "is_not":translate_isnot
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
           "str":"CHARACTER(len=*)",
           "list": "%s,DIMENSION (:), ALLOCATABLE::",
           "array":"%s, DIMENSION(%s)",
           "datetime":"CHARACTER(65)"
           }
    
    functions = {
            'math': {
                'ln':          'LOG',
                'log':         translateLog,
                'tan':         'TAN',
                'sin':         'SIN',
                'cos':         'COS',
                'asin':        'ASIN',
                'acos':        'ACOS',
                'atan':         'ATAN',
                'sqrt':         'SQRT',
                'exp' :         'EXP',
                'ceil':          translateCeil,
				'pow' : translatePow,
                'floor': "FLOOR",
                "isnan": translate_isnan
            },
       'io': {
            'print':    translatePrint,
            'read':       'Console.ReadLine',
            'read_file':  'File.ReadAllText',
            'write_file': 'File.WriteAllText'
        },
            'system': {
                    'min': translateMIN,
                    'max': translateMAX,
                    'abs':'ABS',
                    'round': 'NINT',
                    'pow': translatePow,
                    'modulo':   "modulo",
                    "copy": translateCopy,
                    "list": translateList

                    },
            'datetime':{
                   'datetime': lambda node : Node(type="str", value=argsToStr(node.args))

           }
            
            
        }
    constant = {
            
        'math':{
                
            'pi': '3.14159265'
                
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
                    'index': translateIndex,
                    'allocate': lambda node: Node("call", function ="allocate", args =Node("call", function=node.receiver.name, args = node.args))
                    
                    },
			'array':{
					'len': 'SIZE',
                'sum':'sum',
					'append': lambda node: Node("assignment", target=Node("index", sequence=node.receiver, index=node.args, pseudo_type=node.pseudo_type[0]), value="", pseudo_type="Void"),
                    'allocate': lambda node: Node("call", function ="allocate", args =Node("call", function=node.receiver.name, args = node.args))

			},
            'dict':{
                    'len':'SIZE'
                    }
            }
            

    def method(self):
        pass

def argsToStr(args):
    t=[]
    for arg in args:
        t.append(arg.value)
    return "%s"%('/'.join(t))