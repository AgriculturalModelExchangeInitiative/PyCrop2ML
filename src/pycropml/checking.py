
class Testset(object):
    """ Test """
    def __init__(self, name, parameterset,description, uri=None):
        self.name = name
        self.description = description
        self.uri = uri
        self.parameterset = parameterset
        self.test = []
        self.run = []

class Test(Testset):
    
    def __init__(self, name):
        Testset.__init__(self)
        self.name = name
        
def testset(model, name, kwds):
    if not kwds:
        # look at the tests in the testsets and return it
        return model.testsets.get(name)
    else:
        return Testset(name, **kwds)