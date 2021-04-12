

 //Author:Loic Manceau loic.manceau@inra.fr
 //Institution:INRA
 //Author of revision: 
 //Date first release:6/4/2018
 //Date of revision:

using System;
using System.Collections.Generic;
using System.Xml;
using System.Linq;
using CRA.ModelLayer.MetadataTypes;
using CRA.ModelLayer.Core;
using CRA.ModelLayer.Strategy;
using System.Reflection;
using VarInfo=CRA.ModelLayer.Core.VarInfo;
using Preconditions=CRA.ModelLayer.Core.Preconditions;


using SiriusQualityPhenology;
using CRA.AgroManagement;


//To make this project compile please add the reference to assembly: SiriusQuality-PhenologyComponent, Version=0.0.0.0, Culture=neutral, PublicKeyToken=null
//To make this project compile please add the reference to assembly: CRA.ModelLayer, Version=1.0.5212.29139, Culture=neutral, PublicKeyToken=null
//To make this project compile please add the reference to assembly: mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
//To make this project compile please add the reference to assembly: CRA.AgroManagement2014, Version=0.8.0.0, Culture=neutral, PublicKeyToken=null
//To make this project compile please add the reference to assembly: System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089;

namespace SiriusQualityPhenology.Strategies
{

	/// <summary>
	///Class CalculateGAImean
    /// Calculate Average Green Area Index on the TTWindowForPTQ thermal time periode
    /// </summary>
	public class CalculateGAImean : IStrategySiriusQualityPhenology
	{


