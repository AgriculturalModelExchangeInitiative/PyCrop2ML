
class Description(object):
    """ Model Unit Description.

    A description is defined by:
      - Title
      - Authors
      - Institution
      - Reference
      - Abstract
    """

    def __init__(self):
        self.Title = ''
        self.Authors = ''
        self.Institution = ''
        self.Reference = ''
        self.ShortDescription = ''
        self.ExtendedDescription = ''
