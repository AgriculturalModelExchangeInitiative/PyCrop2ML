
import open_fortran_parser
from path import Path
import collections.abc
import pathlib
import re
import textwrap
import typing as t
import itertools
from pycropml.transpiler.pseudo_tree import Node
import logging
import typed_ast
import typed_ast.ast3 as ty
import ast
import xml.etree.ElementTree as ET
import horast
import horast.nodes as horast_nodes

def make_call_from_slice(slice_):
    """Transform code like '0:n:2' into 'slice(0, n, 2)'."""
    assert isinstance(slice_, ast.Slice), type(slice_)
    lower, upper, step = slice_.lower, slice_.upper, slice_.step
    if lower is None and upper is None and step is None:
        args = []
    elif lower is not None and upper is None and step is None:
        args = [lower, ast.NameConstant(None)]
    elif lower is None and upper is not None and step is None:
        args = [ast.NameConstant(None), upper]
    elif lower is not None and upper is not None and step is None:
        args = [lower, upper]
    elif lower is not None and upper is None and step is not None:
        args = [lower, ast.NameConstant(None), step]
    elif lower is not None and upper is not None and step is not None:
        args = [lower, upper, step]
    else:
        raise NotImplementedError('unsupported slice form: "{}"'.format(ast.dump(slice_)))
    return ast.Call(ast.Name('slice', ast.Load()), args, [])

def make_expression_from_slice(slice_):
    """Transform code like '0:n:2' into a valid expression that is as simple as possible."""
    assert isinstance(slice_, (
        ast.Index, ast.Slice, ast.ExtSlice)), type(slice_)
    if isinstance(slice_, ast.Index):
        return slice_.value
    if isinstance(slice_, ast.Slice):
        lower, upper, step = slice_.lower, slice_.upper, slice_.step
        if lower is None and upper is not None and step is None:
            return upper
        return make_call_from_slice(slice_)
    assert isinstance(slice_, ast.ExtSlice)
    elts = [make_expression_from_slice(dim) for dim in slice_.dims]
    return ast.Tuple(elts=elts, ctx=ast.Load())

def make_st_ndarray(data_type,dimensions_or_sizes):
    """Create a typed_ast node equivalent to: st.ndarray[dimensions, data_type, sizes]."""
    if isinstance(dimensions_or_sizes, int):
        dimensions = dimensions_or_sizes
        sizes = None
    else:
        dimensions = len(dimensions_or_sizes)
        sizes = [make_expression_from_slice(size) for size in dimensions_or_sizes]
    return ast.Subscript(
        value=ast.Attribute(
            value=ast.Name(id='st', ctx=ast.Load()),
            attr='ndarray', ctx=ast.Load()),
        slice=ast.Index(value=ast.Tuple(
            elts=[ast.Num(n=dimensions), data_type] + [
                ast.Tuple(elts=sizes, ctx=ast.Load())] if sizes else [],
            ctx=ast.Load())),
        ctx=ast.Load())


def make_numpy_constructor(function, arg, data_type):
    return ast.Call(
        func=ast.Attribute(
            value=ast.Name(id='np', ctx=ast.Load()),
            attr=function, ctx=ast.Load()),
        args=[arg],
        keywords=[ast.keyword(arg='dtype', value=data_type)])

FORTRAN_PYTHON_TYPE_PAIRS = {
    ('logical', None): 'bool',
    ('integer', None): 'int',
    ('real', None): 'float',
    ('character', t.Any): 'str',
    ('integer', 1): 'np.int8',
    ('integer', 2): 'np.int16',
    ('integer', 4): 'np.int32',
    ('integer', 8): 'np.int64',
    ('real', 2): 'np.float16',
    ('real', 4): 'np.float32',
    ('real', 8): 'np.float64'}


FORTRAN_PYTHON_OPERATORS = {
    # binary
    '+': (ast.BinOp, ast.Add),
    '-': (ast.BinOp, ast.Sub),
    '*': (ast.BinOp, ast.Mult),
    # missing: MatMult
    '/': (ast.BinOp, ast.Div),
    '%': (ast.BinOp, ast.Mod),
    '**': (ast.BinOp, ast.Pow),
    '//': (ast.BinOp, ast.Add),  # concatenation operator, only in Fortran
    # LShift
    # RShift
    # BitOr
    # BitXor
    # BitAnd
    # missing: FloorDiv
    '.eq.': (ast.Compare, ast.Eq),
    '==': (ast.Compare, ast.Eq),
    '.ne.': (ast.Compare, ast.NotEq),
    '/=': (ast.Compare, ast.NotEq),
    '.lt.': (ast.Compare, ast.Lt),
    '<': (ast.Compare, ast.Lt),
    '.le.': (ast.Compare, ast.LtE),
    '<=': (ast.Compare, ast.LtE),
    '.gt.': (ast.Compare, ast.Gt),
    '>': (ast.Compare, ast.Gt),
    '.ge.': (ast.Compare, ast.GtE),
    '>=': (ast.Compare, ast.GtE),
    # Is
    # IsNot
    # In
    # NotIn
    '.and.': (ast.BoolOp, ast.And),
    '.or.': (ast.BoolOp, ast.Or),
    # unary
    # '+': (ast.UnaryOp, ast.UAdd),
    # '-': (ast.UnaryOp, ast.USub),
    '.not.': (ast.UnaryOp, ast.Not),
    # Invert: (ast.UnaryOp, ast.Invert)
    }

