# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 22:59:23 2019

@author: pradal
"""
# coding: utf8
from __future__ import absolute_import
from __future__ import print_function

import sys
import os

from optparse import OptionParser

from path import Path

from pycropml.cyml import transpile_file, transpile_package, transpile_component

from pycropml.transpiler.main import languages


def main():
    usage = """Usage: %prog [options] package language1 [languages]

cyml transpiler translate a cyml source code or a Crop2ML package with algo in cyml
language to target language.

Example
    cyml <source_code.pyx or pkg> <target_language>

    * target language must be:
        py for python
        cs for csharp
        f90 for fortran
        java for java
        cpp for C++
        r for r
    * target platforms :
        apsim, bioma, dssat, openalea, record, simplace, stics

"""
    # TODO
    todo = """
    * target language must be:
        py for python
        cs for csharp
        cpp for c++
        f90 for fortran
        java  for java
        r for R
        simplace for simplace
        sirius for sirius
"""

    parser = OptionParser(usage=usage)

    parser.add_option("-f", "--file", dest="file", metavar="FILE",
                      help="cyml source code FILE to transpile")
    parser.add_option("-p", "--package", dest="package",
                      help="package directory containing a crop2ml directory with algorithms.")
    parser.add_option("-c", "--component", dest="component",
                      help="framework model component directory")
    parser.add_option("-l", "--languages", dest="languages", action="append",
                      choices=languages,
                      help="Target languages : " + ','.join(languages))

    (opts, args) = parser.parse_args()

    sourcef = None
    pyx_filename = None
    package = None
    component = None
    newpackage = None
    langs = []

    if len(parser.option_list) + len(args) < 2:
        parser.error("incorrect number of arguments")

    if opts.file:
        sourcef = pyx_filename = opts.file
    elif opts.package:
        sourcef = package = opts.package
    elif opts.component:
        sourcef = component = opts.component
    else:
        if len(args) == 0:
            parser.print_usage()
            return
        else:
            sourcef = args[0]

    sourcef = Path(sourcef)
    if not sourcef.exists():
        parser.error("Package or file does not exists")

    if opts.languages:
        langs = opts.languages
    else:
        if opts.component:
            newpackage = args[0]
            args = args[1:]
        langs = [a for a in args if a in languages]

    fail = False
    for arg in args:
        if arg == sourcef:
            continue
        if arg not in languages:
            parser.error("%s is not a supported language" % arg)
            fail = True

    if fail:
        return

    if not langs:
        parser.error("No language has been specified")
        print(parser.usage)
        return

    if pyx_filename or len(sourcef.split(".")) == 2:
        # translate from cyml code
        if sourcef.split(".")[1] != "pyx":
            parser.error("Source code %s is not a Cyml file (.pyx estension) " % (str(sourcef)))
            return

        for language in langs:
            status = transpile_file(sourcef, language)
    elif package:
        for language in langs:
            status = transpile_package(sourcef, language)
    else:
        for language in langs:
            status = transpile_component(sourcef, newpackage, language)


if __name__ == '__main__':
    main()