			public CalculateGAImean()
			{
				
				ModellingOptions mo0_0 = new ModellingOptions();
				//Parameters
				List<VarInfo> _parameters0_0 = new List<VarInfo>();
				VarInfo v1 = new VarInfo();
				 v1.DefaultValue = 70;
				 v1.Description = "Thermal time window in which averages are computed";
				 v1.Id = 0;
				 v1.MaxValue = 70000;
				 v1.MinValue = 0;
				 v1.Name = "TTWindowForPTQ";
				 v1.Size = 1;
				 v1.Units = "°Cd";
				 v1.URL = "";
				 v1.VarType = CRA.ModelLayer.Core.VarInfo.Type.STATE;
				 v1.ValueType = VarInfoValueTypes.GetInstanceForName("Double");
				 _parameters0_0.Add(v1);
				mo0_0.Parameters=_parameters0_0;
				//Inputs
				List<PropertyDescription> _inputs0_0 = new List<PropertyDescription>();
				PropertyDescription pd1 = new PropertyDescription();
				pd1.DomainClassType = typeof(SiriusQualityPhenology.PhenologyState);
				pd1.PropertyName = "ListGAITTWindowForPTQ";
				pd1.PropertyType = (( SiriusQualityPhenology.PhenologyStateVarInfo.ListGAITTWindowForPTQ)).ValueType.TypeForCurrentValue;
				pd1.PropertyVarInfo =( SiriusQualityPhenology.PhenologyStateVarInfo.ListGAITTWindowForPTQ);
				_inputs0_0.Add(pd1);
				PropertyDescription pd2 = new PropertyDescription();
				pd2.DomainClassType = typeof(SiriusQualityPhenology.PhenologyState);
				pd2.PropertyName = "ListTTShootTTWindowForPTQ";
				pd2.PropertyType = (( SiriusQualityPhenology.PhenologyStateVarInfo.ListTTShootTTWindowForPTQ)).ValueType.TypeForCurrentValue;
				pd2.PropertyVarInfo =( SiriusQualityPhenology.PhenologyStateVarInfo.ListTTShootTTWindowForPTQ);
				_inputs0_0.Add(pd2);
				PropertyDescription pd3 = new PropertyDescription();
				pd3.DomainClassType = typeof(SiriusQualityPhenology.PhenologyState);
				pd3.PropertyName = "GAI";
				pd3.PropertyType = (( SiriusQualityPhenology.PhenologyStateVarInfo.GAI)).ValueType.TypeForCurrentValue;
				pd3.PropertyVarInfo =( SiriusQualityPhenology.PhenologyStateVarInfo.GAI);
				_inputs0_0.Add(pd3);
				PropertyDescription pd4 = new PropertyDescription();
				pd4.DomainClassType = typeof(SiriusQualityPhenology.PhenologyState);
				pd4.PropertyName = "DeltaTT";
				pd4.PropertyType = (( SiriusQualityPhenology.PhenologyStateVarInfo.DeltaTT)).ValueType.TypeForCurrentValue;
				pd4.PropertyVarInfo =( SiriusQualityPhenology.PhenologyStateVarInfo.DeltaTT);
				_inputs0_0.Add(pd4);
				PropertyDescription pd5 = new PropertyDescription();
				pd5.DomainClassType = typeof(SiriusQualityPhenology.PhenologyState);
				pd5.PropertyName = "pastGAI";
				pd5.PropertyType = (( SiriusQualityPhenology.PhenologyStateVarInfo.pastGAI)).ValueType.TypeForCurrentValue;
				pd5.PropertyVarInfo =( SiriusQualityPhenology.PhenologyStateVarInfo.pastGAI);
				_inputs0_0.Add(pd5);
				mo0_0.Inputs=_inputs0_0;
				//Outputs
				List<PropertyDescription> _outputs0_0 = new List<PropertyDescription>();
				PropertyDescription pd6 = new PropertyDescription();
				pd6.DomainClassType = typeof(SiriusQualityPhenology.PhenologyState);
				pd6.PropertyName = "ListGAITTWindowForPTQ";
				pd6.PropertyType =  (( SiriusQualityPhenology.PhenologyStateVarInfo.ListGAITTWindowForPTQ)).ValueType.TypeForCurrentValue;
				pd6.PropertyVarInfo =(  SiriusQualityPhenology.PhenologyStateVarInfo.ListGAITTWindowForPTQ);
				_outputs0_0.Add(pd6);
				PropertyDescription pd7 = new PropertyDescription();
				pd7.DomainClassType = typeof(SiriusQualityPhenology.PhenologyState);
				pd7.PropertyName = "ListTTShootTTWindowForPTQ";
				pd7.PropertyType =  (( SiriusQualityPhenology.PhenologyStateVarInfo.ListTTShootTTWindowForPTQ)).ValueType.TypeForCurrentValue;
				pd7.PropertyVarInfo =(  SiriusQualityPhenology.PhenologyStateVarInfo.ListTTShootTTWindowForPTQ);
				_outputs0_0.Add(pd7);
				PropertyDescription pd8 = new PropertyDescription();
				pd8.DomainClassType = typeof(SiriusQualityPhenology.PhenologyState);
				pd8.PropertyName = "GAImean";
				pd8.PropertyType =  (( SiriusQualityPhenology.PhenologyStateVarInfo.GAImean)).ValueType.TypeForCurrentValue;
				pd8.PropertyVarInfo =(  SiriusQualityPhenology.PhenologyStateVarInfo.GAImean);
				_outputs0_0.Add(pd8);
				PropertyDescription pd9 = new PropertyDescription();
				pd9.DomainClassType = typeof(SiriusQualityPhenology.PhenologyState);
				pd9.PropertyName = "pastGAI";
				pd9.PropertyType =  (( SiriusQualityPhenology.PhenologyStateVarInfo.pastGAI)).ValueType.TypeForCurrentValue;
				pd9.PropertyVarInfo =(  SiriusQualityPhenology.PhenologyStateVarInfo.pastGAI);
				_outputs0_0.Add(pd9);
				mo0_0.Outputs=_outputs0_0;
				//Associated strategies
				List<string> lAssStrat0_0 = new List<string>();
				mo0_0.AssociatedStrategies = lAssStrat0_0;
				//Adding the modeling options to the modeling options manager
				_modellingOptionsManager = new ModellingOptionsManager(mo0_0);
			
				SetStaticParametersVarInfoDefinitions();
				SetPublisherData();
					
			}



