
import os
def walk(path, ext=None):
    list_of_files = {}
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            if ext:
                if filename.endswith('.%s'%ext): 
                    list_of_files[filename] = os.sep.join([dirpath, filename])
            else:
                list_of_files[filename] = os.sep.join([dirpath, filename])
    return list_of_files