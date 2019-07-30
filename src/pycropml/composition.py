""" Read xml representation of a model composite

"""
from __future__ import absolute_import
from __future__ import print_function
from path import Path
import xml.etree.ElementTree as xml
import six
from pycropml.modelunit import ModelUnit
from pycropml import pparse

class ModelDefinition(object):
    """
    Model name, id, version and step
    """
    def __init__(self, kwds):
        self._attributes = kwds
        for k, v in six.iteritems(kwds):
            self.__setattr__(k,v)

    def __repr__(self):
        return str(self._attributes)


class ModelComposition(ModelDefinition):
    """ Formal description of a Model Composite. """

    def __init__(self, kwds):
        ModelDefinition.__init__(self, kwds)  
        self.description = None
        self.model = []
        self.inputlink=[]
        self.outputlink=[]
        self.internallink=[]
        self.inputs=[]
        self.outputs=[]
 

    def add_description(self, description):
        """ TODO """
        self.description = description

    def __repr__(self):
        return 'ModelComposition'
    
class Description(object):
    """ Model Composition Description.

    A description is defined by:
      - Title
      - Authors
      - Institution
      - Reference
      - Abstract
    """

    def __init__(self):
        self.Title = ''
        self.Authors= ''
        self.Institution = ''
        self.Reference = ''
        self.Abstract = ''

class Models(ModelComposition, ModelUnit):           
    def __init__(self, name, modelid, file, package_name=None):  
        self.name=name
        self.modelid=modelid
        self.file=file
        self.package_name = package_name

 
 
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
        self.modelcompos = []
          
        # Current proxy node for managing properties
        doc = xml.parse(fn)
        root = doc.getroot()

        self.dispatch(root)
        return self.modelcompos

    def dispatch(self, elt):
        #try:
        return self.__getattribute__(elt.tag)(elt)
    
    
    def ModelComposition(self, elts):
        
        """ ModelComposition (Description, Models, Inputlink,Outputlink,externallink)                 
        """
        print('ModelComposition')
        kwds = elts.attrib
        self._modelcompo = ModelComposition(kwds)
        self.modelcompos.append(self._modelcompo)
        

        for elt in list(elts):
            self.dispatch(elt)
   
    
    def Description(self, elts):
        """ Description (Title,Author,Institution,Reference,Abstract)
        """
        print('Description')

        desc = Description()

        for elt in list(elts):
            self.name = desc.__setattr__(elt.tag, elt.text)

        self._modelcompo.add_description(desc)
        
    
    def Composition(self, elts):
        print('Composition')
        
        for elt in list(elts):
            self.dispatch(elt)
          
    def Model(self, elt):
        """ Models
        """
        print('Model')
        
        name=elt.attrib["name"]
        modelid=elt.attrib["id"]
        file = elt.attrib["filename"]
        if "package_name" in elt.attrib:
            package_name=elt.attrib["package_name"]
        else: package_name=None
        
        mod = Models(name, modelid, file, package_name)
        
        self._modelcompo.model.append(mod)
    
    def Links(self, elt):
        
        """
            Retrieve different types of links
        """
        print("link")
        
        inputs = elt.findall("InputLink")
        outputs = elt.findall("OutputLink")
        internals = elt.findall("InternalLink")
        
        for input in inputs:
            inp = input.attrib
            self._modelcompo.inputlink.append(inp)
            if inp["source"] not in self._modelcompo.inputs:
                self._modelcompo.inputs.append(inp["source"])
        
        for output in outputs: 
            
            out = output.attrib        
            self._modelcompo.outputlink.append(out)
            if out["target"] not in self._modelcompo.outputs:
                self._modelcompo.outputs.append(out["target"])
        
        for internal in internals : 
            
            inter = internal.attrib  
            self._modelcompo.internallink.append(inter)     
        
            
def model_parser(fn):
    """ Parse a composite model and return the model.
    
    Returns ModelComposite object of the CropML Model.
    """

    parser = ModelParser()
    return parser.parse(fn)
    

