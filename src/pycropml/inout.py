
class InputOutput(object):
    """
    """
    def __init__(self, kwds):
        self._attributes = kwds
        for k, v in kwds.iteritems():
            self.__setattr__(k,v)

    def __repr__(self):
        return str(self._attributes)



class Input(InputOutput):
    """ Input """
    

class Output(InputOutput):
    """ Output
    """