from pycropml.transpiler.pseudo_tree import Node
import copy

class TreeInterface():
    '''
    Extract specific node
    visits recursively nodes of the tree
    with defined transform_<node_type> methods and transforms in place
    '''
    def __init__(self, tree, alloc=None):
        self.tree=tree
        self.ForSequence = False
        self.nbForSeq=0
        self.dependencies=[]
        self.indexNames=[]
        self.returns=[]
        self.allocated_var = []
        self.functions=[]
        self.alloc = alloc
        self.allocated_var_s = []

    def transform(self, tree,  in_block=False):
        self.nameIndex=[]
        if isinstance(tree, Node):
            if tree.type == "assignment":
                # I want to check if the target name is an allocatable array
                #if tree.target.type == "local" and tree.value.type=="array":
                if tree.target.type == "local" and isinstance(tree.target.pseudo_type, list) and tree.target.pseudo_type[0]=="array":
                    self.allocated_var.append(tree.target.name)
                if tree.target.type == "local" and isinstance(tree.target.pseudo_type, list) and tree.target.pseudo_type[0]=="array" and \
                    tree.value.type == "local" and isinstance(tree.value.pseudo_type, list) and tree.value.pseudo_type[0]=="array":
                    self.allocated_var_s.append(tree.value.name)
                '''if tree.target.type == "tuple":
                    for n in tree.target.elements:
                        if n.type == "local" and isinstance(n.pseudo_type, list) and n.pseudo_type[0]=="array":
                            self.allocated_var.append(n.name)'''
            if tree.type == "declaration":
                for n in tree.decl:
                    if n.type=="array" and "elts" in dir(n) and n.elts and isinstance(n.elts[0], Node) and n.elts[0].type!="int":
                        self.allocated_var.append(n.name)
            if tree.type == "comparison" and tree.op == "is_not":
                self.allocated_var.append(tree.left.name)
            if tree.type=="function_definition":
                self.functions.append(tree)
            if tree.type =="custom_call" and self.alloc and tree.function in self.alloc:
                self.allocated_var.extend(self.alloc[tree.function])
            if tree.type =="for_sequence":
                self.ForSequence = True
                self.nbForSeq =self.nbForSeq+1 
            if tree.type == "custom_call" and tree.function not in self.dependencies:
                self.dependencies.append(tree.function)
            if tree.type=="list" and "list" not in self.dependencies:
                self.dependencies.append("list")
            if tree.type=="function_definition":
                for inp in tree.params:
                    if isinstance(inp.pseudo_type, list):
                        if inp.pseudo_type[0]=="list" and "list" not in self.dependencies:
                            self.dependencies.append("list")                   
            if tree.type=="importfrom":
                self.dependencies.append(tree.name[0])
            
            if tree.type=="implicit_return":
                self.returns.append(tree)
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
    def __init__(self, tree, alloc=None):
        TreeInterface.__init__(self, tree, alloc)
    def api_translate(self):
        transformed = self.transform(self)
        return transformed
    