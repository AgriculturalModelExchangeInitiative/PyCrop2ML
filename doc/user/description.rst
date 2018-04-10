**CropML Description**
======================
| In CropML, a model is either a model unit or a composition of models unit. A ModelUnit  represents the atomic unit of a crop model define by the 
	modelers. A model composition  is a model resulting from the composition of two or more atomic model.
| These models have a specific formal definition in CropML.

Formal definition of a Model Unit in CropML
-------------------------------------------
| The structure of a Model Unit in CropML must be conform to a specific Document Type Definition
	named `ModelUnit.dtd <https://github.com/AgriculturalModelExchangeInitiative/PyCropML/blob/version2/test/data/ModelUnit.dtd>`_ .
| So a Model Unit CropML document is a XML document well-formed and also obeys the rules given in the ModelUnit schema.
| This structure may be described by the below tree:

.. image:: images/modelunit.png

| In the next, we define the major elements of a CropML model unit.

ModelUnit element
^^^^^^^^^^^^^^^^^^
| An atomic model in CropML is declared with `<<ModelUnit>> <https://github.com/AgriculturalModelExchangeInitiative/PyCropML/blob/master/src/pycropml/modelunit.py>`_ element,
	the usual root of CropML ModelUnit document. 
| This element must contain a Description, an Algorithm, Parametersets and Testsets elements and
	may optionally have Inputs and Outputs elements. The restriction of the length of different lists is not imposed.
| ModelUnit element must have an unique id and name attributes which are used to reference an atomic model. It also contains a timestep and unit attribute.
	The unit attribute is used to define the unit that are associated with the model.

Description element
^^^^^^^^^^^^^^^^^^^
This element gives the general information on the model and is composed by a set of character elements. It must contain
Title, Authors, Institution and abstract elements and may optionally contain URI and Reference elements.

Inputs elements
^^^^^^^^^^^^^^^
| The inputs of Model are listed inside an XML element called Inputs within a `dictionary structure  <https://github.com/AgriculturalModelExchangeInitiative/PyCropML/blob/version2/src/pycropml/inout.py>`_ 
	composed by their attributes which declarations are optional(default, max, min, parametertype, variabletype and URI) or required(name, datatype, description, inputtype,
	unit ) and their corresponding value. *Inputs* element must contain one or more inputs elements.
| The required *datatype* attribute is the type of input value specified in *default* (the default value in the input), *min* (the minimum value in the input) and *max*
	(the maximum value in the input). It may be one type of the set of types used in the existing crop modeling platform.
| The *inputtype* attribute makes it possible to distinguish the variables and the parameters of the model. So it must take one of two possible values: *parameter* and *variable*.
| The *parametertype* attribute defines the type of parameter which is specified by one of the following values: *constant*, *species*, *soil* and *genotypic*.
| The *variabletype* defines the type of variable depending on whether it is a *state* or *rate* variable. 
	State variable characterize the behavior of the model and rate variable characterizes the change of a state of the model.

Outputs element
^^^^^^^^^^^^^^^
The outputs of Model are listed inside an XML element called Outputs within a `dictionary structure <https://github.com/AgriculturalModelExchangeInitiative/PyCropML/blob/version2/src/pycropml/inout.py>`_  
composed by their attributes which declarations are optional(variabletype and URI) or required(name, datatype, description, unit, max and min ) and their corresponding value
*Outputs* must contain zero or more output element. The definition of different attributes is same as Input's attributes.

Algorithm element
^^^^^^^^^^^^^^^^^
| The *Algorithm* element defines the building block of CropML model unit and shows the computational method to determine
	the outputs from the inputs. 
| It consists of a set of mathematical equations (relation between inputs), loops and conditional instructions 
	which are well structured in a specific *language*, the algorithm's attribute.

Parametersets element
^^^^^^^^^^^^^^^^^^^^^
| *Parametersets* element contains one or more *Parameterset* elements that define the different ways of setting the model.
	Each *Parameterset* element must have *name* and *description* attributes that respectively represents the name and the description of each setting.
| The different parameterset must contain a list of Param elements that show in attribute the name of the parameter (an input 
	which inputtype equals *parameter*) and the fixed value of this one.

Testsets element
^^^^^^^^^^^^^^^^
| *Testsets* element contains one or more *Testset* elements that define the different run for evaluating the outputs of the model.
	Each *Testset* element must have *name*, *description* and *parameterset* attributes that respectively represents the name, 
	the description of each run and the name of the parameterset related to the Testset. This one allow to retrieve the name and the value of different
	parameters includes in this parameterset.
| The different Testset must contain a list of InputValue and OutputValue elements corresponding respectively to the values
	of inputs used in the run and the values of Outputs that will be asserted.

Formal definition of a Model Composition in CropML
--------------------------------------------------
The structure of a Model Unit in CropML must be conform to a specific Document Type Definition
named `ModelComposition.dtd <https://github.com/AgriculturalModelExchangeInitiative/PyCropML/blob/version2/test/data/ModelComposition.dtd>`_ .
