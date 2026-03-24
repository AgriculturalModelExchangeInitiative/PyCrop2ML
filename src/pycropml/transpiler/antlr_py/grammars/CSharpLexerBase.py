# Manually generated
# From https://github.com/sanskar-dalvi/Code-Nebula/blob/main/grammar

from antlr4 import Lexer

class CSharpLexerBase(Lexer):
    def __init__(self, input, output=None):
        super().__init__(input, output)
        self.interpolatedStringLevel = 0
        self.interpolatedVerbatiums = []
        self.curlyLevels = []
        self.verbatium = False

    def OnInterpolatedRegularStringStart(self):
        self.interpolatedStringLevel += 1
        self.verbatium = False
        self.curlyLevels.append(0)
        self.interpolatedVerbatiums.append(self.verbatium)

    def OnInterpolatedVerbatiumStringStart(self):
        self.interpolatedStringLevel += 1
        self.verbatium = True
        self.curlyLevels.append(0)
        self.interpolatedVerbatiums.append(self.verbatium)

    def OnOpenBrace(self):
        if self.interpolatedStringLevel > 0:
            self.curlyLevels[-1] += 1

    def OnCloseBrace(self):
        if self.interpolatedStringLevel > 0:
            self.curlyLevels[-1] -= 1
            if self.curlyLevels[-1] == 0:
                self.curlyLevels.pop()
                self.interpolatedVerbatiums.pop()
                self.interpolatedStringLevel -= 1

    def InterpolatedStringLevel(self):
        return self.interpolatedStringLevel

    def IsVerbatiumString(self):
        return self.verbatium

    def IsRegularCharInside(self):
        return self.interpolatedStringLevel > 0

    def PopMode(self):
        super().popMode()
        if self._modeStack:
            self.verbatium = self.interpolatedVerbatiums[-1]
