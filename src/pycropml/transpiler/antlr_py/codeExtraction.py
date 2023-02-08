from os import listdir, makedirs
import os

"""

def record_file(package, fil , text):
    #print(text)
    makedirs('dssat', exist_ok = True)
    name = package +  '/temp/' + fil
    file_for = open(name , 'w' , encoding = 'utf8')
    file_for.write( text )
    file_for.close()

def extraction(package,files, balise_start, balise_end, ignore_start=None, ignore_end=None):
    counter = 0
    res = {}
    for fil_ in files:
        res[fil_] = []
        if fil_.endswith('.for') or fil_.endswith('.f90'):
            fil = os.path.join(package, fil_)
            container = ''
            start = False
            with open(fil, 'r' , encoding = 'utf8') as file_:
                for line in file_:
                    if balise_end in line:
                        start = False
                        counter += 1
                        res[fil].append(container)
                        #record_file(package,fil_,container)
                        container = ''
                    elif ignore_start and ignore_start in line:
                        start = False
                    elif ignore_end and ignore_end in line:
                        start = True  
                    elif start == True:
                        container += line
                    elif balise_start in line:
                        start = True
    return res
"""
def extraction(text_, balise_start, balise_end, ignore_start=None, ignore_end=None):
    res = []
    container = ''
    start = False
    text = text_.split("\n")
    for line in text:
        if balise_end in line:
            res.append(container)
            container = ''
            start = False
            continue
            #break
            #start = False
            #record_file(package,fil_,container)
            #container = ''
        elif ignore_start and ignore_start in line:
            start = False
        elif ignore_end and ignore_end in line:
            start = True  
        elif start == True:
            container += line + "\n"
        elif balise_start in line:
            start = True
    return res


def remove(text_, ignore_start, ignore_end):
    container = ''
    start = True
    text = text_.split("\n")
    for line in text:
        if ignore_start and ignore_start in line:
            start = False
        elif ignore_end and ignore_end in line:
            start = True  
        elif start == True:
            container += line + "\n"
    return container