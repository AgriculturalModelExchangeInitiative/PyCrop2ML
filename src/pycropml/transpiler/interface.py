from pycropml.transpiler.pseudo_tree import Node
import copy

class TreeInterface():
    '''
    visits recursively nodes of the tree
    with defined transform_<node_type> methods and transforms in place
    '''
    def __init__(self, tree):
        self.tree=tree
        self.ForSequence = False
        self.nbForSeq=0
        self.dependencies=[]
        self.indexNames=[]

    def transform(self, tree, in_block=False):
        self.nameIndex=[]
        if isinstance(tree, Node):
            if tree.type =="for_sequence":
                self.ForSequence = True
                self.nbForSeq =self.nbForSeq+1 
            if tree.type == "custom_call" and tree.function not in self.dependencies:
                self.dependencies.append(tree.function)
            else:
                tree = self.transform_default(tree)
            return tree
        elif isinstance(tree, list):
            return [self.transform(child) for child in tree]
        else:
            return tree
    
        

    def transform_default(self, tree):
        for field, child in tree.__dict__.items():
            if not field.endswith('type'):
                if isinstance(child, Node):
                    setattr(tree, field, self.transform(child, False))
                elif isinstance(child, list) and field == 'block' or field == 'main':
                    setattr(tree, field, self.transform_block(child))
                elif isinstance(child, list):
                    setattr(tree, field, self.transform(child))
        return tree
  


    def transform_block(self, tree):
        results = []
        for child in tree:
            result = self.transform(child, True)
            if not isinstance(result, list):
                results.append(result)
            else:
                results += result
        return results

class middleware(TreeInterface):
    def __init__(self, tree):
        TreeInterface.__init__(self, tree)
    def api_translate(self):
        transformed = self.transform(self)
        return transformed
    