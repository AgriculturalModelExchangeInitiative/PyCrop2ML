
from pycropml.transpiler.antlr_py.extract_metadata import MetaExtraction
from pycropml.description import Description
from pycropml.composition import ModelComposition
from pycropml.transpiler.antlr_py.extract_metadata_from_comment import ExtractComments, extract_compo
from pycropml.transpiler.antlr_py.extraction import ExtractComments
from openalea.core.pkgmanager import PackageManager
import re


class OpenaleaExtraction(MetaExtraction):
    def __init__(self):
        MetaExtraction.__init__(self)
        self.model = None
        self.mc = None
        self.wf = None
        self.pm = PackageManager()
    
    def retrievePackage(self, wralea_dir):
         self.pm.init(wralea_dir)
         pkg = self.pm.get_composite_nodes()[0]  
         return pkg

    def modelunit(self, file, tree):
        pass
           
    def modelcomposition(self, wf, mu_names):
        #self.pm.clear()
        self.wf =  wf
        doc = self.wf.description
        docs = [x.strip() for x in doc.strip().split('\n')]
        title = docs[0]
        head = {}
        version_pat = r'(-Version:\s*(?P<version>\d+\.*\d+))'
        timestep_pat = r'(-Time step:\s*(?P<timestep>\d+\.*\d*))'
        if re.search(version_pat, docs[1]):
            head["version"] = re.search(version_pat, docs[1]).group("version") 
        if re.search(timestep_pat, docs[1]):
            head["timestep"] = re.search(timestep_pat, docs[1]).group("timestep") 
        
        xx = docs[2:]
        pat_description = r'(^(Authors:|Reference:|Institution:|ExtendedDescription:|ShortDescription))'
        res = []
        i = 0
        while True:
            if re.match(pat_description, xx[i]):
                res.append(xx[i])
            else:
                if res: res[-1] = res[-1]+"\n"+xx[i]
            i = i+1
            if i==len(xx): break
        
        d = Description()
        d.Title = title
        d.Authors = res[0].split("Author:")[-1]
        d.Reference = res[1].split("Reference:")[-1]
        d.Institution = res[2].split("Institution:")[-1]
        d.ExtendedDescription = res[3].split("ExtendedDescription:")[-1]
        d.ShortDescription = res[4].split("ShortDescription:")[-1]

        nodes = self.wf.elt_factory
        inputlink = []
        outputlink = []
        internallink = []

        for eid, link in self.wf.connections.items():
            (source_vid, source_port, target_vid, target_port) = link

            if source_vid == '__in__':
                pkg, factory = nodes[target_vid]
                nf = self.pm[pkg][factory]
                _target = factory+'.'+nf.inputs[target_port]['name']
                _source = self.wf.inputs[source_port]['name']
                inputlink.append({"target": _target, "source":_source})

            elif target_vid == '__out__':
                pkg, factory = nodes[source_vid]
                nf = self.pm[pkg][factory]
                _source = factory+'.'+nf.outputs[source_port]['name']
                _target = self.wf.outputs[target_port]['name']
                outputlink.append({"source": _source, "target":_target})

            else:
                pkg, factory = nodes[source_vid]
                nf = self.pm[pkg][factory]
                _source = factory+'.'+nf.outputs[source_port]['name']
                pkg, factory = nodes[target_vid]
                nf = self.pm[pkg][factory]
                _target = factory+'.'+nf.inputs[target_port]['name']
                internallink.append({"source": _source, "target":_target})
                
        head["name"] = self.wf.name[:-3] if self.wf.name.endswith("_wf") else self.wf.name
        mc = ModelComposition(head)      
        mc.add_description(d)
        mc.inputlink = inputlink
        mc.outputlink = outputlink
        mc.internallink = internallink
        
        mc.model = mu_names
        self.pm = None
        return mc
        
