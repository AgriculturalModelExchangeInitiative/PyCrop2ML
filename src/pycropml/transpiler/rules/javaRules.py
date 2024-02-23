

from pycropml.transpiler.rules.generalRule import GeneralRule
from pycropml.transpiler.pseudo_tree import Node

def translateLenList(node): return Node("method_call", receiver=node.receiver, message=".size()", args=[], pseudo_type=node.pseudo_type)
def translateSum(node): 
    if node.pseudo_type=="float":
        return Node("method_call", receiver=node.receiver, message=".stream().mapToDouble(Double::doubleValue).sum()", args=[], pseudo_type=node.pseudo_type)
    elif node.pseudo_type=="int":
        return Node("method_call", receiver=node.receiver, message=".stream().mapToInt(Integer::intValue).sum()", args=[], pseudo_type=node.pseudo_type)

def translateSumArray(node): 
    if node.pseudo_type=="float":
        return Node(type="method_call", receiver=Node(type="call", function="Arrays.stream", args=[node.receiver], pseudo_type=node.pseudo_type), message=".mapToDouble(Double::doubleValue).sum()")
    elif node.pseudo_type=="int":
        return Node(type="method_call", receiver=Node(type="call", function="Arrays.stream", args=[node.receiver], pseudo_type=node.pseudo_type), message=".mapToInt(Integer::intValue).sum()")

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
            x.append(Node(type="ExprStatNode", expr=Node(type="custom_call", function="System.out.println", args=[n])))
        return x
    else:
        return Node(type="ExprStatNode", expr=Node(type="custom_call", function="System.out.println", args=node.args))
def translatePow(node): 
    if node.pseudo_type=="int":
        return Node(type="custom_call", function="(int) Math.pow", args=node.args)
    return Node(type="custom_call", function="Math.pow", args=node.args)

def translateCopy(node):
    return Node(type="call", function = "new ArrayList<>", args=[Node("local", name=node.args.name)])

def translateLog(node):
    return Node(type="call", function = "Math.log10", args=[node.args[0]])

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
        "int": "Integer",
        "float": "double",
        "bool": "Boolean",
        "array": "%s[] %s",
        "list": "List",
        "tuple": "Pair",
        "str": "String",
        "dict": "HashMap",
        "datetime": "LocalDateTime"
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
            'ln':          'Math.log',
            'log':         translateLog,
            'tan':         'Math.tan',
            'sin':         'Math.sin',
            'cos':         'Math.cos',
            'asin':        'Math.asin',
            'acos':        'Math.acos',
            'atan':         'Math.atan',
            'sqrt':         'Math.sqrt',
            'ceil':         '(int) Math.ceil',
            'round':        'Math.round',
            'exp':         'Math.exp',
            'pow':          'Math.pow',
            'floor':  'Math.floor'

        },
        'io': {
            'print':    translatePrint,
            'read':       'readLine',
            'read_file':  'File.ReadAllText',
            'write_file': 'File.WriteAllText'
        },
        'system': {
            'min': 'Math.min',
            'max': 'Math.max',
            'abs': 'Math.abs',
            'pow': translatePow,
            'copy':translateCopy,
            "round":"Math.round",
        },
        'datetime':{
                'datetime':translateDateTime #trans_format_parse
        }
    }
    
    constant = {
            
        'math':{
                
            'pi': 'Math.PI'
                
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
            'len': translateLenList,
            'append': '.add',
            'sum': translateSum,
            'pop': '.remove',
            'insert_at': ".insert",
            'contains?': '.contains',
            'not contains?': translateNotContains,
            'index': '.indexOf',
            "allocate": lambda node: Node("assignment", target = node.receiver, value = Node("array", elts = node.args, pseudo_type=node.receiver.pseudo_type ))
        },
        'dict': {
            'len': translateLenDict,
            'keys': translateDictkeys, # in assignment
            'values':translateDictValues, # in assignment
            'get':'.get'
        },
        'array':{
                'len': translateLenArray,
                'sum': translateSumArray,
                'append': '.add',
                "allocate": lambda node: Node("assignment", target = node.receiver, value = Node("array", elts = node.args, pseudo_type=node.receiver.pseudo_type ))
                }
    }
    get_properties = '''
    { return %s; }'''
    set_properties = '''
    { this.%s= _%s; } 
    '''
    constructor = '''
    public %s() { }'''

    copy_constr = '''
    public %s(%s toCopy, boolean copyAll) // copy constructor 
    {
        if (copyAll)
        {'''
    copy_constrList = '''
            for (%s c : toCopy.get%s())
            {
                _%s.add(c);
            }
            this.%s = _%s;'''
    copy_constrArray = '''
        for (int i = 0; i < %s; i++)
        {
            %s[i] = toCopy.get%s()[i];
        }'''
    get_properties_compo = '''
    { return _%s.get%s(); }'''
    set_properties_compo = '''
    { %s } '''

    copy_constr_compo = '''
    public %s(%s toCopy) // copy constructor 
    {'''


def argsToStr(args):
    t=[]
    for arg in args:
        t.append(arg.value)
    return '"%s"'%('/'.join(t))
