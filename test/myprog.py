from path import Path
from urlparse import urlparse
from pycropml import pparse, render_python
from test1 import example, cwd, xmls


if (cwd/'data').isdir():
    data = cwd/'data'
elif (cwd/'test'/'data').isdir():
    data = cwd/'test'/'data'
else:
    print('Data directory not found')
models = example()
m, = models
t1, t2 = m.tests

file_psets = {}
file_tsets = {}

# Compute the name of the model
# TODO save the name in the model
name = m.description.Title
name.strip()
name = name.replace(' ', '_').lower()
model_name = name
##


psets = m.parametersets
# Compute for each parameter set the set of parameters.
# A parameter set is a dict of parameter_name and values.
for name in psets:
    ps = psets[name]
    if not ps.params:
        # compute the params from the uri
        # define a function that may do the job
        uri = ps.uri
        parse_res = urlparse(uri)
        if parse_res.scheme == 'file':
            filename = parse_res.netloc
            _filename = data/filename
            if _filename.isfile():
                # read the file and fill the params
                if filename not in file_psets:
                    file_psets[filename] = pparse.pset_parser(_filename, m)
            else:
                assert 0, ('The file '+ filename+ ' do not exists')


# Compute the tests and make the relationships
for test in (t1, t2):
    print 'Test: ',test.name
    name = test.name
    print test.paramsets
    param_values = {}

    uri = test.uri
    print uri
    parse_res = urlparse(uri)
    if parse_res.scheme == 'file':
        filename = parse_res.netloc
        _filename = data/filename

        if _filename.isfile():
            if filename not in file_tsets:
                file_tsets[filename] = pparse.test_parser(_filename, m)


# Build the content of the test with the run
# Generate the Python code

m2p = render_python.Model2Package(models);
m2p.run()
code = m2p.code
exec(code)

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

               
        code = "\n"+"    print ("'"params : {}"'+".format(params)"')'
        
        test_codes.append(code)
        
        code = "    return params"
        
        test_codes.append(code)

        the_code = '\n'.join(test_codes)
        
        exec the_code
        
        print the_code
        
        # Get from the params the different values
        
        func = 'test_%s_run%s()'%(tname, run)
        exec func
        
        # Then, assert that the values are equal to the outs.
        
        assert func == float(outs.values()[0])
        
