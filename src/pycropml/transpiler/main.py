import pycropml.transpiler.generators
import pycropml.transpiler.generators.csharpGenerator
import pycropml.transpiler.generators.pythonGenerator
import pycropml.transpiler.generators.fortranGenerator
from pycropml.transpiler.Parser import parser
from pycropml.transpiler.ast_transform import AstTransformer, transform_to_syntax_tree

language = ['cs','py', 'f90']
NAMES = {'cs':'csharp', 'py':'python', 'f90':'fortran'}

GENERATORS = {
    format: getattr(
                getattr(
                    pycropml.transpiler.generators,
                    '%sGenerator' % NAMES[format]),
                '%sGenerator' % NAMES[format].capitalize())
    for format in language
}

class Main():
    def __init__(self, file,language, models=None):
        self.file = file
        self.language=language
        self.models = models          

    def parse(self):
        self.tree= parser(self.file)
        return self.tree

    def to_ast(self, source):
        self.newtree = AstTransformer(self.tree, source)
        self.dictAst = self.newtree.transformer()
        self.nodeAst= transform_to_syntax_tree(self.dictAst)
        return self.nodeAst

    def to_source(self):
        generator = GENERATORS[self.language](self.nodeAst,self.models)
        node = self.nodeAst.body
        generator.visit(node)
        return ''.join(generator.result)