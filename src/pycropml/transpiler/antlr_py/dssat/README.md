
<u> **From crop DSSAT modeling platform to Crop2ML framework** </u>

<u> **General Expectations:** </u>

A modeler provides an autonomous crop model component. A component could be defined by a set of simpler components (units)
that could be composed hierarchically. The interaction of components is only determined based on their inputs and outputs. Simpler component could be tested independently of others by using only its inputs and outputs.
Based on this component, Crop2ML Models are generated. It consists of creating:
- Model Specification (Meta-information of component)
- Model Algorithms
- Model Initialization
- External Functions (Functions developed by platforms modelers called by the component). It is as if these functions are arguments of the component.

 Specification is generated in a declarative approch, in XML format validated by a DTD whereas Algorithms, Initialization and Functions are generated in CyML language.

<u> **General Requirements:** </u>

 The original code provided by the platform (source) should follow these guidelines:
 1. Define explicitely the inputs and outputs of each units of the component.
 2. In the case where platform doesn't provide a mechanism to set inputs and outputs meta-information, it could be done by code comments inside the source code of the component
 3. !!! Important: The invokation of a routine with the same values of inputs should produce the same values of outputs. This requirement avoids using outputs as global variables and mechanism that preserves local variables or arrays (maintains its value from one call to the next) in the routine.  Likely a routine should not be depend on any computational state other than its inputs and outputs.
 4. Composite variables could be used. However, since that CyML/Crop2ML doesn't provide this datatype, an automatic decomposition of these variables is done. It requires to explicitely describe all the fields of the composite variable that is used in the main parts of the component (Algorithm, Initialization, Function) 
 5. State variables initialization implemented in the Initialization part must depend only on parameters and the exogenous (driven) variables of the component.
 6. Algorithm part depends on parameters, exogenous variables, initialized states and states variables. It could also depend on auxiliary or rates variables dependeing on the component modularity.
 7. Procedures written with programming languages other than the main used by the platforms or the use of external libraries that are not explicitely defined are not able to be handled. If external library must be used, it is necessary to provide its source code and if it is implemented with the required constructions (language intersection++), an equivalent will be provided in CyML by transformation. However, if this library has already equivalent in the main languages, it just needs to integrated in signature in the Crop2ML platform and it will be used as an internal function. 

 <u> **Manual transformation part:** </u>
 
Based on the previous requirements, the original component could be manually transformed to take into account them. Besides, since components are implemented with different approaches and that they could be embedded with the specificities of the platforms, it is useful to provide mechanism that will allow to identify the main part of the components to make easy model transformation.
Then for the transformation, we need to identify:
    * the routines that correspond to the Crop2ML ModelUnits. 
    * The parts of these subroutines that represent initialization and algorithm. Algorithm could be divided into rate calculation, state calculation. 
    * Given that some parts could be specific to the platform environment such as I/O operations, data formatting, and variables declarations statements for these constructions, it is necessary to skip these parts.

For that, we defined some tags (opened and closed) that will be introduced in the source files to distinguish each parts. Each tag should be preceded by the symbol of comment of language of the source code ("!" in fortran, "#" in Python).

                           
|Tags  |Parts of source file|
|-----|--------|
| <CyML Model Begin>/ <CyML Model End> | ModeUnit or ModelComposite     |
|<CyML Initialization Begin> / <CyML Initialization End> | Initialization part      |
|<CyML Rate Begin> / <CyML Rate End> | Rate Calculation part
|<CyML State Begin> / <CyML State End> | State Calculation part 
|<CyML Algorithm Begin> / <CyML Algorithm End> | Algorithm part  
|<CyML Ignore Begin> / <CyML Ignore End> | Ignored Statement
|<CyML Description Begin> / <CyML Description End> | Ignored Statement



<u> **Application with DSSAT components:** </u>


DSSAT modelers provide an autonomous crop model component.
It includes the CMakeLists file that contains the source files.

Transformation process
======================
The transformation process involves these steps:

1. Identify the units (components) and tagged different parts including components descriptions

2. Follow the requirements and make manual transformation. The rest of process will be automatic

3. A parser of CMake file is used to extract the different source files

4. These files are merged in one temporal file and parsed to generate a Fortran ASG (asgT)

5. For each file of the source files:

   5.1. We identify and extract the subroutines that are tagged with ModelUnit tags.

3.2. For each 


Subroutines to ModelUnits:
- For the list of arguments, make sure you specify whether these are inputs only INTENT(in), outputs only INTENT(out) or if they are both inputs and outputs INTENT(inout). 
- Variables without INTENT keyword are considered local variables




Requirements:

- EXternal procedures:
DO NOT USE THEM: modules are allowed! 


- Exhaustive use of the "implicit none" directive to detect bad variable usage