from __future__ import absolute_import
from __future__ import print_function
from path import Path

from pycropml import pparse, render_python
from pycropml import composition
from pycropml.xml2wf import XmlToWf
import pandas, csv

# Fix pb in local path
cwd = Path.getcwd()
if (cwd/'data').isdir():
    data = cwd/'data'
elif (cwd/'test'/'data').isdir():
    data = cwd/'test'/'data'
else:
    print('Data directory not found')



def testXmlwf():
        
    models = pparse.model_parser(data)
    
    # translate cropml model units to python functions and openalea in python_model repository
    render_python.Model2Package(models, dir='.',pkg_name="EnergyBalance").run()
    
    # repository of python models generated  with wralea
    dir = cwd/'python_model'
    
    rep_composite= data/'crop2ml'
    # composite file
    #print(rep_composite.glob("composition*.xml")[0])
    compositionFile = rep_composite.glob("composition*.xml")[0]
    
    xmlwf,= composition.model_parser(compositionFile)

    wf = XmlToWf(xmlwf, dir, "EnergyBalance")
    wf.run()
    #print(wf.inputs, wf.outputs)

    yet_in=[]
    yet_out=[]
    inputfile =dir/"input.txt"
    outputfile =dir/"output.txt"
    fi_in = open(inputfile, "w")
    fi_out = open(outputfile, "w") 
    writer_input = csv.writer(fi_in, lineterminator='\n', delimiter = ";")
    writer_output = csv.writer(fi_out, lineterminator='\n', delimiter = ";")
    i=0
    writer_input.writerow(["name", "description", "input type", "unit"])
    writer_output.writerow(["name", "description", "unit"])
    for inp in wf.inputs:
        for model in models:
            for input in model.inputs :
                if input.name==inp and input.name not in yet_in and input.name not in wf.outputs:
                    writer_input.writerow([inp, input.description.encode("utf-8"), input.inputtype, input.unit.encode("utf-8")])
                    yet_in.append(inp)
                    i=i+1
    
    for out in wf.outputs:
        for model in models:
            for output in model.outputs :
                if output.name==out and output.name not in yet_out:
                    writer_output.writerow([out, output.description.encode("utf-8"), output.unit.encode("utf-8")])
                    yet_out.append(out)
                    i=i+1
  
    
if __name__=='__main__':
    testXmlwf()
