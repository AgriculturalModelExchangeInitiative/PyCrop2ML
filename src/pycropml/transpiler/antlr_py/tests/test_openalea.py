
import re
from weakref import ref

pattern_attr_val = r"(\s*(?P<attribute>\w+)\s*:\s*(?P<value>[\w+\s:,ï\[\]\\_\./\'-]*))"

def attval(pat_name, string):  
    #print( string)
    att = re.findall(pat_name, string)
    #print("hhkkkk", att)
    if att:
        lines = att[0][0].split('\n')[0:-1]
        dic = {}
        for line in lines:
            attribute = re.search(pattern_attr_val, line).group("attribute")
            print(attribute)
            value = re.search(pattern_attr_val, line, re.ASCII).group("value").replace('\r', "")
            dic[attribute] = str(value)
        return dic
    else: return

def test_package():
    

    from openalea.core.pkgmanager import PackageManager
    wralea_dir = "C:/Users/midingoy/Documents/crop2mlcatalog/SQ_Energy_Balance/src/openalea/SQ_Energy_Balance"

    pm = PackageManager()
    pm.init(wralea_dir, True)
    pkg =  pm.get_composite_nodes()[0]
    doc = pkg.description
    docs = [x.strip() for x in doc.strip().split('\n')]
    d = "\n".join(docs[1:])
    xx = docs[1:]
    pat_description = r'(^(Author:|Reference:|Institution:|Abstract:))'
    res = []
    i = 0
    while True:
        if re.match(pat_description, xx[i]):
            res.append(xx[i])
        else:
            if res: res[-1] = res[-1]+"\n"+xx[i]
        i = i+1
        if i==len(xx): break
    
    authors = res[0].split("Author:")[-1]
    reference = res[1].split("Reference:")[-1]
    institution = res[2].split("Institution:")[-1]
    abstract = res[3].split("Abstract:")[-1]
    
    print(authors,'\n', reference,'\n', institution, '\n',abstract)
        
            
    

    
    """description = attval(pat_description, d)   
    #print(description)
    
   docs = [x.strip() for x in doc.strip().split('\n')]
    ls = {"Author":'', "Reference":'', "Institution":'', "Abstract":''}
    for d in docs[1:]:
        
        
        
    #print(docs, len(docs))
    if docs[3].startswith('Institution'):
                institution = docs[3].split(':')[1]
                institution = institution.strip()
                #print(institution)
    else: print("ooooooo")"""

test_package()