""" Units.

"""

from __future__ import absolute_import
from __future__ import print_function
from pycropml.units import cyml_reg
from copy import copy
import xml.etree.ElementTree as xml
import six
from pycropml.pparse import Parser
from path import Path
import os
class UnitDefinition(object):
    """
    """
    def __init__(self, kwds):
        self._attributes = kwds
        for k, v in six.iteritems(kwds):
            self.__setattr__(k,v)

    def __repr__(self):
        return str(self._attributes)


class UnitList(UnitDefinition):
    """ Formal description of a Model Unit. """

    def __init__(self, kwds):
        UnitDefinition.__init__(self, kwds)
        self.unitvs=[]
    
    def __repr__(self):
        return 'Units'

class UnitV(object):
    """ Units.

    """
    def __init__(self,symbol, value, offset,factor, prefixable=None, tex_repr=None):
        self.symbol = symbol 
        self.value = value
        self.offset = offset
        self.factor=factor
        self.prefixable=prefixable
        self.tex_repr = tex_repr



class UnitParser(Parser):
    """ Read an XML file and transform it in our object model.
    """
    def parse(self, crop2mldir):
        self.unitvs = []
        self.crop2ml_dir = crop2mldir
        xmlrep = Path(os.path.join(self.crop2ml_dir,'crop2ml'))
        self.algorep = Path(os.path.join(self.crop2ml_dir,'crop2ml'))  
        f = xmlrep.glob('VarUnit*.xml')[0]
        try:          
        # Current proxy node for managing properties            
            doc = xml.parse(f)
            root = doc.getroot()
            self.dispatch(root)               
        except Exception as e:
            print(("%s is NOT in CropML Format ! %s" % (f, e)))         
        return self.unitvs
           
    def dispatch(self, elt):
        #try:
        return self.__getattribute__(elt.tag)(elt)
        #except Exception, e:
        #    print e
            #raise Exception("Unvalid element %s" % elt.tag)

    def UnitList(self, elts):
        """ (UnitV)
        """
        #print('Unit')
        kwds = elts.attrib
        self._unit = UnitList(kwds)
        self.unitvs.append(self._unit)
        for elt in list(elts):
            self.dispatch(elt)

    def UnitV(self, elt):
        """ Input
        """
        #print('Input: ')
        symbol=elt.attrib["symbol"]
        value=elt.attrib["value"]
        offset=elt.attrib["offset"]
        factor=elt.attrib["factor"]
        prefixable=elt.attrib["prefixable"]
        tex_repr=elt.attrib["tex_repr"]
        _unit = UnitV(symbol, value, offset, factor,prefixable, tex_repr)
        self._unit.unitvs.append(_unit)

def parser(crop2mldir):
    """ 
    Parse a set of Units xml files contained in crop2ml directory
    This function returns units as python object.

    Parameters:
    - Crop2mldir : package directory
    
    Returns  Units object of the Crop2ML Model.
    """
    parser = UnitParser()
    res = parser.parse(crop2mldir)[0]

    #Runtime error if unit already exists in the registry
    from . import units
    for unit in res.unitvs:
        if unit.value not in cyml_reg:
            units.unit_object.define_unit(unit.symbol, (eval(unit.factor), unit.value), registry=cyml_reg)

    return res