# coding: utf8
from pycropml.transpiler.codeGenerator import CodeGenerator

class DocGenerator(CodeGenerator):
    """Generate doc in different target language
        - desccription of the code
        - Inputs details
        - Outputs details        
    """
    def __init__(self, model=None, tag='#'):
        CodeGenerator.__init__(self)
        self.model=model
        self.indent_with=' '*4 
        self.tag = tag
        self.inputs_doc = self.comment(self.doc(model.inputs, "inputs"))
        self.outputs_doc = self.comment(self.doc(model.outputs, "outputs"))
        self.desc = self.comment(self.generate_desc(model))
        
    def comment(self,doc):
        list_com = [self.indent_with + self.tag +x for x in doc.split('\n')]
        com = '\n'.join(list_com)
        return com
    
    def doc(self, x, name):
        doc ="- %s:" %name
        
        for z in x:
            doc+=('''
            - name: %s'''%z.name)
            for j, k in z.__dict__['_attributes'].items() :
                if j!="name":
                    doc+=('''
                          - %s : %s'''%(j,k))
        return doc
    
    def generate_desc(self,model):
        desc = model.description
        _doc="- Description:"           
        _doc += """
            - Model Name: %s
            - Author: %s
            - Reference: %s
            - Institution: %s
            - Abstract: %s""" %(desc.Title, desc.Authors, desc.Reference, desc.Institution, desc.Abstract)
        
        return _doc
    

        
