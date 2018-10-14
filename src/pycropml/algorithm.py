class Algorithm(object):
    """ Algorithm """
 
    def __init__(self, language, development, platform, function=None, filename=None):
        self.language = language 
        self.platform = platform
        self.function = function
        self.filename = filename
        self.development = development