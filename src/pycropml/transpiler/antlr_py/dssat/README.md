
<u> **From crop DSSAT modeling platform to Crop2ML framework** </u>

<u> **Expectations:** </u>

A modeler provides an autonomous crop model component. A component could be defined by a set of simpler components (units)
that could be composed hierarchically. The interaction of components is only determined based on their inputs and outputs. Simpler component could be tested independently of others by using only its inouts and outputs.
Based on this component, Crop2ML Models are generated. It consists of creating:
- Model Specification (Meta-information of component)
- Model Algorithms
- Model Initialization
- External Functions (Functions developed by platforms modelers called by the component)

 Specification is generated in a declarative approch, in XML format validated by a DTD whereas Algorithms, Initialization and Functions are generated in CyML language.

<u> **Requirements:** </u>

 The original code provided by the platform (source) should follow these guidelines:
 1. Define explicitely the inputs and outputs of each units of the component.
 2. In the case where platform doesn't provide a mechanism to set inputs and outputs meta-information, it could be done by code comments inside the source code of the component
 3. !!! Important: The invokation of a routine with the same values of inputs should produce the same values of outputs. This requirement avoids using outputs as global variables and mechanism that preserves local variables or arrays (maintains its value from one call to the next) in the routine.  Likely a routine should not be depend on any computational state other than its inputs and outputs.
 4. Composite variables could be used. However, since that CyML/Crop2ML doesn't provide this datatype, an automatic decomposition of these variables is done. It requires to explicitely describe all the fields of the composite variable that is used in the main parts of the component (Algorithm, Initialization, Function) 
 5. State variables initialization implemented in the Initialization part must depend only on parameters and the exogenous (driven) variables of the component.
 6. Algorithm part depends on parameters, exogenous variables, initialized states and states variables. It could also depend on auxiliary or rates variables dependeing on the component modularity.




DSSAT modelers provide an autonomous crop model component.
It includes the CMakeLists file that contains the source files.

For the transformation, we need to identify:
    * the subroutines that correspond to the Crop2ML ModelUnits. 
    * The parts of these subroutines that represent initialization, rate calculation, state calculation. If rate and state  calculations are not separated, algorithm part must be identified 
    * Given that some parts could be specific to DSSAT environment such as I/O operations, data formatting, and variables declarations statements for these constructions, it is necessary to skip these parts. Then these subroutines that are called inside the code must be specified.

For that, we defined some tags (opened and closed) that will be introduced in the source files to distinguish each parts

                             
|Tags  |Parts of source file|
|-----|--------|
|!%%ModelUnit_Start%% / !%%ModelUnit_End%% | ModeUnit     |
|!%%Initialization_Start%% / !%%Initialization_End%%  | Initialization part      |
|!%%Algorithm_RateCalculation_Start%% / !%%Algorithm_RateCalculation_End%% | Rate Calculation part
|!%%Algorithm_StateCalculation_Start%% / !%%Algorithm_StateCalculation_End%% | Sate Calculation part 
|!%%Algorithm_Part_Start%% / !%%Algorithm_Part_End%%| Algorithm part  
|!%%Ignore_Start%% / !%%Ignore_End%%| Ignored Statement

For the not required subroutines, a tag "!%%NotRequired%%" is placed before these subroutines

Transformation process
======================
The transformation process involves these steps:

1. A parser of CMake file is used to extract the different source files


2. These files are merged in one temporal file and parsed to generate a Fortran ASG (asgT)

3. For each file of the source files:

3.1. We identify and extract the subroutines that are tagged with ModelUnit tags.

3.2. For each 


Subroutines to ModelUnits:
- For the list of arguments, make sure you specify whether these are inputs only INTENT(in), outputs only INTENT(out) or if they are both inputs and outputs INTENT(inout). 
- Variables without INTENT keyword are considered local variables




Requirements:

- EXternal procedures:
DO NOT USE THEM: modules are allowed! 
CyMLTx doesn't handle procedures written with different programming language or using external libraries

- Exhaustive use of the "implicit none" directive to detect bad variable usage