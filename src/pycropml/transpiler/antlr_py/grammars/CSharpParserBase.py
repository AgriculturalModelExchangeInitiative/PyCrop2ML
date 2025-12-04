# Manually generated
# From https://github.com/sanskar-dalvi/Code-Nebula/blob/main/grammar

from antlr4 import Parser

class CSharpParserBase(Parser):
    """Base class for C# parser with helper methods for parsing context"""
    
    def __init__(self, input, output=None):
        super().__init__(input, output)
