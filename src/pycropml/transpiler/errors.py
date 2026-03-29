from __future__ import absolute_import
import os
from pycropml.transpiler.helpers import serialize_type
from pycropml.transpiler.logger import get_logger


logger = get_logger('transpiler.errors')


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

class PseudoCythonParseError(PseudoError):
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
            code_block = format_code_block(code, location)
            message = '%s%s%s:\n%s\n%s^' % (
                ('wrong type %s\n' % serialize_type(wrong_type) if wrong_type else ''),
                data,
                (' on line %d column %d' % location) if location else '',
                code_block,
                (tab_aware(location[1], code_block) if location else ''))
            logger.error(message)
            return exception(message, **options)
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


def _code_lines(code):
    """Normalize code payload to list of lines (supports list/tuple/string)."""
    if code is None:
        return []
    if isinstance(code, (list, tuple)):
        lines = [str(line) for line in code]
    else:
        lines = str(code).splitlines()

    # Cython locations are typically 1-based on meaningful lines; strip a leading
    # empty line introduced by triple-quoted snippets to keep pointers aligned.
    if lines and lines[0] == '':
        lines = lines[1:]
    return lines


def _ansi_enabled():
    if os.environ.get('NO_COLOR'):
        return False
    if os.environ.get('PYCROPML_COLOR') in ('1', 'true', 'TRUE', 'yes', 'YES'):
        return True
    if os.environ.get('TERM') == 'dumb':
        return False
    return False


def _color(text, style):
    if not _ansi_enabled():
        return text
    styles = {
        'bold_red': '\x1b[1;31m',
        'red': '\x1b[31m',
        'yellow': '\x1b[33m',
        'dim': '\x1b[2m',
        'reset': '\x1b[0m',
    }
    prefix = styles.get(style, '')
    reset = styles['reset'] if prefix else ''
    return '%s%s%s' % (prefix, text, reset)


def format_code_block(code, location=None, radius=2):
    """Format code and highlight failing line when location is available."""
    lines = _code_lines(code)
    if not lines:
        return ''

    if not location or len(location) < 2:
        return '\n'.join(lines)

    line_no, col_no = location[0], location[1]
    if not isinstance(line_no, int) or line_no < 1 or line_no > len(lines):
        return '\n'.join(lines)

    start = max(1, line_no - radius)
    end = min(len(lines), line_no + radius)
    out = []
    for idx in range(start, end + 1):
        is_target = idx == line_no
        marker = _color('>>', 'bold_red') if is_target else _color('  ', 'dim')
        line_label = _color('%4d' % idx, 'yellow') if is_target else '%4d' % idx
        out.append('%s %s: %s' % (marker, line_label, lines[idx - 1]))
        if is_target:
            # col_no is 0-based (Cython convention); tab_aware expects 1-based, so +1.
            # An extra +1 compensates for code prefix (9 chars) vs pointer prefix (9 chars).
            pointer_indent = tab_aware(col_no + 1, lines[idx - 1])
            out.append('       %s %s%s' % (_color('|', 'dim'), pointer_indent, _color('^', 'red')))
    return '\n'.join(out)


def tab_aware(location, code):
    '''
    if tabs in beginning of code, add tabs for them, otherwise spaces
    '''
    if not code:
        return ''
    if location is None:
        return ''
    # location is 1-based column in messages; convert to 0-based for slicing.
    index = max(0, int(location) - 1)
    return ''.join(' ' if c != '\t' else '\t' for c in code[:index])