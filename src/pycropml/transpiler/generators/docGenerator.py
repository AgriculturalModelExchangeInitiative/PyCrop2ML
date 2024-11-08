# coding: utf-8
from pycropml.transpiler.codeGenerator import CodeGenerator

class DocGenerator(CodeGenerator):
    """Generate doc in different target language
        - desccription of the code
        - Inputs details
        - Outputs details        
    """
    def __init__(self, model=None, tag='#', indent_with=' '*4 ):
        CodeGenerator.__init__(self)
        self.model=model
        self.indent_with=indent_with 
        self.tag = tag
        if self.model:
            self.inputs_doc = self.comment(self.doc(self.model.inputs, "inputs"))
            self.outputs_doc = self.comment(self.doc(self.model.outputs, "outputs"))
            self.header = self.comment(self.generate_header(self.model))
            self.desc = self.comment(self.generate_desc(self.model))
        
    def comment(self,doc):
        list_com = [self.indent_with + self.tag +x for x in doc.split('\n')]
        com = '\n'.join(list_com)
        return com
    
    def doc(self, x, name):
        doc ="- %s:" %name
        
        for z in x:
            doc+=('''
            * name: %s'''%z.name)
            for j, k in z.__dict__['_attributes'].items() :
                if j!="name":
                    doc+=('''
                          ** %s : %s'''%(j,k))
        return doc
    
    def generate_desc(self,model):
        desc = model.description
        _doc = "- Description:"           
        _doc += """
            * Title: %s
            * Authors: %s
            * Reference: %s
            * Institution: %s
            * ExtendedDescription: %s
            * ShortDescription: %s""" %(desc.Title, desc.Authors, desc.Reference, desc.Institution, desc.ExtendedDescription, desc.ShortDescription)
        
        return _doc
    
    def generate_header(self, model):
        _doc = "- Name: %s -Version: %s, -Time step: %s"%(model.name, model.version, model.timestep)
        return _doc
    

        
