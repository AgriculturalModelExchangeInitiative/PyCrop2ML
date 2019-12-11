from pycropml import render_fortran
from pycropml import render_java
from pycropml import render_csharp
from pycropml.render_cyml import transf
import six
def generate_test_py(model,dir=None):
    tab = ' '*4
    m = model
    #name = m.description.Title
    name = m.name
    name.strip()
    name = name.replace(' ', '_').lower()
    model_name = name
    psets = m.parametersets
    code_test = []
    for v_tests in m.testsets:

        #test_name = v_tests.name  # name of tests
        test_runs = v_tests.test  # different run in the thest
        test_paramsets = v_tests.parameterset  # name of paramsets

        # map the paramsets
        params = {}

        if test_paramsets.strip() != "" and test_paramsets not in list(psets.keys()):
            print(' Unknow parameter %s' % test_paramsets)
        else:
            if test_paramsets.strip() != "":
                params.update(psets[test_paramsets].params)
            for each_run in test_runs:
                test_codes = []

                # make a function that transforms a title into a function name
                tname = list(each_run.keys())[0].replace(' ', '_')
                tname = tname.replace('-', '_')

                (run, inouts) = list(each_run.items())[0]
                ins = inouts['inputs']
                outs = inouts['outputs']

                code = "params= model_%s(" % model_name
                test_codes.append(code)

                run_param = params.copy()
                run_param.update(ins)

                for k, v in six.iteritems(run_param):
                    type = [inp.datatype for inp in m.inputs if inp.name==k][0]
                    code = tab + "%s = %s," % (k, transf(type, v)) 
                    test_codes.append(code)
                code = "     )"
                test_codes.append(code)

                for j, k in enumerate(m.outputs):
                    if k.datatype in ("STRINGLIST", "DATELIST", "STRINGARRAY", "DATEARRAY"):
                        code = "print('%s_estimated =')" % k.name
                        test_codes.append(code)
                        code = "print(params[%s])" % (j) if len(
                            m.outputs) > 1 else "print(params)" % k.name
                        test_codes.append(code)
                        code = "# %s_computed = %s" % (
                            k.name, outs[k.name][0])
                        test_codes.append(code)

                    if k.datatype in ("STRING", "BOOL", "INT", "DATE"):
                        code = "print('%s_estimated =')" % (k.name if k.datatype !="BOOLEAN" else k.datatype.lower().capitalize())
                        test_codes.append(code)
                        code = "print(params[%s])" % (j) if len(
                            m.outputs) > 1 else "print(params)"
                        test_codes.append(code)
                        code = "# %s_computed = %s" % (
                            k.name, outs[k.name][0])
                        test_codes.append(code)

                    if k.datatype in ("DOUBLELIST", "DOUBLEARRAY"):
                        code = "print('%s_estimated =')" % k.name
                        test_codes.append(code)
                        code = "print(numpy.around(params[%s], %s))" % (j, outs[k.name][1]) if len(
                            m.outputs) > 1 else "print(numpy.around(params, %s))" % outs[k.name][1]
                        test_codes.append(code)
                        code = "# %s_computed = %s" % (
                            k.name, outs[k.name][0])
                        test_codes.append(code)

                    if k.datatype in ("INTLIST", "INTARRAY"):
                        code = "print('%s_estimated =')" % k.name
                        test_codes.append(code)
                        code = "print(params[%s])" % (j) if len(
                            m.outputs) > 1 else "print(params)"
                        test_codes.append(code)
                        code = "# %s_computed = %s" % (
                            k.name, outs[k.name][0])
                        test_codes.append(code)

                    if k.datatype == "DOUBLE":
                        code = "print('%s_estimated =')" % k.name
                        test_codes.append(code)
                        code = "print(round(params[%s], %s))" % (j, outs[k.name][1]) if len(
                            m.outputs) > 1 else "print(round(params, %s))" % outs[k.name][1]
                        test_codes.append(code)
                        code = "# %s_computed = %s" % (
                            k.name, outs[k.name][0])
                        test_codes.append(code)

                code = '\n'.join(test_codes)
                code_test.append(code)
    return code_test

def generate_test_f90(model, dir):
    return [render_fortran.Model2Package(model, dir).generate_test(model)]


def generate_test_cs(model, dir):
    return [render_csharp.Model2Package(model, dir).generate_test(model)]

def generate_test_java(model,directory=None):
    return [render_java.Model2Package(model, directory).generate_test(model)]

def generate_test_simplace(model,dir=None):
    pass

def generate_test_sirius(model,dir=None):
    pass

def generate_test_openalea(model,dir=None):
    pass

def generate_test_check(model,dir=None):
    pass