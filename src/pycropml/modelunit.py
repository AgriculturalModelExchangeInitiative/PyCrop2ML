""" Model Description and Model Unit.

"""
import six
class ModelDefinition(object):
    """
    """
    def __init__(self, kwds):
        self._attributes = kwds
        for k, v in six.iteritems(kwds):
            self.__setattr__(k,v)

    def __repr__(self):
        return str(self._attributes)


class ModelUnit(ModelDefinition):
    """ 
    Formal description of a Model Unit. 
    
    """

    def __init__(self, kwds):
        ModelDefinition.__init__(self, kwds)
        self.description = None
        self.inputs = []
        self.outputs = []
        self.function=[]
        self.initialization=[]
        self.algorithms = []
        self.parametersets = {}
        self.testsets = []
        self.path=None

    def add_description(self, description):
        """ TODO """
        self.description = description
    
    @property
    def states(self):
        st=[]
        stname = []
        for n in self.inputs:
            if "variablecategory" in dir(n) and n.variablecategory=="state":
                st.append(n)
                stname.append(n.name)
        for m in self.outputs:
            if "variablecategory" in dir(m) and m.variablecategory=="state" and m.name not in stname:
                st.append(m)
        return st

    @property
    def rates(self):
        rt=[]
        rtname = []
        for n in self.inputs:
            if "variablecategory" in dir(n) and n.variablecategory=="rate":
                rt.append(n)
                rtname.append(n.name)
        for m in self.outputs:
            if "variablecategory" in dir(m) and m.variablecategory=="rate" and m.name not in rtname:
                rt.append(m)
        return rt

    @property
    def auxiliary(self):
        au=[]
        auname = []
        for n in self.inputs:
            if "variablecategory" in dir(n) and n.variablecategory=="auxiliary":
                au.append(n)
                auname.append(n.name)
        for m in self.outputs:
            if "variablecategory" in dir(m) and m.variablecategory=="auxiliary" and m.name not in auname:
                au.append(m)
        return au

    @property
    def exogenous(self):
        ex=[]
        exname = []
        for n in self.inputs:
            if "variablecategory" in dir(n) and n.variablecategory=="exogenous":
                ex.append(n)
                exname.append(n.name)
        for m in self.outputs:
            if "variablecategory" in dir(m) and m.variablecategory=="exogenous" and m.name not in exname:
                ex.append(m)
        return ex

    @property
    def parameters(self):
        pa=[]
        for n in self.inputs:
            if "parametercategory" in dir(n):
                pa.append(n)
        return pa

    def __repr__(self):
        return 'ModelUnit'