INTRINSICS_FORTRAN_TO_PYTHON = {
    # Fortran 77
    'abs': 'abs',  # or np.absolute
    'acos': ('numpy', 'arccos'),
    'aimag': None,
    'aint': None,
    'anint': None,
    'asin': ('numpy', 'arcsin'),
    'atan': ('numpy', 'arctan'),
    'atan2': None,
    'char': None,
    'cmplx': None,
    'conjg': ('numpy', 'conj'),
    'cos': ('numpy', 'cos'),
    'cosh': None,
    'dble': 'float',  # incorrect
    'dim': None,
    'dprod': None,
    'exp': None,
    'ichar': None,
    'index': None,
    'int': 'int',
    'len': None,
    'lge': None,
    'lgt': None,
    'lle': None,
    'llt': None,
    'log': None,
    'log10': None,
    'max': ('numpy', 'maximum'),
    'min': ('numpy', 'minimum'),
    'mod': None,
    'nint': None,
    'real': 'float',
    'sign': ('numpy', 'sign'),
    'sin': ('numpy', 'sin'),
    'sinh': ('numpy', 'sinh'),
    'sqrt': ('numpy', 'sqrt'),
    'tan': ('numpy', 'tan'),
    'tanh': ('numpy', 'tanh'),
    # non-standard Fortran 77
    'getenv': ('os', 'environ'),
    # Fortran 90
    # Character string functions
    'achar': None,
    'adjustl': None,
    'adjustr': None,
    'iachar': None,
    'len_trim': None,
    'repeat': None,
    'scan': None,
    'trim': ('str', 'rstrip'),
    'verify': None,
    # Logical function
    'logical': None,
    # Numerical inquiry functions
    'digits': None,
    'epsilon': ('numpy', 'finfo', 'eps'),
    'huge': ('numpy', 'finfo', 'max'),
    'maxexponent': None,
    'minexponent': None,
    'precision': None,
    'radix': None,
    'range': None,
    'tiny': ('numpy', 'finfo', 'tiny'),  # np.finfo(np.double).tiny ,
    # Bit inquiry function
    'bit_size': None,
    # Vector- and matrix-multiplication functions
    'dot_product': ('numpy', 'dot'),
    'matmul': None,
    # Array functions
    'all': None,
    'any': None,
    'count': ('ndarray', 'count'),
    'maxval': None,
    'minval': None,
    'product': None,
    'sum': 'sum',
    # Array location functions
    'maxloc': ('numpy', 'argmax'),
    'minloc':  ('numpy', 'argmin'),
    # Fortran 95
    'cpu_time': None,
    'present': 'is_not_none',  # TODO: TMP
    'set_exponent': None,
    # Fortran 2003
    # Fortran 2008
    }




def separate_args_and_keywords(args_and_keywords):
    args = []
    keywords = []
    for arg in args_and_keywords:
        if isinstance(arg, ast.keyword):
            keywords.append(arg)
        else:
            args.append(arg)
    assert all(not isinstance(_, ast.keyword) for _ in args), args
    return args, keywords
    
_LOG = logging.getLogger(__name__)

_LANG_NAME_UNRECOGNIZED_MSG = 'language name "{}" is not recognized'

class ContinueIteration(StopIteration):
    """Allows for "continue" keyword within a function called from within a loop."""
    pass

class Registry:
    """General-purpose registry of objects."""
    registered = None

    @classmethod
    def register(cls, member, keys) :
        if cls.registered is None:
            cls.registered = {}
        for key in keys: cls.registered.set(key,member)

    @classmethod
    def find(cls, key) :
        if cls.registered is None:
            return None
        return cls.registered.get(key, None)

class Language(Registry):
    """Properties of a programming language."""
    def __init__(self, names, file_extensions, version):
        """Initialize a Language instance.
        :param names: list of names of the language
        :param file_extensions: file extensions, including the dot
        """
        assert isinstance(names, collections.abc.Sequence), type(names)
        assert names
        assert isinstance(file_extensions, collections.abc.Sequence), type(file_extensions)
        assert file_extensions
        if __debug__:
            for name in names:
                assert isinstance(name, str), type(name)
                assert name
            for file_extension in file_extensions:
                assert isinstance(file_extension, str), type(file_extension)
                assert file_extension
                assert file_extension.startswith('.'), file_extension
        assert isinstance(version, tuple) or version is None
        self.names = [name for name in names]
        self.default_name = self.names[0]
        self.file_extensions = [file_extension.lower() for file_extension in file_extensions]
        self.default_file_extension = self.file_extensions[0]
        self.version = version
    @property
    def lowercase_name(self):
        return self.default_name.lower()

    def has_name(self, name: str):
        assert isinstance(name, str), type(name)
        return name in self.names

    def has_extension(self, file_extension: str):
        assert isinstance(file_extension, str), type(file_extension)
        return file_extension.lower() in self.file_extensions

    def has_extension_of(self, path: pathlib.Path):
        assert isinstance(path, pathlib.Path), type(path)
        _, file_extension = path.splitext(path)
        return self.has_extension(file_extension)

    def __repr__(self):
        return '<{} language object>'.format(self.default_name)

