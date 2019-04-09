from pycropml.transpiler import Parser
from path import Path

def test_parser1():
    filename = Path.getcwd()/"tests_transpiler"/"data"/"example1.pyx"
    tree_example1 = Parser.parser(filename)
    treeast = tree_example1.dump()
    treefile= Path.getcwd()/"tests_transpiler"/"output"/"tree_example1.ast"
    with open(treefile, "w") as fi:
        fi.write(treeast)

test_parser1()
    