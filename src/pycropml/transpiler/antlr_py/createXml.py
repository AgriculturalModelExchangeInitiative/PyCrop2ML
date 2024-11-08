import os
from pathlib import Path

import xmlformatter

from pycropml.transpiler.antlr_py.toxml import Namespace

class ns(Namespace):
    "Custom xml namespace"

class Pl2Crop2ml:
    """ Export a platform component into a Crop2ML ModelUnit.

    """
    def __init__(self, md, pkgname):
        """ Export a workflow into Crop.

        :Parameters:
          - md : A platform component metainformation

        """
        self.md = md
        self.pkgname = pkgname

    def run_unit(self):
        """ Generate Crop2ML specification of a ModelUnit. """
        md = self.md

        # ModelUnit name id version timestep
        xml = ns.ModelUnit(modelid=self.pkgname + "." + str(md.name), name=str(md.name), timestep=md.timestep, version=md.version)
        doc = md.description
        desc = ns.Description(
            ns.Title(doc.Title),
            ns.Authors(doc.Authors),
            ns.Institution(doc.Institution),
            ns.URI(doc.Url if "Url" in dir(doc) else ""),
            ns.Reference(doc.Reference if "Reference" in dir(doc) else ""),
            ns.ExtendedDescription(doc.ExtendedDescription), 
            ns.ShortDescription(doc.ShortDescription if "ShortDescription" in dir(doc) else "")
            )
        inputs = ns.Inputs()
        outputs = ns.Outputs()
        for inp in md.inputs:
            if "variablecategory" in dir(inp):
                if inp.datatype.endswith("ARRAY"):
                    inputs.append(ns.Input(name=inp.name, description=inp.description, inputtype=inp.inputtype, variablecategory=inp.variablecategory,  datatype=inp.datatype, len=inp.len, max=inp.max, min = inp.min, default=inp.default, unit=inp.unit))
                else: inputs.append(ns.Input(name=inp.name, description=inp.description, inputtype=inp.inputtype, variablecategory=inp.variablecategory,  datatype=inp.datatype, max=inp.max, min = inp.min, default=inp.default, unit=inp.unit))
            else: 
                if inp.datatype.endswith("ARRAY"):
                    inputs.append(ns.Input(name=inp.name, description=inp.description, inputtype=inp.inputtype, parametercategory=inp.parametercategory, datatype=inp.datatype, len=inp.len, max=inp.max, min = inp.min, default=inp.default, unit=inp.unit))  
                else: inputs.append(ns.Input(name=inp.name, description=inp.description, inputtype=inp.inputtype, parametercategory=inp.parametercategory, datatype=inp.datatype, max=inp.max, min = inp.min, default=inp.default, unit=inp.unit))
        
        for inp in md.outputs:
            if inp.datatype.endswith("ARRAY"):
                outputs.append(ns.Output(name=inp.name, description=inp.description, datatype=inp.datatype, variablecategory=inp.variablecategory, len=inp.len, max=inp.max, min = inp.min, unit=inp.unit))   
            else: outputs.append(ns.Output(name=inp.name, description=inp.description, datatype=inp.datatype, variablecategory=inp.variablecategory, max=inp.max, min = inp.min, unit=inp.unit))
        algo =ns.Algorithm(language = "cyml", platform ="", filename="algo/pyx/%s.pyx"%md.name)
        xml.append(desc)
        xml.append(inputs)
        xml.append(outputs)
        if md.initialization:
            for f in md.initialization:
                if "algo" in f["filename"]:
                    res = f["filename"]
                else:
                    res = "algo/pyx/%s"%f["filename"]

                init = ns.Initialization(name = f["name"], language="cyml", filename=res)
                xml.append(init)
        if md.function:
            for f in md.function:
                func = ns.Function(name = f, description="", language="cyml", type="external", filename="algo/pyx/%s.pyx"%f)
                xml.append(func)
        xml.append(algo)
        parametersets=ns.Parametersets()
        
        for k, v in md.parametersets.items():
            pa = []
            for r, s in v.params.items(): pa.append( ns.Param(s, name=r))
            parametersets.append(ns.Parameterset(pa , name=k, description=v.description))
            
        testsets=ns.Testsets()
        
        for testset in md.testsets:
            test = []
            for each_run in testset.test:
                tname = list(each_run.keys())[0].replace(' ', '_')
                tname = tname.replace('-', '_')
                (run, inouts) = list(each_run.items())[0]
                ins = inouts['inputs']
                outs = inouts['outputs']
                inp = []
                out = []
                for k, v in ins.items():
                    inp.append(ns.InputValue(v, name = k))
                for k, v in outs.items():
                    if isinstance(v, tuple):
                        out.append(ns.OutputValue(v[0], name = k, precision=v[1]))
                    else:
                        out.append(ns.OutputValue(v, name = k))
                    
                test.append(ns.Test(inp, out, name=tname))
                
            testsets.append(ns.Testset(test, name=testset.name, parameterset=testset.parameterset, description=testset.description))
        
        xml.append(parametersets)
        xml.append(testsets)

        return xml


    def run_compo(self):
        """ Generate Crop2ML specification of a CompositeModel from a workflow. """
        md = self.md
        name = md.name[:-9] if md.name.endswith("Component") else md.name
        # ModelComposition name id version timestep
        xml = ns.ModelComposition(name=name, id=self.pkgname + "." + name, version=md.version, timestep=md.timestep)

        # Extract the description of the wf
        # TODO: Do it in a generic way
        doc = md.description
        desc = ns.Description(
            ns.Title(doc.Title),
            ns.Authors(doc.Authors),
            ns.Institution(doc.Institution),
            ns.Reference(doc.Reference if "Reference" in dir(doc) else ""),
            ns.ExtendedDescription(doc.ExtendedDescription),
            ns.ShortDescription(doc.ShortDescription if "ShortDescription" in dir(doc) else "")
            )

        xml.append(desc)

        composition = ns.Composition()
        for m in md.model:
            composition.append(ns.Model(name=m, id=self.pkgname+'.'+m, filename='unit.'+m+'.xml'))

        links = ns.Links()

        for m in md.inputlink:
            links.append(ns.InputLink(target = m["target"], source = m["source"]))

        for m in md.internallink:
            links.append(ns.InternalLink(target = m["target"], source = m["source"]))

        for m in md.outputlink:
            links.append(ns.OutputLink(target = m["target"], source = m["source"]))

        composition.append(links)

        xml.append(composition)

        return xml
    


