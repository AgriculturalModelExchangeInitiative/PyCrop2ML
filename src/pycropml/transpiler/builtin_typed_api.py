# coding: utf8
from __future__ import absolute_import
from pycropml.transpiler.errors import PseudoCythonTypeCheckError
from pycropml.transpiler.helpers import serialize_type
from Cython.Compiler import ExprNodes
from six.moves import zip


# based on pseudo
V = '_' # we don't really typecheck or care for a lot of the arg types, so just use this
_ = ()


'''Methods used to:
    -check data types compatibility
    
    - inference type compared with type declared
    
    - methods on builtin functions to check consistency
        
'''
def builtin_type_check(namespace, function, receiver, args):
    fs = TYPED_API[namespace]
    if fs == 'library':
        fs = TYPED_API['_%s' % namespace]
    # print(namespace, function, receiver, args, TYPED_API[namespace])
    # input(0)
    if function not in fs:        
        raise  PseudoCythonTypeCheckError('wrong usage of %s' % str(function))
    x = fs[function]

    a = namespace + '#' + function if receiver else namespace + ':' + function
    if namespace == 'list' or namespace == 'array':
        if not isinstance(receiver['pseudo_type'], list):
            generics = {'@t': args[0]['pseudo_type']}
            if receiver['pseudo_type']=="list": receiver["pseudo_type"]=["list",args[0]['pseudo_type']]
        else:
            generics = {'@t': receiver['pseudo_type'][1]}
    elif namespace == 'dict':
        generics = {'@k': receiver['pseudo_type'][1], '@v': receiver['pseudo_type'][2]}
    else:
        generics = {}

    
    s = []
    if x[0][0] == '*':
        e = x[0][1:]
        for arg in args:
            s.append(simplify(e, generics))
            arg_check(s[-1], arg, a)
    else:
        if len(x) - 1 != len(args):   
            raise PseudoCythonTypeCheckError("%s expects %d args not %d" % (a, len(x) - 1, args))
        for e, arg in zip(x[:-1], args):
            s.append(simplify(e, generics))
            arg_check(s[-1], arg, a)
    s.append(simplify(x[-1], generics))
    return s

def arg_check(expected_type, args, a):
    if expected_type != args['pseudo_type'] and expected_type != 'Any' and not(expected_type == 'Number' and (args['pseudo_type'] == 'int' or args['pseudo_type'] == 'float')):
        raise PseudoCythonTypeCheckError('%s expected %s not %s' % (a, serialize_type(expected_type), serialize_type(args['pseudo_type'])))

def simplify(kind, generics):
    if not generics:
        return kind
    elif isinstance(kind, str):
        if kind[0] == '@' and kind in generics:
            return generics[kind]
        else:
            return kind
    else:
        return [simplify(child, generics) for child in kind]

# refactoring here in future

def add(l, r):
    if l == 'float' and r in ['float', 'int']  or r == 'float' and l in ['float', 'int'] :
        return [l, r, 'float']
    elif l == 'int' and r == 'int':
        return [l, r, 'int']
    elif l == 'str' and r == 'str':
        return [l, r, 'str']
    elif isinstance(l, list) and l[0] == 'list' and l == r:
        return [l, r, l]
    elif l =="unknown" or r=="unknown":
        return [l, r, "unknown"]
    elif l =="unknown" or r=="unknown":
        return [l, r, "unknown"]
    else:
        raise PseudoCythonTypeCheckError("wrong types for +: %s and %s" % (serialize_type(l), serialize_type(r)))

def sub(l, r):
    if l == 'float' and r in ['float', 'int'] or r == 'float' and l in ['float', 'int']:
        return [l, r, 'float']
    elif l == 'int' and r == 'int':
        return [l, r, 'int']
    elif l =="unknown" or r=="unknown":
        return [l, r, "unknown"]    
    else:
        raise PseudoCythonTypeCheckError("wrong types for -: %s and %s" % (serialize_type(l), serialize_type(r)))

def mul(l, r):
    if l == 'float' and r in ['float', 'int'] or r == 'float' and l in ['float', 'int']:
        return [l, r, 'float']
    elif l == 'int' and r == 'int':
        return [l, r, 'int']
    elif l == 'int' and (isinstance(r, list) and r[0] == 'list' or r == 'str'): 
        return [l, r, r]
    elif r == 'int' and (isinstance(l, list) and l[0] == 'list' or l == 'str'):
        return [l, r, l]
    elif l =="unknown" or r=="unknown":
        return [l, r, "unknown"]    
    else:
        raise PseudoCythonTypeCheckError("wrong types for *: %s and %s" % (serialize_type(l), serialize_type(r)))

