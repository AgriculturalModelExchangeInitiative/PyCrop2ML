import argparse
import sys

from antlr4 import FileStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener

from .composition_compiler import compile_composition, write_composition_xml
from .composition_visitor import CompositionSemanticError
from .grammars.Crop2MLCompositionLexer import Crop2MLCompositionLexer
from .grammars.Crop2MLCompositionParser import Crop2MLCompositionParser


class CollectingErrorListener(ErrorListener):

    def __init__(self):
        self.errors = []

    def syntaxError(
        self,
        recognizer,
        offendingSymbol,
        line,
        column,
        message,
        exception,
    ):
        self.errors.append(
            f"{line}:{column}: {message}"
        )


def validate(filename, model_directory=None):
    error_listener = CollectingErrorListener()

    lexer = Crop2MLCompositionLexer(
        FileStream(filename, encoding="utf-8")
    )
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)

    parser = Crop2MLCompositionParser(
        CommonTokenStream(lexer)
    )
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    parser.composition()

    if error_listener.errors:
        for error in error_listener.errors:
            print(error, file=sys.stderr)
        return False

    try:
        compile_composition(filename, model_directory)
    except (CompositionSemanticError, OSError, ValueError) as error:
        print(error, file=sys.stderr)
        return False

    print(f"{filename}: valid")
    return True


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Validate a Crop2ML composition algorithm."
    )
    parser.add_argument("composition_file", help="composition algorithm to validate")
    parser.add_argument(
        "--models",
        dest="model_directory",
        help="directory containing unit.*.xml (discovered automatically by default)",
    )
    parser.add_argument(
        "--write-xml",
        nargs="?",
        const="",
        metavar="FILE",
        help="write the generated composition XML; omit FILE for the default name",
    )
    args = parser.parse_args(argv)

    try:
        valid = validate(args.composition_file, args.model_directory)
        if valid and args.write_xml is not None:
            output = args.write_xml or None
            generated = write_composition_xml(
                args.composition_file,
                output_file=output,
                crop2ml_directory=args.model_directory,
            )
            print(f"Generated {generated}")
    except OSError as error:
        parser.error(str(error))

    return 0 if valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
