from __future__ import absolute_import
from __future__ import print_function
import sys
try:
    from openalea.core.external import *
    from openalea.core.pkgmanager import PackageManager
    from openalea.core import node
except:
    inter = None
    package = None
    node = None
    has_openalea = False
    
from pycropml.render_python import generate_doc
from pycropml.pparse import model_parser


class XmlToWf(object):


    def __init__(self, xmlwf,dir_, pkg_name):
        self.xmlwf = xmlwf
        self.dir=dir_
        self.pkg_name = pkg_name
        self.inputLinks = self.xmlwf.inputlink
        self.outputLinks = self.xmlwf.outputlink
        self.internalLinks = self.xmlwf.internallink
        self.diff_in = self.xmlwf.diff_in
        self.diff_out = self.xmlwf.diff_out
        print(self.diff_in)
        print(self.diff_out)
        self.inputs = []
        self.outputs = []
    
    def run(self):
        self.doc = generate_doc(self.xmlwf)
        self.pkg = self.retrievePackage(self.pkg_name)
        self.compositeNodeInputs()
        self.compositeNodeOutputs()
        self.wf = CompositeNode(self.inputs_wf, self.outputs_wf)
        self.createNodes()
        # BUG: replace doc with description
        wf_factory = CompositeNodeFactory(self.xmlwf.name+"_wf", description=self.doc)
        self.connectOutputs()
        self.connectInputs()
        self.connectInternal()
        self.wf.to_factory(wf_factory)
        if wf_factory.name in self.pkg:
            del self.pkg[wf_factory.name]
        self.pkg.add_factory(wf_factory)

        self.pkg.write()

    def retrievePackage(self, name):
         pm = PackageManager()
         pm.init(self.dir, False)
         pkg = pm[name]
         return pkg

    def compoPack(self, name):
        for model in self.xmlwf.model:
            if model.name == name and model.package_name:
                self.dir = model.path
        

    def compareInterface(self,interfaces):
        test= True
        n = 1

        while(test and n!=len(interfaces)):
            if interfaces[n].min != interfaces[n-1].min:
                test=False
                break
            elif interfaces[n].max!=interfaces[n-1].max:
                test=False
                break
            elif interfaces[n].step!=interfaces[n-1].step:
                test=False
                break
            elif type(interfaces[n])!=type(interfaces[n-1]):
                test=False
                break
            n=n+1
        return test


    def compositeNodeInputs(self):
        ins=[]
        names = []

        for link in self.inputLinks:
            name = link["source"]
            if name not in names:
                names.append(name)
        # some models can have the same inputs. These inputs must have the same interfaces
        for name in names:
            links_sameName = [link for link in self.inputLinks if link["source"]==name]
            #print(links_sameName)
            if len(links_sameName)!=1:
                interfaces=[]
                try:
                    for j in links_sameName:
                        model= j["target"].split('.')[0]
                        inputs = self.pkg[model].inputs
                        interface=[inp["interface"] for inp in inputs if inp["name"]==name]
                        interfaces.append(interface[0])
                    #assert self.compareInterface(interfaces)== True
                except AssertionError:
                    print(("inequal interface: %s %s"% (interfaces, links_sameName)))
                for inp in inputs:
                    if inp["name"]==name and "value" in inp:
                        value=inp["value"]
                        break
                if value:
                    din=dict(name=name, interface = interfaces[0], value=value)
                else:
                    din=dict(name=name, interface = interfaces[0])
                ins.append(din)
                self.inputs.append(name) 
            else:
                value=None
                model= links_sameName[0]["target"].split('.')[0]
                if model in self.pkg:
                    inputs = self.pkg[model].inputs
                    if name in list(self.diff_in.values()): name = findname(name, self.diff_in)
                    interface=[inp["interface"] for inp in inputs if inp["name"]==name]
                    for inp in inputs:
                        if inp["name"]==name and "value" in inp:
                            value=inp["value"]
                            break
                    if value:
                        din=dict(name=name, interface = interface[0], value=value)
                    else:
                        din=dict(name=name, interface = interface[0])
                    ins.append(din)
                    self.inputs.append(name)

        self.inputs_wf = ins



    def compositeNodeOutputs(self):

        outs=[]
        # model units outputs must be unique. So model composite output is targeted by an unique output link
        for link in self.outputLinks:
            name =  link["target"]
            if name in list(self.diff_out.values()): name = findname(name, self.diff_out)
            model_src, out_src= link["source"].split('.')
            if model_src in self.pkg:
                outputs = self.pkg[model_src].outputs
                interface=[out["interface"] for out in outputs if out["name"]==name]
                dout= dict(name=name, interface = interface[0])
                outs.append(dout)
                self.outputs.append(name)

        self.outputs_wf = outs


    def createNodes(self):
        self.nodes = {}
        for m in self.xmlwf.model:
            if m.name in self.pkg:
                nf = self.pkg[m.name].instantiate()
                nid =  self.wf.add_node(nf)
                self.nodes[m.name] = nid

    def connectInputs(self):
        for link in self.inputLinks:
            src, tgt = link['source'], link['target']
            if src in list(self.diff_in.values()): src = findname(src, self.diff_in)
            port_out = src
            name_tgt, port_in = tgt.split('.')
            if name_tgt in self.nodes:
                ns, nt = self.wf.id_in, self.nodes[name_tgt]
                try:
                    pout, pin = self.wf.node(ns).map_index_out[port_out],  self.wf.node(nt).map_index_in[port_in]
                except KeyError:
                    if port_out not in self.wf.node(ns).map_index_out:
                        print('Error input link src : ', src)
                    else:
                        print(('Error input link tgt: ', tgt))
                    continue
                self.wf.connect(ns, pout, nt, pin)

    def connectOutputs(self):
        for link in self.outputLinks:
            src, tgt = link['source'], link['target']
            if tgt in list(self.diff_out.values()): tgt = findname(tgt, self.diff_out)
            name_src, port_out = src.split('.')
            port_in = tgt
            if name_src in self.nodes:
                ns, nt = self.nodes[name_src], self.wf.id_out
                try:
                    pout, pin = self.wf.node(ns).map_index_out[port_out],  self.wf.node(nt).map_index_in[port_in]
                except KeyError:
                    if port_out not in self.wf.node(ns).map_index_out:
                        print('Error output link src: ', src)
                    else:
                        print(('Error output link tgt: ', tgt))
                    continue
                self.wf.connect(ns, pout, nt, pin)

    def connectInternal(self):
        for link in self.internalLinks:
            src, tgt = link['source'], link['target']
            name_src, port_out = src.split('.')
            name_tgt, port_in = tgt.split('.')
            if name_tgt in self.nodes and name_src in self.nodes:
                ns, nt = self.nodes[name_src], self.nodes[name_tgt]
                try:
                    pout, pin =self. wf.node(ns).map_index_out[port_out],  self.wf.node(nt).map_index_in[port_in]
                except KeyError:
                    if port_out not in self.wf.node(ns).map_index_out:
                        print('Error : ', src)
                    else:
                        print(('Error : ', tgt))
                    continue
                self.wf.connect(ns, pout, nt, pin)

def findname(val, dictionary):
    for k, v in dictionary.items():  
        if v == val:
            return k   
    return None