class Algorithm(object):
    """ Algorithm """
 
    def __init__(self, language, development, platform, filename=None):
        self.language = language 
        self.platform = platform
        self.filename = filename
        self.development = development