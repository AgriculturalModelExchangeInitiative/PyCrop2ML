"""from pycropml import composition
from pycropml.pparse import model_parser
from path import Path
import networkx as nx
from collections import defaultdict
from IPython.display import Image, display
from networkx.drawing.nx_pydot import to_pydot
from pycropml.render_cyml import signature"""

from pkg_resources import iter_entry_points
from path import Path
import os
import sys
import time
import imp
DEBUG = False
SEARCH_OUTSIDE_ENTRY_POINTS = True


class UnknownNodeError (Exception):

    def __init__(self, name):
        Exception.__init__(self)
        self.message = "Cannot find node : %s" % (name)

    def __str__(self):
        return self.message

def get_default_home_dir():
    """ Return the home directory (valid on linux and windows) """

    if sys.platform != 'win32':
        return os.path.expanduser('~')

    def valid(path):
        if path and os.path.isdir(path):
            return True
        return False

    def env(name):
        return os.environ.get(name, '')

    homeDir = env('USERPROFILE')
    if not valid(homeDir):
        homeDir = env('HOME')
    elif not valid(homeDir):
        homeDir = '%s%s' % (env('HOMEDRIVE'), env('HOMEPATH'))
    elif not valid(homeDir):
        homeDir = env('SYSTEMDRIVE')
    elif not valid(homeDir):
        homeDir = 'C:\\'

    if homeDir and (not homeDir.endswith('\\')):
        homeDir += '\\'

    return homeDir


def get_openalea_home_dir(name='.pycrop2ml'):
    """
    Return the crop2ml home directory
    If it doesn't exist, create it
    """

    home = get_default_home_dir()

    aleahome = os.path.join(home, name)
    if(not os.path.exists(aleahome)):
        os.mkdir(aleahome)

    return aleahome

def get_userpkg_dir(name='user_pkg'):
    """
    Get user package directory (the place where are the
    wralea.py files).
    If it doesn't exist, create it
    """
    aleahome = get_openalea_home_dir()
    wraleahome = os.path.join(aleahome, name)
    if(not os.path.exists(wraleahome)):
        os.mkdir(wraleahome)

    return wraleahome


def lower(item):
    try:
        item = item.lower()
    finally:
        return item


def is_protected(item):
    """ Return true the item is protected """

    try:
        return item.startswith('#')
    except:
        return False


def protected(item):
    " Return corresponding protected name for item "
    return "#" + item


class PackageDict(dict):
    """
    Dictionnary with case insensitive key
    This object is able to handle protected entry begining with an '#'
    """

    def __init__(self, *args):
        self.nb_public = None
        dict.__init__(self, *args)

    def __getitem__(self, item):
        item = lower(item)

        try:
            return dict.__getitem__(self, item)
        except KeyError:
            # Try to return protected entry
            return dict.__getitem__(self, protected(item))

    def __setitem__(self, item, y):

        # Update nb public key
        if (self.nb_public and
           not self.has_key(item) and
           not is_protected(item)):
            self.nb_public += 1

        return dict.__setitem__(self, lower(item), y)

    def __contains__(self, key):
        return self.has_key(key)

    def has_key(self, key):

        key = lower(key)
        if (dict.has_key(self, key)):
            return True
        else:
            return dict.has_key(self, protected(key))

    def __delitem__(self, key):

        # Update nb public key
        if (self.nb_public and not is_protected(key)):
            self.nb_public -= 1

        return dict.__delitem__(self, lower(key))

    def get(self, key, default=None):
        return dict.get(self, lower(key), default)

    def iter_public_values(self):
        """ Iterate througth dictionnary value (remove protected value)  """

        for k, v in self.items():
            if (not is_protected(k)):
                yield v

    def nb_public_values(self):
        """ Return the number of unprotected values """

        if (self.nb_public is None):
            l = lambda x: not is_protected(x)
            ks = filter(l, self.iterkeys())
            self.nb_public = len(ks)

        return self.nb_public


