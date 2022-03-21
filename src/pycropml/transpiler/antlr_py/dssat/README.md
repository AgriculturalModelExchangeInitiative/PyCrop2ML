
From crop DSSAT modeling platform to Crop2ML framework
======================================================

<u> **General Expectations:** </u>

A modeler provides an autonomous crop model component. A component could be defined by a set of simpler components (units)
that could be composed hierarchically. The interaction of components is only determined based on their inputs and outputs. Simpler component could be tested independently of others by using only its inputs and outputs.
Based on this component, Crop2ML Models are generated. It consists of creating:
- Model Specification (Meta-information of component)
- Model Algorithms (Compute part)
- Model Initialization
- External Functions (Functions developed by platforms modelers called by the component). It is as if these functions are arguments of the component.

 Specification is generated in a declarative approch, in XML format validated by a DTD whereas Algorithms, Initialization and Functions are generated in CyML language.

<u> **General Requirements:** </u>

 The original code provided by the platform (source) should follow these guidelines:
 1. Define explicitely the inputs and outputs of each unit of the component.
 2. In the case where platform doesn't provide a mechanism to set inputs and outputs meta-information, it could be done by code comments inside the source code of the component. A format of code comments for inputs/outputs description is provided
 3. !!! Important: The invocation of a routine with the same values of inputs should produce the same values of outputs. This requirement avoids using outputs as global variables and mechanism that preserves local variables or arrays (maintains its value from one call to the next) in the routine.  Likewise a routine should not depend on any computational state other than its inputs and outputs.
 4. Composite variables could be used. However, since that CyML/Crop2ML doesn't provide this datatype, an automatic decomposition of these variables is done. It requires to explicitely describe all the fields of the composite variable that are used in the main parts of the component (Algorithm, Initialization, Function) 
 5. State variables initialization implemented in the Initialization part must depend only on parameters and the exogenous (driven) variables of the component.
 6. Algorithm part depends on parameters, exogenous variables, initialized states and state variables. It could also depend on auxiliary or rates variables depending on the component modularity.
 7. Procedures written with programming languages other than the main used by the platforms or the use of external libraries that are not explicitely defined are not able to be handled. If external library must be used, it is necessary to provide its source code and if it is implemented with the required constructions (language intersection++), an equivalent will be provided in CyML by transformation. However, if this library has already equivalent in the main languages, it just needs to integrated in signature in the Crop2ML platform and it will be used as an internal function. 
 8. The main language constructs in algorithm, initialization and external functions parts are:

        8.1. Assignment

        8.2. Branching

        8.3. Looping (definite and undefinite iteration)

        8.4. Binary operations

        9.4. Usual mathematical functions

 <u> **Manual transformation part:** </u>
 
Based on the previous requirements, the original component could be manually transformed to take into account them. Besides, since components are implemented with different approaches and that they could be embedded with the specificities of the platforms, it is useful to provide mechanism that will allow to identify the main part of the components to make easy model transformation.
Then for the transformation, we need to identify:

    * the routines that correspond to the Crop2ML ModelUnits. 

    * The parts of these subroutines that represent initialization and algorithm (computation). Algorithm could be divided into rate calculation, state calculation.

    * Given that some parts could be specific to the platform environment such as I/O operations, data formatting, and the variables declarations statements for these constructs, it is necessary to skip these parts. ATTENTION!!! The code must be syntactically valid after ignoring some parts otherwise it cannot be parsed.

For that, we defined some tags (opened and closed) that will be introduced in the source files to distinguish each part. Each tag should be preceded by the symbol of comment of language of the source code ("!" in fortran, "#" in Python).

                           
|Tags  |Parts of source file|
|-----|--------|
| %%CyML Model Begin%% / %%CyML Model End%% | ModeUnit or ModelComposite     |
| %%CyML Initialization Begin%% / %%CyML Initialization End%% | Initialization part      |
| %%CyML Rate Begin%% / %%CyML Rate End%% | Rate Calculation part
| %%CyML State Begin%% / %%CyML State End%% | State Calculation part 
| %%CyML Compute Begin%% / %%CyML Compute End%% | Algorithm part  
| %%CyML Ignore Begin%% / %%CyML Ignore End%% | Ignored Statement
| %%CyML Description Begin%% / %%CyML Description End%% | Ignored Statement


<u> **Model description:** </u>

