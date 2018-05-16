# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 00:53:52 2018

@author: midingoy
"""


import os
from path import Path
from jinja2 import Environment, FileSystemLoader
import pycropml
from test import test1	
from flask import Flask,  url_for

#PATH = os.path.dirname(os.path.abspath("./hello.py"))
PATH = Path.getcwd()/'doc'/'model'
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)
	
def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


def create_index_html():
    fname = "output.html"
    models = test1.example()
    #z = url_for('static', filename='mon_style.css')
	
    context = {
        'titre' : "MODELS", 
		'mots' : models,
		
    }
    #
    with open(fname, 'w') as f:
        html = render_template('accueil.html', context)
        f.write(html.encode('utf-8'))

def main():
    create_index_html()

if __name__ == "__main__":
    main()
	
	