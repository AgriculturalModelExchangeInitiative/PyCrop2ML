import pycropml.transpiler.generators
import pycropml.transpiler.generators.csharpGenerator
import pycropml.transpiler.generators.pythonGenerator
from pycropml.transpiler.Parser import parser
from pycropml.transpiler.ast_transform import AstTransformer, transform_to_syntax_tree

language = ['cs','py']
NAMES = {'cs':'csharp', 'py':'python'}

GENERATORS = {
    format: getattr(
                getattr(
                    pycropml.transpiler.generators,
                    '%sGenerator' % NAMES[format]),
                '%sGenerator' % NAMES[format].capitalize())
    for format in language
}

class Main():
    def __init__(self, file,language):
        self.file = file
        self.language=language

    def parse(self):
        self.tree= parser(self.file)
        return self.tree

    def to_ast(self, source):
        newtree = AstTransformer(self.tree, source)
        dictAst = newtree.transformer()
        self.nodeAst= transform_to_syntax_tree(dictAst)
        return self.nodeAst

    def to_source(self):
        generator = GENERATORS[self.language]()
        node = self.nodeAst.body
        generator.visit(node)
        return ''.join(generator.result)
    
    