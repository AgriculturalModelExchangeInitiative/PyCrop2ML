
<u> From crop DSSAT modeling platform to Crop2ML framework </u>

DSST modelers provide an autonomous crop model component.
It includes the CMakeLists file that contains the source files.

For the transformation, we need to identify:
    * the subroutines that correspond to the Crop2ML ModelUnits. 
    * The parts of these subroutines that represent initialization, rate calculation, state calculation. If rate and state  calculations are not separated, algorithm part must be identified 
    * Given that some parts could be specific to DSSAT environment such as I/O operations, data formatting, and variables declarations statements for these constructions, it is necessary to skip these parts. 

For that, we defined some tags (opened and closed) that will be introduced in the source files to distinguish each parts

                             
|Tags  |Parts of source file|
|-----|--------|
|!%%ModelUnit_Start%% / !%%ModelUnit_End%% | ModeUnit     |
|!%%Initialization_Start%% / !%%Initialization_End%%  | Initialization part      |
|!%%Algorithm_RateCalculation_Start%% / !%%Algorithm_RateCalculation_End%% | Rate Calculation part
|!%%Algorithm_StateCalculation_Start%% / !%%Algorithm_StateCalculation_End%% | Sate Calculation part 
|!%%Algorithm_Part_Start%% / !%%Algorithm_Part_End%%| Algorithm part  
|!%%Ignore_Start%% / !%%Ignore_End%%| Ignored Statement



Transformation process
======================
The transformation process involves these steps:

1. A parser of CMake file is used to extract the different source files


2. Provide the Fortran90 grammar based on ANTLR that allows parsing Fortran fix and free-form. 


