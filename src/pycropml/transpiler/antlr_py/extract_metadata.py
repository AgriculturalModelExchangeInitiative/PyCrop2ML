
# coding: utf-8

from pycropml.transpiler.pseudo_tree import Node
from pycropml.transpiler.antlr_py.extract_metadata_from_comment import ExtractComments, extract

class MetaExtraction():
    def __init__(self):
        self.parameters = {}
        self.getTree = []

    def getFromComment(self, file, c_st_single, c_st_multi, c_end_multi):
        comments = ExtractComments(file, c_st_single, c_st_multi, c_end_multi)
        model_mdata = extract(comments)
        return model_mdata
    
    def getTypeNode(self, tree, nodetype, change=True):
        """get nodes of type nodetype

        Args:
            tree (Node): a tree in where the nodes are searched
            nodetype (str): the type of the nodes
            change (bool, optional): check if it is the same type of node which is searched. Defaults to True.
        """
        if change:
            self.getTree = []
            change = False
        if isinstance(tree, Node):
            if tree.type == nodetype:
                self.getTree.append(tree)
            for field, child in tree.__dict__.items():
                ztree = getattr(tree, field)
                if isinstance(ztree, Node):
                    self.getTypeNode(ztree, nodetype, False)
                if isinstance(ztree, list):
                    self.translist(ztree, nodetype)
        elif isinstance(tree, list):
            self.translist(tree, nodetype)   
        else:
            return 
                        
    def translist(self, tree, nodetype):
        for ch in tree:
            self.getTypeNode(ch, nodetype, False) 
    

    def getAttNode(self, tree, **attVal):
        """
        get the nodes (as a tree) with a specific value of attribute 

        Args:
            tree (Node): a tree in which the node will be searched
            attValue (dict): the value and the attribute of the node

        Returns:
            List[Node]: a list of nodes 
        """
        nodes = []
        for node in tree:
            check = [getattr(node,attName) == attValue for attName, attValue in attVal.items() if attName in dir(node)]
            if all(check):
                nodes.append(node)
        return nodes
    
    def getmethod(self, tree, nameMethod, func=False, class_type=None):
        """This method return a specific method name. It can be used to get the algorithm

        Args:\n
            - tree (Node): a tree from where the method will be extracted \n
            - nameMethod (str): the name of the method 

        Returns:
            Node: a specific method
        """
        if func:
            self.getTypeNode(tree, "function_definition")
        else:
            self.getTypeNode(tree, "methodDef")
        methNode = self.getTree
        meth = self.getAttNode(methNode,**{"name":nameMethod}) if not class_type else  self.getAttNode(methNode,**{"name":nameMethod, "class_":class_type})
        if meth:
            if len(meth)==1: return meth[0]
            else: return meth
        else: return None

    def externFunction(self, tree, algo, type_=False, rec=None):
        self.getTypeNode(algo, "custom_call")
        custom_call = self.getTree
        res_meth = []
        for c in custom_call :
            if c and c.function!=rec :
                namespace = c.namespace if "namespace" in dir(c) else None
                if (c.function, namespace) not in res_meth:
                    res_meth.append((c.function, namespace))
        
        getmeth = []
        if res_meth:
            for r in res_meth:
                if r[-1] and hasattr(r[-1], 'pseudo_type'):
                    mth = self.getmethod(tree, r[0], type_, r[-1].pseudo_type)
                else:
                     mth = self.getmethod(tree, r[0], type_)
                getmeth.append(mth)
        return getmeth



