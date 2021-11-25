# coding: utf8
from pycropml.transpiler.pseudo_tree import Node
class NodeVisitor(object):
    '''
        Define a method which browse the graph and call a methode constructed from the type
        of each node of the graph
    '''
    def visit(self, node):
        '''

        Parameters
        ----------
        node : TYPE
            DESCRIPTION.

        Raises
        ------
        NotImplementedError
            DESCRIPTION.

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
        if isinstance(node, list):
            for n in node:
                self.visit(n)
        if not isinstance(node, Node):
            return node
        elif hasattr(self, 'visit_%s' % node.type):
            return getattr(self, 'visit_%s' % node.type)(node)
        else:
            raise NotImplementedError("no action for %s" % node.type)
