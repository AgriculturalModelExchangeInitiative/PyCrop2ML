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


    def run(self):
        """TODO.
        """
        self.generate_package()


    def generate_package(self):
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
        nb = nbf.v4.new_notebook()

        text = """\
# Automatic generation of Notebook using PyCropML
This notebook implements a crop model."""
        nb['cells'] = [nbf.v4.new_markdown_cell(text),
                       nbf.v4.new_code_cell(self.code)]

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
        self.codetest = "'Test generation'\n\n"

        self.codetest += "from model import *\n\n"

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

                code = '\n'
                test_codes.append(code)

                code = "def test_%s_run%s():"%(tname, run)
                test_codes.append(code)
                code = "    params= %s("%model_name
                test_codes.append(code)

                run_param = params.copy()
                run_param.update(ins)

                for k, v in run_param.iteritems():
                    code = "    %s = %s,"%(k,v)
                    test_codes.append(code)
                code = "     )"
                test_codes.append(code)

                if len(outs) <= 1:
                    code = tab + "params = round(params, 2)"
                    test_codes.append(code)

                    code = tab + "out_computed = {}".format( float(outs.values()[0]))
                    test_codes.append(code)

                    code = tab + "assert params == out_computed"
                    test_codes.append(code)
                else:
                    code = tab + "params = [round(p, 2) for p in params]"
                    test_codes.append(code)

                    code = tab + "out_computed = ["+ ', '.join([outs[o] for o in m.outputs]) + "]"
                    test_codes.append(code)

                    code = tab + "assert params == out_computed"
                    test_codes.append(code)


                #func = 'test_%s_run%s()'%(tname, run)
                #code = "assert  "+ func+'["params"]=='+func+'["out_computed"]'
                #test_codes.append(code)

                code = '\n'.join(test_codes)

                print (code)

                self.codetest += code

        return self.codetest

    def write_tests(self):
        """ TODO: Manage several models rather tha just one.
        """
        files = []
        count = 0
        for model in self.models:
            codetest = self.generate_test(model)
            ext = '' if count == 0 else str(count)
            filename = self.dir/"testrun%s.py"%ext
            with open(filename, "w") as python_file:
                python_file.write(codetest)
                files.append(filename)
            count +=1
        return files



