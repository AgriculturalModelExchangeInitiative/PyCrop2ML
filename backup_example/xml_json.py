import json
import xmltodict
from path import Path


def convert(xml_file, xml_attribs=True):
    with open(xml_file, "rb") as f:  
        d = xmltodict.parse(f, xml_attribs=xml_attribs)
        return json.dumps(d, indent=2)



if __name__ == '__main__':		
	# Fix pb in tlocal path
	cwd = Path.getcwd()
	if (cwd/'data').isdir():
		data = cwd/'data'
	elif (cwd/'test'/'data').isdir():
		data = cwd/'test'/'data'
	else:
		print('Data directory not found')

	xmls = data.glob('*.xml')
	fn = data.glob('Example*.xml')[0]
 		
	json_file=convert(fn)
	with open(cwd/"jsonfile.json","w") as f:
		f.write(json_file)
	