def validate_indentation(code: str, path: pathlib.Path = None):
    """Raise error if code isn't consistently indented (either only with spaces, or only with tabs).
    Path is optional and used only for diagnostic purposes (i.e. if error happens).
    """
    if not isinstance(code, str):
        raise TypeError('code must be string but {} given'.format(type(code)))
    assert path is None or isinstance(path, pathlib.Path), type(path)

    lines = code.splitlines(keepends=True)
    whitespace = r'[ \t]*'
    mixed_indent = r'( {0}\t{0})|(\t{0} {0})'.format(whitespace)
    indent_by_spaces = r'[ ]+'
    indent_by_tabs = r'[\t]+'
    indented_with_spaces = None  # type: t.Optional[bool]
    for i, line in enumerate(lines):
        # check if indentation is not mixed
        if re.match(mixed_indent, line) is not None:
            raise ValueError('{}:{} mixed indentation found in {}'.format(
                '<string>' if path is None else path, i, repr(line)))

        # check if indentation type is consistent
        if indented_with_spaces is None:
            if re.match(indent_by_spaces, line) is not None:
                indented_with_spaces = True
            elif re.match(indent_by_tabs, line) is not None:
                indented_with_spaces = False
        elif indented_with_spaces:
            if re.match(indent_by_tabs, line) is not None:
                raise ValueError(
                    '{}:{} after space indent in previous lines, tab indent found in {}'
                    .format('<string>' if path is None else path, i, repr(line)))
        else:
            if re.match(indent_by_spaces, line) is not None:
                raise ValueError(
                    '{}:{} after tab indent in previous lines, space indent found in {}'
                    .format('<string>' if path is None else path, i, repr(line)))


class Parser(Registry):

    """Extract abstract representation of syntax from the source code."""

    def __init__(self, default_scopes: t.Sequence[t.Tuple[int, t.Optional[int]]] = None):
        """Initialize new Parser instance.
        Default scopes, if provided, limit parsing to the given line sections unless the default
        is overriden.
        """
        if default_scopes is None:
            default_scopes = [(0, None)]
        self.default_scopes = default_scopes

    def parse(self, code: str, path: pathlib.Path = None,
              scopes: t.Sequence[t.Tuple[int, t.Optional[int]]] = None, dedent: bool = True):
        """Parse given code into a language-specific AST.
        If path is provided, use it to guide the parser if necessary, as well as for diagnostics.
        """
        assert isinstance(code, str), type(code)
        assert path is None or isinstance(path, pathlib.Path), type(path)
        assert scopes is None or isinstance(scopes, collections.abc.Sequence), type(scopes)

        if scopes is None:
            scopes = self.default_scopes
        parsed_scopes = []
        for begin, end in scopes:
            assert isinstance(begin, int), type(begin)
            assert end is None or isinstance(end, int), type(end)
            if begin == 0 and end is None:
                code_scope = code
            else:
                lines = code.splitlines(keepends=True)
                if end is None:
                    end = len(lines)
                code_scope = ''.join(lines[begin:end])
            validate_indentation(code_scope, path)
            if dedent:
                code_scope = textwrap.dedent(code_scope)
            parsed_scope = self._parse_scope(code_scope, path)
            parsed_scopes.append(parsed_scope)
        if len(scopes) == 1:
            return parsed_scopes[0]
        return self._join_scopes(parsed_scopes)

    def _parse_scope(self, code: str, path: pathlib.Path = None):
        raise NotImplementedError('{} is abstract'.format(type(self).__name__))

    def _join_scopes(self, parsed_scopes):
        raise NotImplementedError('{} cannot join multiple parsed scopes'
                                  .format(type(self).__name__))

import pathlib
import xml.etree.ElementTree as ET
class FortranParser(Parser):
    
    def _parse_scope(self, code: str, path: pathlib.Path = None) -> ET.Element:
        assert path is not None, path
        return open_fortran_parser.parse(path, verbosity=100, raise_on_error=True)

