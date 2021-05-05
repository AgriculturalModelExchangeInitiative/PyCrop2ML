import copy
class ParseTreeNode():

    label = None
    ntype = None;
    parent =None
    tree=None
    iid=None
    sidx = 0
    eidx = 0
    id = 0
    children = [];
    cnt = 0;   
    
    def __init__(self, tree, parent=None,nt=None, label=None, sidx=None,  eidx=None):
        self.tree = tree;
        self.id = ParseTreeNode.cnt+1;
        self.children = [];
        self.ntype = nt;
        self.label = label;
        self.parent = parent;
        self.sidx = sidx;
        self.eidx = eidx

    @classmethod
    def ParseTreeNode(self, tree, nod):
        self.id = nod.id;
        self.ntype = nod.ntype;
        self.label = nod.label;
        self.eidx = nod.eidx;
        self.sidx = nod.sidx;
        for c in nod.children: 
            cnod = ParseTreeNode(tree, c);
            cnod.parent = self;
            self.tree.nodes.add(cnod);
            self.children.add(cnod);
    
    def getChild(self, i):
        if i < 0 or i > len(self.children):
            print("Index must be greater than or equal to zero and less than the children size");
        return self.children[i]
    
    def getLastChild(self):
        if len(self.children)!=0 :
            return self.children[len(self.children) - 1];
        return None;    
  
    def getFirstChild(self ):
        if len(self.children)!=0:
            return self.children[0]
        return None;

    def setParent(self,par):
        self.parent = par

    def hasParent(self) :
        return self.parent != None;

    def getParent(self) :
        return self.parent

    def hasChildren(self) :
        return len(self.children)!=0

    def getChildren(self) :
        return self.children

    def addChild(self, n) :
        self.children.add(n);

    def delChild(self, n) :
        self.children.remove(n);

    def  replaceChild(self, oldNode,  newNode) :
        if (self.children.contains(oldNode)) :
            self.children[self.children.index(oldNode)] = newNode;
            newNode.parent = self;

    def getId(self):
        return self.id


    def getRule(self) :
        return self.ntype

    def getEscapedLabel(self) :
        import re
        return re.escape(self.label);

    def getSidx(self) :
        return self.sidx;

    def getEidx(self) :
        return self.eidx;

    def isTerminal(self) :
        return self.isLeaf() and len(self.ntype)==0

    def getLabel(self) :
        return self.label;

    def hashCode(self) :
        return id;

    def equals(self, o) :
        if not isinstance(o, ParseTreeNode):
            return False
        n = o;
        return n.id == id and n.ntype == self.ntype and  n.label==self.label and self.children==n.children

    def toString(self) :
        return self.id + " " + self.ntype + " " + self.label;

    def isLeaf(self) :
        return len(self.children)==0


