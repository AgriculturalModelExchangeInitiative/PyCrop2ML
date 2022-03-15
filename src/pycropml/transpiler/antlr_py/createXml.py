from py.xml import Namespace



class ns(Namespace):
    "Custom xml namespace"

class Pl2Crop2ml(object):
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
        xml = ns.ModelUnit(modelid=self.pkgname + "." + str(md.name), name=str(md.name), timestep="1", version="001")
        doc = md.description
        desc = ns.Description(
            ns.Title(doc.Title),
            ns.Authors(doc.Authors),
            ns.Institution(doc.Institution),
            ns.Reference(doc.Reference),
            ns.ExtendedDescription(doc.ExtendedDescription),
            ns.Url(doc.Url if "Url" in dir(doc) else "")
            )
        inputs = ns.Inputs()
        outputs = ns.Outputs()
        for inp in md.inputs:
            if "variablecategory" in dir(inp):
                inputs.append(ns.Input(name=inp.name, description=inp.description, inputtype=inp.inputtype, variablecategory=inp.variablecategory,  datatype=inp.datatype, max=inp.max, min = inp.min, default=inp.default, unit=inp.unit))
            else: inputs.append(ns.Input(name=inp.name, description=inp.description, inputtype=inp.inputtype, parametercategory=inp.parametercategory, datatype=inp.datatype, max=inp.max, min = inp.min, default=inp.default, unit=inp.unit))
        for inp in md.outputs:
            outputs.append(ns.Output(name=inp.name, description=inp.description, datatype=inp.datatype, variablecategory=inp.variablecategory, max=inp.max, min = inp.min, unit=inp.unit))
        algo =ns.Algorithm(language = "cyml", platform ="", filename="algo/pyx/%s.pyx"%md.name)
        xml.append(desc)
        xml.append(inputs)
        xml.append(outputs)
        xml.append(algo)
        if md.function:
            for f in md.function:
                func = ns.Function(name = f, description="", language="cyml", type="external", filename="algo/pyx/%s.pyx"%f)
                xml.append(func)
        parametersets=ns.Parametersets()
        parametersets.append(ns.Parameterset(name="", description=""))
        testsets=ns.Testsets()
        testsets.append(ns.Testset(name="", parameterset="",description=""))
        xml.append(parametersets)
        xml.append(testsets)

        return xml


    def run_compo(self):
        """ Generate Crop2ML specification of a CompositeModel from a workflow. """
        md = self.md
        name = md.name[:-9] if md.name.endswith("Component") else md.name
        # ModelComposition name id version timestep
        xml = ns.ModelComposition(name=name, id=self.pkgname + "." + name, version="001", timestep="1")

        # Extract the description of the wf
        # TODO: Do it in a generic way
        doc = md.description
        desc = ns.Description(
            ns.Title(doc.Title),
            ns.Authors(doc.Authors),
            ns.Institution(doc.Institution),
            ns.Reference(doc.Reference),
            ns.ExtendedDescription(doc.ExtendedDescription)
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