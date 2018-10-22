""" License, Header

"""
from copy import copy
import xml.etree.ElementTree as xml
from . import modelunit as munit
from . import description
from . import inout
from . import parameterset as pset
from . import checking
from . import algorithm

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
        
        for f in fn:
            
        # Current proxy node for managing properties
            doc = xml.parse(f)
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
        """ ModelUnit (Description,Inputs,Outputs,Algorithm,Parametersets,
                     Testsets)
        """
        print('ModelUnit')
        kwds = elts.attrib
        self._model = munit.ModelUnit(kwds)
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
    
    def Algorithm(self, elt):
        """ Algorithm
        """
        print('Algorithm')
        
        language=elt.attrib["language"]
        platform=elt.attrib["platform"]
        development = elt.text
        
        if "function" in elt.attrib: 
            function=elt.attrib["function"]
            filename=elt.attrib["filename"]
            algo = algorithm.Algorithm(language, development, platform, function, filename)
        else: 
            algo = algorithm.Algorithm(language, development, platform)
        
        self._model.algorithms.append(algo)

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



    def Testsets(self, elts):
        """ Testsets (Testset)
        """
        print('Testsets')

        for elt in list(elts):
            self.Testset(elt)
            
        self.testsets = self._model.testsets

    def Testset(self, elts):
        """ Testset(Test)
        """
        print('Testset')
        properties = elts.attrib
        name = properties.pop('name')
        print name

        _testset = checking.testset(self._model, name, properties)

        for elt in list(elts):
            print elt        
            testname = elt.attrib['name'] # name of test
            print(testname)
            input_test={}
            output_test={}
            param_test={}
            #_test = checking.Test(name)                    
            for j in elt.findall("InputValue"):  # all inputs
                name = j.attrib["name"]
                input_test[name]=j.text
            for j in elt.findall("OutputValue"):  # all outputs
                name = j.attrib["name"]
                output_test[name]=[j.text,j.attrib["precision"]]
                param_test = {"inputs":input_test, "outputs":output_test}
            _testset.test.append({testname:param_test})
                    
            #self._model.testsets.setdefault(name, []).append(_testset)
        self._model.testsets.append(_testset)


def model_parser(fn):
    """ Parse a set of models as xml files and return the models.
    
    Returns ModelUnit object of the CropML Model.
    """

    parser = ModelParser()
    return parser.parse(fn)

