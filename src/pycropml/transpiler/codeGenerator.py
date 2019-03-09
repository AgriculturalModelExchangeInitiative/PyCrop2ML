# coding: utf8
from __future__ import absolute_import
from __future__ import print_function
from pycropml.transpiler.nodeVisitor import NodeVisitor
class CodeGenerator(NodeVisitor):
    def __init__(self, add_line_information=False):
        self.result = []        
        self.indent_with = ' '*4
        self.add_line_information = add_line_information
        self.indentation = 0
        self.new_lines = 0
        self.precedence = [0]

    def write(self, x):
        if self.new_lines:
            if self.result:
                self.result.append('\n' * self.new_lines)
            self.result.append(self.indent_with * self.indentation)
            self.new_lines = 0
        self.result.append(x)

    def newline(self, node=None, extra=0):
        self.new_lines = max(self.new_lines, 1 + extra)
        if node is not None and self.add_line_information:
            self.write('# line: %s' % node.lineno)
            self.new_lines = 1

    def body(self, statements):
        self.new_line = True
        self.indentation += 1
        if isinstance(statements, list):
            for stmt in statements:
                self.visit(stmt)
        else: self.visit(statements)
        self.indentation -= 1

    def body_or_else(self, node):
        self.body(node.block)
        if "otherwise" in dir(node):
            self.newline()
            self.write('else')
            self.body(node.otherwise) 
         
    def emit_sequence(self, node, parens=(u"", u"")):
        open_paren, close_paren = parens
        items = node
        self.write(open_paren)
        self.comma_separated_list(items)
        self.write(close_paren)  
    
    def comma_separated_list(self, items):
        if len(items) > 0:
            for item in items[:-1]:
                self.visit(item)
                self.write(u", ")
            self.visit(items[-1])  
    
    def visit_for_sequence(self, node):
        self.visit(node.sequence)
    
    def visit_local(self, node):
        self.write(node.name)

    def visit_int(self, node):
        self.write(node.value)
    
        
    def visit_comparison(self, node):
        self.write('(')
        self.visit_binary_op(node)
        self.write(')')
    
    def visit_ExprStatNode(self, node):
        self.newline(node)
        self.visit(node.expr)
        self.write(";")
        
    binop_precedence = {
        'or': 1,
        'and': 2,
        # unary: 'not': 3, '!': 3,
        'in': 4, 'not_in': 4, 'is': 4, 'is_not': 4, '<': 4, '<=': 4, '>': 4, '>=': 4, '!=': 4, '==': 4,
        '|': 5,
        '^': 6,
        '&': 7,
        '<<': 8, '>>': 8,
        '+': 9, '-': 9,
        '*': 10, '@': 10, '/': 10, '//': 10, '%': 10,
        # unary: '+': 11, '-': 11, '~': 11
        '**': 12,
    }
    
    unop_precedence = {
        'not': 3, '!': 3,
        '+': 11, '-': 11, '~': 11,
        }
    
    def operator_enter(self, new_prec):
        old_prec = self.precedence[-1]
        if old_prec > new_prec:
            self.write(u"(")
        self.precedence.append(new_prec)
    
    def operator_exit(self):
        old_prec, new_prec = self.precedence[-2:]
        if old_prec > new_prec:
            self.write(u")")
        self.precedence.pop()
    
    def visit_array(self, node):
        for n in node.elements:
            self.visit(n)
            if n!= node.elements[-1]:
                self.write(",")
    
    def emit_string(self, node, prefix=u''):
        repr_val = repr(node.value)
        if repr_val[0] in 'ub':
            repr_val = repr_val[1:]
        self.write(u"%s%s" % (prefix, repr_val))  
    
    def visit_binary_op(self, node):
        op = node.op
        prec = self.binop_precedence.get(op, 0)
        self.operator_enter(prec)
        self.visit(node.left)
        self.write(u" %s " % self.binary_op[op].replace('_', ' '))
        self.visit(node.right)
        self.operator_exit()
    
    def visit_unary_op(self, node):
        op = node.operator
        prec = self.unop_precedence[op]
        self.operator_enter(prec)
        self.write(u"%s" % self.unary_op[op])
        self.visit(node.value)
        self.operator_exit()
        
    def safe_double(self, node):
        if rb'"' in node.value:
            if rb"'" in node.value:
                s = '"%s"' % node.value.replace('"', '\\"')
            else:
                s = "'%s'" % node.value
        else:
            s = '"%s"' % node.value
        self.write(s)
    
    def visit_simpleCall(self, node):
        self.visit(node.value)
        self.write(" %s "%node.op)
        self.visit(node.sequence)