class PseudoGroup(PackageDict):
    """ Data structure used to separate dotted naming (packages, category) """

    sep = '.'  # Separator
    mimetype = "pycrop2ml/package"

    def __init__(self, name):
        """ Name is the pseudo package name """

        PackageDict.__init__(self)
        self.name = name
        self.item = None

    def new(self, name):
        """todo"""
        return PseudoGroup(name)

    def get_id(self):
        """todo"""
        return self.name

    def get_tip(self):
        """todo"""
        return self.name

    def add_name(self, name, value):
        """ Add a value in the structure with the key name_tuple """

        if(not name):
            # if value is a dict we include sub nodes
            self.item = value
            try:
                for k, v in value.iteritems():
                    self[k] = v
            except:
                try:
                    self[str(id(value))] = value
                except Exception as e:
                    print(e)
                    pass
            return

        splitted = name.split(self.sep, 1)
        key = splitted[0]

        if(len(splitted) > 1):
            remain = splitted[1]
        else:
            remain = None

        # Create sub dict if necessary
        if not dict.has_key(self, key.lower()):
            self[key] = self.new(key)

        try:
            self[key].add_name(remain, value)
        except Exception as e:
            print ('Package %s[%s]' % (self.name, name))
            print (e)
            try:
                self[str(id(key))].add_name(remain, value)
            except Exception as e:
                print ('Unable to find these nodes: %s' % value)
                print (e)
                pass


class Package(PackageDict):
    """
    A Package is a dictionnary of node factory.
    Each node factory is able to generate node and their widgets.
    Meta informations are associated with a package.
    """

    # type information for drag and drop.
    mimetype = "pycrop2ml/package"

    def __init__(self, name, metainfo, path=None):
        """
        Create a Package
        :param name: a unique string used as a unique identifier for the package
        :param path: path where the package lies (a directory or a full wralea path)
        :param metainfo: a dictionnary for metainformation.
        Attended keys for the metainfo parameters are:
            - license: a string ex GPL, LGPL, Cecill, Cecill-C
            - version: a string
            - authors: a string
            - institutes: a string
            - url: a string
            - description: a string for the package description
            - publication: optional string for publications
        """

        PackageDict.__init__(self)

        self.name = name
        self.metainfo = metainfo

        # package directory

        if (not path):
            # package directory
            import inspect
            # get the path of the file which call this function
            call_path = os.path.abspath(inspect.stack()[1][1])
            self.path = os.path.dirname(call_path)
            self.wralea_path = call_path

        # wralea.py path is specified
        else:
            if (not os.path.exists(path)):
                os.mkdir(path)
            if (not os.path.isdir(path)):
                self.path = os.path.dirname(path)
                self.wralea_path = path

            else:
                self.path = path
                self.wralea_path = os.path.join(self.path, "model.py")
                self.crop2ml_path = os.path.join(self.path, "crop2ml")

            #wralea_name = name.replace('.', '_')

    def is_directory(self):
        """
        New style package.
        A package is embeded in a unique directory.
        This directory can not contain more than one package.
        Thus, you can move, copy or delete a package by acting on the directory without ambiguity.
        Return True if the package is embeded in a directory.
        """
        return self.wralea_path.endswith("model.py")

    def is_editable(self):
        """
        A convention (for the GUI) to ensure that the user can modify the package.
        """
        return False

    def get_pkg_files(self):
        """
        Return the list of xml filename of the package.
        The filename are relative to self.path
        """

        #assert self.is_directory()

        ret = []
        for file in os.listdir(self.crop2ml_path):
            src = os.path.join(self.crop2ml_path, file)
            if (not os.path.isfile(src) or
               file.endswith(".pyc") or
               file.endswith(".py") or
               file.startswith(".")):
                continue
            ret.append(file)

        return ret

    def remove_files(self):
        """ Remove pkg files """
        assert False

    def reload(self):
        """ Reload all xml file of the package """

        sources = self.get_pkg_files()

        s = set()  # set of full path name
        for f in sources:
            s.add(os.path.abspath(os.path.join(self.path, f)))
        '''
        for module in sys.modules.values():
            if (not module):
                continue
            try:
                modulefile = os.path.abspath(module.__file__)
                if (modulefile in s):
                    module.oa_invalidate = True
                    reload(module)
                    print ("Reloaded ", module.__name__)
            except:
                pass
        '''
        return s
    def get_crop2ml_path(self):
        """ Return the full path of the wralea.py (if set) """
        return self.crop2ml_path

    def get_id(self):
        """ Return the package id """
        return self.name

    def get_tip(self):
        """ Return the package description """

        str = "<b>Package:</b>%s<br/>\n" % (self.name, )
        try:
            str += "<b>Description : </b>%s<br/>\n" % (self.metainfo['description'].replace('\n', '<br/>'), )
        except:
            pass
        try:
            str += "<b>Authors :</b> %s<br/>\n" % (self.metainfo['authors'],)
        except:
            pass
        try:
            str += "<b>Institutes :</b> %s<br/>\n" % (self.metainfo['institutes'], )
        except:
            pass

        try:
            str += "<b>URL : </b>%s<br/>\n" % (self.metainfo['url'], )
        except:
            pass

        return str

    def get_metainfo(self, key):
        """
        Return a meta information.
        See the standard key in the __init__ function documentation.
        :param key: todo
        """
        return self.metainfo.get(key, "")

    def add_modelunit(self, modelunit):
        """ Add to the package a factory ( node or subgraph ) """


        if (modelunit.name in self):
            raise Exception("modelunit %s already defined. Ignored !" % (modelunit.name, ))

        self[modelunit.name] = modelunit
        modelunit.package = self

        # Check validity
        # oops: this is a hack.
        # When the factory is a data factory that do not reference a file, raise an error.
        # This function return True or raise an error to have a specific diagnostic.
        try:
            modelunit.is_valid()

        except Exception as e:
            modelunit.package = None
            del(self[modelunit.name])
            raise e

        # Add Aliases
        if (modelunit.alias):
            for a in modelunit.alias:
                self[protected(a)] = modelunit

    def update_modelunit(self, old_name, modelunit):
        """ Update factory (change its name) """

        del(self[old_name])
        self.add_modelunit(modelunit)

    def get_names(self):
        """ Return all the factory names in a list """

        return self.keys()

    def get_modelunit(self, modelid):
        """ Return the factory associated with id """

        try:
            modelunit = self[modelid]
        except KeyError:
            raise UnknownNodeError("%s.%s" % (self.name, id))

        return modelunit


