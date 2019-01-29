from path import Path

from pycropml import pparse, render_python
from pycropml import composition
from pycropml.xml2wf import XmlToWf

# Fix pb in local path
cwd = Path.getcwd()
if (cwd/'data').isdir():
    data = cwd/'data'
elif (cwd/'test'/'data').isdir():
    data = cwd/'test'/'data'
else:
    print('Data directory not found')



def testXmlwf():
    
    #model_units = data.glob('unit*.xml')
    
    models = pparse.model_parser(data)
    
    # translate cropml model units to python functions and openalea in python_model repository
    render_python.Model2Package(models, dir='.',pkg_name="Phenology").run()
    
    # repository of python models generated  with wralea
    dir = cwd/'python_model'
    
    rep_composite= data/'crop2ml'
    # composite file
    #print(rep_composite.glob("composition*.xml")[0])
    compositionFile = rep_composite.glob("composition*.xml")[0]
    
    xmlwf,= composition.model_parser(compositionFile)

    XmlToWf(xmlwf, dir, "Phenology").run()
    
if __name__=='__main__':
    testXmlwf()
