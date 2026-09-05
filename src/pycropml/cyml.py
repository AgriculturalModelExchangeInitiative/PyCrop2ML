# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 22:59:23 2019

@author: midingoy
"""
import os
from pathlib import Path
from pycropml.transpiler.main import Main
from pycropml import render_cyml, nameconvention
from pycropml.pparse import model_parser
from pycropml.writeTest import WriteTest
from pycropml.topology import Topology
from pycropml.code2nbk import Model2Nb
from pycropml.transpiler.source_registry import SOURCES, load_source_adapter
from pycropml.transpiler.target_registry import get_target, load_target_callable

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


def prefix(model):
    pref = model.modelid.split(".")[0]
    return pref


def transpile_package(package, language):
    """ translate from crop2ml package"""
    target = get_target(language)
    if target.extension is None:
        raise ValueError(f"Target {language!r} does not define a file extension")
    sourcef = package
    pkg = Path(package)
    namep = pkg.name

    models = model_parser(pkg)  # parse xml files and create python model object
    output = pkg / "src"
    dir_test = pkg / "test"
    dir_doc = pkg / "doc"

    # Generate packages if the directories does not exists.
    output.mkdir(exist_ok=True)
    dir_test.mkdir(exist_ok=True)
    dir_doc.mkdir(exist_ok=True)

    dir_images = dir_doc / 'images'
    dir_images.mkdir(exist_ok=True)


    m2p = render_cyml.Model2Package(models, dir=output)
    m2p.generate_package()  # generate cyml models in "pyx" directory
    tg_rep1 = output / language  # target language models  directory in output
    dir_test_lang = dir_test / language
    
    tg_rep1.mkdir(exist_ok=True)

    namep_ = namep.replace("-", "_")
    tg_rep = tg_rep1 / namep_
    tg_rep.mkdir(exist_ok=True)

    dir_test_lang.mkdir(exist_ok=True)

    m2p.write_tests()

    # generate cyml functions
    cyml_rep = output / 'pyx'  # cyml model directory in output

    # create topology of composite model
    T = Topology(namep, package)
    mc_name = T.model.name

    # Record VPZ
    # if language == "record":
    # vpz = Crop2ML_Vpz(T)
    # print(vpz.create())

    # domain class
    domain_class_factory = load_target_callable(language, "domain_class_factory")
    if domain_class_factory:
        domain_class_factory([T.model], tg_rep, mc_name)
    # wrapper
    wrapper_factory = load_target_callable(language, "wrapper_factory")
    if wrapper_factory:
        wrapper_factory(T.model, tg_rep, mc_name)

    # Transform model unit to languages and platforms
    for k, file in enumerate(p for p in cyml_rep.iterdir() if p.is_file()):
        with file.open('r') as fi:
            source = fi.read()
        name = file.stem
        for model in models:  # in the case we haven't the same order
            if name.lower() == model.name.lower() and prefix(model) != "function":
                test = Main(file, language, model, T.model.name)
                test.parse()
                test.to_ast(source)
                code = test.to_source()
                filename = tg_rep / f"{nameconvention.signature(model, target.extension)}.{target.extension}"
                with filename.open("wb") as tg_file:
                    tg_file.write(code.encode('utf-8'))
                if target.generate_notebooks:
                    Model2Nb(model, code, name, dir_test_lang).generate_nb(language, tg_rep, namep, mc_name)
                    # code2nbk.generate_notebook(code, name, dir_nb_lang)

    # Create Cyml Composite model
    T_pyx = T.algo2cyml(dir_images)
    fileT = cyml_rep / f"{mc_name}Component.pyx"
    with fileT.open("wb") as tg_file:
        tg_file.write(T_pyx.encode('utf-8'))

    filename = tg_rep / f"{mc_name}Component.{target.extension}"
    code = T.compotranslate(language).encode('utf-8')
    if code:
        with filename.open("wb") as tg_file:
            tg_file.write(code)

    # Create a platform-specific simulation when the target provides one.
    simulation_class = load_target_callable(language, "simulation_class")
    if simulation_class:
        simulation = simulation_class(T.model, package_name=namep)
        simulation.generate()
        code = ''.join(simulation.result)
        filename = tg_rep / "simulation.py"
        initfile = tg_rep / "__init__.py"
        with filename.open("wb") as tg_file:
            tg_file.write(code.encode("utf-8"))
        with initfile.open("wb") as tg_file:
            tg_file.write("".encode("utf-8"))

        setup = simulation_class(T.model, package_name=namep)
        #setup.generate_setup()
        setup.generate_pyproject()
        code = ''.join(setup.result)
        setupfile = tg_rep1 / "pyproject.toml"
        with setupfile.open("wb") as tg_file:
            tg_file.write(code.encode("utf-8"))

    status = 0
    return status


def transpile_component(component, package, language):
    """
    Transform a framework model component to Crop2ML/CyML

    Args:
        component (path): a Crop2ML folder containing a repository of a framework model component
        language (str): a language or framework

    Returns:
        package: Crop2ML package containing xml files and 
    """

    adapter = load_source_adapter(language)
    adapter(component, package)

    return 0