class PackageManager():
    def __init__(self):
        self.syspath = sys.path[:]
        self.pkgs = PackageDict()
        self.user_crop2ml_path = set()
        self.sys_crop2ml_path = set()
        self.category = PseudoGroup("")        
        

    def set_sys_crop2ml_path(self):
        """ Define the default composition files search path

        For that, we look for "composition" entry points
        and deprecated_wralea entry point
        if a package is declared as deprecated_wralea,
        the module is not load
        """

        if self.sys_crop2ml_path:
            print("yesyesy")
            return

        self.sys_crop2ml_path = set()

        if DEBUG:
            res = {}
        # Use setuptools entry_point

        if SEARCH_OUTSIDE_ENTRY_POINTS:
            self.add_crop2ml_path(os.path.dirname(__file__), self.sys_crop2ml_path)
            self.add_crop2ml_path(get_userpkg_dir(), self.sys_crop2ml_path)
        if DEBUG:
            return res


    def add_package(self, package):
        """ Add a package to the pkg manager """

        # Test if the package is deprecated

        self[package.get_id()] = package
        self.update_category(package)

    def update_category(self, package):
        """ Update the category dictionary with package contents """

        for nf in iter(package.values()):
            # skip the deprecated name (starting with #)
            if is_protected(nf.name):
                continue

            # empty category
            if not nf.category:
                nf.category = "Unclassified"

            # parse the category
            for c in nf.category.split(","):
                # we work in lower case by convention
                c = c.strip().lower()

                # search for the sub category (split by .)
                try:
                    c_root, c_others = c.split('.', 1)
                except:  # if there is no '.', c_others is empty
                    c_root = c
                    c_others = ''

                if c_root in self.user_category.keywords:
                    # reconstruct the name of the category
                    c_temp = self.user_category.keywords[c_root] + '.' + c_others.title()
                    self.category.add_name(c_temp, nf)
                else:
                    self.category.add_name(c.title(), nf)


    def init(self, dirname=None, verbose=True):
        """ Initialize package manager

        If dirname is None, find composition files on the system
        else load directory
        """

        # output redirection
        if(not verbose):
            sysout = sys.stdout
            sys.stdout = open(os.devnull, 'w')

        try:

            if (not dirname):
                self.find_and_register_packages()
            else:
                self.load_directory(dirname)

        finally:

            if(not verbose):
                sys.stdout.close()
                sys.stdout = sysout    

    def reload(self, pkg=None):
        """ Reload one or all packages.
        If the package `pkg` is None reloa all the packages.
        Else reload only `pkg`.
        """

        if(not pkg):
            self.clear()
            self.find_and_register_packages(no_cache=True)
            for p in self.pkgs.values():
                p.reload()
        else:
            pkg.reload()
            self.load_directory(pkg.path)
            #self.notify_listeners("update")
            
    def clear(self):
        """ Remove all packages """

        self.user_crop2ml_path = set()
        self.sys_crop2ml_path = set()

        self.pkgs = PackageDict()
        self.recover_syspath()
        self.category = PseudoGroup('Root')  

    def rebuild_category(self):
        """ Rebuild all the category """

        self.category = PseudoGroup('Root')
        for p in self.pkgs.values():
            self.update_category(p)

    def create_readers(self, crop2ml_files):
        return filter(None, (self.get_pkgreader(f) for f in crop2ml_files))

    def find_and_register_packages(self, no_cache=False):
        """
        Find all composite model on the system and register them
        If no_cache is True, ignore cache file
        """

        self.set_sys_crop2ml_path()
        self.set_user_crop2ml_path()
        if DEBUG:
            t1 = time.clock()

        crop2ml_files = self.find_all_crop2ml()
        readerlist = self.create_readers(crop2ml_files)

        # readerlist = self.find_wralea_files()

        if DEBUG:
            t2 = time.clock()
            print ('-------------------')
            print ('find_crop2ml_files takes %f seconds' % (t2 - t1))

        if DEBUG:
            res = {}
        for x in readerlist:
            if DEBUG:
                tn = time.clock()
            x.register_packages(self)
            if DEBUG:
                tt = time.clock() - tn
                print ('register package ', x.get_pkg_name(), 'in ', time.clock() - tn)
                res[x.filename]=tt
        if DEBUG:
            t3 = time.clock()
            print ('-------------------')
            print ('register_packages takes %f seconds' % (t3 - t2))


        self.rebuild_category()

        if DEBUG:
            return res

    def load_directory(self, dirname):
        """ Load a directory containing wraleas"""

        dirname = os.path.abspath(dirname)

        if(not os.path.exists(dirname) or
           not os.path.isdir(dirname)):
            print("Package directory : %s does not exists." % (dirname,))
            # self.log.add("Package directory : %s does not exists."%(dirname,))
            return None

        self.add_crop2ml_path(dirname, self.user_crop2ml_path)

        # find wralea
        readers = self.find_crop2ml_dir(dirname)
        if not readers:
            readers = self.find_vlab_dir(dirname)
        ret = None
        for r in readers:
            if r:
                ret = r.register_packages(self)
            else:
                print("Unable to load package %s." % (dirname,))
                ret = None
        if(readers):

            self.rebuild_category()
        return ret

    def add_crop2ml_path(self, path, container):
        """
        Add a search path for wralea files

        :param path: a path string
        :param container: set containing the path
        """

        if not os.path.isdir(path):
            return

        # Ensure to add a non existing path
        for p in container:
            common = os.path.commonprefix((p, path))
            # the path is already in wralepath
            if (common == p and os.path.join(common, path[len(common):]) == path):
                return
            # the new path is more generic, we keep it
            if(common == path and
               os.path.join(common, p[len(common):]) == p):
                container.remove(p)
                container.add(path)
                return
        # the path is absent
        container.add(path)

    def find_crop2ml_dir(self, directory, recursive=True):
        """
        Find in a directory wralea files,
        Search recursivly is recursive is True

        :return : a list of pkgreader instances
        """

        if DEBUG:
            t0 = time.clock()

        crop2ml_files = set()
        if(not os.path.isdir(directory)):
            print("%s Not a directory" % repr(directory))
            # self.log.add("%s Not a directory"%repr(directory))
            return []

        p = Path(directory).abspath()

        # search for wralea.py
        if recursive and SEARCH_OUTSIDE_ENTRY_POINTS:
            for f in p.walkfiles("*model*.py"):
                crop2ml_files.add(str(f))
        else:
            crop2ml_files.update(p.glob("*model*.py"))

        for f in crop2ml_files:
            print("Package Manager : found %s" % f)
            # self.log.add("Package Manager : found %s" % f)

        if DEBUG:
            t1 = time.clock()
            dt = t1 - t0
            print ('search crop2ml files takes %f sec' % dt)

        readers = map(self.get_pkgreader, crop2ml_files)

        if DEBUG:
            t2 = time.clock()
            dt1 = t2 - t1
            print( 'readers takes %f sec: ' % (dt1,))

        return readers
    
    def get_pkgreader(self, filename):
        """ Return the pkg reader corresponding to the filename """

        reader = None
        if(filename.endswith('model.py')):
                reader = PyPackageReaderModel(filename)
        else:
            return None

        return reader    

    def __getitem__(self, key):
        try:
            return self.pkgs[key]
        except KeyError:
            raise UnknownPackageError(key)

    def __setitem__(self, key, val):
        self.pkgs[key] = val
        #self.notify_listeners("update")

    def __len__(self):
        return len(self.pkgs)

    def __delitem__(self, item):
        r = self.pkgs.__delitem__(item)
        self.rebuild_category()
        #self.notify_listeners("update")
        return r

    def __contains__(self, key):
        return self.has_key(key)

    def keys(self):
        return self.pkgs.keys()

    def items(self):
        return self.pkgs.items()

    def values(self):
        return self.pkgs.values()

    def iterkeys(self):
        return self.pkgs.iterkeys()

    def iteritems(self):
        return self.pkgs.iteritems()

    def itervalues(self):
        return self.pkgs.itervalues()

    def has_key(self, *args):
        return self.pkgs.has_key(*args)

    def get(self, *args):
        return self.pkgs.get(*args)


