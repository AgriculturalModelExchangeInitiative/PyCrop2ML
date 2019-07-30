# {# pkglts, base

from . import version
from IPython.display import display
from pycropml.interface import design
display(design.d)

display()
# {#pkglts,
__import__('pkg_resources').declare_namespace(__name__)
# #}
__version__ = version.__version__

# #}
