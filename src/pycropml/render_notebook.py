""" License, Header

Use pkglts


Problems:
- name of a model unit?
"""
from __future__ import print_function
from path import Path

# The package used to generate Notebook
import nbformat as nbf

from . import render_python as rp



class Model2Nb(rp.Model2Package):
    """ Generate a Jupyter Notebook from a set of models.
    """

    def __init__(self, models, dir=None):
        """TODO.

        """
        super(Model2Nb, self).__init__(models, dir=dir)
        self.with_import = False


    def run(self):
        """TODO.
        """
        self.generate_notebook()


    def generate_notebook(self):
        """Generate a Python package equivalent to the xml definition.

        Args:
        - models : a list of model
        - dir: the directory where the code is generated.

        Returns:
        - None or status
        """
        for model in self.models:
            self.generate_component(model)

        # Create a directory (mymodel)
        cwd = Path(self.dir)
        directory=cwd/'notebook'
        if (directory).isdir() :
            _dir = directory
        else:
            _dir = directory.mkdir()


        # In the directory notebook/model.py
        # TODO: The code need to be generated locally in different methods.

        nb = nbf.v4.new_notebook()

        text = """\
# Automatic generation of Notebook using PyCropML
This notebook implements a crop model."""
        _cells = nb['cells'] = [nbf.v4.new_markdown_cell(text),
                       nbf.v4.new_code_cell(self.code)]


        # Generate the tests
        text_test = """\
## Run the model with a set of parameters.
Each run will be defined in its own cell."""
        _cells.append(nbf.v4.new_markdown_cell(text_test))

        for model in self.models:
            code_tests = self.generate_test(model)
            for code in code_tests:
                _cells.append(nbf.v4.new_code_cell(code))


        fname = _dir/'test.ipynb'
        with open(fname, "w") as f:
            nbf.write(nb, f)
        return self.code


    def generate_test(self, model_unit):

        tab = ' '*4
        m = model_unit
        name = m.description.Title
        name.strip()
        name = name.replace(' ', '_').lower()
        model_name = name
        psets = m.parametersets
        # self.codetest = "'Test generation'\n\n"
        # if self.with_import:
        #     self.codetest += "from model import *\n\n"

        code_test = []

        for v_tests in m.tests.values():

            test_name = v_tests[0].name  # name of tests
            test_runs = v_tests[0].run  # different run in the thest
            test_paramsets = v_tests[0].paramsets  # name of paramsets

        # map the paramsets
            params = {}
            for pname in test_paramsets:
                if pname not in psets:
                    print('Unknow parameter %s'%pname)
                else:
                    params.update(psets[pname].params)

            for each_run in test_runs :
                test_codes = []

            # make a function that transforms a title into a function name
                tname = test_name.replace(' ', '_')
                tname = tname.replace('-', '_')


                (run, inouts) = each_run.items()[0]

                ins = inouts['inputs']
                outs = inouts['outputs']

                #code = '\n'
                #test_codes.append(code)

                #code = "def test_%s_run%s():"%(tname, run)
                #test_codes.append(code)
                code = "params= %s("%model_name
                test_codes.append(code)

                run_param = params.copy()
                run_param.update(ins)

                for k, v in run_param.iteritems():
                    code = tab + "%s = %s,"%(k,v)
                    test_codes.append(code)
                code = tab + ")"
                test_codes.append(code)


                if len(outs) <= 1:
                    code = "print(round(params, 2))"
                    test_codes.append(code)

                    code = "\n"
                    test_codes.append(code)

                    code = "# output = {}".format( float(outs.values()[0]))
                    test_codes.append(code)

                else:
                    code = "print([round(p, 2) for p in params])"
                    test_codes.append(code)

                    code = "\n" + "# outputs = ["+ ', '.join([outs[o] for o in m.outputs]) + "]"
                    test_codes.append(code)


                #func = 'test_%s_run%s()'%(tname, run)
                #code = "assert  "+ func+'["params"]=='+func+'["out_computed"]'
                #test_codes.append(code)

                code = '\n'.join(test_codes)
                code_test.append(code)

        return code_test