class XmlAST():
    def __init__(self):
        self._import_statements = dict()
        self._transforms = [f for f in dir(self) if f.startswith('_') and not f.startswith('__')]
    
    def get_one(self, node, xpath):
        found = node.find(xpath)
        if found is None:
            raise SyntaxError('no "{}" found in "{}":\n{}'
                              .format(xpath, node.tag, ET.tostring(node).decode().rstrip()))
        return found
    
    def getAll(self, node, xpath, result=True):
        found = node.findall(xpath)
        if result and not found:
            raise SyntaxError('no "{}" found in "{}":\n{}'
                              .format(xpath, node.tag, ET.tostring(node).decode().rstrip()))
        return found
    
    def generalize(self, syntax):
        return self.transform_one(syntax)
    
    def transform_one(self, node, warn=False, ignored = None, parent = None):
        assert isinstance(node, ET.Element), type(node)
        transform_name = '_{}'.format(node.tag.replace('-', '_'))
        if transform_name not in self._transforms:
            if ignored and node.tag in ignored:
                raise ContinueIteration()
            if warn:
                if parent is None:
                    _LOG.warning('no transformer available for node "%s"', node.tag)
                else:
                    _LOG.warning('no transformer available for node "%s", a subnode of "%s"',
                                 node.tag, parent.tag)
                _LOG.debug('%s', ET.tostring(node).decode().rstrip())
                raise ContinueIteration()
            if parent is None:
                raise NotImplementedError('no transformer available for node "{}":\n{}'
                                          .format(node.tag, ET.tostring(node).decode().rstrip()))
            else:
                raise NotImplementedError(
                    'no transformer available for node "{}", a subnode of "{}":\n{}'
                    .format(node.tag, parent.tag, ET.tostring(node).decode().rstrip()))
        if ignored and node.tag in ignored:
            _LOG.info('ignoring existing transformer for %s', node.tag)
            raise ContinueIteration()
        _transform = getattr(self, transform_name)
        transformed = _transform(node)
        return transformed

    def transform_all(self, nodes, warn=False, skip_empty=False, ignored=False, parent = None):
        assert isinstance(nodes, (ET.Element, collections.abc.Iterable)), type(nodes)
        transformed = []
        for node in nodes:
            try:                
                assert isinstance(node, ET.Element), type(node)
                if skip_empty and not node.attrib and len(node) == 0:
                    continue 
                transformed.append(self.transform_one(node, warn, ignored, parent))
            except ContinueIteration:
                continue
        return transformed

    
    def transform_all_subnodes(self, node, warn= False, skip_empty= False, ignored = None):
        """Transform all subnodes of a given node."""
        assert isinstance(node, ET.Element), type(node)
        return self.transform_all(node, warn, skip_empty, ignored, node)


    @property
    def import_statements(self):
        return list(itertools.chain(*[statements
                                      for _, statements in self._import_statements.items()]))

    def ensure_import(self, canonical_name: str, alias: t.Optional[str] = None):
        if (canonical_name, alias) not in self._import_statements:
            if canonical_name in ('mpif.h', '?'):  # TODO: other ways to include MPI?
                self.ensure_mpi(canonical_name, alias)
            else:
                self._import_statements[canonical_name, alias] = {"type":"Import", 
                "module":canonical_name, "asname":alias}                                    

    def ensure_mpi(self, canonical_name, alias):
        # if ('mpi4py', None) not in self._import_statements:
        self._import_statements[canonical_name, alias] = {"type" : "importfrom",  "namespace":'mpi4py', "name":'MPI', "asname":None}

    def no_transform(self, node):
        raise NotImplementedError(
            'not implemented handling of:\n{}'.format(ET.tostring(node).decode().rstrip()))