			/// <summary>
			/// Description of the model
			/// </summary>
			public string Description
			{
				get { return "Calculate Average Green Area Index on the TTWindowForPTQ thermal time periode"; }
			}
			
			/// <summary>
			/// URL to access the description of the model
			/// </summary>
			public string URL
			{
				get { return "http://biomamodelling.org"; }
			}
		


			/// <summary>
			/// Domain of the model.
			/// </summary>
			public string Domain
			{
				get {  return "Crop"; }
			}

			/// <summary>
			/// Type of the model.
			/// </summary>
			public string ModelType
			{
				get { return "Development"; }
			}

			/// <summary>
			/// Declare if the strategy is a ContextStrategy, that is, it contains logic to select a strategy at run time. 
			/// </summary>
			public bool IsContext
			{
					get { return  false; }
			}

			/// <summary>
			/// Timestep to be used with this strategy
			/// </summary>
			public IList<int> TimeStep
			{
				get
				{
					IList<int> ts = new List<int>();
					
					return ts;
				}
			}
	

			private PublisherData _pd;
			private  void SetPublisherData()
			{
					// Set publishers' data
					
				_pd = new CRA.ModelLayer.MetadataTypes.PublisherData();
				_pd.Add("Creator", "loic.manceau@inra.fr");
				_pd.Add("Date", "6/4/2018");
				_pd.Add("Publisher", "INRA");
			}

			public PublisherData PublisherData
			{
				get { return _pd; }
			}


			private ModellingOptionsManager _modellingOptionsManager;
			
			public ModellingOptionsManager ModellingOptionsManager
			{
				get { return _modellingOptionsManager; }            
			}


			/// <summary>
			/// Return the types of the domain classes used by the strategy
			/// </summary>
			/// <returns></returns>
			public IEnumerable<Type> GetStrategyDomainClassesTypes()
			{
				return new List<Type>() {  typeof(SiriusQualityPhenology.PhenologyState),typeof(SiriusQualityPhenology.PhenologyState),typeof(CRA.AgroManagement.ActEvents) };
			}


			
			// Getter and setters for the value of the parameters of the strategy. The actual parameters are stored into the ModelingOptionsManager of the strategy.

			
			public Double TTWindowForPTQ
			{ 
				get {
						VarInfo vi= _modellingOptionsManager.GetParameterByName("TTWindowForPTQ");
						if (vi != null && vi.CurrentValue!=null) return (Double)vi.CurrentValue ;
						else throw new Exception("Parameter 'TTWindowForPTQ' not found (or found null) in strategy 'CalculateGAImean'");
				 } set {
							VarInfo vi = _modellingOptionsManager.GetParameterByName("TTWindowForPTQ");
							if (vi != null)  vi.CurrentValue=value;
						else throw new Exception("Parameter 'TTWindowForPTQ' not found in strategy 'CalculateGAImean'");
				}
			}

			// Getter and setters for the value of the parameters of a composite strategy
			
	

			
            /// <summary>
            /// Set parameter(s) current values to the default value
            /// </summary>
            public void SetParametersDefaultValue()
            {
				_modellingOptionsManager.SetParametersDefaultValue();
				 

					//GENERATED CODE END - PLACE YOUR CUSTOM CODE BELOW - Section5
					//Code written below will not be overwritten by a future code generation

					//Custom initialization of the parameter. E.g. initialization of the array dimensions of array parameters

					//End of custom code. Do not place your custom code below. It will be overwritten by a future code generation.
					//PLACE YOUR CUSTOM CODE ABOVE - GENERATED CODE START - Section5 
            }

	

