""" License, Header

"""

import xml.etree.ElementTree as xml
from . import modelunit as munit
from . import description
from . import inout
from . import parameterset as pset
from . import checking

class Parser(object):
    """ Read an XML file and transform it in our object model.
    """

    def parse(self, fn):
        raise Exception('Not Implemented')


    def dispatch(self, elt):
        return self.__getattribute__(elt.tag)(elt)


class ModelParser(Parser):
    """ Read an XML file and transform it in our object model.
    """

    def parse(self, fn):
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

        self._model = munit.ModelUnit()
        self.models.append(self._model)

        for elt in list(elts):
            self.dispatch(elt)


    def Description(self, elts):
        """ Description (Title,Author,Institution,Reference,Abstract)
        """
        print('Description')

        desc = description.Description()

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
        _input = inout.Input(properties)
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
        _output = inout.Output(properties)
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

        _parameterset = pset.parameterset(self._model, name, properties)

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
            t = checking.Test(**(elt.attrib))
            for ps in list(elt):
                name = ps.attrib['name']
                t.paramsets.append(name)
            self._model.tests.append(t)


class ParametersParser(ModelParser):

    def parse(self, fn, model):
        self._model = model
        self.parametersets = {}

        # Current proxy node for managing properties

        doc = xml.parse(fn)
        root = doc.getroot()

        self.dispatch(root)

        return self.parametersets

    def Parameterset(self, elts):
        """ Parameterset
        """
        print('Parameterset: ')
        properties = elts.attrib
        name = properties.pop('name')

        _parameterset = pset.parameterset(self._model, name, properties)

        for elt in list(elts):
            self.param(_parameterset, elt)

        self.parametersets[name] = _parameterset

class TestParser(ModelParser):

    def parse(self, fn, model):
        self._model = model
        self.tests = {}

        # Current proxy node for managing properties

        doc = xml.parse(fn)
        root = doc.getroot()

        self.dispatch(root)

        return self.parametersets

    def Parameterset(self, elts):
        """ Parameterset
        """
        print('Parameterset: ')
        properties = elts.attrib
        name = properties.pop('name')

        _parameterset = pset.parameterset(self._model, name, properties)

        for elt in list(elts):
            self.param(_parameterset, elt)

        self.parametersets[name] = _parameterset


def model_parser(fn):
    """ Parse a set of models as xml files and return the models.
    """
    parser = ModelParser()
    return parser.parse(fn)

def pset_parser(fn, model):
    """ Parse a set of parameter as xml files and return the parameters.
    """
    parser = ParametersParser()
    return parser.parse(fn, model)

def test_parser(fn, model):
    """ TODO. """
