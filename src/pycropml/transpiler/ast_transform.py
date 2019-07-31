# coding: utf-8
from __future__ import absolute_import
from __future__ import print_function
from Cython.Compiler import ExprNodes, Nodes
from pycropml.transpiler.pseudo_tree import Node
from pycropml.transpiler.env import Env
from pycropml.transpiler.builtin_typed_api import *
from pycropml.transpiler.errors import PseudoCythonTypeCheckError, PseudoCythonNotTranslatableError, translation_error, type_check_error
from pycropml.transpiler.api_transform import FUNCTION_API, METHOD_API, Standard
from Cython.Compiler.StringEncoding import EncodedString
from pycropml.transpiler.helpers import *
from six.moves import map
from six.moves import zip

class AstTransformer():
    def __init__(self, tree, code):
        self.tree = tree
        self.lines = [''] + code.split('\n')  # to access line of instruction
        self.type_env = Env(dict(list(TYPED_API.items())), None)

    def transformer(self):
        self.base = 0
        self.body = []
        self.arguments = []
        self.returnValue = []
        self.declarations = []
        self.definitions = []
        self._definition_index = {'functions': {}}
        self._hierarchy = {}
        self._imports = []
        self._fromimport = {}
        self._tuple_used = []
        self._tuple_assigned = []
        self.function_name = 'top level'
        self.type_env['functions'] = {}
        self.visit_top_level(self.tree.body)
        self.main = []
        self.forSequence = False
        self.signature = self.visit_definitions()
        body = self.visit_node(self.tree.body)
        self.type_env['__name__'] = "str"
        return {'type': 'module','definition':self.signature, 'body': body if isinstance(body, list) else [body]}

    def visit_definitions(self):
        definitions = []
        for definition in self.definitions:
            if definition[0] == 'function':
                definitions.append(
                    self._definition_index['functions'][definition[1]])
            else:
                print("error")  # do Assert
        return definitions

    def visit_top_level(self, nodes):
        if isinstance(nodes, ExprNodes.ImportNode):
            module_name = nodes.module_name.value
            self._imports.append(module_name)
            self.type_env.top['_%s' %
                              module_name], self.type_env.top[module_name] = self.type_env.top[module_name], 'library'
            return {"type": "import",
                    "module": module_name,
                    }
        elif isinstance(nodes, Nodes.FromImportStatNode):
            module = nodes.module.module_name.value
            if module == "math" and nodes.module.name_list.args[0].value == "*":
                name_list = list(FUNCTION_API["math"].keys())
            else:
                name_list = [name.value for name in nodes.module.name_list.args]
            self._fromimport[module] = name_list
            return {"type": "importfrom",
                    "namespace": module,
                    "name": name_list
                    }
        elif isinstance(nodes, Nodes.DefNode):
            self.definitions.append(('function', nodes.name))
            self._definition_index['functions'][nodes.name] = nodes
            self.type_env.top['functions'][nodes.name] = [
                'Function'] + ([None] * len(nodes.args)) + [None]
            self.type_env.top[nodes.name] = self.type_env.top['functions'][nodes.name]
        elif isinstance(nodes, Nodes.StatListNode):
            for node in nodes.stats:
                if isinstance(node, Nodes.DefNode):
                    self.visit_top_level(node)

    def visit_node(self, node):
        if isinstance(node, ExprNodes.ImportNode):
            return self.visit_top_level(node)
        if isinstance(node, Nodes.FromImportStatNode):
            return self.visit_top_level(node)
        elif isinstance(node, Nodes.Node):
            fields = {field: getattr(node, field)
                      for field in node.child_attrs}
            if "self" in fields:
                fields.pop("self")
            l = getattr(node, 'pos', None)
            fields["node"] = node
            if l:
                fields['location'] = l[1], l[2]
            else:
                fields['location'] = None
            return getattr(self, 'visit_%s' % type(node).__name__.lower())(**fields)
        elif isinstance(node, list):
            results = []
            for n in node:
                x = self.visit_node(n)
                if isinstance(x, list):
                    results.extend(x)
                else:
                    results.append(x)
            return results
        elif isinstance(node, dict):
            return {k: self.visit_node(v) for k, v in node.items()}
        else:
            return node

    def visit_statlistnode(self, node, stats, location):
        results = []
        for n in stats:
            x = self.visit_node(n)
            if isinstance(n, Nodes.DefNode) and not self.definitions:
                self.visit_top_level(n)
            if isinstance(x, list):
                results.extend(x)
            else:
                results.append(x)
        return results

    def visit_printstatnode(self, node, arg_tuple, stream, location):
        return {"type": "print",
                "elements": [self.visit_node(arg) for arg in arg_tuple.args],
                "pseudo_type": ['Tuple']+[self.visit_node(arg)["pseudo_type"] for arg in arg_tuple.args]}

    def visit_singleassignmentnode(self, node, lhs, rhs, location):
        if isinstance(rhs, Nodes.Node) and not isinstance(rhs, ExprNodes.ImportNode):
            value_node = self.visit_node(rhs)
        elif isinstance(rhs, ExprNodes.ImportNode):
            return self.visit_top_level(rhs)
        else:
            value_node = rhs
        if isinstance(lhs, ExprNodes.NameNode) and not isinstance(rhs, ExprNodes.ImportNode):
            name = lhs.name
            e = self.type_env[name]
            if e is None:
                self.notdeclared(name, location[0])
            elif e:
                if e in ("list", "dict", "tuple", "array"):
                    a = self._compatible_types(
                        e, value_node['type'], "can't change the type of variable %s in %s " % (name, self.function_name))
                else:
                    a = self._compatible_types(e, value_node['pseudo_type'], "can't change the type of variable %s in %s at %s " % (
                        name, self.function_name, location[0]))
            return {
                'type': 'assignment',
                'target': {
                        'type': 'local',
                        'name': name,
                        'pseudo_type': e
                },
                'value': value_node,
                'pseudo_type': 'Void'
            }
        meth = [d for m in list(self._fromimport.values()) for d in m]
        if isinstance(lhs, ExprNodes.TupleNode):
            if isinstance(rhs, ExprNodes.SimpleCallNode):
                if rhs.function.name not in meth:
                    print("err")
                else:
                    return {
                        'type': 'assignment',
                        'target': self.visit_node(lhs),
                        'value': self.visit_node(rhs),
                        'pseudo_type': 'Void'
                    }
            elif not isinstance(rhs, ExprNodes.TupleNode):
                raise translation_error(
                    'assignment error',
                    location, self.lines[location[0]])
            elif len(lhs.args) != len(rhs.args):
                raise translation_error(
                    'expected %d number of values on right' % len(lhs.args),
                    location, self.lines[location[0]])
            rights = []
            used = []
            u = 0
            for t, child in zip(lhs.args, rhs.args):
                child_node = self.visit_node(child)
                x = self.visit_node(t)
                for a in self._tuple_used[u:]:
                    used.append({
                        'type': 'assignment',
                        'target': {'type': 'local', 'name': a[0], 'pseudo_type': a[1]['pseudo_type']},
                        'value': a[1],
                        'pseudo_type': 'Void'
                    })
                    self.type_env.top[a[0]] = a[1]['pseudo_type']
                u = len(self._tuple_used)
                rights.append(self.visit_singleassignmentnode(
                    node, t, child_node, location))
                self._tuple_assigned.append(rights[-1]['target'])
            self._tuple_assigned = []
            self._tuple_used = []
            return used + rights
        elif isinstance(lhs, ExprNodes.IndexNode) or isinstance(lhs, ExprNodes.SliceIndexNode):
            z = self.visit_node(lhs)
            if z['type'] == 'index' or z['type'] == "sliceindex":
                return {
                    'type': 'assignment',
                    'target': z,
                    'value': value_node,
                    'pseudo_type': 'Void'
                }
            elif z['type'] == 'standard_method_call':  # slice
                if z['pseudo_type'] != value_node['pseudo_type']:
                    raise type_check_error(
                        'expected %s' % serialize_type(z['pseudo_type']),
                        getattr(rhs, 'location',
                                location), self.lines[location[0]],
                        wrong_type=value_node['pseudo_type'])
                z['message'] = 'set_%s' % z['message']
                z['args'].append(value_node)
                z['pseudo_type'] = 'Void'
                return z

    def visit_inplaceassignmentnode(self, node, lhs, rhs, location):
        z = node.end_pos()
        newNode = ExprNodes.BinopNode(
            pos=z, operand1=lhs, operand2=rhs, operator=node.operator)
        return self.visit_singleassignmentnode(node, lhs, ExprNodes.BinopNode(pos=z, operand1=lhs, operand2=rhs, operator=node.operator, node=newNode), location)

    def visit_binopnode(self, node, operand1, operand2, location):
        op = node.operator
        left_node, right_node = self.visit_node(
            operand1), self.visit_node(operand2)
        binop_type = TYPED_API['operators'][op](
            left_node['pseudo_type'], right_node['pseudo_type'])[-1]
        return {'type': 'binary_op',
                'op': op,
                'left': left_node,
                'right': right_node,
                'pseudo_type': binop_type
                }

    def visit_namenode(self, node, location):
        id = node.name
        id_type = self.type_env[id]
        if id_type is None:
            raise type_check_error(
                '%s is not defined' % id,
                location, self.lines[:location[1]])
        else:
            z = {'type': 'local', 'name': id, 'pseudo_type': id_type}
            if z in self._tuple_assigned:
                if not any(a[0] == '_old_%s' % id for a in self._tuple_used):
                    self._tuple_used.append(('_old_%s' % id, z))
                    z = {'type': 'local', 'name': '_old_%s' % id,
                         'pseudo_type': id_type}
            return z

    def visit_intnode(self, node, location):
        if int(node.value) < 0:
            return {
            'type': 'unary_op',
                    'operator': '-',
                    'value':{'type':"int",
                             'value':str(-int(node.value)),
                             "pseudo_type":"int"                        
                            },
                    'pseudo_type': "int"
                    }  
        return {'type': 'int', 'value': node.value, 'pseudo_type': 'int'}

    def visit_floatnode(self, node, location):
        '''if float(node.value) < 0.0:
            return {
            'type': 'unary_op',
                    'operator': '-',
                    'value': str(-float(node.value)),
                    'pseudo_type': "float"
                    }'''        
        return {'type': 'float', 'value': node.value, 'pseudo_type': 'float'}

    def visit_listnode(self, node, args, mult_factor, location):
        if not args:
            return {'type': 'list', 'elements': [], 'pseudo_type': ['list', None]}
        element_nodes, element_type = self.visit_elements(args, 'list')
        return {
            'type': 'list',
            'pseudo_type': ['list', element_type],
            'elements': element_nodes
        }

    def visit_boolnode(self, node, location):
        return {'type': 'bool', 'value': node.value, 'pseudo_type': 'bool'}

    def visit_indexnode(self, node, base, index, location):
        value_node = self.visit_node(base)
        # print("val",value_node)
        if isinstance(base, ExprNodes.IndexNode):
            value_general_type = "array"
        else:
            value_general_type = self._general_type(value_node['pseudo_type'])
        if value_general_type not in INDEXABLE_TYPES and value_general_type != "unknown":
            raise type_check_error('pseudo-cython can use [] only on String, List, Dictionary or Tuple',
                                   location, self.lines[location[0]],
                                   wrong_type=value_node['pseudo_type'])
        if isinstance(index, Nodes.Node):
            z = self.visit_node(index)
            if value_general_type in ['str', 'list', 'tuple'] and z['pseudo_type'] != 'int':
                raise PseudoCythonTypeCheckError(
                    'a non int index for %s %s' % (value_general_type, z['pseudo_type']))
            if value_general_type == 'dict' and z['pseudo_type'] != value_node['pseudo_type'][1]:
                raise PseudoCythonTypeCheckError('a non %s index for %s %s' % (
                    value_node['pseudo_type'][1], value_general_type, z['pseudo_type']))
            if value_general_type == 'str':
                pseudo_type = 'str'
            elif value_general_type in ('list', 'array', "tuple", "dict", "unknown"):
                pseudo_type = value_node['pseudo_type'][1]
            result = {
                'type': 'index',
                'sequence': value_node,
                'index': z,
                'pseudo_type': pseudo_type
            }
            return result
        else:
            print("todo")
            """
            TODO
            """
            #return self._translate_slice(receiver=value_node, upper=slice.upper, step=slice.step, lower=slice.lower, location=location)

    def visit_unicodenode(self, node, location):
        return {'type': 'unicode', 'value':  node.value, 'pseudo_type': 'str'}

    def visit_stringnode(self, node, location):
        return {'type': 'str', 'value':  node.value, 'pseudo_type': 'str'}

    def visit_tuplenode(self, node, args, mult_factor, location):
        element_nodes, accidentaly_homogeneous, element_type = self.visit_elements(
            args, 'tuple', homogeneous=False)
        return {
            'type': 'array' if accidentaly_homogeneous else 'tuple',
            'pseudo_type': ['array', element_type, len(args)] if accidentaly_homogeneous else ['tuple'] + element_type,
            'elements': element_nodes
        }

    def visit_dictnode(self, node, key_value_pairs, location):
        if not key_value_pairs:
            return {'type': 'dict', 'pairs': [], 'pseudo_type': ['dict', None, None]}
        pairs = [{'type': 'pair', 'key': self.visit_node(
            key_value_pairs[0].key), 'value': self.visit_node(key_value_pairs[0].value)}]
        key_type, value_type = pairs[0]['key']['pseudo_type'], pairs[0]['value']['pseudo_type']
        for a, b in zip(key_value_pairs[1:], key_value_pairs[1:]):
            pairs.append({'type': 'pair', 'key': self.visit_node(
                a.key), 'value': self.visit_node(b.value)})
            key_type, value_type = self._compatible_types(key_type, pairs[-1]['key']['pseudo_type'], "can't use different types for keys of a dictionary"),\
                self._compatible_types(
                    value_type, pairs[-1]['value']['pseudo_type'], "can't use different types for values of a dictionary")
        return {
            'type': 'dict',
            'pseudo_type': ['dict', key_type, value_type],
            'pairs': pairs
        }

    def visit_unaryminusnode(self, node, operand, location):
        return {
            'type': 'unary_op',
                    'operator': '-',
                    'value': self.visit_node(operand),
                    'pseudo_type': self.visit_node(operand)['pseudo_type']
        }

    def visit_notnode(self, node, operand, location):
        return {
            'type': 'unary_op',
                    'operator': 'not',
                    'value': self.visit_node(operand),
                    'pseudo_type': self.visit_node(operand)['pseudo_type']
        }

    def visit_unaryplusnode(self, node, operand, location):
        return {
            'type': 'unary_op',
                    'operator': '+',
                    'value': self.visit_node(operand),
                    'pseudo_type': self.visit_node(operand)['pseudo_type']
        }

    def visit_elements(self, elements, kind, homogeneous=True):
        element_nodes = self.visit_node([elements[0]])
        element_type = element_nodes[0]['pseudo_type']
        if not homogeneous:
            element_types = [element_type]
        accidentaly_homogeneous = False
        for j, element in enumerate(elements[1:]):
            element_nodes.append(self.visit_node(element))
            if homogeneous:
                element_type = self._compatible_types(
                    element_nodes[-1]['pseudo_type'], element_type, "can't use different types in a %s" % kind)
            else:
                element_types.append(element_nodes[-1]['pseudo_type'])
                if accidentaly_homogeneous:
                    element_type = self._compatible_types(
                        element_type, element_nodes[-1]['pseudo_type'], '', silent=True)
                    accidentaly_homogeneous = element_type is not True
        return (element_nodes, element_type) if homogeneous else (element_nodes, accidentaly_homogeneous, element_type if accidentaly_homogeneous else element_types)

    def visit_simplecallnode(self, node, function, coerced_self, args, arg_tuple, location):

        if isinstance(function, ExprNodes.NameNode) and function.name in BUILTIN_FUNCTIONS:
            if function.name in ['any', 'all', 'sum']:
                if len(args) != 1:
                    raise translation_error('%s expected 1 arg, not %d' % (function.name, len(args)),
                                            location, self.lines[location[0]])
                else:
                    arg_node = self.visit_node(args[0])
                    if function.name != 'sum':
                        if arg_node['pseudo_type'] != ['list', 'bool']:
                            raise type_check_error('%s expected list[bool]' % function.name,
                                                   location,
                                                   self.lines[location[0]],
                                                   wrong_type=arg_node['pseudo_type'])
                        message = function.name
                        return {
                            'type': 'standard_method_call',
                            'receiver': arg_node,
                            'message': message,
                            'args': [],
                            'pseudo_type': "bool"
                        }
                    else:
                        if arg_node['pseudo_type'] != ['list', 'int'] and arg_node['pseudo_type'] != ['list', 'float'] and arg_node['pseudo_type'] != "unknown":
                            raise type_check_error('%s expected list[int] / list[float]' % function.name,
                                                   location,
                                                   self.lines[location[0]],
                                                   wrong_type=arg_node['pseudo_type'])
                        message = function.name
                        _type = arg_node['pseudo_type'][1]
                        return {
                            'type': 'standard_method_call',
                            'receiver': arg_node,
                            'message': 'sum',
                            'args': [],
                            'pseudo_type': _type
                        }
            else:
                arg_nodes = self.visit_node(args)
                return self._translate_builtin_call('global', function.name, arg_nodes, location, attrib=0)

        elif isinstance(function, ExprNodes.NameNode):
            if not self._fromimport and function.name not in list(self.type_env.top['functions'].keys()):
                print("errr")
            c = self.type_env.top['functions']
            message = function.name
            param_types = [param['pseudo_type'] for param in self.visit_node(args)]
            if message in c:
                if len(c[message]) == 2 or len(c[message]) > 2 and c[message][1]:
                    g = self.type_env.top.values.get("functions", {}).get(message)[1:]
                    q = self._type_check(g,message, param_types)[-1]
                else:
                    v = self.function_name
                    x = [f for f in self.signature if f.name == message]
                    #argx = [a["pseudo_type"] for a in self.visit_node(x[0].args)]
                    self._definition_index["functions"][message] = self.visit_node(x[0])
                    q = c[message][-1]
                    #returnx = [self.visit_node(x[0].body.stats[-1])["pseudo_type"]]
                    #q = self._type_check(argx+returnx,message, param_types)[-1]
                    self.function_name = v                                
                return {
                    "type": "custom_call",
                    "args": self.visit_node(args),
                    "function": message,
                    "pseudo_type": q}
            else:
                arg_nodes = [arg if not isinstance(
                    arg, ExprNodes.Node) else self.visit_node(arg) for arg in args]
                meth = [d for m in list(self._fromimport.values()) for d in m]
                if function.name not in meth:
                    print("err")
                else:
                    if self.retrieve_library(function.name) not in self._imports:
                        self._imports.append(
                            self.retrieve_library(function.name))
                    return self._translate_builtin_call(self.retrieve_library(function.name), function.name, arg_nodes, location, attrib=0)
        elif isinstance(function, ExprNodes.AttributeNode):
            value_node = self.visit_node(function.obj)
            function = function.attribute
            if value_node['pseudo_type'] == 'library':  # math.log
                return self._translate_builtin_call(value_node['name'], function, self.visit_node(args), location, attrib=1)
            # [2].append
            elif self._general_type(value_node['pseudo_type']) in PSEUDON_BUILTIN_TYPES:
                return self._translate_builtin_method_call(self._general_type(value_node['pseudo_type']), value_node, function, self.visit_node(args), location)
            else:
                print('TODO method_call')

    def retrieve_library(self, func):
        for lib, meth in self._fromimport.items():
            for m in meth:
                if m == func:
                    library = lib
                    break
        return library

    def _translate_builtin_method_call(self, class_type, base, message, args, location):
        if class_type not in METHOD_API:
            raise translation_error(
                "pseudo-cython doesn't support %s" % class_type,
                location, self.lines[location[0]],
                suggestions='pseudo-cython support those builtin classes:\n%s' % ' '.join(
                    PSEUDON_BUILTIN_TYPES[k] for k in METHOD_API.keys()))
        api = METHOD_API.get(class_type, {}).get(message)
        if not api:
            raise translation_error(
                "pseudo-cython doesn\'t support %s#%s" % (
                    serialize_type(class_type), message),
                location, self.lines[location[0]],
                suggestions='pseudo-cython supports those %s methods:\n%s' % (
                    PSEUDON_BUILTIN_TYPES[class_type],
                    prepare_table(TYPED_API[class_type], ORIGINAL_METHODS.get(class_type)).strip()))
        if isinstance(api, Standard):
            #print(args,class_type, base, message)
            if base["pseudo_type"] == "list":
                self.type_env.top[base["name"]] = [
                    "list", args[0]["pseudo_type"]]
            return api.expand([base] + args)
        else:
            for count, b in api.items():
                if len(args) == count:
                    return b.expand([base] + args)
            raise translation_error(
                'pseudo-cython doesn\'t support %s%s with %d args' % (
                    serialize_type(class_type), message, len(args)),
                location, self.lines[location[0]])

    def _translate_builtin_call(self, namespace, function, args, location, attrib):
        if namespace != 'global' and namespace not in self._imports:
            raise type_check_error(
                'module %s not imported: impossible to use %s' % (
                    namespace, function),
                location, self.lines[location[0]],
                suggestions='a tip: pseudo-cython currently supports only import, no import as or from..import')
        if namespace not in FUNCTION_API and namespace not in self._imports:
            raise translation_error(
                "pseudo-cython doesn't support %s" % namespace,
                location, self.lines[location[0]],
                suggestions='pseudo-cython supports methods from\n  %s' % ' '.join(
                    k for k in FUNCTION_API if k != 'global'))
        if namespace in FUNCTION_API:
            api = FUNCTION_API[namespace].get(function)
            if not api:
                raise translation_error('pseudo-cython doesn\' t support %s %s' % (namespace, function),
                                        location, self.lines[location[0]],
                                        suggestions='pseudo-cython supports those %s functions\n  %s' % (
                    namespace,
                    prepare_table(TYPED_API[namespace], ORIGINAL_METHODS.get(namespace)).strip()))

            elif not isinstance(api, dict):
                z = api.expand(args)
                if attrib == 1:
                    z["attrib"] = 1
                return z
            else:
                for count, (a, b) in enumerate(list(api.items())):
                    if len(args) == a:
                        return b.expand(args)
                raise translation_error(
                    'pseudo-cython doesn\'t support %s%s with %d args' % (
                        namespace, function, len(args)),
                    location, self.lines[location[0]])
        if namespace in self._imports:
            return {
                'type': 'custom_call',
                'namespace': namespace,
                'args': self.visit_node(args),
                'pseudo_type': "unknown",
                'function': function
            }

    def visit_condexprnode(self, node, test, true_val, false_val, location):
        val1 = self.visit_node(true_val)
        val2 = self.visit_node(false_val)
        a = self._compatible_types(
            val1["pseudo_type"], val2["pseudo_type"], "can't change the type of variable")
        return {
            'type': 'cond_expr_node',
            'test': self.visit_node(test),
            'true_val': self.visit_node(true_val),
            'pseudo_type': a,
            'false_val': self.visit_node(false_val)
        }

    def visit_mulnode(self, node, operand1, operand2, location):
        op = node.operator
        operand1 = node.operand1
        operand2 = node.operand2
        left_node, right_node = self.visit_node(
            operand1), self.visit_node(operand2)
        binop_type = TYPED_API['operators'][op](
            left_node['pseudo_type'], right_node['pseudo_type'])[-1]
        return {'type': 'binary_op',
                'op': op,
                'left': left_node,
                'right': right_node,
                'pseudo_type': binop_type
                }

    def visit_divnode(self, node, operand1, operand2, location):
        op = node.operator
        operand1 = node.operand1
        operand2 = node.operand2
        left_node, right_node = self.visit_node(
            operand1), self.visit_node(operand2)
        binop_type = TYPED_API['operators'][op](
            left_node['pseudo_type'], right_node['pseudo_type'])[-1]
        return {'type': 'binary_op',
                'op': op,
                'left': left_node,
                'right': right_node,
                'pseudo_type': binop_type
                }

    def visit_subnode(self, node, operand1, operand2, location):
        op = node.operator
        operand1 = node.operand1
        operand2 = node.operand2
        left_node, right_node = self.visit_node(
            operand1), self.visit_node(operand2)
        binop_type = TYPED_API['operators'][op](
            left_node['pseudo_type'], right_node['pseudo_type'])[-1]
        return {'type': 'binary_op',
                'op': op,
                'left': left_node,
                'right': right_node,
                'pseudo_type': binop_type
                }

    def visit_addnode(self, node, operand1, operand2, location):
        op = node.operator
        operand1 = node.operand1
        operand2 = node.operand2
        left_node, right_node = self.visit_node(
            operand1), self.visit_node(operand2)
        binop_type = TYPED_API['operators'][op](
            left_node['pseudo_type'], right_node['pseudo_type'])[-1]
        return {'type': 'binary_op',
                'op': op,
                'left': left_node,
                'right': right_node,
                'pseudo_type': binop_type
                }

    def visit_modnode(self, node, operand1, operand2, location):
        op = node.operator
        operand1 = node.operand1
        operand2 = node.operand2
        left_node, right_node = self.visit_node(
            operand1), self.visit_node(operand2)
        binop_type = TYPED_API['operators'][op](
            left_node['pseudo_type'], right_node['pseudo_type'])[-1]

        return {
            'type': 'standard_call',
                    'namespace': 'system',
                    'args': [left_node, right_node],
                    'pseudo_type': binop_type,
                    'function': 'modulo'
        }

    def visit_pownode(self, node, operand1, operand2, location):
        op = node.operator
        operand1 = node.operand1
        operand2 = node.operand2
        left_node, right_node = self.visit_node(
            operand1), self.visit_node(operand2)
        binop_type = TYPED_API['operators'][op](
            left_node['pseudo_type'], right_node['pseudo_type'])[-1]

        return {
            'type': 'standard_call',
                    'namespace': 'system',
                    'args': [left_node, right_node],
                    'pseudo_type': binop_type,
                    'function': 'pow'
        }

    def visit_exprstatnode(self, node, expr, location):
        return {
            "type": "ExprStatNode",
            "expr": self.visit_node(expr)
        }

    def visit_defnode(self, node, args, star_arg, starstar_arg, decorators, body, return_type_annotation, location):
        self.function_name = node.name
        arg_nodes = [arg if not isinstance(
            arg, Nodes.Node) else self.visit_node(arg) for arg in args]
        env = {a["name"]: a["pseudo_type"] for a in arg_nodes}
        self.type_env, old_type_env = self.type_env.top.child_env(
            env), self.type_env
        
        domain_func = list(env.values())
        '''domain_func = []
        for arg in args:
            if isinstance(arg.declarator, Nodes.CArrayDeclaratorNode):
                domain_func.append(["array", arg.base_type.name])
            else:
                domain_func.append(arg.base_type.name)'''
        self.type_env.top["functions"][node.name][1:-1] = domain_func
        children = self.visit_node(body)
        self.type_env = old_type_env
        q = {
            'type':   "function_definition",
            'name':   node.name,
            'params': arg_nodes,
            'pseudo_type': self.type_env.top["functions"][node.name],
            'return_type': self.type_env.top["functions"][node.name][-1],
            'block': children
        }
        return q

    def visit_cargdeclnode(self, node, base_type, declarator, default, annotation, location):
        name = declarator.base.name if isinstance(
            declarator, Nodes.CArrayDeclaratorNode) else declarator.name
        if default is None:
            decl = {"name": name, "type": self.visit_node(base_type)[1]}
        else:
            decl = {"name": name, "type": base_type.name}
        if default and type(default) not in ( ExprNodes.ListNode, ExprNodes.DictNode, ExprNodes.TupleNode):
            de = self.visit_node(default)
            if isinstance(default, ExprNodes.UnaryMinusNode):
                decl["value"] = str(-float(de["value"]["value"]))
            elif isinstance(default, ExprNodes.NameNode): 
                decl["value"] = de["name"] 
            else: decl["value"] = de["value"] 
            decl["pseudo_type"] = de["pseudo_type"]
            if not isinstance(default, ExprNodes.NameNode):
                self._compatible_types(base_type.name, decl["pseudo_type"], "can't change the type of variable %s in %s " % (
                name, self.function_name))
        elif default and (isinstance(default, ExprNodes.ListNode)or isinstance(default, ExprNodes.TupleNode)):
            arglist = []
            for arg in default.args:
                arglist.append(self.visit_node(arg))
            decl["elements"] = arglist
            if type(default) == ExprNodes.ListNode:
                self.visit_node(default)
                decl["pseudo_type"] = ["list"]+[arglist[0]["pseudo_type"]]
            else:
                decl["pseudo_type"] = ["tuple"]+[arg["pseudo_type"]
                                                 for arg in arglist]
        elif isinstance(default, ExprNodes.DictNode):
            default = self.visit_node(default)
            decl["pairs"] = default["pairs"]
            decl["pseudo_type"] = default["pseudo_type"]

        elif isinstance(declarator, Nodes.CArrayDeclaratorNode):
            de = declarator
            if isinstance(de.dimension, ExprNodes.NameNode):
                elts = [{'type': 'local', 'name': de.dimension.name, 'pseudo_type': "int"}]
            
            elif isinstance(de.dimension, ExprNodes.IntNode):
                elts = [ {'type': 'int', 'value': de.dimension.value, 'pseudo_type': 'int'}]
            
            elif de.dimension is None:
                elts = []
            else:
                elts = []
                for d in self.visit_node(de.dimension.args):
                    elts.append(d)
            dim = len(elts)
            decl = {"name": de.base.name, "type": "local", "dim": dim,
                    "elts": elts, "pseudo_type": ["array", base_type.name]}
            #self.type_env[de.base.name]= decl["pseudo_type"]
        else:
            decl["pseudo_type"] = self.visit_node(base_type)[1]
        self.arguments.append(decl)
        return decl


    def newtype(self):
        tt={"intarray":["array",["array", "int"]],
            "doublearray":["array", ["array", "double"]],
            "booleanarray":["array", ["array","bool"]],
            "stringarray":["array",["array","string"]],
            "intlist":["list",["list", "int"]],
            "doublelist":["list", ["list", "double"]],
            "booleanlist":["list", ["list","bool"]],
            "stringlist":["list",["list","string"]],
            "int":["int","int"],
            "double":["float","float"],
            "float":["float","float"],
            "str":["str","str"],
            "bool":["bool","bool"],
            "list":["list","list"],
            "array":["array","array"]}
        return tt
        
        
    def visit_csimplebasetypenode(self, node, location):
        return self.newtype()[node.name][0], self.newtype()[node.name][1]

    def visit_cvardefnode(self, node, base_type, declarators, location):
        x = []
        for de in declarators:
            if not isinstance(de, Nodes.CArrayDeclaratorNode):
                if self.type_env[de.name]:
                    raise PseudoCythonTypeCheckError(
                        "%s is already declared" % de.name)
                decl = {"name": de.name,
                        "type": self.visit_node(base_type)[0], "lineno": location}
                if de.default is None:
                    #self.type_env[de.name] = base_type.name
                    self.type_env[de.name] = self.visit_node(base_type)[1]
                    #decl["pseudo_type"] = decl["type"]
                    decl["pseudo_type"] = self.visit_node(base_type)[1]
                if type(de.default) in (ExprNodes.IntNode,ExprNodes.UnaryMinusNode, ExprNodes.FloatNode, ExprNodes.UnicodeNode, ExprNodes.StringNode, ExprNodes.BoolNode):
                    value_node = self.visit_node(de.default)
                    if isinstance(de.default, ExprNodes.UnaryMinusNode):
                        decl["value"] = str(-float(value_node["value"]["value"]))
                    else: decl["value"] = value_node["value"] 
                    decl["pseudo_type"] = value_node["pseudo_type"]
                    self.type_env[de.name] = decl["pseudo_type"]
                    self._compatible_types(
                        decl['type'], decl["pseudo_type"], "can't change the type of variable %s in %s " % (de.name, self.function_name))

                if type(de.default) in (ExprNodes.ListNode, ExprNodes.TupleNode):
                    arglist = []
                    for arg in de.default.args:
                        arglist.append(self.visit_node(arg))
                    decl["elements"] = arglist
                    if type(de.default) == ExprNodes.ListNode:
                        self.visit_node(de.default)
                        decl["pseudo_type"] = ["list", self.visit_node(arglist[0])[
                            "pseudo_type"]]
                    else:
                        decl["pseudo_type"] = [
                            "tuple"]+[self.visit_node(arg)["pseudo_type"] for arg in arglist]
                    self.type_env[de.name] = decl["pseudo_type"]
                if isinstance(de.default, ExprNodes.DictNode):
                    default = self.visit_node(de.default)
                    decl["pairs"] = default["pairs"]
                    decl["pseudo_type"] = default["pseudo_type"]
                    self.type_env[de.name] = default["pseudo_type"]
                    a = self._compatible_types(
                        base_type.name, decl["pseudo_type"][0], "can't change the type of variable %s in %s " % (de.name, self.function_name))
            else:
                if self.type_env[de.base.name]:
                    raise PseudoCythonTypeCheckError(
                        "%s is already declared" % de.base.name)
                if isinstance(de.dimension, ExprNodes.NameNode) or isinstance(de.dimension, ExprNodes.IntNode):
                    elts = [self.visit_node(de.dimension)]                    
                if de.dimension is None:
                    elts = []
                else:
                    elts = self.visit_node(de.dimension)#[]
                    #for d in self.visit_node(de.dimension.args):
                        #elts.append(d)
                dim = len(elts)
                decl = {"name": de.base.name, "type": "array", "dim": dim, "elts": elts,
                        "pseudo_type": ["array", base_type.name], "lineno": location}
                self.type_env[de.base.name] = decl["pseudo_type"]
            self.declarations.append(decl)
            x.append(decl)
        return {
            "type": "declaration",
            "decl": x
        }

    def visit_continuestatnode(self, node, location):
        return {
            "type": "continuestatnode"
        }

    def visit_breakstatnode(self, node, location):
        return {
            "type": "breakstatnode"
        }

    def visit_forinstatnode(self, node, target, iterator, item, body, else_clause, location):
        sketchup, env = self._translate_iter(target, iterator.sequence)

        """for label, value in env.items():
            print("gg", label, value)
            #if not self.type_env.top[label]:
                #raise self.notdeclared(label, location[0])
            self.type_env.top[label] = value"""
        self.in_for = True
        sketchup['block'] = self.visit_node(body)
        sketchup['type'] = 'for' + sketchup['type'] + '_statement'
        sketchup['pseudo_type'] = 'Void'
        return sketchup

    def _translate_iter(self, target, k):
        if isinstance(k, ExprNodes.SimpleCallNode) and isinstance(k.function, ExprNodes.NameNode):
            if k.function.name == 'enumerate':
                if len(k.args) != 1 or not isinstance(target, ExprNodes.TupleNode) or len(target.args) != 2:
                    raise PseudoCythonTypeCheckError(
                        'enumerate expected one arg not %d and two indices' % len(k.args))
                return self._translate_enumerate(target.args, k.args[0])
            elif k.function.name == 'range':
                if isinstance(target, ExprNodes.NameNode):
                    return self._translate_range([target], k.args)
                elif not isinstance(target, (ExprNodes.NameNode, ExprNodes.TupleNode)) or isinstance(target, ExprNodes.TupleNode) and len(target.elts) != 2:
                    raise PseudoCythonTypeCheckError(
                        'range expected two indices')
                elif not k.args or len(k.args) > 3:
                    raise PseudoCythonTypeCheckError(
                        'range expected 1 to 3 args not %d' % len(k.args))
                return self._translate_range(target.args, k.args)
            elif k.function.name == 'zip':
                if len(k.args) < 2 or not isinstance(target, ExprNodes.TupleNode) or len(k.args) != len(target.args):
                    raise PseudoCythonTypeCheckError(
                        'zip expected 2 or more args and the same number of indices not %d' % len(k.args))
                print("TO DO")
                #return self._translate_zip(target.args, k.args)

        sequence_node = self.visit_node(k)       
        self._confirm_iterable(sequence_node['pseudo_type'])


        if isinstance(target, ExprNodes.TupleNode):
            raise PseudoCythonNotTranslatableError(
                "pseudo doesn't support tuples yet")
        elif not isinstance(target, ExprNodes.NameNode):
            raise PseudoCythonNotTranslatableError(
                "pseudo doesn't support %s as an iterator" % sequence_node['type'])
        target_pseudo_type = self.type_env[target.name]
        #target_pseudo_type = self._element_type(sequence_node['pseudo_type'])
        self.forSequence = True
        return {
            'type': '',
            'sequences': {'type': 'for_sequence', 'sequence': sequence_node},
            'iterators': {
                'type': 'for_iterator',
                'iterator': {
                    'type':       'local',
                    'pseudo_type': target_pseudo_type,
                    'name':        target.name
                }
            }
        }, {target.name: target_pseudo_type}

    def _translate_enumerate(self, targets, sequence):
        sequence_node = self.visit_node(sequence)
        self._confirm_iterable(sequence_node['pseudo_type'])

        if not isinstance(targets[0], ExprNodes.NameNode) or not isinstance(targets[1], ExprNodes.NameNode):
            raise PseudoCythonTypeCheckError(
                'expected a name for an index not %s' % type(targets[0]).__name__)
        if self._general_type(sequence_node['pseudo_type']) == 'dict':
            q = 'items'
            k = 'key'
            v = 'value'
        else:
            q = 'index'
            k = 'index'
            v = 'iterator'
        iterator_type = self._element_type(sequence_node['pseudo_type'])
        return {
            'type': '',
            'sequences': {'type': 'for_sequence_with_' + q, 'sequence': sequence_node},
            'iterators': {'type': 'for_iterator_with_' + q,
                          k: {
                              'type': 'local',
                              'pseudo_type': 'int',
                              'name': targets[0].name
                          },
                          v: {
                              'type': 'local',
                              'pseudo_type': iterator_type,
                              'name': targets[1].name
                          }}
        }, {targets[0].name: 'int', targets[1].name: iterator_type}

    def _confirm_iterable(self, sequence_type):
        sequence_general_type = self._general_type(sequence_type)
        if sequence_general_type not in ITERABLE_TYPES:
            raise PseudoCythonTypeCheckError(
                'expected an iterable type, not %s' % serialize_type(sequence_type))

    def _translate_range(self, targets, range):
        if len(range) == 1:
            start, end, step = {'type': 'int', 'value': 0, 'pseudo_type': 'int'}, self.visit_node(
                range[0]), {'type': 'int', 'value': 1, 'pseudo_type': 'int'}
        elif len(range) == 2:
            start, end, step = self.visit_node(range[0]), self.visit_node(
                range[1]), {'type': 'int', 'value': 1, 'pseudo_type': 'int'}
        else:
            start, end, step = tuple(map(self.visit_node, range[:3]))
        for label, r in [('start', start), ('end', end), ('step', step)]:
            if r['pseudo_type'] != 'int':
                raise PseudoCythonTypeCheckError(
                    'expected int for range %s index' % label)

        if not isinstance(targets[0], ExprNodes.NameNode):
            raise PseudoCythonTypeCheckError(
                'index is not a name %s' % type(targets[0]).__name__)
        return {
            'type': '_range',
            'start': start,
            'end': end,
            'step': step,
            'index': {
                'type': 'local',
                'pseudo_type': 'int',
                'name': targets[0].name
            }
        }, {targets[0].name: 'int'}

    def _element_type(self, sequence_type):
        if isinstance(sequence_type, list):
            if sequence_type[0] == 'dict':
                return sequence_type[2]
            elif sequence_type[0] == 'list':
                return sequence_type[1]
        elif sequence_type == 'str':
            return 'str'

    def visit_sliceindexnode(self, node, start, stop, base, slice, location):
        receiver = self.visit_node(base)
        base = 'sliceindex' if receiver['pseudo_type'] != 'str' else 'substr'
        if stop:
            upper_node = self.visit_node(stop)
            self._confirm_index(upper_node['pseudo_type'], 'int', getattr(
                stop, 'location', location), 'slice index')
        if start:
            lower_node = self.visit_node(start)
            self._confirm_index(lower_node['pseudo_type'], 'int', getattr(
                start, 'location', location), 'slice index')
        if stop and start:
            name = base
            values = [lower_node, upper_node]
        elif stop:
            name = '%s_to' % base
            values = [upper_node]
        elif start:
            name = '%s_from' % base
            values = [lower_node]
        else:
            name = 'slice_'
            values = []
        return {
            'type': base,
            'receiver': receiver,
            'message': name,
            'args': values,
            'pseudo_type': receiver['pseudo_type']
        }

    def visit_returnstatnode(self, node, value, location):
        value_node = self.visit_node(value)
        whiplash = self.type_env.top["functions"][self.function_name]
        if value_node is None:
            raise type_check_error("expected a non-void return type for %s" %
                                   self.function_name, location, self.lines[location[0]], wrong_type='Void')

        elif whiplash[-1] and whiplash[-1] != value_node['pseudo_type']:
            raise type_check_error(
                "expected %s return type for %s" % (serialize_type(whiplash[-1]), self.function_name), location, self.lines[location[0]], wrong_type=value_node['pseudo_type'])
        elif whiplash[-1] is None:
            whiplash[-1] = value_node['pseudo_type']
        s = {
            'type': 'implicit_return',
            'value': value_node,
            'pseudo_type': value_node['pseudo_type']
        }
        self.returnValue.append(s)
        return s

    def visit_ifstatnode(self, node, if_clauses, else_clause, location):
        otherwise = []
        if len(if_clauses) > 1:
            for clause in if_clauses:
                if clause == if_clauses[0]:
                    tests = self.visit_node(clause.condition)
                    blocks = self.visit_node(clause.body)
                else:
                    r = self.visit_node(clause)
                    otherwise.append(r)
        else:
            tests = self.visit_node(if_clauses[0].condition)
            blocks = self.visit_node(if_clauses[0].body)
        if else_clause:
            block = self.visit_node(else_clause)
            r = {
                'type': 'else_statement',
                'block': [block] if isinstance(block, dict) else block,
                'pseudo_type': 'Void'
            }
            otherwise.append(r)
        blocks = [blocks] if isinstance(blocks, dict) else blocks
        R = {
            'type': 'if_statement',
            'test': tests,
            'block': blocks,
            'pseudo_type': 'Void',
            'otherwise': otherwise
        }
        return R

    def visit_ifclausenode(self, node, body, condition, location):
        self.base = self.base+1
        block = self.visit_node(body)
        return {
            'type': 'if_statement' if self.base == 0 else 'elseif_statement',
            'test': self.visit_node(condition),
            'block': [block] if isinstance(block, dict) else block,
            'pseudo_type': 'Void'
        }

    def visit_whilestatnode(self, node, condition, body, else_clause, location):
        test_node = self.visit_node(condition)
        return {
            'type': 'while_statement',
            'test': test_node,
            'block': self.visit_node(body),
            'pseudo_type': 'Void'
        }

    def visit_primarycmpnode(self, node, operand1, operand2, coerced_operand2, cascade, location):
        #print(node.operator, location)
        if node.operator not in PSEUDO_OPS[ExprNodes.PrimaryCmpNode]:
            raise("error")
        else:
            op = node.operator
            right_node = self.visit_node(operand2)
            left_node = self.visit_node(operand1)
        if node.operator not in ["in", "not_in"]:
            self._confirm_comparable(
                op, left_node['pseudo_type'], right_node['pseudo_type'], location)
            result = {
                'type': 'comparison',
                'op':   op,
                'left': left_node,
                'right': right_node,
                'pseudo_type': 'bool'
            }
        else:
            sequence_node = right_node
            element_node = left_node
            result = {
                'type': 'standard_method_call',
                'receiver': sequence_node,
                'message': 'contains?' if op == "in" else "not contains?",
                'args': [element_node],
                'pseudo_type': 'Boolean'
            }
        return result

    def visit_boolbinopnode(self, node, operand1, operand2, location):
        op = node.operator
        right_node = self.visit_node(operand1)
        result = right_node
        left_node, right_node = right_node, self.visit_node(operand2)
        result = {
            'type': 'binary_op',
            'op':   op,
            'left': result,
            'right': right_node,
            'pseudo_type': left_node['pseudo_type']
        }
        return result

    def _confirm_comparable(self, o, l, r, location):
        if o == '==' and l != r or o != '==' and (isinstance(l, list) or isinstance(r, list) or
                                                  l != r or l not in COMPARABLE_TYPES):
            raise type_check_error(
                '%s not comparable with %s' % (
                    serialize_type(l), serialize_type(r)),
                location, self.lines[location[0]],
                suggestions='comparable types in pseudo-cython: %s' % ' '.join(COMPARABLE_TYPES))

    def notdeclared(self, name, line):
        raise PseudoCythonTypeCheckError("variable %s is not declared at line %s\n" % (name, line),
                                         )

    def _compatible_types(self, from_, to, err, silent=False):
        '''if from_[0] == "array":
            from_[0] = "list"'''
        if from_ == "unknown" or to == "unknown":
            return to
        if isinstance(from_, str) or isinstance(from_, EncodedString):
            if not isinstance(to, str) and not isinstance(to, EncodedString):
                if silent:
                    return False
                else:
                    raise PseudoCythonTypeCheckError(
                        err + ' from %s to %s' % (serialize_type(from_), serialize_type(to)))

            elif from_ == to:
                return to

            elif from_ in self._hierarchy:
                if to in self._hierarchy:
                    if to in self._hierarchy[from_][1]:
                        return from_

                    base = to
                    while base:
                        if from_ in self._hierarchy[base][1]:
                            return base
                        base = self._hierarchy[base][0]
                if silent:
                    return False
                else:
                    raise PseudoCythonTypeCheckError(
                        err + ' from %s to %s' % (serialize_type(from_), serialize_type(to)))
            elif from_ == 'int' and to == 'float':
                raise PseudoCythonTypeCheckError(
                    err + ' from %s to %s' % (serialize_type(from_), serialize_type(to)))
            elif silent:
                return False
            else:
                raise PseudoCythonTypeCheckError(
                    err + ' from %s to %s' % (serialize_type(from_), serialize_type(to)))
        else:
            if not isinstance(to, list) or len(from_) != len(to) or from_[0] != to[0]:
                if silent:
                    return False
                else:
                    raise PseudoCythonTypeCheckError(
                        err + ' from %s to %s' % (serialize_type(from_), serialize_type(to)))
            for f, t in zip(from_[1:-1], to[1:-1]):
                self._compatible_types(f, t, err)
            return to

    def _testable(self, test_node):
        t = self._general_type(test_node['pseudo_type'])
        if t != TESTABLE_TYPE:
            if t in TYPES_WITH_LENGTH:
                return {
                    'type': 'standard_method_call',
                    'args': test_node,
                    'function': 'present?',
                    'pseudo_type': 'bool'
                }
            elif t in NUMBER_TYPES:
                return {
                    'type': 'comparison',
                    'pseudo_type': 'bool',
                    'op': '>',
                    'left': test_node,
                    'right': {'type': 'int', 'pseudo_type': 'int', 'value': 0}
                }
            else:
                return test_node

    def assert_translatable(self, node, **pairs):
        for label, (expected, actual) in pairs.items():
            if actual != expected:
                raise PseudoCythonNotTranslatableError(
                    "%s in %s is not a part of pseudo-translatable cython" % (label if label[-1] != '_' else label[:-1], node))

    def _type_check(self, g,message, types):
        if not g:
            raise PseudoCythonTypeCheckError("%s is not defined" % message)

        return self._real_type_check(g, types, '%s#%s' % ("function", message))

    def _real_type_check(self, g, types, name):
        if len(g) - 1 != len(types):
            raise PseudoCythonTypeCheckError("%s expected %d args" % (name, len(g) - 1))

        for j, (a, b) in enumerate(zip(g[0:-1], types)):
            general = self._compatible_types(b, a, "can't convert %s %dth arg" % (name, j))

        return g

    def _confirm_index(self, index_type, expected, location, window):
        if index_type != 'int':
            raise type_check_error(
                'expected Int for %s' % window,
                location, self.lines[location[0]],
                wrong_type=index_type)

    def _general_type(self, t):
        if isinstance(t, list):
            return t[0]
        else:
            return t

# retrieve from pseudo-python
def transform_to_syntax_tree(tree):
    '''Generate a Node class from the tree in dict format    
    '''
    if isinstance(tree, dict) and 'type' in tree:
        return Node(tree['type'], **{k: transform_to_syntax_tree(v) for k, v in tree.items() if k != 'type'})
    elif isinstance(tree, dict):
        return {k: transform_to_syntax_tree(v) for k, v in tree.items()}
    elif isinstance(tree, list):
        return [transform_to_syntax_tree(v) for v in tree]
    else:
        return tree
