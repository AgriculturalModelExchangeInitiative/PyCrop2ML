""" Read xml representation of a component.

"""
from path import Path

import xml.etree.ElementTree as xml


data = Path('data')
xmls = data.glob('*.xml')


##############################################################################
# Model Unit Representation


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

class Description(object):
    """ Model Unit Description.

    A description is defined by:
      - Title
      - Author
      - Institution
      - Reference
      - Abstract
    """

    def __init__(self):
        self.Title = ''
        self.Author= ''
        self.Institution = ''
        self.Reference = ''
        self.Abstract = ''


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


class Parameterset(object):
    """ Parameter set """
 
    def __init__(self, name, description, uri=None):
        self.name = name
        self.description = description
        self.uri = uri
        self.params = {}
        
    def _load_from_uri(self):
        pass
    

class Test(object):
    """ Test """
    def __init__(self, name, description, uri=None):
        self.name = name
        self.description = description
        self.uri = uri
        self.paramsets = []

class Algorithm(object):
    """ Algorithm """

def parameterset(model, name, kwds):
    if not kwds:
        # look at the parameters in the parametersets and return it
        return model.parametersets.get(name)
    else:
        return Parameterset(name, **kwds)
    
    
##############################################################################
# Parser representation


class Parser(object):
    """ Read an XML file and transform it in our object model.
    """

    def parse(self, fn):
        self.trash = []
        self.models = []

        # Current proxy node for managing properties

        doc = xml.parse(fn)
        root = doc.getroot()

        self.dispatch(root)

        return self.models

    def dispatch(self, elt):
        #try:
        return self.__getattribute__(elt.tag)(elt)
        #except Exception, e:
        #    print e
            #raise Exception("Unvalid element %s" % elt.tag)

    def ModelUnit(self, elts):
        """ ModelUnit (Description,Inputs,Ouputs,Algorithm,Parametersets,
                     Tests)
        """
        print('ModelUnit')

        self._model = ModelUnit()
        self.models.append(self._model)

        for elt in list(elts):
            self.dispatch(elt)


    def Description(self, elts):
        """ Description (Title,Author,Institution,Reference,Abstract)
        """
        print('Description')

        desc = Description()

        for elt in list(elts):
            self.name = desc.__setattr__(elt.tag, elt.text)

        self._model.add_description(desc)

    def Inputs(self, elts):
        """ Inputs (Input)
        """
        print('Inputs')

        for elt in list(elts):
            self.dispatch(elt)

    def Input(self, elts):
        """ Input
        """
        print('Input: ')
        properties = elts.attrib
        _input = Input(properties)
        self._model.inputs.append(_input)

    def Outputs(self, elts):
        """ Ouputs (Output)
        """
        print('Outputs')

        for elt in list(elts):
            self.dispatch(elt)

    def Output(self, elts):
        """ Output
        """
        print('Output: ')

        properties = elts.attrib
        _output = Output(properties)
        self._model.outputs.append(_output)
        
    def Parametersets(self, elts):
        """ Parametersets (Parameterset)
        """
        print('Parametersets')

        for elt in list(elts):
            self.Parameterset(elt)

    def Parameterset(self, elts):
        """ Parameterset
        """
        print('Parameterset: ')
        properties = elts.attrib
        name = properties.pop('name')

        _parameterset = parameterset(self._model, name, properties)

        for elt in list(elts):
            self.param(_parameterset, elt)
        
        name = _parameterset.name
        self._model.parametersets[name] = _parameterset
        
            
    def param(self, pset, elt):
        """ Param
        """
        print('Param: ', elt.attrib, elt.text)
        properties = elt.attrib
        
        name = properties['name']
        pset.params[name] = elt.text
       
    
    def Algorithm(self, elt):
        """ Algorithm
        """
        print('Algorithm', elt.text)

        self._model.algorithm = elt.text

  

    def Tests(self, elts):
        """ Tests (Test)
        """
        print('Tests')
        for elt in list(elts):
            # todo
            t = Test(**(elt.attrib))
            for ps in list(elt):
                name = ps.attrib['name']
                t.paramsets.append(name)
            self._model.tests.append(t)


##############################################################################
# Test on Example

def test1():
    fn = data.glob('Example*.xml')[0]

    parser = Parser()
    model = parser.parse(fn)
    return model