class XmlASTFortran(XmlAST):

    """Transform Fortran AST in XML format into typed CyML AST.

    The Fortran AST in XML format is provided by XML output generator for Open Fortran Parser.

    """
    def __init__(self, split_declarations=True):
        super().__init__()
        self._split_declarations = split_declarations
        self._now_parsing_file = False

    def _file(self, node):
        if not self._now_parsing_file:
            self._now_parsing_file = True
            body = self.transform_all_subnodes(node, ignored={'start-of-file', 'end-of-file'})
            self._now_parsing_file = False
            body = [self._import_statements] + body
        else:
            return {"type": 'ExprStatNode', "expr": {"type" : 'custom_call',"function" : "print",
                "args":'file',"path": node.attrib['path']}}
        return {"type":"top_level", "body":body}
    
    def _module(self, node):
        body = self.transform_all_subnodes(self.get_one(node, './body'), ignored={'statement','module-subprogram'})
        members_node = node.find('./members')
        conditional = body
        if members_node is None:
            return conditional
        members = self.transform_all_subnodes(members_node, ignored ={'module-subprogram', 'module-subprogram-part',"attr-spec" })
        if not members:
            members = []
        clsdef = {"type":node.attrib['name'],"body":members, "decorator_list":[]}
        return {"type" : "start", "cond" : conditional, "defi" : clsdef}

    def _specification(self, node: ET.Element):
        print("node", node)
        declarations = self.transform_all_subnodes(node, skip_empty=True, ignored={
            'declaration-construct', 'specification-part',"attr-spec" })
        print('de', declarations)
        return {"type":'decl', "args":declarations}

    def _declaration(self, node) :
        declaration_type = node.attrib.get('type', None)
        if declaration_type is None:
            return
        elif declaration_type == 'implicit':
            return self._declaration_implicit(node)
        elif declaration_type =='variable':
            return {"type":"declaration", "decl":self._declaration_variable(node)}
        elif declaration_type == 'parameter':
            return self._declaration_parameter(node)

        details = self.transform_all_subnodes(node, ignored={'attr-spec'})
        
        return details if details else []
    
    def _declaration_variable(self, node: ET.Element):
        """Reorganize data from multi-variable declaration into sequence of annotated assignments."""
        # variable names
        variables_and_values = self.transform_all_subnodes(
            self.get_one(node, './variables'), skip_empty=True,
            ignored={'entity-decl-list__begin', 'entity-decl-list','attr-spec' })
        if not variables_and_values:
            _LOG.error('%s', ET.tostring(node).decode().rstrip())
            raise SyntaxError('at least one variable expected in variables list')
        variables = [var for var, _ in variables_and_values]
        # base type of variables
        base_type = self.transform_one(self.get_one(node, './type'))

        # dimensionality information (only for array types)
        dimensions_node = node.find('./dimensions')
        variable_dimensions = [getattr(var, 'fortran_metadata', {}).get('dimensions', None)
                               for var in variables]
        has_variable_dimensions = any([_ is not None for _ in variable_dimensions])
        if has_variable_dimensions and not self._split_declarations:
            raise NotImplementedError('inline dimensions not implemented yet')
        if dimensions_node is not None and has_variable_dimensions:
            raise SyntaxError(
                'declaration dimension data as well as per-variable dimension data present')
        if dimensions_node is not None:
            dimensions = self.transform_one(dimensions_node)
            assert len(dimensions) >= 1
            self.ensure_import('static_typing', 'st')
            annotation = make_st_ndarray(base_type, dimensions)
            annotations = [annotation for _ in variables]
        elif has_variable_dimensions:
            self.ensure_import('static_typing', 'st')
            annotations = [base_type if _ is None else make_st_ndarray(base_type, _)
                           for _ in variable_dimensions]
        else:
            annotations = [base_type for _ in variables]

        # initial values
        if dimensions_node is not None:
            values = [None if val is None else make_numpy_constructor('array', val, base_type)
                      for _, val in variables_and_values]
        elif has_variable_dimensions:
            assert len(variables_and_values) == len(variable_dimensions)
            values = [None if val is None
                      else (val if dim is None else make_numpy_constructor('array', val, base_type))
                      for (_, val), dim in zip(variables_and_values, variable_dimensions)]
        else:
            values = [val for _, val in variables_and_values]

        metadata = {'is_declaration': True}
        intent_node = node.find('./intent')
        if intent_node is not None:
            metadata['intent'] = intent_node.attrib['type']

        attributes = ('allocatable', 'asynchronous', 'external', 'intrinsic', 'optional',
                      'parameter', 'pointer', 'protected', 'save', 'target', 'value', 'volatile')
        for attribute in attributes:
            if node.find('./attribute-{}'.format(attribute)) is not None:
                metadata['is_{}'.format(attribute)] = True

        if metadata:
            metadata_node = horast_nodes.Comment(
                value=ast.Str(' Fortran metadata: {}'.format(repr(metadata))), eol=False)

        _handled = {'variables', 'type', 'dimensions', 'intent'}
        extra_results = self.transform_all_subnodes(node, ignored={
            'type-declaration-stmt'} | _handled | {'attribute-{}'.format(_) for _ in attributes})
        if extra_results:
            _LOG.warning('ignoring additional information in the declaration:\n%s', extra_results)

        if not self._split_declarations:
            raise NotImplementedError()
        assignments = [{"name":var, "type":ann, "value":val}
                       for var, ann, val in zip(variables, annotations, values)]
        if metadata:
            new_assignments = []
            for assignment in assignments:
                assignment.update({"metadata":metadata})
                new_assignments.append(assignment)
                new_assignments.append(metadata_node)
            assignments = new_assignments

        return assignments
    
    def _attr_spec(self, node):
        pass

    def _declaration_parameter(self, node):
        return 
    
    def _comment(self, node: ET.Element) :
        comment = node.attrib['text']
        if not comment or comment[0] not in ('!', 'c', 'C'):
            raise SyntaxError('comment token {} has unexpected prefix'.format(repr(comment)))
        comment = comment[1:]
        return [comment]
    
    def _statement(self, node):
        details = self.transform_all_subnodes(node, ignored={
            'action-stmt', 'executable-construct', 'execution-part-construct',
            'do-term-action-stmt',  # until do loop parsing implementation is changed
            'execution-part'})
        return [
            detail if isinstance(detail, (
                ast.Return, ast.Delete, ast.Assign, ast.AugAssign,
                ast.AnnAssign, ast.For, ast.While,
                ast.If, ast.With,
                ast.Assert,
                ast.Expr, ast.Pass, ast.Break,
                ast.Continue))
            else detail
            for detail in details]           

    def _declaration_implicit(self, node):
        subtype = node.attrib['subtype'].lower()
        if subtype == 'none':
            annotation = {"type":"implicit", "value":None}
        implicit = annotation
        #implicit.fortran_metadata = {'is_declaration': True}
        return implicit

    def _assignment(self, node):
        target = self.transform_all_subnodes(self.get_one(node, './target'))
        value = self.transform_all_subnodes(self.get_one(node, './value'))
        if len(target) != 1:
            raise SyntaxError(
                'exactly 1 target expected but {} given {} in:\n{}'
                .format(len(target), target, ET.tostring(node).decode().rstrip()))
        target = target[0]
        #assert isinstance(target, ast.AST)
        if len(value) != 1:
            raise SyntaxError(
                'exactly 1 value expected but {} given {} in:\n{}'
                .format(len(value), value, ET.tostring(node).decode().rstrip()))
        value = value[0]
        #assert isinstance(value, ast.AST)
        return {"type": "assignment", "target":target, "value":value}


    _intrinsics_converters = {}



    def _subscripts(self, node: ET.Element, postprocess: bool = True):
        subscripts = self.transform_all_subnodes(node, ignored={
            'section-subscript-list__begin', 'section-subscript-list'})
        assert len(subscripts) == int(node.attrib['count'])
        if not postprocess:
            return subscripts
        if any(isinstance(_, ast.Slice) for _ in subscripts):
            if len(subscripts) == 1:
                return subscripts[0]
            return ast.ExtSlice(dims=[
                (_ if isinstance(_, (ast.Index, ast.Slice))
                 else ast.Index(value=_)) for _ in subscripts])
        assert all(not isinstance(_, (ast.Index, ast.Slice, ast.ExtSlice))
                   for _ in subscripts), subscripts
        if len(subscripts) == 1:
            return ast.Index(value=subscripts[0])
        return ast.Index(value=ast.Tuple(elts=subscripts, ctx=ast.Load()))

    def _subscript(self, node: ET.Element):
        subscripts = self.transform_all_subnodes(node, ignored={'section-subscript'})
        if not subscripts:
            assert node.attrib['type'] == 'empty'
            return ast.Slice(lower=None, upper=None, step=None)
        if len(subscripts) != 1:
            self.no_transform(node)
        assert node.attrib['type'] in ('simple', 'range')
        return subscripts[0]

    def _variable(self, node: ET.Element):
        value_node = node.find('./initial-value')
        value = None
        if value_node is not None:
            values = self.transform_all_subnodes(value_node, ignored={'initialization'})
            assert len(values) == 1, values
            value = values[0]
        variable = node.attrib['name']
        metadata = {}
        dimensions_node = node.find('./dimensions')
        if dimensions_node is not None:
            metadata['dimensions'] = self.transform_one(dimensions_node)
        if metadata:
            variable.fortran_metadata = metadata
        return variable, value


    def _name(self, node: ET.Element):
        name_str = node.attrib['id']
        name = name_str
        name_str = name_str.lower()
        name_type = node.attrib['type'] if 'type' in node.attrib else None
        is_intrinsic = name_str in self._intrinsics_converters

        subscripts_node = node.find('./subscripts')
        try:
            args = self._subscripts(subscripts_node, postprocess=False) if subscripts_node else []
            args, keywords = separate_args_and_keywords(args)
            call = ast.Call(func=name, args=args, keywords=keywords)
            if is_intrinsic:
                if subscripts_node is None:
                    _LOG.warning('found intrinsic name "%s" without any subscripts', name_str)
                else:
                    name_type = 'function'
                    call = self._intrinsics_converters[name_str](self, call)
        except SyntaxError:
            _LOG.info('transforming name to call failed as below (continuing despite that)',
                      exc_info=True)

        slice_ = self._subscripts(subscripts_node) if subscripts_node else None
        subscript = ast.Subscript(value=name, slice=slice_, ctx=ast.Load())

        if name_type in ('procedure', 'function'):
            return call
        elif not subscripts_node:
            return {"type":"local", "name":name, "pseudo_type":name_type}
        elif name_type in ('variable',):
            return {"type":"local", "name":subscript, "pseudo_type":name_type}
        elif not slice_:
            return call
        elif name_type in ('ambiguous',):
            return subscript
        elif name_type is not None:
            raise NotImplementedError('unrecognized name type "{}" in:\n{}'
                                      .format(name_type, ET.tostring(node).decode().rstrip()))
        elif name_type is None:
            raise NotImplementedError('no name type in:\n{}'
                                      .format(ET.tostring(node).decode().rstrip()))
        raise NotImplementedError('not implemented handling of:\n{}'
                                  .format(ET.tostring(node).decode().rstrip()))

    def _value(self, node: ET.Element):
        values = self.transform_all_subnodes(node)
        assert len(values) == 1, values
        return values[0]

    def _operation(self, node: ET.Element):
        if node.attrib['type'] == 'multiary':
            return self._operation_multiary(node)
        if node.attrib['type'] == 'unary':
            return self._operation_unary(node)
        raise NotImplementedError('not implemented handling of:\n{}'
                                  .format(ET.tostring(node).decode().rstrip()))

    def _operation_multiary(
            self, node: ET.Element):
        operators_and_operands = self.transform_all_subnodes(node, skip_empty=True, ignored={
            'add-operand', 'mult-operand', 'power-operand', 'and-operand', 'or-operand',
            'parenthesized_expr', 'primary', 'level-2-expr', 'level-3-expr'})
        assert isinstance(operators_and_operands, list), operators_and_operands
        assert len(operators_and_operands) % 2 == 1, operators_and_operands

        operation_type, _ = operators_and_operands[1]
        if operation_type is ast.BinOp:
            return self._operation_multiary_arithmetic(operators_and_operands)
        if operation_type is ast.BoolOp:
            return self._operation_multiary_boolean(operators_and_operands)
        if operation_type is ast.Compare:
            return self._operation_multiary_comparison(operators_and_operands)
        raise NotImplementedError('not implemented handling of:\n{}'
                                  .format(ET.tostring(node).decode().rstrip()))

    def _operation_multiary_arithmetic(
            self, operators_and_operands: t.Sequence[t.Union[ast.AST, t.Tuple[
                t.Type[ast.BinOp], t.Type[ast.AST]]]]):
        operators_and_operands = list(reversed(operators_and_operands))
        operators_and_operands += [(None, None)]

        root_operation = None  # type: ast.BinOp
        operation = None  # type: ast.BinOp
        root_operation_type = None
        root_operator_type = None
        zippped = zip(operators_and_operands[::2], operators_and_operands[1::2])
        for operand, (operation_type, operator_type) in zippped:
            if root_operation is None:
                root_operation_type = operation_type
                root_operator_type = operator_type
                if root_operation_type is not ast.BinOp:
                    raise NotImplementedError('root operation initialisation')
                root_operation = ast.BinOp(
                    left=None, op=root_operator_type(), right=operand)
                operation = root_operation
                continue
            if operation_type is not None:
                assert operation_type is root_operation_type, (operation_type, root_operation_type)
                operation.left = ast.BinOp(left=None, op=operator_type(), right=operand)
                operation = operation.left
            else:
                operation.left = operand

        return root_operation

    def _operation_multiary_boolean(self, operators_and_operands):
        operators_and_operands += [(None, None)]
        root_operation = None
        root_operation_type = None
        root_operator_type = None
        zippped = zip(operators_and_operands[::2], operators_and_operands[1::2])
        for operand, (operation_type, operator_type) in zippped:
            if root_operation is None:
                root_operation_type = operation_type
                root_operator_type = operator_type
                if root_operation_type is not ast.BoolOp:
                    raise NotImplementedError('root operation initialisation')
                root_operation = ast.BoolOp(
                    op=root_operator_type(), values=[operand])
                continue
            if operation_type is not None:
                assert operation_type is root_operation_type, (operation_type, root_operation_type)
                assert operator_type is root_operator_type, (operator_type, root_operator_type)
            #root_operation.values.append(operand)

        return root_operation

    def _literal(self, node):
        literal_type = node.attrib['type']
        if literal_type == 'bool':
            return ast.NameConstant(value={
                'false': False,
                'true': True}[node.attrib['value']])
        if literal_type == 'int':
            return ast.Num(n=int(node.attrib['value']))
        if literal_type == 'real':
            value = node.attrib['value']
            if 'D' in value:
                value = value.replace('D', 'E', 1)
            return ast.Num(n=float(value))
        if literal_type == 'char':
            assert len(node.attrib['value']) >= 2
            begin = node.attrib['value'][0]
            end = node.attrib['value'][-1]
            assert begin == end
            return ast.Str(node.attrib['value'][1:-1], '')
        _LOG.warning('%s', ET.tostring(node).decode().rstrip())
        raise NotImplementedError('literal type "{}" not supported'.format(literal_type))



    def _operation_multiary_comparison(
            self, operators_and_operands: t.Sequence[t.Union[ast.AST, t.Tuple[
                t.Type[ast.Compare], t.Type[ast.AST]]]]) -> ast.Compare:
        assert len(operators_and_operands) == 3, operators_and_operands
        left_operand, (operation_type, operator_type), right_operand = operators_and_operands
        assert operation_type is ast.Compare
        assert not isinstance(right_operand, list), right_operand
        return ast.Compare(
            left=left_operand, ops=[operator_type()], comparators=[right_operand])

    def _operation_unary(self, node: ET.Element):
        operators_and_operands = self.transform_all_subnodes(node, skip_empty=True, ignored={
            'signed-operand', 'and-operand', 'parenthesized_expr', 'primary'})
        assert isinstance(operators_and_operands, list), operators_and_operands
        assert len(operators_and_operands) == 2, operators_and_operands
        operation_type, operator_type = operators_and_operands[0]
        if operation_type is ast.BinOp:
            operation_type, operator_type = {
                (ast.BinOp, ast.Add): (ast.UnaryOp, ast.UAdd),
                (ast.BinOp, ast.Sub): (ast.UnaryOp, ast.USub)
                }[operation_type, operator_type]
        operand = operators_and_operands[1]
        return operation_type(op=operator_type(), operand=operand)

    def _operand(self, node: ET.Element):
        operand = self.transform_all_subnodes(node, ignored={
            'add-operand__add-op', 'mult-operand__mult-op', 'and-operand__not-op'})
        if len(operand) != 1:
            _LOG.warning('%s', ET.tostring(node).decode().rstrip())
            # _LOG.error("%s", operand)
            #_LOG.error([typed_astunparse.unparse(_).rstrip() for _ in operand])
            raise SyntaxError(
                'expected exactly one operand but got {} in:\n{}'
                .format(len(operand), ET.tostring(node).decode().rstrip()))
        return operand[0]

    def _operator(
            self, node: ET.Element):
        return FORTRAN_PYTHON_OPERATORS[node.attrib['operator'].lower()]

    def _subroutine(self, node):
        header_node = self.get_one(node, './header')
        arguments_node = header_node.find('./arguments')
        if arguments_node is None:
            arguments = {"type":"function_definition", "args":[]}
        else:
            arguments = self.transform_one(arguments_node)
        body = self.transform_all_subnodes(self.get_one(node, './body'))
        function_def = {"type":"function_definition",  "name":node.attrib['name'], "params":arguments, "body":body, "decorator_list":[],
            "return_type":[], "pseudo_type" : []}
        members_node = node.find('./members')
        if members_node is not None:
            members = self.transform_all_subnodes(members_node, ignored={'module-subprogram',
                'internal-subprogram', 'internal-subprogram-part'})
            assert members
            function_def.fortran_metadata = {'contains': members}
        return function_def
    
    def _arguments(self, node):
        return Node(type = "name", name=self.transform_all_subnodes(node, ignored={
                'dummy-arg-list__begin', 'dummy-arg-list',
                'generic-name-list__begin', 'generic-name-list'}))

    def _argument(self, node):
        if 'name' not in node.attrib:
            raise SyntaxError(
                '"name" attribute not present in:\n{}'.format(ET.tostring(node).decode().rstrip()))
        values = self.transform_all_subnodes(node, skip_empty=False, ignored={
            'actual-arg', 'actual-arg-spec', 'dummy-arg'})
        if values:
            assert len(values) == 1
            _LOG.warning('generating invalid Python AST: keyword() in arguments()')
            return {"type": type(values[0]), "arg":node.attrib['name'], "value":values[0]}
        return node.attrib['name']

    def _type(self, node):
        name = node.attrib['name'].lower()
        length = self.transform_one(self.get_one(node, './length')) \
            if node.attrib['hasLength'] == 'true' else None
        kind = self.transform_one(self.get_one(node, './kind')) \
            if node.attrib['hasKind'] == 'true' else None
        if length is not None and kind is not None:
            raise SyntaxError(
                'only one of "length" and "kind" can be provided, but both were given'
                ' ("{}" and "{}" respectively) in:\n{}'
                .format(length, kind, ET.tostring(node).decode().rstrip()))
        if name == 'character':
            if length is not None:
                if isinstance(length, ast.Num):
                    length = length.n
                _LOG.info(
                    'ignoring string length "%i" in:\n%s',
                    length, ET.tostring(node).decode().rstrip())
            return ast.parse(FORTRAN_PYTHON_TYPE_PAIRS[name, t.Any], mode='eval').body
        elif length is not None:
            self.ensure_import('numpy', 'np')
            return ast.parse(FORTRAN_PYTHON_TYPE_PAIRS[name, length], mode='eval').body
        elif kind is not None:
            self.ensure_import('numpy', 'np')
            if isinstance(kind, ast.Num):
                kind = kind.n
            if not isinstance(kind, int):
                python_type = ast.parse(
                    FORTRAN_PYTHON_TYPE_PAIRS[name, None], mode='eval').body
                self.ensure_import('static_typing', 'st')
                static_type = ast.Attribute(
                    value='st',
                    attr=python_type, ctx=ast.Load())
                return ast.Subscript(
                    value=static_type, slice=ast.Index(value=kind), ctx=ast.Load())
            return ast.parse(FORTRAN_PYTHON_TYPE_PAIRS[name, kind], mode='eval').body
        else:
            if node.attrib['type'] == 'derived':
                return ast.Call(func=ast.Name(id='type', ctx=ast.Load()),
                                       args=[ast.Name(id=name, ctx=ast.Load())],
                                       keywords=[])
            assert node.attrib['type'] == 'intrinsic'
            return FORTRAN_PYTHON_TYPE_PAIRS[name, None]
        raise NotImplementedError(
            'not implemented handling of:\n{}'.format(ET.tostring(node).decode().rstrip()))






from pathlib import Path
path = Path("C:/Users/midingoy/Documents/THESE/pycropml_pheno/test/Tutorial/test.f90")
path2 = Path("C:/Users/midingoy/Documents/THESE/pycropml_pheno/test/Tutorial/energybalance_pkg/src/f90/canopytemperature.f90")
with open(path2, "r") as fi:
    code = fi.read()
res = FortranParser().parse(code, path2)
path3 = Path("C:/Users/midingoy/Documents/THESE/pycropml_pheno/test/Tutorial/xmlfortran.xml")

with open(path3, "w") as p:
    p.write(ET.tostring(res).decode().rstrip())

xmlast = XmlASTFortran().transform_all_subnodes(res)