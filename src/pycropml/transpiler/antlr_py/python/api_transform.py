# coding: utf8
##########################################

# inspired from pseudo-python

from __future__ import absolute_import
from __future__ import print_function
from pycropml.transpiler.builtin_typed_api import builtin_type_check
from pycropml.transpiler.errors import PseudoCythonTypeCheckError
from pycropml.transpiler.pseudo_tree import  Node
from datetime import datetime

class Standard:
    '''
    Standard classes should respond to expand and to return
    valid nodes on expand
    '''
    pass

class StandardCall(Standard):
    '''
    converts to a standard call of the given namespace and function
    '''
    def __init__(self, namespace, function, expander=None):
        self.namespace = namespace
        self.function  = function
        self.expander = expander

    def expand(self, args):
        if not self.expander:
            q = builtin_type_check(self.namespace, self.function, None, args)[-1]
            return {'type': 'standard_call', 'namespace': self.namespace, 'function': self.function, 'args': args, 'pseudo_type': q}
        else:
            return self.expander(self.namespace, self.function, args)


class StandardCallAttrib(Standard):
    '''
    converts to a standard call of the given namespace and function
    '''
    def __init__(self, namespace, function, expander=None):
        self.namespace = namespace
        self.function  = function
        self.expander = expander

    def expand(self, args=[]):
        if not self.expander:
            q = builtin_type_check(self.namespace, self.function, None, args=[])[-1]
            return {'type': 'standard_call', 'namespace': self.namespace, 'function': self.function, 'args': [], 'pseudo_type': q}
        else:
            return self.expander(self.namespace, self.function, args)
class StandardMethodCall(Standard):
    '''
    converts to a method call of the same class
    '''
    def __init__(self, type, message, default=None, expander=None):
        self.type = type
        self.message = message
        self.default = default
        self.expander = expander

    def expand(self, args):
        if self.default and len(args) - 1 in self.default:
            args += self.default[len(args) - 1]
        if not self.expander:
            q = builtin_type_check(self.type, self.message, args[0], args[1:])[-1]
            return {'type': 'standard_method_call', 'receiver': args[0], 'message': self.message, 'args': args[1:], 'pseudo_type': q}
        else:
            return self.expander(self.type, self.message, args)


class StandardSwapper(Standard):
    def __init__(self, type, message):
        self.type = type
        self.message = message

    def expand(self, args):
        if len(args) < 2:
            raise PseudoCythonTypeCheckError('%s expects more args' % self.message)
        q = builtin_type_check(self.type, self.message, args[1], [args[0]])[-1]
        return {'type': 'standard_method_call', 'receiver': args[1], 'args': [args[0]], 'message': self.message, 'pseudo_type': q}

def int_expander(type, message, args):
    return len_expander(type, message, args)

def float_expander(type, message, args):
    return len_expander(type, message, args)

def len_expander(type, message, args):
    receiver_type = args[0]['pseudo_type']
    if isinstance(receiver_type, list):
        a = receiver_type[0]
    else:
        a = receiver_type
    # print(a, message, args[0], args[1:])
    # input(0)
    if message == 'len' and 'special' in args[0]: # len(sys.argv)
        return {'type': 'standard_call', 'namespace': 'system', 'function': 'arg_count', 'args': [], 'pseudo_type': 'Int'}
    else:
        q = builtin_type_check(a, message, args[0], args[1:])
        if a =="str" and message =="float" and args[0]["value"]==b"nan":
            return {"type":'notAnumber', 'value' : 'nan', 'pseudo_type':'float'}
        else: 
            return {'type': 'standard_method_call', 'receiver':args[0], 'args': [], 'message': message, 'pseudo_type': q[-1]}

def min_expander(type, message, args):
    if len(args)==1:
        return {'type': 'standard_call', 'namespace': 'system', 'function': 'min', 'args': args, 'pseudo_type': args[0]["pseudo_type"][1]}
    else:
        for i in range(len(args)-1):
            if args[i]["pseudo_type"]!=args[i+1]["pseudo_type"]:
                pseudo = "float"
                break
            else: pseudo = args[i]["pseudo_type"]
        return {'type': 'standard_call', 'namespace': 'system', 'function': 'min', 'args': args, 'pseudo_type': pseudo}
        