def generate_unitfile(package, mu, package_name):
    """_summary_

    Args:
        package (str): Path of Crop2ML package where ModelUnit xml file will be stored
        mu (ModelUnit): ModelUnit object
    """
    xml_ = Pl2Crop2ml(mu, package_name).run_unit()
    filename = os.path.join(package,  "crop2ml", "unit.%s.xml"%(mu.name))
    with open(filename, "wb") as xml_file:
        r = '<?xml version="1.0" encoding="UTF-8"?>\n'
        r += '<!DOCTYPE ModelUnit PUBLIC " " "https://raw.githubusercontent.com/AgriculturalModelExchangeInitiative/crop2ml/master/ModelUnit.dtd">\n'
        r += xml_.unicode(indent=4)#.encode('utf-8')
        xml_file.write(r.encode()) 
        #formatter = xmlformatter.Formatter(indent="1", indent_char="\t", encoding_output="ISO-8859-1", preserve=["literal"])
        #g = formatter.format_string(r)       
        #xml_file.write(g)   

def generate_compositefile(package, mc, package_name):
    """_summary_

    Args:
        package (str): Path of Crop2ML package where ModelComposite xml file will be stored
        mu (ModelUnit): ModelComposition object
    """
    xml_ = Pl2Crop2ml(mc, package_name).run_compo()
    filename = os.path.join(package,  "crop2ml", "composition.%s.xml"%(mc.name))
    with open(filename, "wb") as xml_file:
        r = '<?xml version="1.0" encoding="UTF-8"?>\n'
        r += '<!DOCTYPE ModelComposition PUBLIC " " "https://raw.githubusercontent.com/AgriculturalModelExchangeInitiative/crop2ml/master/ModelComposition.dtd">\n'
        r += xml_.unicode(indent=4)#.encode('utf-8')
        xml_file.write(r.encode()) 
        #formatter = xmlformatter.Formatter(indent="1", indent_char="\t", encoding_output="ISO-8859-1", preserve=["literal"])
        #g = formatter.format_string(r)       
        #xml_file.write(g)

def create_repo(package):
    crop2ml_rep = Path(os.path.join(package, 'crop2ml'))
    if not crop2ml_rep.is_dir():
        crop2ml_rep.mkdir()
    algo_rep = Path(os.path.join(crop2ml_rep, 'algo'))
    if not algo_rep.is_dir():
        algo_rep.mkdir()
    cyml_rep = Path(os.path.join(algo_rep, 'pyx'))
    if not cyml_rep.is_dir():
        cyml_rep.mkdir() 
