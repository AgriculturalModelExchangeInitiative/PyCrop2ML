class Function(object):
    """ Function """
 
    def __init__(self,name, language, filename, type, description):
        self.language = language 
        self.name = name
        self.filename = filename
        self.type=type
        self.description=description