class AbstractPackageReader(object):
    """
    Abstract class to add a package in the package manager.
    """

    def __init__(self, filename):
        """
        Build a package from a specification file.
        filename may be a __wralea__.py file for instance.
        """
        self.filename = filename

    def register_packages(self, pkgmanager):
        """ Create and add a package in the package manager. """
        raise NotImplementedError()

class PyPackageReader(AbstractPackageReader):
    """
    Build packages from wralea file
    Use 'register_package' function
    """

    def filename_to_module(self, filename):
        """ Transform the filename ending with .py to the module name """
        start_index = 0
        end_index = len(filename)

        # delete the .py at the end
        if (filename.endswith('.py')):
            end_index = -3
        # Windows case (e.g. C:/...)
        if (filename[1] == ':'):
            start_index = 2

        modulename = filename[start_index:end_index]

        l = modulename.split(os.path.sep)
        modulename = '.'.join(l)

        return modulename

    def get_pkg_name(self):
        """ Return the OpenAlea (uniq) full package name """
        m = self.filename_to_module(self.filename)
        m = m.replace(".", "_")
        return m

    def register_packages(self, pkgmanager):
        """ Execute model.py """

        pkg = None
        
        basename = os.path.basename(self.filename)
        basedir = os.path.abspath(os.path.dirname(self.filename))

        modulename = self.get_pkg_name()
        print("mod", modulename)
        base_modulename = self.filename_to_module(basename)
        print("basmod", base_modulename)

        # Adapt sys.path
        sys.path.append(basedir)

        if (modulename in sys.modules):
            del sys.modules[modulename]

        (file, pathname, desc) = imp.find_module(base_modulename, [basedir])
        try:
            wraleamodule = imp.load_module(modulename, file, pathname, desc)
            print("wr", wraleamodule, type(wraleamodule))
            print("pk", pkgmanager)
            pkg = self.build_package(wraleamodule, pkgmanager)

        except Exception as e:
            try:
                print('%s yes 1 is invalid : %s' % (self.filename, e))
            except Exception as e:
                print ('%s yes 2 is invalid : %s' % (self.filename, e))
                pass

        except:  # Treat all exception
            pkgmanager.add('%s is yes3  invalid :' % (self.filename, ))

        if (file):
            file.close()

        # Recover sys.path
        sys.path.pop()

        return pkg

    def build_package(self, wraleamodule, pkgmanager):
        """ Build package and update pkgmanager """
        print("pk", pkgmanager)
        try:
            wraleamodule.register_packages(pkgmanager)

        except AttributeError:
            # compatibility issue between two types of reader
            reader = PyPackageReaderModel(self.filename)
            reader.build_package(wraleamodule, pkgmanager)

