from __future__ import absolute_import
from pycropml.transpiler.helpers import serialize_type
class PseudoError(Exception):
    def __init__(self, message, suggestions=None, right=None, wrong=None):
        super(PseudoError, self).__init__(message)

        self.suggestions = suggestions
        self.right = right
        self.wrong = wrong

class PseudoCythonNotTranslatableError(PseudoError):
    pass

class PseudoCythonTypeCheckError(PseudoError):
    pass

def cant_infer_error(name, line):
    return PseudoCythonTypeCheckError("pseudo-cython can't infer the types for %s:\n%s\n" % (name, line),
            suggestions='you need to either:\n' +
                        '    ensure %s is reachable from a call in your top scope\n' % name +
                        '    e.g. a(..) in top scope, b(..) in a body, %s() in b body\n' % name +
                        '    or provide type hints (see https://docs.python.org/3/library/typing.html)'
                        )

def beautiful_error(exception):
    def f(function):
        def decorated(data, location=None, code=None, wrong_type=None, **options):
            return exception('%s%s%s:\n%s\n%s^' % (
                ('wrong type %s\n' % serialize_type(wrong_type) if wrong_type else ''),
                data,
                (' on line %d column %d' % location) if location else '',
                code or '',
                (tab_aware(location[1], code) if location else '')),
                **options)
        return decorated
    return f

def notInmplemented(exception):
    def f(function):
        def decorated(data, location):
            return exception("%s is not implemented at %s"%(data, location))
        return decorated
    return f

@notInmplemented(PseudoCythonTypeCheckError)
def isNotImplemented(data, location):
    pass

@beautiful_error(PseudoCythonTypeCheckError)
def type_check_error(data, location=None, code=None, wrong_type=None, **options):
    pass

@beautiful_error(PseudoCythonNotTranslatableError)
def translation_error(data, location=None, code=None, wrong_type=None, **options):
    pass

def tab_aware(location, code):
    '''
    if tabs in beginning of code, add tabs for them, otherwise spaces
    '''
    return ''.join(' ' if c != '\t' else '\t' for c in code[:location])