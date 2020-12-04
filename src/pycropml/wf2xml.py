import sys
from openalea.core.external import *
from openalea.core.pkgmanager import PackageManager

from py.xml import Namespace

class ns(Namespace):
    "Custom xml namespace"

class Wf2Xml(object):
    """ Export an OpenAlea Workflow into a Crop2ML Model composite.

    """
    def __init__(self, wf, pmanager=None):
        """ Export a workflow into OpenAlea.

        :Parameters:
          - wf : an OpenAlea workflow (factory)

        """
        self.wf = wf
        if pmanager is None:
            self.pmanager = PackageManager()
        else:
            self.pmanager = pmanager

    def run(self):
        """ Generate Crop2ML specification of a CompositeModel from a workflow. """
        wf = self.wf

        # ModelComposition name id version timestep
        xml = ns.ModelComposition(name=wf.name, id=wf.package.name, version="001", timestep="1")

        # Extract the description of the wf
        # TODO: Do it in a generic way
        doc = wf.description
        docs = [x.strip() for x in doc.strip().split('\n')]

        if len(docs) == 5:
            title = docs[0]
            if docs[1].startswith('Author'):
                authors = docs[1].split(':')[1]
                authors = authors.strip()
            else:
                authors = wf.authors

            if docs[2].startswith('Reference'):
                references = docs[2].split(':')[1]
                references = references.strip()
            else:
                references = wf.description

            if docs[3].startswith('Institution'):
                institution = docs[3].split(':')[1]
                institution = institution.strip()
            else:
                institution = wf.package.metainfo.get('institutes', '')

            if docs[4].startswith('Abstract'):
                abstract = docs[4].split(':')[1]
                abstract = abstract.strip()
            else:
                abstract = ''

        # Description
        desc = ns.Description(
            ns.Title(title),
            ns.Authors(authors),
            ns.Institution(institution),
            ns.Reference(references),
            ns.Abstract(abstract)
            )

        xml.append(desc)

        composition = ns.Composition()
        for k, v in wf.elt_factory.iteritems():
            pkg, name = v
            composition.append(ns.Model(name=name, id=pkg+'.'+name, filename='unit.'+name+'.xml'))

        links = ns.Links()


        nodes = wf.elt_factory

        for eid, link in wf.connections.iteritems():
            (source_vid, source_port, target_vid, target_port) = link

            if source_vid == '__in__':
                pkg, factory = nodes[target_vid]
                nf = self.pmanager[pkg][factory]
                _target = factory+'.'+nf.inputs[target_port]['name']
                _source = wf.inputs[source_port]['name']
                links.append(ns.InputLink(target=_target, source=_source))

            elif target_vid == '__out__':
                pkg, factory = nodes[source_vid]
                nf = self.pmanager[pkg][factory]
                _source = factory+'.'+nf.inputs[source_port]['name']
                _target = wf.outputs[target_port]['name']
                links.append(ns.OutputLink(source=_source, target=_target))

            else:
                pkg, factory = nodes[source_vid]
                nf = self.pmanager[pkg][factory]
                _source = factory+'.'+nf.inputs[source_port]['name']
                pkg, factory = nodes[target_vid]
                nf = self.pmanager[pkg][factory]
                _target = factory+'.'+nf.inputs[target_port]['name']

                links.append(ns.InternalLink(target=_target, source=_source))

        composition.append(links)

        xml.append(composition)

        print(xml.unicode(indent=4).encode('utf8'))
        return xml
