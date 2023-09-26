import six

class InputOutput(object):
    """
    """
    def __init__(self, kwds):
        self.min = None
        self.max = None
        self._attributes = kwds
        for k, v in six.iteritems(kwds):
            self.__setattr__(k, v)

    def __repr__(self):
        return str(self._attributes)



class Input(InputOutput):
    """ Input """


class Output(InputOutput):
    """ Output
    """

    def __setattr__(self, k, v):
        print("output.__setattr__(", k, ",", v, ")")
        if k == "name" and self._attributes["name"] == "newSoilTemperature" and v == "soilTemperature":
            print("here")
        InputOutput.__setattr__(self, k, v)
