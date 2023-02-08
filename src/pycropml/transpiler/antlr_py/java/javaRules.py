

from pycropml.transpiler.rules.generalRule import GeneralRule
from pycropml.transpiler.pseudo_tree import Node

def translateLenList(node): return Node("method_call", receiver=node.receiver, message=".size()", args=[], pseudo_type=node.pseudo_type)
def translateSum(node): 
    if node.pseudo_type=="float":
        return Node("method_call", receiver=node.receiver, message=".stream().mapToDouble(Double::doubleValue).sum()", args=[], pseudo_type=node.pseudo_type)
    elif node.pseudo_type=="int":
        return Node("method_call", receiver=node.receiver, message=".stream().mapToInt(Integer::intValue).sum()", args=[], pseudo_type=node.pseudo_type)

def translateDateTime(node): 
    x="""
        try{
            %s = format.parse("%s");
        }  catch (ParseException var4) {
            var4.printStackTrace();
        }
    """   
    return x
def translateNotContains(node): return Node("unary_op", operator="not", value=Node("standard_method_call", receiver=node.receiver, message="contains?", args=node.args, pseudo_type=node.pseudo_type))
def translateLenDict(node): return Node("method_call", receiver=node.receiver, message=".size()", args=[], pseudo_type=node.pseudo_type)
def translateLenArray(node): return Node("method_call", receiver=node.receiver, message=".length", args=[], pseudo_type=node.pseudo_type)
def translateDictkeys(node): return Node("method_call", receiver=node.receiver, message=".keySet()", args=[], pseudo_type=node.pseudo_type)
def translateDictValues(node): return Node("method_call", receiver=node.receiver, message=".values()", args=[], pseudo_type=node.pseudo_type)
def translatePrint(node):
    if node.args[0].type=="tuple":
        x=[]
        for n in node.args[0].elements:
            if "value" in dir(n) and n.value in [b'\r', b'\t', b'\n']: continue
            x.append(Node(type="ExprStatNode", expr=Node(type="custom_call", function="print", args=[n])))
        return x
    else:
        return {"type":"ExprStatNode", "expr":{'type':"custom_call", "function":"print", "args":node.args}}
    
def translatePow(node): 
    if node.pseudo_type=="int":
        return Node(type="custom_call", function="(int) Math.pow", args=node.args)
    return Node(type="custom_call", function="Math.pow", args=node.args)

def translateCopy(node):
    return Node(type="call", function = "new ArrayList<>", args=[Node("local", name=node.args.name)])


class Java_CymlRules(GeneralRule):
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
                 "!=": "!="
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
        "double": "float",
        "Double": "float",
        "Integer": "int",
        "bool": "boolean",
        "array": "array",
        "List": "list",
        "tuple": "tuple",
        "String": "str",
        "HashMap": "dict",
        "LocalDateTime": "datetime"
    }
    types2 = {
        "int": "Integer",
        "float": "Double",
        "str": "String",
        "bool":"Boolean",
        "datetime":"LocalDateTime",
        "Date":"LocalDateTime"
    }

    functions = {
        'math': {
            'ln':          'log10',
            'log':         'log',
            'tan':         'tan',
            'sin':         'sin',
            'cos':         'cos',
            'asin':        'asin',
            'acos':        'acos',
            'atan':         'atan',
            'sqrt':         'sqrt',
            'ceil':         '(int) ceil',
            'round':        'round',
            'exp':         'exp',
            'pow':          'pow',
            'floor':  'floor'

        },
        'io': {
            'print':    translatePrint,
            'read':       'readLine',
            'read_file':  'File.ReadAllText',
            'write_file': 'File.WriteAllText'
        },
        'system': {
            'min': 'min',
            'max': 'max',
            'abs': 'abs',
            'pow': translatePow,
            'copy':translateCopy
        },
        'datetime':{
                'datetime':translateDateTime #trans_format_parse
        }
    }
    
    constant = {
            
        'math':{
                
            'pi': 'pi'
                
                }            
        }
    
    

    methods = {

        'int': {
            'float': '(double)'
        },
        'float': {
            'int': '(int)',
            'float':'(double)'
        },
        'str': {
            'int': 'Integer.parseInt',
            'find': '.IndexOf',
            'float': 'Double.'
        },
        'list': {
            'len': 'len',
            'append': 'append',
            'sum': 'sum',
            'pop': 'pop',
            'insert_at': "insert_at",
            'contains?': 'contains?',
            'not contains?': "not contains?",
            'index': 'index'
        },
        'dict': {
            'len': 'len',
            'keys': translateDictkeys, # in assignment
            'values':translateDictValues, # in assignment
            'get':'.get'
        },
        'array':{
                'len': "len",
                'append': 'append'   
                }
    }

def argsToStr(args):
    t=[]
    for arg in args:
        t.append(arg.value)
    return '"%s"'%('/'.join(t))
