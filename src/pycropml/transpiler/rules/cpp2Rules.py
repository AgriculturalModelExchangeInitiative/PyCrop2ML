from pycropml.transpiler.rules.generalRule import GeneralRule
from pycropml.transpiler.pseudo_tree import Node

def translate_len_list(node):
    return Node("call", function="int", args=[
        Node("method_call", receiver=node.receiver, message=".size()", args=[], pseudo_type=node.pseudo_type)])


def translate_len_str(node):
    return Node("method_call", receiver=node.receiver, message=".length()", args=[], pseudo_type=node.pseudo_type)


def translate_log(node):
    return Node("call", function="std::log10", args=[node.args[0]], pseudo_type=node.pseudo_type)


def translate_sum(node):
    if "name" in dir(node.receiver):
        #print(node.receiver.y)
        if "cpp_struct_name" in dir(node.receiver) and node.receiver.cpp_struct_name is not None:
            name = f"{node.receiver.cpp_struct_name}.{node.receiver.name}"
        else:
            name = node.receiver.name
        return Node("call", function="accumulate",
                    args=[Node("local", name=f"{name}.begin()"),
                        Node("local", name=f"{name}.end()"),
                        Node("int", value="0" if node.receiver.pseudo_type[1] == "int" else "0.0")],
                    pseudo_type=node.pseudo_type)
    

def translate_not_contains(node):
    return Node("call", function="!", args=[Node("standard_method_call", receiver=node.receiver,
                                                 message="contains?", args=node.args, pseudo_type=node.pseudo_type)])


def translate_len_dict(node):
    return Node("call", function="int", args=[
        Node("method_call", receiver=node.receiver, message=".size()", args=[], pseudo_type=node.pseudo_type)])


def translate_len_array(node):
    return Node("call", function="int", args=[
        Node("method_call", receiver=node.receiver, message=".size()", args=[], pseudo_type=node.pseudo_type)])


def translate_key_dict(node):
    return Node("method_call", receiver=node.receiver, message=".Keys", args=[], pseudo_type=node.pseudo_type)


def translate_get(node):
    if "value" in dir(node.args[0]):
        return Node("index", sequence=Node("local", name=node.receiver.name,
                                           pseudo_type=node.receiver.pseudo_type),
                    index=Node(node.args[0].type, value=node.args[0].value, pseudo_type=node.args[0].pseudo_type),
                    pseudo_type="Void")
    elif "name" in dir(node.args[0]):
        return Node("index", sequence=Node("local", name=node.receiver.name,
                                           pseudo_type=node.receiver.pseudo_type),
                    index=Node(node.args[0].type, name=node.args[0].name, pseudo_type=node.args[0].pseudo_type),
                    pseudo_type="Void")


def translate_pop(node):
    return Node("custom_call", receiver=node.receiver, function=f"{node.receiver.name}.erase",
                args=[Node(type="binary_op", left=Node(type="local", name=f"{node.receiver.name}.begin()"), op="+",
                           right=node.args)], pseudo_type=node.pseudo_type)


def translate_insert(node):
    return Node("custom_call", receiver=node.receiver, function=f"{node.receiver.name}.insert",
                args=[Node(type="binary_op", left=Node(type="local", name=f"{node.receiver.name}.begin()"), op="+",
                           right=node.args[0]), node.args[1]], pseudo_type=node.pseudo_type)


def translate_contains(node):
    if "name" in dir(node.receiver):
        return Node(type="binary_op", op="!=",
                    left=Node("custom_call", receiver=node.receiver, function="find",
                              args=[Node(type="local", name=f"{node.receiver.name}.begin()"),
                                    Node(type="local", name=f"{node.receiver.name}.end()"),
                                    node.args[0]]),
                    right=Node(type="local", name="%s.end()" % node.receiver.name))
    else:
        if "elements" in dir(node.receiver):
            args_str = ", ".join([str(arg.value) for arg in node.receiver.elements])
            return Node(type="binary_op", op=">",
                        left=Node("custom_call", receiver=node.receiver,
                                  function=f"std::set<{CppRules.types[node.receiver.pseudo_type[1]]}>({{\"{args_str}\"}}).count",
                                  args=[node.args[0]]),
                        right=Node(type="int", value="0"))

def translate_index(node):
    return Node(type="binary_op", op="-",
                left=Node("custom_call", receiver=node.receiver, function="find",
                          args=[Node(type="local", name=f"{node.receiver.name}.begin()"),
                                Node(type="local", name=f"{node.receiver.name}.end()"),
                                node.args[0]]),
                right=Node(type="local", name=f"{node.receiver.name}.begin()"))


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


def translate_min(node):
    return translate_min_max(node, "std::min")


def translate_max(node):
    return translate_min_max(node, "std::max")

class CppRules(GeneralRule):
    def __init__(self):
        GeneralRule.__init__(self)

    binary_op = {"and": "&&",
                 "or": "||",
                 "not": "!",
                 "is_not": "!=",
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
        "not": "!",
        "+": "+",
        "-": "-",
        "~": "~"
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
        "math": {
            "ln": "std::log",
            "log": translate_log,
            "tan": "std::tan",
            "sin": "std::sin",
            "cos": "std::cos",
            "asin": "std::asin",
            "acos": "std::acos",
            "atan": "std::atan",
            "sqrt": "std::sqrt",
            "ceil": "(int) std::ceil",
            "round": "std::round",
            "exp": "std::exp",
            "pow": "std::pow",
            "floor": "std::floor",
            "isnan": "std::isnan",
        },
        "io": {
            "print": "std::cout << ",
            "read": "Console.ReadLine",
            "read_file": "File.ReadAllText",
            "write_file": "File.WriteAllText"
        },
        "system": {
            "min": translate_min,
            "max": translate_max,
            "abs": "std::abs",
            "pow": "std::pow"
        },
        "datetime": {
            "datetime": lambda node: Node(type="str", value=args_to_str(node.args))
        }
    }

    constant = {
        "math": {
            "pi": "M_PI"
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
            'len': translate_len_str
        },
        'list': {
            'len': translate_len_list,
            'append': '.push_back',
            'sum': translate_sum,
            'pop': translate_pop,
            'insert_at': translate_insert,
            'contains?': translate_contains,
            'not contains?': translate_not_contains,
            'index': translate_index,
            "allocate": lambda node: Node("assignment", target=node.receiver,
                                          value=Node("list", elements=node.args,
                                                     pseudo_type=node.receiver.pseudo_type))
        },
        'dict': {
            'len': translate_len_dict,
            'keys': translate_key_dict,
            "get": translate_get
        },
        'array': {
            'len': translate_len_array,
            'sum': translate_sum,
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


def args_to_str(args):
    t = []
    for arg in args:
        t.append(arg.value)
    return '/'.join(t)