def max_expander(type, message, args):
    if len(args)==1:
        return {'type': 'standard_call', 'namespace': 'system', 'function': 'max', 'args': args, 'pseudo_type': args[0]["pseudo_type"][1]}
    else:
        for i in range(len(args)-1):
            if args[i]["pseudo_type"]!=args[i+1]["pseudo_type"]:
                pseudo = "float"
                break
            else: pseudo = args[i]["pseudo_type"]
        return {'type': 'standard_call', 'namespace': 'system', 'function': 'max', 'args': args, 'pseudo_type':pseudo}
  
def abs_expander(type, message, args):
    return {'type': 'standard_call', 'namespace': 'system', 'function': 'abs', 'args': args, 'pseudo_type': args[0]["pseudo_type"]}

def datetime_expander(type, message, args):
    if len(args)==3:
        a = datetime(eval(args[0]["value"]),eval(args[1]["value"]),eval(args[2]["value"]) )
    elif len(args)==4:
        a = datetime(eval(args[0]["value"]),eval(args[1]["value"]),eval(args[2]["value"]),eval(args[3]["value"]) )
    elif len(args)==5:
        a = datetime(eval(args[0]["value"]),eval(args[1]["value"]),eval(args[2]["value"]),eval(args[3]["value"]),eval(args[4]["value"]) )
    elif len(args)==6:
        a = datetime(eval(args[0]["value"]),eval(args[1]["value"]),eval(args[2]["value"]),eval(args[3]["value"]),eval(args[4]["value"]),eval(args[5]["value"]) )
    else: raise PseudoCythonTypeCheckError('datetime expects 3, 4, 5 or 6 args')
    
    return {'type': 'standard_call', 'namespace': 'datetime', 'function': 'datetime', 'args': args, 'pseudo_type': 'datetime'}

def array_expander(type, message, args):
    if args[-1]["type"]=="list":
        res = {'type': 'array', 'elements': args[-1]["elements"], 'dim': len(args[-1]["elements"]), 'pseudo_type': ['array',args[-1]["pseudo_type"][-1]]}
    else:
        res = {'type': 'array', 'elements': args[-1], 'pseudo_type': ['array',args[-1]["pseudo_type"][-1]]}
    return res

def copy_expander(type, message, args):
    return {'type': 'standard_call', 'namespace': 'system', 'function':'copy', 'args': args[0], 'pseudo_type': args[0]["pseudo_type"]}


def pow_expander(type, message, args):
    x1 = args[0]["pseudo_type"]
    x2 = args[1]["pseudo_type"]
    if x1=="int" and x2=="int" : 
        if "value" in dir(args[1]):
            val = -(int(args[1]["value"]["value"])) if args[1]["type"]=="unary_op" else args[1]["value"] 
            if int(val)<0:
                q="float"
            else:
                q="int"
        else:
            if args[1]["pseudo_type"]=="int": q = "int"
            else: q="float"
    else:
        q="float"

    return {'type': 'standard_call', 'namespace': 'system', 'function': 'pow', 'args': args, 'pseudo_type':q}

def modulo_expander(type, message, args):
    return {'type': 'standard_call', 'namespace': 'system', 'function': 'modulo', 'args': args, 'pseudo_type':"int"}

def integr_expander(type, message, args):
    
    if isinstance(args[0]["pseudo_type"], list) and isinstance(args[1]["pseudo_type"] ,list):
        if args[1]["pseudo_type"][1] != args[0]["pseudo_type"][1]:
            raise PseudoCythonTypeCheckError('wrong usage of %s integr')
            
    if isinstance(args[0]["pseudo_type"], list) and not isinstance(args[1]["pseudo_type"] ,list):
        if args[1]["pseudo_type"] != args[0]["pseudo_type"][1]:
            raise PseudoCythonTypeCheckError('wrong usage of %s integr')
            
    return {'type': 'standard_call', 'namespace': 'system', 'function': 'integr', 'args': args, 'pseudo_type':args[0]["pseudo_type"]}