A simple format is provided for the description of inputs and outputs. It will be contained in the description tags.
Each variable or parters will be described as folloxs as:

Name Description (Unit) (default, [minimum, maximum]) category inputype



 <u> **Transformation process** </u>

The transformation process involves these steps:

1. Identify the units (components) and tag different parts including components description

2. Follow the requirements and make manual transformation. The rest of process will be automatic

3. All the files of the component are merged in one temporal file and parsed to generate a Fortran ASG (asgT)

4. For each file of the source files:

   4.1. We identify and extract the routines that are tagged with ModelUnit tags.

   4.2. If the file is tagged with ModelUnit tags, component description is retrieved and transformed in Crop2ML XML file based of this routine inputs and outputs. Likewise, its ASG (asgM) is extracted from asgT.

   4.3. If the routine call a function, its ASG will be extracted from asgT and the external function will be generated in CyML 

   4.4. If initialization or/and Algorithm or rate or/and state are found, the part of code is extracted from the file and is transformed into CyML. The local variables of each part are well filtred.


<u> **Application with DSSAT components:** </u>

DSSAT modelers provide an autonomous crop model component.
It includes the CMakeLists file that contains the source files. A parser of CMake file is used to extract the different source files.

    <u> **Some DSSAT requirements** </u>
    
    1. DSSAT uses Subroutine to implement a component. So, it is useful to explicit the inputs and outputs of the component (Requirement 1). Since a subroutine cannot return a value through its name, it must return the computation results, if any, through its argument. Therefore, we have two cases to consider:

     1.1 Use INTENT keyword: IN, OUT and INOUT

     1.2. Or put a comment next to arguments that represent inputs (!inputs), outputs (!outputs). If a subroutine argument can receive a value that is changed during computations its intent is INOUT, then for that case !inout will be put.

     1.3. Variables without INTENT keyword are considered local variables

    2. DSSAT uses SAVE statement that preserves the local variables values for the next invocation that breaks the Requirement 3. To change that manually, This type of local variable should be defined as subroutine arguments. 

    3. Exhaustive use of the "implicit none" directive to detect bad variable usage


Example: DSSAT-EPIC Soil Temperature component.

This component is provided with a CMakeLists file that contains 5 files:

- STEMP_EPIC.for : It is the main component that describes the initialization and compute part of Soil Temperature component
- ASKEE_DSSAT_EPIC.for: The main program to run the component
- ModuleDefs.for: A module where some variables are described incuding control variables
- OPSTEMP.for: A routine to write Outputs values
- DATES.for: A routine to format dates inputs.

Taking the main component STEMP_EPIC routine, it will be tagged with ModelUnit Tag as well as the initialization and rates calculations parts. Some parts of the code could be ignored with "ignore tag" such as calling OPSTEMP.for, DATES.for. STEMP_EPIC call SOILT_EPIC (defined in STEMP_EPIC.for) which is the only important function required for reusing this component. Control variable could be ignored since initialization and compute parts will be generated independently. The choice is left to whoever wants to reuse to combine the initialization and the algorithm. The declaration of some variables that are not useful for the rest of the code could be ignored such as DOY, YEAR, DYNAMIC.

After analyzing the component, few changes are needed:

  NDays, TDL, WetDay and TMA are considered as local variables in the original code and are not defined as the subroutine arguments. The code is expressive and limits the number of arguments since that SAVE statement is used and their values can be preserved. However, in a declarative way it is useful to define them as subroutine arguments since they are initialized in the Initialization part and their values are used in the computation part. As in Requirement 6 the computation part will take in arguments initialized variables. Likewise, in the ratecalculation the previous values of these variables are required, that forces to consider them as arguments with INOUT INTENT. ST is defined as Output but it's changed as INOUT.

  Regarding the called routine SOILT_EPIC, it uses a local variable X2_PREV which is used in an assignment without being assigned and which is then assigned with X2_AVG. So, for the first invocation of SOILT_EPIC, X2_PREV takes the default values 0.0 and it will assigned X2_AVG. For the next invocation, the value of X2_PREV is the previous value of X2_AVG, that breaks the Requirement 3. X2_PREV will be defined explicitely as argument.


After these changes, the component is translated into Crop2ML/CyML. One test is added based on the ASKEE_DSSAT_EPIC file. By using the values of arguments in this file, the initialization outputs are calculated and used to set the initialize states argument of the Algorithm (Compute). The same result will be produced compared to the results by running the original component. 