import shutil
class PyPackageReaderModel(PyPackageReader):
    """
    Build a package from  a __wralea__.py
    Use module variable
    """


    def build_package(self, wraleamodule, pkgmanager):
        """ Build package and update pkgmanager """
        print('buid')
        name = wraleamodule.__dict__.get('__name__', None)
        edit = wraleamodule.__dict__.get('__editable__', False)
        print(name, edit)
        # Build Metainfo
        metainfo = dict(
            version='',
            license='',
            authors='',
            institutes='',
            description='',
            url='',
            icon='',
            alias=[], )

        for k, v in wraleamodule.__dict__.items():

            if not (k.startswith('__') and k.endswith('__')):
                continue
            k = k[2:-2]  # remove __
            if k not in metainfo:
                continue
            metainfo[k] = v
        print("met", metainfo)
        # Build Package
        path = wraleamodule.__file__
        print("path", path)
        if (path.endswith('.pyc')):
            path = path.replace('.pyc', '.py')

        if (not edit):
            print("no")
            p = Package(name, metainfo, path)
        else:
            print('yes')
            p = UserPackage(name, metainfo, path) 
        print("p",p)           
        pkgmanager.add_package(p)
   
    def check_exist(self):
        pass
    
    
    def contain_pkg(self, pkg):
        pk={}
        for root, dirs, files in os.walk(pkg):
            if "crop2ml" in dirs:
                pk[root.split('/')[-1]]=root              
        return pk
    
    def get_path(self,pkg,name):
        di = self.contain_pkg(pkg)
        wf_path={}
        for k, v in di.items():
            wf_name = k.split('\\')[-1]
            wf_path[wf_name]=v
        if name in wf_path.keys():
            return wf_path[name]
        else:
            print("pkge doesn't exist")



 
        
