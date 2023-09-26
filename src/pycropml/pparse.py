""" License, Header

"""
from __future__ import absolute_import
from __future__ import print_function
from copy import copy
import xml.etree.ElementTree as xml
from . import modelunit as munit
from . import description
from . import inout
from . import parameterset as pset
from . import checking
from . import algorithm
from . import function
from . import initialization
import os.path
import os
from path import Path

class Parser(object):
    """Read an XML file and transform it in our object model."""
    def parse(self, crop2ml_dir):
        raise Exception('Not Implemented')

    def dispatch(self, elt):
        return self.__getattribute__(elt.tag)(elt)


class ModelParser(Parser):
    """Read an XML file and transform it in our object model."""
    def parse(self, crop2ml_dir):
        self.models = []
        self.crop2ml_dir = crop2ml_dir
        xmlrep = Path(os.path.join(self.crop2ml_dir, 'crop2ml'))
        self.algorep = Path(os.path.join(self.crop2ml_dir, 'crop2ml'))
        fn = xmlrep.glob('unit*.xml') + xmlrep.glob('function*.xml')+xmlrep.glob('init*.xml')
        try:
            for f in fn:           
        # Current proxy node for managing properties            
                doc = xml.parse(f)
                root = doc.getroot()
                self.dispatch(root)               
        except Exception as e:
            print(("%s is NOT in CropML Format ! %s" % (f, e)))         
        return self.models
           
    def dispatch(self, elt):
        #try:
        return self.__getattribute__(elt.tag)(elt)
        #except Exception, e:
        #    print e
            #raise Exception("Unvalid element %s" % elt.tag)

    def ModelUnit(self, elts):
        """ModelUnit (Description,Inputs,Outputs,Algorithm,Parametersets, Testsets)"""
        #print('ModelUnit')
        kwds = elts.attrib
        self._model = munit.ModelUnit(kwds)
        self._model.path = os.path.abspath(self.crop2ml_dir)   
        self.models.append(self._model)
        for elt in list(elts):
            self.dispatch(elt)

    def Description(self, elts):
        """Description (Title,Authors,Institution,Reference,Abstract)"""
        #print('Description')
        desc = description.Description()
        for elt in list(elts):
            #self.name = desc.__setattr__(elt.tag, elt.text)
            desc.__setattr__(elt.tag, elt.text)
        self._model.add_description(desc)

    def Inputs(self, elts):
        """Inputs (Input)"""
        #print('Inputs')
        for elt in list(elts):
            self.dispatch(elt)

    def Input(self, elts):
        """Input"""
        #print('Input: ')
        properties = elts.attrib
        _input = inout.Input(properties)
        self._model.inputs.append(_input)

    def Outputs(self, elts):
        """Outputs (Output)"""
        #print('Outputs')

        for elt in list(elts):
            self.dispatch(elt)

    def Output(self, elts):
        """Output"""
        #print('Output: ')

        properties = elts.attrib
        _output = inout.Output(properties)
        self._model.outputs.append(_output)
    
    def Initialization(self, elt):
        language = elt.attrib["language"]
        name = elt.attrib["name"]
        filename = elt.attrib["filename"]
        #description =elt.attrib["description"]
        code = initialization.Initialization(name, language, filename)
        self._model.initialization.append(code)

    def Function(self, elt):
        language = elt.attrib["language"]
        name = elt.attrib["name"]
        filename = elt.attrib["filename"]
        type = elt.attrib["type"]
        description = elt.attrib["description"]
        code = function.Function(name, language, filename, type, description)    
        self._model.function.append(code)
        
    def Algorithm(self, elt):
        """Algorithm"""
        #print('Algorithm')
        
        language = elt.attrib["language"]
        platform = elt.attrib["platform"]

        if "filename" in elt.attrib:
            filename = elt.attrib["filename"]
            #file = self.algorep/ os.path.splitext(filename)[1][1:]/filename
            file = Path(os.path.join(self.algorep, filename))
            with open(file, 'r') as f:
                development = f.read()
            algo = algorithm.Algorithm(language, development, platform, filename)
        else:
            development = elt.text
            algo = algorithm.Algorithm(language, development, platform)
        
        self._model.algorithms.append(algo)

    def Parametersets(self, elts):
        """Parametersets (Parameterset)"""
        #print('Parametersets')

        for elt in list(elts):
            self.Parameterset(elt)

    def Parameterset(self, elts):
        """Parameterset"""
        #print('Parameterset: ')
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
        #print('Param: ', elt.attrib, elt.text)
        properties = elt.attrib

        name = properties['name']
        pset.params[name] = elt.text

    def Testsets(self, elts):
        """ Testsets (Testset)
        """
        #print('Testsets')

        for elt in list(elts):
            self.Testset(elt)
            
        self.testsets = self._model.testsets

    def Testset(self, elts):
        """ Testset(Test)"""
        #print('Testset')
        properties = elts.attrib
        name = properties.pop('name')
        #print name

        _testset = checking.testset(self._model, name, properties)

        for elt in list(elts):
            #print elt        
            testname = elt.attrib['name'] # name of test
            #print(testname)
            input_test = {}
            output_test = {}
            param_test = {}
            #_test = checking.Test(name)                    
            for j in elt.findall("InputValue"):  # all inputs
                name = j.attrib["name"]
                input_test[name]=j.text
            for j in elt.findall("OutputValue"):  # all outputs
                name = j.attrib["name"]
                if len(j.attrib) == 2:
                    output_test[name] = [j.text,j.attrib["precision"]]
                else: output_test[name] = [j.text]
                param_test = {"inputs": input_test, "outputs": output_test}
            _testset.test.append({testname:param_test})
                    
            #self._model.testsets.setdefault(name, []).append(_testset)
        self._model.testsets.append(_testset)


def model_parser(crop2ml_dir):
    """
    Parse a set of models as xml files contained in crop2ml directory
    and algorithm in src directory
    This function returns models as python object.
    
    Returns ModelUnit object of the Crop2ML Model.
    """

    parser = ModelParser()
    return parser.parse(crop2ml_dir)

    # cache previous calls
    #if not hasattr(model_parser, "dir_to_models"):
    #    model_parser.dir_to_models = {}

    #if crop2ml_dir not in model_parser.dir_to_models:
    #    parser = ModelParser()
    #    model_parser.dir_to_models[crop2ml_dir] = parser.parse(crop2ml_dir)

    #return model_parser.dir_to_models[crop2ml_dir]

