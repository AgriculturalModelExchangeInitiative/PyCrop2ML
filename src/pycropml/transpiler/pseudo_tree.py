# coding: utf8
from __future__ import absolute_import
import yaml
class Node:
    """
    The new Node generated with specific properties.
    These properties are automatically set
    
    Example: Node(type='local', name='l', pseudo_type="int") to represent a int variable declaration
    """
    def __init__(self, type, **fields):
        self.type = type
        self.__dict__.update(fields) 
        if 'pseudo_type' not in fields:
            self.pseudo_type = 'Void'
        if 'comments' not in fields:
            self.comments = []
    
    @property
    def y(self):
        result = yaml.dump(self)
        return result.replace('!!python/object:pycropml.transpiler.pseudo_tree.', '')

    def __eq__(self, a):
        return all(getattr(self, f) == getattr(a, f, None) for f in self.__dict__)