def div(l, r, lo=None):
    if l == 'float' and r in ['float', 'int'] or r == 'float' and l in ['float', 'int']:
        return [l, r, 'float']
    elif l == 'int' and r == 'int':
        return [l, r, 'int']
        #raise PseudoCythonTypeCheckError("cast one variable at line %s position %s between /: %s and %s" % (lo[0], lo[1], serialize_type(l), serialize_type(r)))
    elif l =="unknown" or r=="unknown":
        return [l, r, "unknown"]    
    else:
        raise PseudoCythonTypeCheckError("wrong types for /: %s and %s" % (serialize_type(l), serialize_type(r)))

def pow_(l, r):
    if l == 'float' and r in ['float', 'int'] or r == 'float' and l in ['float', 'int']:
        return [l, r, 'float']
    elif l == 'int' and r == 'int':
        return [l, r, 'int']
    elif l =="unknown" or r=="unknown":
        return [l, r, "unknown"]    
    else:
        raise PseudoCythonTypeCheckError("wrong types for **: %s and %s" % (serialize_type(l), serialize_type(r)))

def mod(l, r):
    if l == 'int' and r == 'int':
        return [l, r, 'int']
    elif l == 'str' and (r == 'str' or r == ['array', 'str']):
        return [l, ['array', 'str'], 'str']   
    else:
        raise PseudoCythonTypeCheckError("wrong types for modulo : %s and %s" % (serialize_type(l), serialize_type(r)))

def and_(l, r):
    if l == 'bool' and r == 'bool':
        return 'bool'
    else:
        raise PseudoCythonTypeCheckError("wrong types for and: %s and %s" % (serialize_type(l), serialize_type(r)))

def or_(l, r):
    if l == 'bool' and r == 'bool':
        return 'bool'
    else:
        raise PseudoCythonTypeCheckError("wrong types for or: %s and %s" % (serialize_type(l), serialize_type(r)))        

def binary_and(l, r):
    if l == r == 'int':
        return l
    else:
        raise PseudoCythonTypeCheckError("wrong types for &: %s and %s" % (serialize_type(l), serialize_type(r)))

def binary_or(l, r):
    if l == r == 'int' or l == r == 'Set':
        return l
    else:
        raise PseudoCythonTypeCheckError("wrong types for |: %s and %s" % (serialize_type(l), serialize_type(r)))



TYPED_API = {
        
    '__name__':'str',
    # methods
    'global': {
        'exit':  ['int', 'Void'],
        'to_str': ['Any', 'str']
    },

    'system': {
        'args':         [['list', 'str']]
    },


    'math': {
        'tan':          ['Number', 'float'],
        'atan':          ['Number', 'float'],
        'sin':          ['Number', 'float'],
        'asin':          ['Number', 'float'],
        'cos':          ['Number', 'float'],
        'acos':          ['Number', 'float'],
        'ln':           ['Number', 'float'],
        'log':          ['Number', 'Number', 'float'],
        'sqrt':         ['Number', 'float'],
        'ceil':         ['float', 'int'],
        'exp':          ['float','float'],
        'pi': 'pi',
        'floor':["Number", "int"]
        
        
    },

    'operators': {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div,
        '**': pow_,
        '%': mod,
        '&':   binary_and,
        '|':   binary_or,
    },
    
    'list': {
        'append':       ['@t', ['list', '@t']],
        'pop':        ['int','@t'],
        'insert':     ['@t', ['list', '@t']],
        'insert_at':  ['int', '@t', ['list', '@t']],
        'concat':     [['list', '@t'], ['list', '@t']],
        'repeat':     ['int', ['list', '@t']],
        'extend':  [['list', '@t'], 'Void'],
        'remove':     ['@t', 'Void'],
        'len':     ['int'],
        'join':       [['list', 'str'], 'str'],
        'map':        [['Function', '@t', '@y'], ['list', '@y']],
        'filter':     [['Function', '@t', 'bool'], ['list', '@t']],
        'index':      ['@t','int'],
        'copy':[['list','@t'],['list','@t']],
        'allocate': ['int',['list', '@t']]
    },

    'dict': {
        'keys':       [['list','@k']],
        'values':     [['list', '@v']],
        'len':     ['int'],
        'get':     ['@k','@v']
    },

    'datetime': {
        'datetime':['datetime'],
        'year':     ['int'],
        'month':    ['int'],
        'day':     ['int'],
        'hour':    ['int'],
        'minute':    ['int'],
        'second':     ['int']

    },



    'str': {
        'find':       ['str', 'int'],
        'int':     ['int'],
        'split':      ['str', ['list', 'str']],
        'c_format':   [['array', 'str'], 'str'],
        'upper':      ['str'],
        'lower':      ['str'],
        'title':      ['str'],
        'center':     ['int', 'str', 'str'],
        'find_from':  ['str', 'int', 'int'],
        'len':     ['int'],
        'float':['float']
    },

    'int': {'int': ['int'], 'float': ['float']},
    'float': {'int': ['int'], 'float': ['float']},
    'array': {
        'array': ['array'],
        'len':      ['int'],
        'index':       ['@t', 'int'],
        'count':       ['@t', 'int'],
        'append':       ['@t', ['array', '@t']],
        'allocate': ['int',['array', '@t']]
    },

    '_generic_list':    ['list', '@t'],
    '_generic_array':   ['array', '@t'],
    '_generic_Tuple':   ['Tuple', '@t'],
    '_generic_Dictionary': ['Dictionary', '@k', '@v'],
    # 'list#pop':        [_, '@t'],
    # 'list#insert':     [_, 'Null'],
    # 'list#remove':     [_, 'Null'],
    # 'list#remove_at':  [_, 'Null'],
    # 'list#length':     [_, 'int'],
    # 'list#concat_one': [_, 'list<@t>'],
    # 'list#concat':     [_, 'list<@t>'],
    # 'list#[]':         [_, '@t'],
    # 'list#[]=':        [_, 'Null'],
    # 'list#slice':      [_, 'list<@t>'],

    # 'Dict#keys':       [_, 'list<@k>'],
    # 'Dict#values':     [_, 'list<@v>'],
}
    
