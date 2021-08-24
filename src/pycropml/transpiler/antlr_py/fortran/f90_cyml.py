from pycropml.transpiler.pseudo_tree import Node
class F90_Cyml_ast():
    
    op = lib.binary_op
    
    def __init__(self, tree, model=None, name=None, var= []):
        self.tree = tree
        self.model = model
        self.name = name
        self.recursive = False
        self.type_env = Env()
        self.var =  var


    def visit(self, node):
        '''
        Parameters
        ----------
        node : TYPE
            DESCRIPTION.

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
        if isinstance(node, list):
            results = []
            for n in node:
                x = self.visit(n)
                if isinstance(x, list):
                    results.extend(x)
                else:
                    results.append(x)
            return results
        elif isinstance(node, Node):
            return getattr(self, 'visit_%s'%(node.type))(node)
        else: 
            return node