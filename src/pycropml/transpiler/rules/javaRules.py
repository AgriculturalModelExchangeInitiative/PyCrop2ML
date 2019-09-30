

from pycropml.transpiler.rules.generalRule import GeneralRule
from pycropml.transpiler.pseudo_tree import Node

def translateLenList(node): return Node("method_call", receiver=node.receiver, message=".size()", args=[], pseudo_type=node.pseudo_type)
def translateSum(node): 
    if node.pseudo_type=="float":
        return Node("method_call", receiver=node.receiver, message=".stream().mapToDouble(Double::doubleValue).sum()", args=[], pseudo_type=node.pseudo_type)
    elif node.pseudo_type=="int":
        return Node("method_call", receiver=node.receiver, message=".stream().mapToInt(Int::intValue).sum()", args=[], pseudo_type=node.pseudo_type)

def trans_format_parse(node): return Node("standard_call", args=Node(type="str", value=argsToStr(node.args), pseudo_type="str"), function="format.parse", pseudo_type=node.pseudo_type)
def translateNotContains(node): return Node("unary_op", operator="not", value=Node("standard_method_call", receiver=node.receiver, message="contains?", args=node.args, pseudo_type=node.pseudo_type))
def translateLenDict(node): return Node("method_call", receiver=node.receiver, message=".size()", args=[], pseudo_type=node.pseudo_type)
def translateLenArray(node): return Node("method_call", receiver=node.receiver, message=".length", args=[], pseudo_type=node.pseudo_type)
def translateDictkeys(node): return Node("method_call", receiver=node.receiver, message=".keySet()", args=[], pseudo_type=node.pseudo_type)

class JavaRules(GeneralRule):
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
        "float": "double",
        "bool": "boolean",
        "array": "%s[] %s= new %s",
        "list": "List",
        "tuple": "Tuple",
        "str": "String",
        "dict": "TreeMap",
        "datetime": "Date"
    }
    types2 = {
        "int": "Integer",
        "float": "Double",
        "str": "String",
        "bool":"Boolean",
        "datetime":"Date",
        "Date":"Date"
    }

    functions = {
        'math': {
            'ln':          'Math.log',
            'log':         'Math.log',
            'tan':         'Math.tan',
            'sin':         'Math.sin',
            'cos':         'Math.cos',
            'asin':        'Math.asin',
            'acos':        'Math.acos',
            'atan':         'Math.atan',
            'sqrt':         'Math.sqrt',
            'ceil':         'Math.ceil',
            'round':        'Math.round',
            'exp':         'Math.exp',
            'pow':          'Math.pow'

        },
        'system': {
            'min': 'Math.min',
            'max': 'Math.max',
            'abs': 'Math.abs',
            'pow': 'Math.pow'
        },
        'datetime':{
                'datetime':"format.parse"#trans_format_parse
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
            'int': '(int)',
            'find': '.IndexOf',
            'float': 'Double.'
        },
        'list': {
            'len': translateLenList,
            'append': '.add',
            'sum': translateSum,
            'pop': '.remove',
            'insert_at': ".insert",
            'contains?': '.contains',
            'not contains?': translateNotContains,
            'index': '.indexOf'
        },
        'dict': {
            'len': translateLenDict,
            'keys': translateDictkeys,
            'get':'.get'
        },
        'array':{
                'len': translateLenArray,
                'append': '.add'   
                }
    }
    get_properties = '''
    {
        return %s;
    }'''
    set_properties = '''
    {
        this.%s= _%s;
    } 
    '''
    constructor = '''
    public %s()
    {
           
    }'''

    copy_constr = '''
    public %s(%s toCopy, boolean copyAll) // copy constructor 
    {
        if (copyAll)
        {'''
    copy_constrList = '''
            for (%s c : toCopy.%s)
            {
                _%s.add(c);
            }
            this.%s = _%s;'''
    copy_constrArray = '''
        for (int i = 0; i < %s; i++)
        {
            _%s[i] = toCopy._%s[i];
        }'''
    get_properties_compo = '''
    {
        return _%s.get%s();
    }'''
    set_properties_compo = '''
    {
        %s
    } '''

    copy_constr_compo = '''
    public %s(%s toCopy) // copy constructor 
    {'''


def argsToStr(args):
    t=[]
    for arg in args:
        t.append(arg.value)
    return '"%s"'%('/'.join(t))
