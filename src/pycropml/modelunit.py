
class ModelUnit(object):
    """ Formal description of a Model Unit. """

    def __init__(self):
        self.description = None
        self.inputs = []
        self.outputs = []
        self.parametersets = {}
        self.algorithm = None
        self.tests = []

    def add_description(self, description):
        """ TODO """
        self.description = description

    def __repr__(self):
        return 'ModelUnit'
