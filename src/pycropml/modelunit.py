""" Model Description and Model Unit.

"""
class ModelDefinition(object):
    """
    """
    def __init__(self, kwds):
        self._attributes = kwds
        for k, v in kwds.iteritems():
            self.__setattr__(k,v)

    def __repr__(self):
        return str(self._attributes)


class ModelUnit(ModelDefinition):
    """ Formal description of a Model Unit. """

    def __init__(self, kwds):
        ModelDefinition.__init__(self, kwds)
        self.description = None
        self.inputs = []
        self.outputs = []
        self.function=[]
        self.Initialization=[]
        self.algorithms = []
        self.parametersets = {}
        self.testsets = []

    def add_description(self, description):
        """ TODO """
        self.description = description

    def __repr__(self):
        return 'ModelUnit'