import shutil
class UserPackage(Package):
    """ Package user editable and persistent """

    def __init__(self, name, metainfo, path=None):
        """ @param path : directory where to store wralea and module files """

        if (not path):
            import inspect
            # get the path of the file which call this function
            path = os.path.abspath(inspect.stack()[1][1])
        print("path", path)
        print("name", name, metainfo, path)
        Package.__init__(self, name, metainfo, path)


import string

class PyPackageWriter(object):
    """ Write a wralea python file """

    wralea_template = """
# This file has been generated at $TIME
$PKG_DECLARATION
"""

    pkg_template = """
$PKGNAME
$METAINFO
"""

    def __init__(self, package):
        """ Package to write """

        self.package = package

    def __repr__(self):
        """ Return a string with the package declaration """

        pstr = string.Template(self.pkg_template)

        editable = isinstance(self.package, UserPackage)

        metainfo = '__editable__ = %s\n' % (repr(editable))

        for (k, v) in self.package.metainfo.iteritems():
            key = "__%s__" % (k)
            val = repr(v)
            metainfo += "%s = %s\n" % (key, val)

        result = pstr.safe_substitute(PKGNAME="__name__ = %s" % (repr(self.package.name)),
                                      METAINFO=metainfo,
                                      )

        return result

    def get_str(self):
        """ Return string to write """

        pstr = repr(self)
        wtpl = string.Template(self.wralea_template)

        result = wtpl.safe_substitute(
            TIME=time.ctime(),
            PKG_DECLARATION=pstr)

        return result

    def write_wralea(self, full_filename):
        """ Write the wralea.py in the specified filename """

        try:
            result = self.get_str()
        except Exception as e:
            print(e)
            print("FILE HAS NOT BEEN SAVED !!")
            return
        handler = open(full_filename, 'w')
        handler.write(result)
        handler.close()
        # Recompile
        import py_compile
        py_compile.compile(full_filename)


'''
from pycropml import package
pkg1=Path("C:/Users/midingoy/Documents/THESE/pycropml_pheno/test/Tutorial/test")
pk = package.PackageManager()
pk.init(pkg1)
pk.contain_pkg(pkg1)

'''