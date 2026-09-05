import sys
import os
from pathlib import Path

from pycropml.transpiler.Parser import parser
from pycropml.transpiler.ast_transform import AstTransformer, transform_to_syntax_tree
from pycropml.transpiler.logger import get_logger
from pycropml.transpiler.target_registry import (
    TARGETS,
    get_target,
    load_composer,
    load_generator,
)


logger = get_logger('transpiler.main')

languages = list(TARGETS)


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
        logger.debug('Parsing source input')
        self.tree = parser(self.file)
        logger.debug('Parsing completed')
        return self.tree

    def to_ast(self, source):
        logger.debug('Building AST')
        self.newtree = AstTransformer(self.tree, source, self.models)
        self.dictAst = self.newtree.transformer()
        self.nodeAst = transform_to_syntax_tree(self.dictAst)
        logger.debug('AST build completed')
        return self.nodeAst

    def to_source(self):
        generator_class = load_generator(self.language)
        generator = generator_class(self.nodeAst, self.models, self.name)
        # node = self.nodeAst.body
        node = self.nodeAst
        generator.visit(node)
        z = ''.join(generator.result)
        if get_target(self.language).format_fortran:
            z = formater(z)
        return z

    def translate(self):
        composer_class = load_composer(self.language)
        generator = composer_class(self.nodeAst, self.models, self.name)
        node = self.nodeAst
        generator.visit(node)
        z = ''.join(generator.result)
        if get_target(self.language).format_fortran:
            z = formater(z)
        return z
