# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 22:59:23 2019

@author: midingoy
"""
from pathlib import Path
from pycropml.transpiler.main import Main
from pycropml.transpiler.source_registry import SOURCES, get_source
from pycropml.transpiler.target_registry import get_target
from pycropml.transpiler.target_pipeline import TargetPipeline

cymltx_languages = list(SOURCES)

def transpile_file(source, language):
    target = get_target(language)
    if target.extension is None:
        raise ValueError(f"Target {language!r} does not define a file extension")
    sourcef = source
    file = Path(sourcef)
    with file.open('r') as fi:
        source = fi.read()
    name = file.stem
    test = Main(file, language)
    test.parse()
    test.to_ast(source)
    code = test.to_source()
    filename = f"{name}.{target.extension}"
    with open(filename, "wb") as tg_file:
        tg_file.write(code.encode('utf-8'))
    return 0


def transpile_package(package, language):
    """Translate a Crop2ML package through the target-generation pipeline."""
    return TargetPipeline(package, language).run()


def transpile_component(component, package, language):
    """
    Transform a framework model component to Crop2ML/CyML

    Args:
        component (path): a Crop2ML folder containing a repository of a framework model component
        language (str): a language or framework

    Returns:
        package: Crop2ML package containing xml files and 
    """

    source = get_source(language)
    source.convert(component, package)

    return 0
