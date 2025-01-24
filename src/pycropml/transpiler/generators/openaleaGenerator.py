
from pycropml.transpiler.generators.pythonGenerator import PythonGenerator, PythonCompo
import os
from pycropml.composition import model_parser
from path import Path

try:
    from openalea.core import interface as inter
    from openalea.core import package, CompositeNodeFactory, CompositeNode
    from openalea.core import node
    from pycropml.xml2wf import XmlToWf
    from openalea.core.pkgmanager import PackageManager
except:
    inter = None
    package = None
    node = None
    has_openalea = False

class OpenaleaGenerator(PythonGenerator):
    """ This class contains the specific properties of
    OpenAlea and use the NodeVisitor to generate a csharp
    code source from a well formed syntax tree.
    """
    
    def __init__(self, tree=None, model=None, name=None):
        self.tree = tree
        self.model=model
        self.name = name
        self.indent_with=' '*4
        PythonGenerator.__init__(self, tree, model, name)

    def visit_module(self, node):
        self.newline(extra=1)
        self.newline(node)
        self.write("# coding: utf8")
        self.newline(node)
        #self.write("from pycropml.units import u")
        #self.newline(node)
        self.write("from copy import copy\nfrom array import array\nfrom math import *\nfrom typing import *\nfrom datetime import datetime\n")
        self.newline(node)
        self.visit(node.body)

    def visit_local(self, node):
        self.write(node.name)

    def visit_int(self, node):
        self.write(node.value)

    def visit_float(self, node):
        self.write(node.value)

    def visit_importfrom(self, node):
        if self.imp:
            self.newline(node)
            if node.namespace not in ["math", "array", "typing", "datetime"]:
                self.write('from %s import ' % (node.namespace))
                for idx, item in enumerate(node.name):
                    if idx:
                        self.write(', ')
                    self.write(item)

class OpenaleaCompo(PythonCompo):

    def __init__(self, tree, model=None, name=None):
        self.tree = tree
        self.model = model
        self.name = name
        PythonCompo.__init__(self,tree, model, self.name)
        self.generate_wralea(self.model)

    def generate_wralea(self, mc):
        """Generate wralea factories from the meta-information of the the model units."""

        '''if not has_openalea:
            return'''

        # TODO
        metainfo = {'version': '0.0.1',
                    'license': 'CECILL-C',
                    'authors': 'AMEI Consortium',
                    'institutes': '',
                    'description': 'CropML Model library.',
                    'url': 'http://crop2ml.org',
                    'icon': ''}
        metainfo['alias']= [mc.name]
        
        split_name = (mc.id).lower().split('.') # remove the name of the workflow
        names = split_name[:-1] if len(split_name) >2 else split_name
        names.insert(0, 'amei')
        name = '.'.join(names).lower()
        wra_path = mc.path.split(os.path.sep)[-1]
        path = Path(os.path.join(mc.path,"src","openalea", wra_path))
        _package = package.UserPackage(name, metainfo, path)
        for model in mc.model:
            if not model.package_name or model.package_name=="unit":		
                _factory = self.generate_factory(model)
                print(_factory.name)
                _package.add_factory(_factory)
            else:
                pass
        print(_package, _package.name)
        _package.write() 
        writer = XmlToWf(mc, path, name)
        writer.run()
        writer.pkg.name = name
        writer.pkg.write() 



    
    def generate_factory(self, model):
        """Create a Node Factory from CropML model unit."""
        '''if not has_openalea:
            return'''

        inputs = []
        for input in model.inputs:
            name = input.name
            dtype = input.datatype
            interface = openalea_interface(input)
            if dtype not in ('STRING', 'BOOLEAN' ,'DATE') and 'default' in dir(input):
                print(input.default)
                value = eval(input.default) if input.default else 0
                _in = dict(name=name, interface=interface, value=value)
            elif 'default' in dir(input):
                value=input.default.capitalize() if dtype=="BOOLEAN" else input.default
                _in = dict(name=name, interface=interface, value=value)
            elif 'default' not in dir(input):
                _in = dict(name=name, interface=interface)

            #value = eval(input.default) if dtype != 'string'else input.default

            inputs.append(_in)

        outputs = []
        for output in model.outputs:
            name = output.name
            dtype = output.datatype
            interface = openalea_interface(output)

            _out = dict(name=name, interface=interface)
            outputs.append(_out)

        _factory = node.Factory(name=model.name,
                                description=model.description.ExtendedDescription,
                                nodemodule=signature(model),
                                nodeclass="model_%s"%(signature(model)),
                                inputs=inputs,
                                outputs=outputs,
                                )
        return _factory   
    


def signature(model):
    name = model.name
    name = name.strip()
    name = name.replace(' ', '_').lower()
    return name

def openalea_interface(inout):
    if inter is None:
        return None

    dtype = inout.datatype.lower().strip()
    interface = None

    kwds = {}
    if inout.min:
        kwds['min'] = inout.min
    if inout.max:
        kwds['max'] = inout.max

    if dtype in ('int', 'float', 'double') :
        interface =inter.IInt if dtype == 'int' else inter.IFloat
        if ('min' in kwds) and ('max' in kwds):
            #print(inout)
            interface = interface(min=eval(inout.min), max=eval(inout.max))
        elif 'min' in kwds:
            interface = interface (min=eval(inout.min))
        elif 'max' in kwds:
            interface = interface(max=eval(inout.max))

    elif dtype == 'string':
        interface = inter.IStr

    elif dtype == "boolean":
        interface = inter.IBool

    elif dtype == "date":
        interface = inter.IDateTime

    elif dtype in ("doublelist", "intlist", "stringlist","datelist", "doublearray", "intarray", "datearray"):
        interface=inter.ISequence

    return interface
