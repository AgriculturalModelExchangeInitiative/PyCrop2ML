""" Read xml representation of a component.

"""
from path import Path

import xml.etree.ElementTree as xml


data = Path('data')
xmls = data.glob('*.xml')


class ModelUnit(object):
    """ Formal description of a Model Unit. """

    def __init__(self):
        self.description = None
        self.inputs = []
        self.outputs = []
        self.parametersets = []
        self.algorithm = None
        self.tests = []

    def add_description(description):
        """ TODO """
        self.description = description

class Description(object):
    """ Model Description. """

class Test(object):
    """ Test """

class Algorithm(object):
    """ Algorithm """


def test1():
    fn = data.glob('Example*.xml')[0]

    doc = xml.parse(fn)
    root = doc.getroot()
    return root
