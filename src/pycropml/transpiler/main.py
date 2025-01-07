import sys

import pycropml.transpiler.generators
import pycropml.transpiler.generators.csharpGenerator
import pycropml.transpiler.generators.cppGenerator
import pycropml.transpiler.generators.cpp2Generator
import pycropml.transpiler.generators.pythonGenerator
import pycropml.transpiler.generators.fortranGenerator
import pycropml.transpiler.generators.javaGenerator
import pycropml.transpiler.generators.simplaceGenerator
import pycropml.transpiler.generators.apsimGenerator
import pycropml.transpiler.generators.recordGenerator
import pycropml.transpiler.generators.dssatGenerator
import pycropml.transpiler.generators.sticsGenerator
import pycropml.transpiler.generators.biomaGenerator
# Sirius is managed by BioMa
import pycropml.transpiler.generators.siriusGenerator
# import pycropml.transpiler.generators.sirius2Generator
import pycropml.transpiler.generators.checkGenerator
import pycropml.transpiler.generators.rGenerator
import pycropml.transpiler.generators.openaleaGenerator

from pycropml.transpiler.Parser import parser
from pycropml.transpiler.ast_transform import AstTransformer, transform_to_syntax_tree
import os
from path import Path

languages = [
    'r', 'cs', 'cpp', "cpp2", 'py', 'f90', 'java', 'simplace', 'sirius',  # 'sirius','sirius2',
    'openalea', 'check', 'apsim', 'record', 'dssat', 'stics', 'bioma']
NAMES = {
    'r': 'r',
    'cs': 'csharp',
    'cpp': 'cpp',
    "cpp2": "cpp2",
    'py': 'python',
    'f90': 'fortran',
    'java': 'java',
    'simplace': 'simplace',
    #'sirius':'sirius',
    # "sirius2":"sirius2",
    'openalea': 'openalea',
    'check': 'check',
    'apsim': 'apsim',
    'sirius': 'sirius',
    "record": "record",
    "dssat": "dssat",
    "stics": "stics",
    "bioma": "bioma"
}

GENERATORS = {
    format_: getattr(
        getattr(
            pycropml.transpiler.generators,
            '%sGenerator' % NAMES[format_]),
        '%sGenerator' % NAMES[format_].capitalize())
    for format_ in languages
}

COMPOSERS = {
    format_: getattr(
        getattr(
            pycropml.transpiler.generators,
            '%sGenerator' % NAMES[format_]),
        '%sCompo' % NAMES[format_].capitalize())
    for format_ in languages
}


def formater(code):
    z = code.strip().split("\n")
    code = ""
    for j in z:
        if j.strip().startswith("!"):
            code += j + "\n"
        else:
            code += formaterNext(j)
    return code


def formaterNext(line):
    nbmax = 70
    tab = " "
    code = ""
    s = 0
    ff = len(line) - len(line.lstrip())
    line = line.strip()
    h = ""
    if len(line) <= nbmax or line[-1] == "&":
        code += tab * ff + line
    while len(line) > nbmax and line[-1] != "&":

        nb = nbmax
        z = ff + 8 if s > 0 else ff
        while (line[nb - 1] != " ") and nb > 1:
            nb = nb - 1
        if nb > 1:
            h += tab * z + line[0:nb] + " &\n"
            line = (line[nb:]).strip()
            if len(line) <= nbmax:
                h += tab * (ff + 8) + line
                break
        else:
            h += tab * z + line
            break
        s = s + 1

    code += h + "\n"

    return code


class Main:
    def __init__(self, file, language, models=None, name=None):
        self.file = file
        self.language = language
        self.models = models
        if sys.version_info[0] > 3:
            self.path = os.path.abspath(file)
        else:
            self.path = Path(self.file)
            self.file = self.file
        self.name = name

        self.tree = None
        self.newtree = None
        self.dictAst = None
        self.nodeAst = None

    def parse(self):
        self.tree = parser(self.file)
        return self.tree

    def to_ast(self, source):
        self.newtree = AstTransformer(self.tree, source, self.models)
        self.dictAst = self.newtree.transformer()
        self.nodeAst = transform_to_syntax_tree(self.dictAst)
        return self.nodeAst

    def to_source(self):
        generator = GENERATORS[self.language](self.nodeAst, self.models, self.name)
        # node = self.nodeAst.body
        node = self.nodeAst
        generator.visit(node)
        z = ''.join(generator.result)
        if self.language == 'f90' or self.language == 'dssat' or self.language == 'stics':
            z = formater(z)
        return z

    def translate(self):
        generator = COMPOSERS[self.language](self.nodeAst, self.models, self.name)
        node = self.nodeAst
        generator.visit(node)
        z = ''.join(generator.result)
        if self.language == 'f90' or self.language == 'dssat' or self.language == 'stics':
            z = formater(z)
        return z
