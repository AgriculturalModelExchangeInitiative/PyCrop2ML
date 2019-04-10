# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 22:59:23 2019

@author: pradal
"""
# coding: utf8
from path import Path
import os.path
import sys

from cyml import transpile_file, transpile_package

from pycropml.transpiler.main import languages

def main():


    usage = """
        cyml transpiler translate a cyml source code or a Crop2ML package with algo in cyml
        language to target language .
    Example
       cyml <source_code.pyx or pkg> <target_language>

    * target language must be:
        py for python
        cs for csharp
        cpp for c++
        f90 for fortran
        java  for java
        r for R

"""

    if len(sys.argv)!=3:
        print(usage)
        return

    sourcef = sys.argv[1]
    language = sys.argv[2]

    if language not in languages:
        print(usage)
        return

    if len(sourcef.split(".")) == 2:
        # translate from cyml code
        if sourcef.split(".")[1] != "pyx":
            print(usage)
            return

        status = transpile_file(sourcef, language)

    else:
        status = transpile_package(sourcef, language)


if __name__ == '__main__':
    main()
