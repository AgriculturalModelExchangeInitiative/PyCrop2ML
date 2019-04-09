from openalea.core.external import *
from openalea.core.pkgmanager import PackageManager
from pycropml.render_python import generate_doc


class XmlToWf(object):


    def __init__(self, xmlwf,dir, pkg_name):
        self.xmlwf = xmlwf
        self.dir=dir
        self.pkg_name = pkg_name
        self.inputLinks = self.xmlwf.inputlink
        self.outputLinks = self.xmlwf.outputlink
        self.internalLinks = self.xmlwf.internallink

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
                        #print(j)
                        #print(model)
                        #print(self.pkg[model])
                        inputs = self.pkg[model].inputs
                        #print(inputs)
                        interface=[inp["interface"] for inp in inputs if inp["name"]==name]
                        #print(interface)
                        interfaces.append(interface[0])

                    #assert self.compareInterface(interfaces)== True
                except AssertionError:
                    print("inequal interface: %s %s"% (interfaces, links_sameName))
                for inp in inputs:
                    if inp["name"]==name and "value" in inp:
                        value=inp["value"]
                        break

                if value:
                    din=dict(name=name, interface = interfaces[0], value=value)
                else:
                    din=dict(name=name, interface = interfaces[0])
                ins.append(din)

            else:
                value=None
                model= links_sameName[0]["target"].split('.')[0]
                print(model)
                inputs = self.pkg[model].inputs
                #print(inputs)
                interface=[inp["interface"] for inp in inputs if inp["name"]==name]
                #print(interface)
                for inp in inputs:
                    if inp["name"]==name and "value" in inp:
                        value=inp["value"]
                        break
                if value:
                    din=dict(name=name, interface = interface[0], value=value)
                else:
                    din=dict(name=name, interface = interface[0])
                ins.append(din)
        self.inputs_wf = ins



    def compositeNodeOutputs(self):

        outs=[]
        # model units outputs must be unique. So model composite output is targeted by an unique output link
        for link in self.outputLinks:
            print("out %s"%link)
            name =  link["target"]
            print(name)
            model_src, out_src= link["source"].split('.')
            outputs = self.pkg[model_src].outputs
            interface=[out["interface"] for out in outputs if out["name"]==name]
            dout= dict(name=name, interface = interface[0])
            outs.append(dout)

        self.outputs_wf = outs


    def createNodes(self):
        self.nodes = {}
        for m in self.xmlwf.model:
            nf = self.pkg[m.name].instantiate()
            nid =  self.wf.add_node(nf)
            self.nodes[m.name] = nid

    def connectInputs(self):
        for link in self.inputLinks:
            src, tgt = link['source'], link['target']
            port_out = src
            name_tgt, port_in = tgt.split('.')

            ns, nt = self.wf.id_in, self.nodes[name_tgt]
            try:
                pout, pin = self.wf.node(ns).map_index_out[port_out],  self.wf.node(nt).map_index_in[port_in]
            except KeyError:
                if port_out not in self.wf.node(ns).map_index_out:
                    print('Error input link src : ', src)
                else:
                    print('Error input link tgt: ', tgt)
                continue
            self.wf.connect(ns, pout, nt, pin)

    def connectOutputs(self):
        for link in self.outputLinks:
            src, tgt = link['source'], link['target']
            name_src, port_out = src.split('.')
            port_in = tgt

            ns, nt = self.nodes[name_src], self.wf.id_out
            try:
                pout, pin = self.wf.node(ns).map_index_out[port_out],  self.wf.node(nt).map_index_in[port_in]
            except KeyError:
                if port_out not in self.wf.node(ns).map_index_out:
                    print('Error output link src: ', src)
                else:
                    print('Error output link tgt: ', tgt)
                continue
            self.wf.connect(ns, pout, nt, pin)

    def connectInternal(self):
        for link in self.internalLinks:
            src, tgt = link['source'], link['target']
            name_src, port_out = src.split('.')
            name_tgt, port_in = tgt.split('.')

            ns, nt = self.nodes[name_src], self.nodes[name_tgt]
            try:
                pout, pin =self. wf.node(ns).map_index_out[port_out],  self.wf.node(nt).map_index_in[port_in]
            except KeyError:
                if port_out not in self.wf.node(ns).map_index_out:
                    print('Error : ', src)
                else:
                    print('Error : ', tgt)
                continue
            self.wf.connect(ns, pout, nt, pin)
