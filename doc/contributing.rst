Contributing Guide
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is a wiki for anything related to the contributing on [[Crop2ML|https://github.com/AgriculturalModelExchangeInitiative|Crop2ML]] which is a project of the
Agricultural Model Exchange Initiative.
For more information about this project, please visit CropML documentation [[Crop2ML|https://cropmlformat.readthedocs.io/en/latest/?badge=latest|documentation]]: 

----

Quick Links
^^^^^^^^^^^

 * [[Project Git Repository|https://github.com/cython/cython|Git Repository]] (and [[Change Log|https://github.com/cython/cython/blob/master/CHANGES.rst|Change Log]])
 * [[ Differences between Cython and Pyrex|https://cython.readthedocs.io/en/latest/src/userguide/pyrex_differences.html| Differences between Cython and Pyrex]]
 * [[Unsupported Python features|https://cython.readthedocs.io/en/latest/src/userguide/limitations.html|Unsupported Python features]] (aka TODO list)
 * [[ Hacker-Guide: How to work on the Cython compiler itself|HackerGuide| Hacker-Guide: How to work on the Cython compiler itself]]
 * [[ Enhancement proposals|enhancements| Enhancement proposals]] (CEPs)
 * [[ Projects using Cython|projects| Projects using Cython]]
 * [[ Comparison with SWIG|SWIG| Comparison with SWIG]]
 * [[Automatic .pxd/.pyx generation|AutoPxd|Automatic .pxd/.pyx generation]] from C or C++ header files.

Cython Installers
-----------------

 * [[PyPi|http://pypi.python.org/pypi/Cython/|PyPi]] via ``easy_install`` or pip
 * [[Gentoo Ebuild|http://packages.gentoo.org/package/dev-python/cython|Gentoo Ebuild]]
 * [[Debian package|http://packages.debian.org/sid/cython|Debian package]] (not always up to date)
 * [[ Installing Cython on Windows|InstallingOnWindows| Installing Cython on Windows]]



Tips and Tricks
---------------

 * [[Getting started|http://docs.cython.org/src/quickstart/index.html|Getting started]]
 * [[ Using early binding techniques to improve speed|http://docs.cython.org/en/latest/src/userguide/early_binding_for_speed.html| Using early binding techniques to improve speed]]
 * [[ Writing Cython programs in pure Python|http://docs.cython.org/src/tutorial/pure.html| Writing Cython programs in pure Python]]
 * [[ Helpful notes for wrapping C++ APIs|http://docs.cython.org/en/latest/src/userguide/wrapping_CPlusPlus.html| Helpful notes for wrapping C++ APIs]]
 * [[ Discussion of all the options how to wrap C/C++ code to Python|WrappingCorCpp| Discussion of all the options how to wrap C/C++ code to Python]]
 * [[WritingFastPyrexCode|http://www.sagemath.org:9001/WritingFastPyrexCode|WritingFastPyrexCode]]
 * [[ Successful creation of a hierarchy of modules in a package|PackageHierarchy| Successful creation of a hierarchy of modules in a package]]
 * [[ One method for source-level debugging|http://docs.cython.org/en/latest/src/userguide/debugging.html| One method for source-level debugging]]
 * [[ Dynamic Memory Allocation (malloc, realloc, free)|http://docs.cython.org/en/latest/src/tutorial/memory_allocation.html| Dynamic Memory Allocation (malloc, realloc, free)]]
 * [[Profiling]]
 * [[ Building a Windows Installer|BuildingWindowsInstaller| Building a Windows Installer]]
 * [[Embedding Python|EmbeddingCython|Embedding Python]] to create standalone Cython programs.
 * [[List Subclass Example|ListExample|List Subclass Example]] Adding mathematical operations to subclassed built-in list.
 * Working with Numpy

    * [[Tutorial for NumPy users|http://docs.cython.org/en/latest/src/userguide/numpy_tutorial.html|Tutorial for NumPy users]]
    * [[Accessing a Numpy pointer for passing to C|http://docs.cython.org/en/latest/src/userguide/memoryviews.html#pass-data-from-a-c-function-via-pointer]]

People
^^^^^^

[[Stefan Behnel|http://scoder.behnel.de/|Stefan Behnel]], [[Robert Bradshaw|http://www.math.washington.edu/~robertwb/|Robert Bradshaw]], [[Dag Seljebotn|http://heim.ifi.uio.no/dagss/|Dag Seljebotn]], Lisandro Dalcin.

Mailing Lists
^^^^^^^^^^^^^

Our development mailing list is [[cython-dev|http://mail.python.org/mailman/listinfo/cython-devel|cython-dev]]
and user mailing list at http://groups.google.com/group/cython-users.

In the past we also used a [[Google group|http://groups.google.com/group/cython|Google group]] and a list at [[BerliOS Developer|https://lists.berlios.de/mailman/listinfo/cython-dev|BerliOS Developer]]. You can still read [[the archives at Gmane|http://blog.gmane.org/gmane.comp.python.cython.devel|the archives at Gmane]].

Project Goals
^^^^^^^^^^^^^

 * Fully supported easy-to-use test suite, including the normal CPython test suite.
 * Easy installation and usage.
 * Rich, accessible documentation.  Make sure the examples are plenty and can be automatically tested.
 * Make Cython part of the standard distribution of Python (like ctypes).
 * Compile all Python code except for possibly some obvious exclusions, which will be worked out by developers.
 * Very fast when the user explicitly declares types (but we're not going to make promises with type inference).  Precise benchmarks.
 * Mitigate or eliminate the need for users to invoke the Python/C API directly without sacrificing performance.

Documentation
^^^^^^^^^^^^^

 * See http://docs.cython.org/.
 * Official Pyrex [[Language Overview|http://www.cosc.canterbury.ac.nz/greg.ewing/python/Pyrex/version/Doc/LanguageOverview.html|Language Overview]] (note the [[changes|http://hg.cython.org/cython|changes]] though).
  * [[Extension Types|http://www.cosc.canterbury.ac.nz/greg.ewing/python/Pyrex/version/Doc/Manual/extension_types.html|Extension Types]]
  * [[Sharing Declarations Between Pyrex Modules|http://www.cosc.canterbury.ac.nz/greg.ewing/python/Pyrex/version/Doc/Manual/sharing.html|Sharing Declarations Between Pyrex Modules]]
  * [[FAQ|http://www.cosc.canterbury.ac.nz/greg.ewing/python/Pyrex/version/Doc/FAQ.html|FAQ]]
  * [[Quick Guide to Pyrex|http://ldots.org/pyrex-guide/|Quick Guide to Pyrex]] from Michael JasonSmith.
 * CategoryCythonDoc lists pages that are related to Cython documentation.
 * [[ Pure Python mode|pure| Pure Python mode]]
 * SAGE Days 4 talk highlighting some of the [[differences between Pyrex and SageX|http://cython.org/talks/SageX.pdf|differences between Pyrex and SageX]] (the predecessor of Cython).
----

CategoryHomepage