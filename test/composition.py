""" Read xml representation of a model composite

"""
from path import Path
import xml.etree.ElementTree as xml

# Fix pb in tlocal path
cwd = Path.getcwd()
if (cwd/'data'/'usecase').isdir():
    data = cwd/'data'/'usecase'
elif (cwd/'test'/'data'/'usecase').isdir():
    data = cwd/'test'/'data'/'usecase'
else:
    print('Data directory not found')

xmls = data.glob('*.xml')


##############################################################################
# Test on Example

def example():

    composition = data.glob("composition*.xml")[0]
    
    models = model_parser(composition)
    return models
    
################################################################################


class ModelDefinition(object):
    """
    """
    def __init__(self, kwds):
        self._attributes = kwds
        for k, v in kwds.iteritems():
            self.__setattr__(k,v)

    def __repr__(self):
        return str(self._attributes)


class ModelComposition(ModelDefinition):
    """ Formal description of a Model Unit. """

    def __init__(self, kwds):
        ModelDefinition.__init__(self, kwds)  
        self.description = None
        self.model = []
        self.inputlink=[]
        self.outputlink=[]
        self.internallink=[]
 

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

class Models(object):
          
    def __init__(self, name, id, file):
        self.name=name
        self.id=id
        self.file=file
 
 
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
        
        """ ModelComposition (Description,Inputlink,Outputlink,externallink)                   Testsets)
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
        id=elt.attrib["id"]
        file = elt.attrib["filename"]
        
        
        mod = Models(name, id, file)
        
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
        
        for output in outputs: 
            
            out = output.attrib        
            self._modelcompo.outputlink.append(out)
        
        for internal in internals : 
            
            inter = internal.attrib  
            self._modelcompo.internallink.append(inter)     
        
            
def model_parser(fn):
    """ Parse a composite model and return the model.
    
    Returns ModelComposite object of the CropML Model.
    """

    parser = ModelParser()
    return parser.parse(fn)
    
    
    
####### test
"""
from test import composition
m, = composition.example()
"""

#############   
    
    