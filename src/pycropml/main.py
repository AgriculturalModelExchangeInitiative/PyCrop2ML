# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 22:59:23 2019

@author: pradal
"""
# coding: utf8

from __future__ import absolute_import
from __future__ import print_function

from optparse import OptionParser

from pathlib import Path

from pycropml.cyml import transpile_file, transpile_package, transpile_component

from pycropml.transpiler.logger import configure_logging, get_logger
from pycropml.transpiler.source_registry import SOURCES
from pycropml.transpiler.target_registry import TARGETS


def _validate_platforms(parser, requested, supported, kind):
    """Validate and deduplicate source or target names from the command line."""
    unknown = [name for name in requested if name not in supported]
    if unknown:
        available = ", ".join(sorted(supported))
        parser.error(
            f"{unknown[0]} is not a supported {kind}. "
            f"Supported {kind}s: {available}"
        )
    return list(dict.fromkeys(requested))


def main():
    targets = ", ".join(TARGETS)
    sources = ", ".join(SOURCES)
    usage = f"""Usage:
    %prog -f FILE TARGET [TARGET ...]
    %prog -p PACKAGE TARGET [TARGET ...]
    %prog -c COMPONENT OUTPUT SOURCE [SOURCE ...]
    %prog PACKAGE TARGET [TARGET ...]

Translate a CyML file or Crop2ML package to a target, or convert an existing
platform component into a Crop2ML package.

Available targets: {targets}
Available sources: {sources}

"""

    parser = OptionParser(usage=usage)

    parser.add_option("-f", "--file", dest="file", metavar="FILE",
                      help="cyml source code FILE to transpile")
    parser.add_option("-p", "--package", dest="package",
                      help="package directory containing a crop2ml directory with algorithms.")
    parser.add_option("-c", "--component", dest="component",
                      help="framework model component directory")
    parser.add_option("-l", "--languages", dest="languages", action="append",
                      metavar="NAME",
                      help="source or target name; may be repeated")
    parser.add_option("--log-level", dest="log_level", default="WARNING",
                      help="Logging level: DEBUG, INFO, WARNING, ERROR, CRITICAL (default: WARNING)")

    (opts, args) = parser.parse_args()
    configure_logging(opts.log_level)
    cli_logger = get_logger('cli')
    cli_logger.debug('CLI started with args=%s options=%s', args, opts)

    selected_modes = [opts.file, opts.package, opts.component]
    if sum(value is not None for value in selected_modes) > 1:
        parser.error("use only one of --file, --package, or --component")

    positional = list(args)
    if opts.file is not None:
        sourcef = opts.file
    elif opts.package is not None:
        sourcef = opts.package
    elif opts.component is not None:
        sourcef = opts.component
    else:
        if not positional:
            parser.print_usage()
            return
        sourcef = positional.pop(0)

    sourcef = Path(sourcef)
    if not sourcef.exists():
        if opts.component is not None:
            source_kind = "Component directory"
        elif opts.file is not None:
            source_kind = "CyML file"
        else:
            source_kind = "Package path"
        parser.error(f"{source_kind} does not exist: {sourcef}")

    if opts.component is not None:
        if not positional:
            parser.error("an output package is required with --component")
        newpackage = positional.pop(0)
        supported = SOURCES
        kind = "source"
    else:
        newpackage = None
        supported = TARGETS
        kind = "target"

    requested = list(opts.languages or []) + positional
    langs = _validate_platforms(parser, requested, supported, kind)

    if not langs:
        parser.error(f"No {kind} has been specified")

    if opts.component is not None:
        for language in langs:
            cli_logger.info('Converting %s source component %s', language, sourcef)
            transpile_component(sourcef, newpackage, language)
    elif sourcef.is_file():
        # translate from cyml code
        if sourcef.suffix.lower() != ".pyx":
            parser.error("Source code %s is not a CyML file (.pyx extension)" % sourcef)

        for language in langs:
            cli_logger.info('Transpiling file %s to %s', sourcef, language)
            transpile_file(sourcef, language)
    else:
        for language in langs:
            cli_logger.info('Transpiling package %s to %s', sourcef, language)
            transpile_package(sourcef, language)


if __name__ == '__main__':
    main()