ORIGINAL_METHODS = {
    'list': {
        'append':       'append(element)',
        'pop':        'pop',
        'insert':     'insert(element)',
        'insert_at':  'insert(element, index)',
        'index':       'index(element)',
        'concat':     '+',
        'repeat':     '*',
        'extend':  'extend(other)',
        'remove':     'remove',
        'length':     'len',
        'copy':'copy',
        'map':        'list comprehension / map',
        'filter':     'list comprehension / filter',
        'allocate':'allocate(element)'
    },

    'dict': {
        'keys':       'keys',
        'values':     'values',
        'length':     'len',
        'copy':'copy',
        'get': 'get(element)'
    },

    'int': {
        'int':     'int',
        'float':   'float'
    },
    'float': {
        'int':     'int',
        'float':   'float'
    },
    'str': {
        'find':       'index(substr)',
        'join':       'join(elements)',
        'split':      'split(delimiter)',
        'c_format':   '%',
        'format':     'format(*elements)',
        'upper':      'upper',
        'lower':      'lower',
        'title':      'title',
        'center':     'center',
        'find_from':  'index(substr, index)',
        'int':     'int'
    },


    'array': {
        'length':      'len',
        'find':        'find(element)',
        'count':       'count(element)',
        'append':       'append(element)',
        'allocate':'allocate(element)'
    },

    'tuple': {
        'length':       'len'
    }
}
    



BUILTIN_TYPES = {
    'int':      'int',
    'float':    'float',
    'object':   'Object',
    'str':      'str',
    'list':     'list',
    'dict':     'dict',
    'tuple':    'tuple',
    'bool':     'bool',
    'array':    'array',
    "datetime": 'datetime'
}

PSEUDON_BUILTIN_TYPES = {v: k for k, v in BUILTIN_TYPES.items()}

BUILTIN_SIMPLE_TYPES = {
    'int':      'int',
    'float':    'float',
    'str':      'str',
    'bool':     'bool'
}

KEY_TYPES = {'str', 'int', 'float', 'bool'}

PSEUDO_KEY_TYPES = {'str', 'int', 'float', 'bool'}

BUILTIN_FUNCTIONS = {'print', 'input', 'str', 'set', 'int','float', 'len', 'any', 'all', 'sum', 'min', 'max', 'abs','pow', "mean", "count", "copy", "integr","array", "round", 'list', 'range'}

FORBIDDEN_TOP_LEVEL_FUNCTIONS = {'map', 'filter'}

ITERABLE_TYPES = {'str', 'list', 'dict', 'array'}

TESTABLE_TYPE = 'bool'

INDEXABLE_TYPES = {'str', 'list', 'dict', 'array', 'tuple'}

COMPARABLE_TYPES = {'int', 'float', 'str'}

TYPES_WITH_LENGTH = {'str', 'list', 'dict', 'array', 'tuple', 'Set'}

NUMBER_TYPES = {'int', 'float'}


PSEUDO_OPS = {
    ExprNodes.AddNode: '+',
    ExprNodes.SubNode: '-',
    ExprNodes.MulNode: '*',
    ExprNodes.DivNode: '/',
    ExprNodes.PowNode: '**',
    ExprNodes.PrimaryCmpNode: ['==','<','>','<=','>=','!=', 'in', 'not_in',"is"],
    ExprNodes.ModNode: '%',
    ExprNodes.BoolBinopNode: ['and','or']
}







##############################################
