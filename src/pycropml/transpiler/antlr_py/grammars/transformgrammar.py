"""Adapt the C# ANTLR grammars for the Python target.

The upstream C# grammars use ``this.`` in semantic actions.  Python-target
generated code needs ``self.`` instead.  Only the C# lexer and parser are
selected by default; other grammar families must not be changed implicitly.
"""

import re
import shutil
import sys
from pathlib import Path


DEFAULT_GRAMMARS = ("CSharpLexer.g4", "CSharpParser.g4")

def main(files=None):
    """Adapt the selected grammars in the current directory.

    When no paths are supplied, only ``CSharpLexer.g4`` and
    ``CSharpParser.g4`` are transformed.  Original files are copied to
    ``.bak`` before being rewritten, so the operation remains recoverable.
    """
    paths = [Path(file) for file in (files or DEFAULT_GRAMMARS)]
    for path in paths:
        transform_grammar(path)

def transform_grammar(file_path):
    """Transform one grammar and retain an adjacent ``.bak`` copy."""
    file_path = Path(file_path)
    if not file_path.is_file():
        raise FileNotFoundError(f"Could not find grammar: {file_path}")

    backup = file_path.with_name(file_path.name + ".bak")
    shutil.copy2(file_path, backup)
    source = file_path.read_text(encoding="utf-8")
    adapted = re.sub(r"!this\.", "not self.", source)
    adapted = re.sub(r"(?<![A-Za-z0-9_])this\.", "self.", adapted)
    file_path.write_text(adapted, encoding="utf-8")
    print(f"Adapted {file_path} (backup: {backup})")

if __name__ == '__main__':
    main(sys.argv[1:])