			// Define the properties of the static VarInfo of the parameters
			private static void SetStaticParametersVarInfoDefinitions()
			{                                
                TTWindowForPTQVarInfo.Name = "TTWindowForPTQ";
				TTWindowForPTQVarInfo.Description =" Thermal time window in which averages are computed";
				TTWindowForPTQVarInfo.MaxValue = 70000;
				TTWindowForPTQVarInfo.MinValue = 0;
				TTWindowForPTQVarInfo.DefaultValue = 70;
				TTWindowForPTQVarInfo.Units = "°Cd";
				TTWindowForPTQVarInfo.ValueType = CRA.ModelLayer.Core.VarInfoValueTypes.GetInstanceForName("Double");

				
       
			}

			//Parameters static VarInfo list 
			
				private static VarInfo _TTWindowForPTQVarInfo= new VarInfo();
				/// <summary> 
				///TTWindowForPTQ VarInfo definition
				/// </summary>
				public static VarInfo TTWindowForPTQVarInfo
				{
					get { return _TTWindowForPTQVarInfo; }
				}					
			
			//Parameters static VarInfo list of the composite class
						
	

		    /// <summary>
			/// Test to verify the postconditions
			/// </summary>
			public string TestPostConditions(SiriusQualityPhenology.PhenologyState phenologystate,SiriusQualityPhenology.PhenologyState phenologystate1, string callID)
			{
				try
				{
					//Set current values of the outputs to the static VarInfo representing the output properties of the domain classes				
					
					SiriusQualityPhenology.PhenologyStateVarInfo.ListGAITTWindowForPTQ.CurrentValue=phenologystate.ListGAITTWindowForPTQ;
					SiriusQualityPhenology.PhenologyStateVarInfo.ListTTShootTTWindowForPTQ.CurrentValue=phenologystate.ListTTShootTTWindowForPTQ;
					SiriusQualityPhenology.PhenologyStateVarInfo.GAImean.CurrentValue=phenologystate.GAImean;
					SiriusQualityPhenology.PhenologyStateVarInfo.pastGAI.CurrentValue=phenologystate.pastGAI;
					
					//Create the collection of the conditions to test
					ConditionsCollection prc = new ConditionsCollection();
					Preconditions pre = new Preconditions();            
					
					
					RangeBasedCondition r6 = new RangeBasedCondition(SiriusQualityPhenology.PhenologyStateVarInfo.ListGAITTWindowForPTQ);
					if(r6.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.PhenologyStateVarInfo.ListGAITTWindowForPTQ.ValueType)){prc.AddCondition(r6);}
					RangeBasedCondition r7 = new RangeBasedCondition(SiriusQualityPhenology.PhenologyStateVarInfo.ListTTShootTTWindowForPTQ);
					if(r7.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.PhenologyStateVarInfo.ListTTShootTTWindowForPTQ.ValueType)){prc.AddCondition(r7);}
					RangeBasedCondition r8 = new RangeBasedCondition(SiriusQualityPhenology.PhenologyStateVarInfo.GAImean);
					if(r8.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.PhenologyStateVarInfo.GAImean.ValueType)){prc.AddCondition(r8);}
					RangeBasedCondition r9 = new RangeBasedCondition(SiriusQualityPhenology.PhenologyStateVarInfo.pastGAI);
					if(r9.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.PhenologyStateVarInfo.pastGAI.ValueType)){prc.AddCondition(r9);}

					

					//GENERATED CODE END - PLACE YOUR CUSTOM CODE BELOW - Section4
					//Code written below will not be overwritten by a future code generation

        

					//End of custom code. Do not place your custom code below. It will be overwritten by a future code generation.
					//PLACE YOUR CUSTOM CODE ABOVE - GENERATED CODE START - Section4 

					//Get the evaluation of postconditions
					string postConditionsResult =pre.VerifyPostconditions(prc, callID);
					//if we have errors, send it to the configured output 
					if(!string.IsNullOrEmpty(postConditionsResult)) { pre.TestsOut(postConditionsResult, true, "PostConditions errors in component SiriusQualityPhenology.Strategies, strategy " + this.GetType().Name ); }
					return postConditionsResult;
				}
				catch (Exception exception)
				{
					//Uncomment the next line to use the trace
					//TraceStrategies.TraceEvent(System.Diagnostics.TraceEventType.Error, 1001,	"Strategy: " + this.GetType().Name + " - Unhandled exception running post-conditions");

					string msg = "Component SiriusQualityPhenology.Strategies, " + this.GetType().Name + ": Unhandled exception running post-condition test. ";
					throw new Exception(msg, exception);
				}
			}

			/// <summary>
			/// Test to verify the preconditions
			/// </summary>
			public string TestPreConditions(SiriusQualityPhenology.PhenologyState phenologystate,SiriusQualityPhenology.PhenologyState phenologystate1, string callID)
			{
				try
				{
					//Set current values of the inputs to the static VarInfo representing the input properties of the domain classes				
					
					SiriusQualityPhenology.PhenologyStateVarInfo.ListGAITTWindowForPTQ.CurrentValue=phenologystate.ListGAITTWindowForPTQ;
					SiriusQualityPhenology.PhenologyStateVarInfo.ListTTShootTTWindowForPTQ.CurrentValue=phenologystate.ListTTShootTTWindowForPTQ;
					SiriusQualityPhenology.PhenologyStateVarInfo.GAI.CurrentValue=phenologystate.GAI;
					SiriusQualityPhenology.PhenologyStateVarInfo.DeltaTT.CurrentValue=phenologystate.DeltaTT;
					SiriusQualityPhenology.PhenologyStateVarInfo.pastGAI.CurrentValue=phenologystate.pastGAI;

					//Create the collection of the conditions to test
					ConditionsCollection prc = new ConditionsCollection();
					Preconditions pre = new Preconditions();
            
					
					RangeBasedCondition r1 = new RangeBasedCondition(SiriusQualityPhenology.PhenologyStateVarInfo.ListGAITTWindowForPTQ);
					if(r1.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.PhenologyStateVarInfo.ListGAITTWindowForPTQ.ValueType)){prc.AddCondition(r1);}
					RangeBasedCondition r2 = new RangeBasedCondition(SiriusQualityPhenology.PhenologyStateVarInfo.ListTTShootTTWindowForPTQ);
					if(r2.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.PhenologyStateVarInfo.ListTTShootTTWindowForPTQ.ValueType)){prc.AddCondition(r2);}
					RangeBasedCondition r3 = new RangeBasedCondition(SiriusQualityPhenology.PhenologyStateVarInfo.GAI);
					if(r3.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.PhenologyStateVarInfo.GAI.ValueType)){prc.AddCondition(r3);}
					RangeBasedCondition r4 = new RangeBasedCondition(SiriusQualityPhenology.PhenologyStateVarInfo.DeltaTT);
					if(r4.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.PhenologyStateVarInfo.DeltaTT.ValueType)){prc.AddCondition(r4);}
					RangeBasedCondition r5 = new RangeBasedCondition(SiriusQualityPhenology.PhenologyStateVarInfo.pastGAI);
					if(r5.ApplicableVarInfoValueTypes.Contains( SiriusQualityPhenology.PhenologyStateVarInfo.pastGAI.ValueType)){prc.AddCondition(r5);}
					prc.AddCondition(new RangeBasedCondition(_modellingOptionsManager.GetParameterByName("TTWindowForPTQ")));

					

					//GENERATED CODE END - PLACE YOUR CUSTOM CODE BELOW - Section3
					//Code written below will not be overwritten by a future code generation

        

					//End of custom code. Do not place your custom code below. It will be overwritten by a future code generation.
					//PLACE YOUR CUSTOM CODE ABOVE - GENERATED CODE START - Section3 
								
					//Get the evaluation of preconditions;					
					string preConditionsResult =pre.VerifyPreconditions(prc, callID);
					//if we have errors, send it to the configured output 
					if(!string.IsNullOrEmpty(preConditionsResult)) { pre.TestsOut(preConditionsResult, true, "PreConditions errors in component SiriusQualityPhenology.Strategies, strategy " + this.GetType().Name ); }
					return preConditionsResult;
				}
				catch (Exception exception)
				{
					//Uncomment the next line to use the trace
					//	TraceStrategies.TraceEvent(System.Diagnostics.TraceEventType.Error, 1002,"Strategy: " + this.GetType().Name + " - Unhandled exception running pre-conditions");

					string msg = "Component SiriusQualityPhenology.Strategies, " + this.GetType().Name + ": Unhandled exception running pre-condition test. ";
					throw new Exception(msg, exception);
				}
			}

	
		


		 	/// <summary>
			/// Run the strategy to calculate the outputs. In case of error during the execution, the preconditions tests are executed.
			/// </summary>
			public void Estimate(SiriusQualityPhenology.PhenologyState phenologystate,SiriusQualityPhenology.PhenologyState phenologystate1,CRA.AgroManagement.ActEvents actevents)
			{
				try
				{
					CalculateModel(phenologystate,phenologystate1,actevents);

					//Uncomment the next line to use the trace
					//TraceStrategies.TraceEvent(System.Diagnostics.TraceEventType.Verbose, 1005,"Strategy: " + this.GetType().Name + " - Model executed");
				}
				catch (Exception exception)
				{
					//Uncomment the next line to use the trace
					//TraceStrategies.TraceEvent(System.Diagnostics.TraceEventType.Error, 1003,		"Strategy: " + this.GetType().Name + " - Unhandled exception running model");

					string msg = "Error in component SiriusQualityPhenology.Strategies, strategy: " + this.GetType().Name + ": Unhandled exception running model. "+exception.GetType().FullName+" - "+exception.Message;				
					throw new Exception(msg, exception);
				}
			}

		

			private void CalculateModel(SiriusQualityPhenology.PhenologyState phenologystate,SiriusQualityPhenology.PhenologyState phenologystate1,CRA.AgroManagement.ActEvents actevents)
			{				
				

				//GENERATED CODE END - PLACE YOUR CUSTOM CODE BELOW - Section1
				//Code written below will not be overwritten by a future code generation

                double dTTshoot = phenologystate.DeltaTT;
                double dailyGAI = phenologystate.GAI;

                List<double> TTList = new List<double>();
                List<double> GAIList = new List<double>();

                for (int i = 0; i < phenologystate1.ListTTShootTTWindowForPTQ.Count; i++)
                {
                    TTList.Add(phenologystate1.ListTTShootTTWindowForPTQ[i]);
                    GAIList.Add(phenologystate1.ListGAITTWindowForPTQ[i]);
                }


                TTList.Add(dTTshoot);
                GAIList.Add(dailyGAI);



                double SumTT=TTList.Sum();
                int count=0;

                while (SumTT > TTWindowForPTQ /*+ dTTshoot*/)
                {

                    SumTT -=TTList[count];
                    count++;
                }

                phenologystate.ListTTShootTTWindowForPTQ = new List<double>();
                phenologystate.ListGAITTWindowForPTQ = new List<double>();

                for (int i = count; i < TTList.Count; i++)
                {
                    phenologystate.ListTTShootTTWindowForPTQ.Add(TTList[i]);
                    phenologystate.ListGAITTWindowForPTQ.Add(GAIList[i]);
                }

                double GAI = Math.Max(phenologystate1.pastGAI, phenologystate.ListGAITTWindowForPTQ.Average());
                phenologystate.pastGAI = GAI;
                phenologystate.GAImean = GAI;

				//End of custom code. Do not place your custom code below. It will be overwritten by a future code generation.
				//PLACE YOUR CUSTOM CODE ABOVE - GENERATED CODE START - Section1 
			}

			


				//GENERATED CODE END - PLACE YOUR CUSTOM CODE BELOW - Section2
				//Code written below will not be overwritten by a future code generation

				//End of custom code. Do not place your custom code below. It will be overwritten by a future code generation.
				//PLACE YOUR CUSTOM CODE ABOVE - GENERATED CODE START - Section2 
	}
}
