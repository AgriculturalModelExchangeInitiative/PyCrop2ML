

from pycropml.transpiler.rules.generalRule import GeneralRule
from pycropml.transpiler.pseudo_tree import Node

def translateLenList(node): return Node("method_call", receiver=node.receiver, message=".size()", args=[], pseudo_type=node.pseudo_type)
def translateLenStr(node): return Node("method_call", receiver=node.receiver, message=".length()", args=[], pseudo_type=node.pseudo_type)
def translateSum(node): return Node("call", function="accumulate", args=[Node("local",name="%s.begin()"%node.receiver.name), Node("local",name="%s.end()"%node.receiver.name), Node("local",name="decltype(%s)::value_type(0)"%node.receiver.name)], pseudo_type=node.pseudo_type)
def translateNotContains(node): return Node("call", function="!", args=[Node("standard_method_call", receiver=node.receiver, message="contains?", args=node.args, pseudo_type=node.pseudo_type)])
def translateLenDict(node): return Node("method_call", receiver=node.receiver, message=".size()", args=[], pseudo_type=node.pseudo_type)
def translateLenArray(node): return Node("method_call", receiver=node.receiver, message=".Length", args=[], pseudo_type=node.pseudo_type)
def translatekeyDict(node): return Node("method_call", receiver=node.receiver, message=".Keys", args=[], pseudo_type=node.pseudo_type)
def translateget(node): 
    if "value" in dir(node.args[0]):
        return Node('index',sequence = Node('local',name= node.receiver.name, pseudo_type = node.receiver.pseudo_type), index= Node(node.args[0].type, value = node.args[0].value, pseudo_type= node.args[0].pseudo_type), pseudo_type = "Void")
    elif "name" in dir(node.args[0]):
        return Node('index',sequence = Node('local',name= node.receiver.name, pseudo_type = node.receiver.pseudo_type), index= Node(node.args[0].type, name = node.args[0].name, pseudo_type= node.args[0].pseudo_type), pseudo_type = "Void")
def translatePop(node):  return Node("custom_call", receiver=node.receiver, function="%s.erase"%node.receiver.name, args=[Node(type="binary_op",left=Node(type="local",name="%s.begin()"%(node.receiver.name)),op="+",right= node.args)], pseudo_type=node.pseudo_type)
def translateInsert(node): return Node("custom_call", receiver=node.receiver, function="%s.insert"%node.receiver.name, args=[Node(type="binary_op",left=Node(type="local",name="%s.begin()"%(node.receiver.name)),op="+",right= node.args[0]), node.args[1]], pseudo_type=node.pseudo_type)
def translateContains(node): return Node(type="binary_op", op="!=",left=Node("custom_call", receiver=node.receiver, function="find", args=[Node(type="local",name="%s.begin()"%(node.receiver.name)),\
    Node(type="local",name="%s.end()"%(node.receiver.name)),\
        node.args[0]]), right=Node(type="local",name="%s.end()"%node.receiver.name))
def translateIndex(node): return Node(type="binary_op", op="-",left=Node("custom_call", receiver=node.receiver, function="find", args=[Node(type="local",name="%s.begin()"%(node.receiver.name)),\
    Node(type="local",name="%s.end()"%(node.receiver.name)),\
        node.args[0]]), right=Node(type="local",name="%s.begin()"%node.receiver.name))

def translateMIN(node):
    args=[]
    if len(node.args)>=2:
        for i in range(len(node.args)):
            if node.args[i].pseudo_type!=node.pseudo_type:
                node.args[i] = Node(type="call", function=node.pseudo_type,args =node.args[i], pseudo_type=node.pseudo_type )
            args.append(node.args[i])
        node.type = "call"
        node.args = args
        node.function = "min"
    return node

class CppRules(GeneralRule):
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
        "bool": "bool",
        "array": "array<%s, %s> ", # 
        "list": "vector",
        "tuple": "tuple",
        "str": "string",
        "dict": "map",
        "datetime":"string",
    }

    functions = {
        'math': {
            'ln':          'log',
            'log':         'log10',
            'tan':         'tan',
            'sin':         'asin',
            'cos':         'cos',
            'asin':        'asin',
            'acos':        'acos',
            'atan':         'atan',
            'sqrt':         'sqrt',
            'ceil':         '(int) ceil',
            'round':        'round',
            'exp':         'exp',
            'pow':          'pow'

        },
        'io': {
            'print':    "cout<<",
            'read':       'Console.ReadLine',
            'read_file':  'File.ReadAllText',
            'write_file': 'File.WriteAllText'
        },
        'system': {
            'min': translateMIN,
            'max': 'max',
            'abs': 'abs',
            'pow': 'pow'},
        'datetime':{
            'datetime': ' new DateTime'
        }
    }

    constant = {
            
        'math':{
                
            'pi': 'M_PI'
                
                }            
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
            'find': '.find',
            'len':translateLenStr
        },
        'list': {
            'len': translateLenList,
            'append': '.push_back',
            'sum': translateSum,
            'pop': translatePop,
            'insert_at': translateInsert,
            'contains?': translateContains,
            'not contains?': translateNotContains,
            'index': translateIndex
        },
        'dict': {
            'len': translateLenDict,
            'keys': translatekeyDict,
            "get": translateget
        },
        'array':{
                'len': translateLenArray,
                'append': '.Add'

                
                }
    }
    public_properties = '''
    {
        get
        {
            return this._%s;
        }
        set
        {
            this._%s= value;
        } 
    }'''

    public_properties_wrap = '''{ get { return %s.%s;}} 
     '''  
    constructor = '''
    %s::%s()
    {
           
    }
    '''

    copy_constr = '''
    public %s(%s toCopy, bool copyAll) // copy constructor 
    {
    if (copyAll)
    {
    '''
    copy_constrList = '''
        for (int i = 0; i < toCopy.%s.Count; i++)
        {
            %s.Add(toCopy.%s[i]);
        }
    '''
    copy_constrArray = '''
        for (int i = 0; i < %s; i++)
        {
            _%s[i] = toCopy._%s[i];
        }
    '''
    public_properties_compo = '''
    {
        get
        {
            return _%s.%s;
        }
        set
        {
            %s
        } 
    }
    '''
    copy_constr_compo = '''
void %s(%s& toCopy): this() // copy constructor 
{
'''