FUNCTION_API = {
    'global': {
        'input':    StandardCall('io', 'read'),
        'print':    StandardCall('io', 'display'),
        'str':      StandardCall('global', 'to_string'),
        'min':      StandardCall('global', 'min', expander=min_expander),
        'max':      StandardCall('global', 'max', expander=max_expander),
        'abs':      StandardCall('global', 'abs', expander = abs_expander),
        'len':      StandardMethodCall('list', 'len', expander=len_expander),
        'int':      StandardMethodCall('float', 'int', expander=int_expander),
        'float':    StandardMethodCall('int', 'float', expander=float_expander),
        'pow':      StandardCall('global', 'pow', expander = pow_expander),
        'modulo':      StandardCall('global', 'modulo', expander = modulo_expander),
        'copy':      StandardCall('global', 'copy', expander = copy_expander),
        'integr':      StandardCall('global', 'integr', expander = integr_expander),
        'array': StandardCall('global', 'integr', expander = array_expander)
        
        
    },

    'math': {
        'log':      {
            1:      StandardCall('math', 'ln'),
            2:      StandardCall('math', 'log')
        },

        'sin':      StandardCall('math', 'sin'),
        'cos':      StandardCall('math', 'cos'),
        'tan':      StandardCall('math', 'tan'),
        'acos':     StandardCall('math', 'acos'),
        'asin':     StandardCall('math', 'asin'),
        'atan':     StandardCall('math', 'atan'),
        'sqrt':     StandardCall('math', 'sqrt'),
        'ceil':     StandardCall('math', 'ceil'),
        'exp':      StandardCall('math', 'exp')
        
    },
    'datetime':{
        'datetime': StandardMethodCall('datetime', 'datetime', expander = datetime_expander )
        

    },
    'array':{
        'array': StandardMethodCall('numpy', 'array', expander = array_expander )
    }    
    
}

METHOD_API = {
    'str': {
        'split':      StandardMethodCall('str', 'split'),
        'join':       StandardSwapper('str', 'join'),
        'upper':      StandardMethodCall('str', 'upper'),
        'lower':      StandardMethodCall('str', 'lower'),
        'title':      StandardMethodCall('str', 'title'),
        'center':     StandardMethodCall('str', 'center', default={1: [{'type': 'str', 'value': ' ', 'pseudo_type': 'str'}]}),
        'find':      {
            1:        StandardMethodCall('str', 'find'),
            2:        StandardMethodCall('str', 'find_from')
        }
    },
    'list': {
        'append':   StandardMethodCall('list', 'append'),
        'pop':      StandardMethodCall('list', 'pop'),
        'insert':   {
            1:      StandardMethodCall('list', 'insert'),
            2:      StandardMethodCall('list', 'insert_at')
        },
        'remove':   StandardMethodCall('list', 'remove'),
        'extend':   StandardMethodCall('list', 'extend'),
        'map':      StandardMethodCall('list', 'map'),
        'filter':   StandardMethodCall('list', 'filter'),
        'copy':     StandardMethodCall('list', 'copy'),
        'index':    StandardMethodCall('list', 'index')
    },

    'dict': {
        'keys':     StandardMethodCall('dict', 'keys'),
        'values':   StandardMethodCall('dict', 'values'),
        'get':    StandardMethodCall('dict', 'get'),
        '[]':       StandardMethodCall('dict', 'getitem'),
        '[]=':      StandardMethodCall('dict', 'setitem')
    },

    'datetime': {
        'year':     StandardCallAttrib('datetime', 'year'),
        'month':     StandardCallAttrib('datetime', 'month'),
        'day':     StandardCallAttrib('datetime', 'day'),
        'hour':     StandardCallAttrib('datetime', 'hour'),
        'minute':     StandardCallAttrib('datetime', 'minute'),
        'second':     StandardCallAttrib('datetime', 'second')

    },

    'array': {
            'append':   StandardMethodCall('array', 'append'),
            'allocate': StandardMethodCall('array', 'allocate')
    },

    'tuple': {
    }
}

CONSTANT_API = {
      'math':{
              
              'pi':{'type':'constant', 'library':'math', 'pseudo_type':'float', 'name':'pi'}
              
              }  
        }

OPERATOR_API = {
    'list':  {
        '+':    'concat',
        '*':    'repeat'
    },
    'str': {
        '+':    'concat',
        '*':    'repeat',
        '%':    'c_format'
    }
}

