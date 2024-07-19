from pycropml.transpiler.rules.generalRule import GeneralRule
from pycropml.transpiler.pseudo_tree import Node


def translateLenList(node):
    return Node("method_call", receiver=node.receiver, message=".size()", args=[], pseudo_type=node.pseudo_type)


def translateLenStr(node):
    return Node("method_call", receiver=node.receiver, message=".length()", args=[], pseudo_type=node.pseudo_type)


def translateLog(node):
    return Node("call", function="std::log10", args=[node.args[0]], pseudo_type=node.pseudo_type)


def translateSum(node):
    if "name" in dir(node.receiver):
        print(node.receiver.y)
        return Node("call", function="accumulate",
                    args=[Node("local", name=f"{node.receiver.name}.begin()"),
                        Node("local", name=f"{node.receiver.name}.end()"),
                        Node("int", value="0" if node.receiver.pseudo_type[1] == "int" else "0.0")],
                    pseudo_type=node.pseudo_type)
    

def translateNotContains(node):
    return Node("call", function="!", args=[Node("standard_method_call", receiver=node.receiver,
                                                 message="contains?", args=node.args, pseudo_type=node.pseudo_type)])


def translateLenDict(node):
    return Node("method_call", receiver=node.receiver, message=".size()", args=[], pseudo_type=node.pseudo_type)


def translateLenArray(node):
    return Node("method_call", receiver=node.receiver, message=".size()", args=[], pseudo_type=node.pseudo_type)


def translatekeyDict(node):
    return Node("method_call", receiver=node.receiver, message=".Keys", args=[], pseudo_type=node.pseudo_type)


def translateget(node):
    if "value" in dir(node.args[0]):
        return Node('index', sequence=Node('local', name=node.receiver.name,
                                           pseudo_type=node.receiver.pseudo_type),
                    index=Node(node.args[0].type, value=node.args[0].value, pseudo_type=node.args[0].pseudo_type),
                    pseudo_type="Void")
    elif "name" in dir(node.args[0]):
        return Node('index', sequence=Node('local', name=node.receiver.name,
                                           pseudo_type=node.receiver.pseudo_type),
                    index=Node(node.args[0].type, name=node.args[0].name, pseudo_type=node.args[0].pseudo_type),
                    pseudo_type="Void")


def translatePop(node):
    return Node("custom_call", receiver=node.receiver, function="%s.erase" % node.receiver.name, args=[
        Node(type="binary_op", left=Node(type="local", name=f"{node.receiver.name}.begin()"), op="+",
             right=node.args)], pseudo_type=node.pseudo_type)


def translateInsert(node):
    return Node("custom_call", receiver=node.receiver, function=f"{node.receiver.name}.insert",
                args=[Node(type="binary_op", left=Node(type="local", name=f"{node.receiver.name}.begin()"), op="+",
                           right=node.args[0]), node.args[1]], pseudo_type=node.pseudo_type)


def translateContains(node):
    return Node(type="binary_op", op="!=",
                left=Node("custom_call", receiver=node.receiver, function="find",
                          args=[Node(type="local", name=f"{node.receiver.name}.begin()"),
                                Node(type="local", name=f"{node.receiver.name}.end()"),
                                node.args[0]]),
                right=Node(type="local", name="%s.end()" % node.receiver.name))


def translateIndex(node):
    return Node(type="binary_op", op="-",
                left=Node("custom_call", receiver=node.receiver, function="find",
                          args=[Node(type="local", name=f"{node.receiver.name}.begin()"),
                                Node(type="local", name=f"{node.receiver.name}.end()"),
                                node.args[0]]),
                right=Node(type="local", name="%s.begin()" % node.receiver.name))


def translate_min_max(node, f):
    args = []
    if len(node.args) >= 2:
        for arg in node.args:
            if arg.pseudo_type != node.pseudo_type:
                arg = Node(type="call", function=CppRules.types[node.pseudo_type], args=arg,
                           pseudo_type=node.pseudo_type)
            args.append(arg)
        node.type = "call"
        node.args = args
        node.function = f
    return node


def translateMIN(node):
    return translate_min_max(node, "std::min")


def translateMAX(node):
    return translate_min_max(node, "std::max")


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
                 "!=": "!="}

    unary_op = {
        'not': '!',
        '+': '+',
        '-': '-',
        '~': '~'
    }

    types = {
        "int": "int",
        "float": "double",
        "double": "double",
        "bool": "bool",
        "array": "std::vector<%s>(%s) ",
        "list": "std::vector",
        "tuple": "std::tuple",
        "str": "std::string",
        "dict": "std::map",
        "datetime": "std::string",
    }

    typesCrop = {
        "integer": "int",
        "double": "double",
        "float": "double",
        "boolean": "bool",
        "array": "std::vector<%s>(%s) ",
        "list": "std::vector",
        "tuple": "std::tuple",
        "string": "std::string",
        "dict": "std::map",
        "datetime": "std::string",
    }

    functions = {
        'math': {
            'ln': 'std::log',
            'log': translateLog,
            'tan': 'std::tan',
            'sin': 'std::sin',
            'cos': 'std::cos',
            'asin': 'std::asin',
            'acos': 'std::acos',
            'atan': 'std::atan',
            'sqrt': 'std::sqrt',
            'ceil': '(int) std::ceil',
            'round': 'std::round',
            'exp': 'std::exp',
            'pow': 'std::pow',
            'floor': 'std::floor'

        },
        'io': {
            'print': "std::cout << ",
            'read': 'Console.ReadLine',
            'read_file': 'File.ReadAllText',
            'write_file': 'File.WriteAllText'
        },
        'system': {
            'min': translateMIN,
            'max': translateMAX,
            'abs': 'std::abs',
            'pow': 'std::pow'},
        'datetime': {
            'datetime': lambda node: Node(type="str", value=argsToStr(node.args))
        }
    }

    constant = {
        'math': {
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
            'len': translateLenStr
        },
        'list': {
            'len': translateLenList,
            'append': '.push_back',
            'sum': translateSum,
            'pop': translatePop,
            'insert_at': translateInsert,
            'contains?': translateContains,
            'not contains?': translateNotContains,
            'index': translateIndex,
            "allocate": lambda node: Node("assignment", target=node.receiver,
                                          value=Node("list", elements=node.args,
                                                     pseudo_type=node.receiver.pseudo_type))
        },
        'dict': {
            'len': translateLenDict,
            'keys': translatekeyDict,
            "get": translateget
        },
        'array': {
            'len': translateLenArray,
            'sum': translateSum,
            'append': '.Add',
            "allocate": lambda node: Node("assignment", target=node.receiver,
                                          value=Node("list", elements=node.args,
                                                     pseudo_type=node.receiver.pseudo_type))
        }
    }

    public_properties = '''\
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

    public_properties_wrap = "{ get { return %s.%s;}}\n"

    constructor = '''\
%s::%s()
{
       
}
'''

    copy_constr = '''\
public %s(%s toCopy, bool copyAll) // copy constructor 
{
if (copyAll)
{
'''

    copy_constrList = '''\
for (int i = 0; i < toCopy.get%s().Count; i++)
{
    %s.Add(toCopy.get%s()[i]);
}
'''

    copy_constrArray = '''\
for (int i = 0; i < %s; i++)
{
    %s[i] = toCopy.get%s()[i];
}
'''
    public_properties_compo = '''\
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

    copy_constr_compo = '''\
void %s(%s& toCopy): this() // copy constructor 
{
'''


def argsToStr(args):
    t = []
    for arg in args:
        t.append(arg.value)
    return '/'.join(t)
