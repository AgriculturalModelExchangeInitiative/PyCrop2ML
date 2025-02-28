/*
 * SIMPLACE - Scientific Impact assessment and Modeling PLattform for Advanced Crop and Ecosystem management
 *
 * This file is part of the SIMPLACE (before SMILEUtil) project.
 *
 * SIMPLACE is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * SIMPLACE is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with SIMPLACE.  If not, see <http://www.gnu.org/licenses/>.
 *
 * STMPsimCalculator.java
 *
 * Responsible developers: Gunther Krauss, Crop Science Group, Katzenburgweg 5, 53115 Bonn, Germany
 *                         Andreas Enders, Crop Science Group, Katzenburgweg 5, 53115 Bonn, Germany
 * Contact Information:    lapit@uni-bonn.de
 * More information on <http://www.simplace.net>
 */

package SoilTemperature.original;

import static java.lang.StrictMath.*;

import net.simplace.sim.model.FWSimComponent;
import net.simplace.sim.util.FWSimVarMap;
import net.simplace.sim.util.FWSimVariable;
import net.simplace.sim.util.FWSimVariable.CONTENT_TYPE;
import net.simplace.sim.util.FWSimVariable.DATA_TYPE;

import java.util.HashMap;

import org.jdom2.Element;


/**
 *
 * Calculates the soil temperature in n layers depending on climate and soil conditions.
 *
 * WIKI_START
 *
 * === STMP ===
 * Soil temperature of the soil layers is calculated using the formula:
 * WIKI_END
 * \[
 * \begin{eqnarray}
 * STMP&=&LAG \cdot STMP0+(1.0-LAG) \cdot (FZ \cdot (AVT-DST0)+DST0)   \label{stmp}
 * \end{eqnarray}
 * \]
 * WIKI_START
 *
 * === Reference: ===
 * Williams, J.R., Izaurralde, C.A., 2005.
 * The APEX model, Blackland Research Center Reports, Vol. 2. Blackland Research Center, USDA, Temple, Texas, USA
 *
 *  === STMP calculation ===
 * Daily average soil temperature at the center of each soil layer is simulated for use in nutrient cycling and hydrology.
 * The basic soil temperature equation is shown in Eq \(\eqref{stmp}\) with
 *
 * WIKI_END
 * \[
 * \begin{eqnarray}
 *  FZ&=&\frac{X1}{X1+\exp(-0.8669-2.0775 \cdot X1)}    \\
 *  X1&=&0.5 \cdot \frac{Z(l)+Z(l-1)}{DD}              \label{x1}
 * \end{eqnarray}
 * \]
 * WIKI_START
 *
 * where
 * STMP is the soil temperature at the center of a soil layer in °C,
 * Z is the depth from the surface to the bottom of the soil layer l in m,
 * LAG is a coefficient ranging from 0.0 to 1.0 that allows proper weighting of yesterday's temperature STMP0,
 * AVT is the long-term average annual air temperature at the site,
 * DST0 is the soil surface temperature, and DD is the damping depth in m.
 * Thus, given yesterday's temperature,
 * Eq \(\eqref{stmp}\) estimates today's temperature as a function of soil surface temperature, depth, and a lag coefficient.
 * It is assumed that the temperature remains almost constant at the damping depth and is approximately AVT.
 * Obviously, Eq \(\eqref{stmp}\) makes near surface temperatures a strong function of DST0.
 * As depth increases, AVT has more influence until finally at the damping depth, the temperature is within 5% of AVT.
 *
 * The damping depth is a function of soil bulk density and water content as expressed in the equation
 *
 * WIKI_END
 * \[
 * \begin{eqnarray}
 *     DD&=&DP \cdot \exp(\ln(\frac{0.5}{DP}) \cdot \frac{1.-WC}{1.+WC} \cdot 2)      \\
 *     DP&=&1.+\frac{2.5 \cdot ABD}{ABD+\exp(6.53-5.63 \cdot ABD)}        \\
 *     WC&=&0.001 \cdot \frac{ST}{Z(n) \cdot (0.356-0.144 \cdot ABD)}
 * \end{eqnarray}
 * \]
 * WIKI_START
 *
 * where
 * DP is the maximum damping depth for the soil in m,
 * ABD is the average soil bulk density of the profile in t m-3,
 * n is the number of soil layers in the profile, and
 * ST is the water stored in the profile in mm.
 *
 * To complete the solution of Eq \(\eqref{stmp}\), the soil surface temperature must be estimated.
 * The first step is to estimate the bare soil surface temperature.
 *
 * WIKI_END
 * \[
 * \begin{eqnarray}
 *    DST&=&0.5 \cdot (TMX+TMN)+(TMX-TMN) \cdot \frac{RA \cdot (1.0-AB)-14.}{20}  \label{dst}
 * \end{eqnarray}
 * \]
 * WIKI_START
 *
 * The first term in \(\eqref{dst}\) estimates bare soil temperature to equal average daily air temperature.
 * The second term adjusts the basic estimate using the net radiation as a driver and half the temperature difference as a range.
 * The adjustment changes signs at a net radiation value of 14 MJ m-2 d-1.  If the soil surface is not bare, the surface temperature can be affected
 * considerably by the amount of cover (crop residue or snow).  This effect can be simulated
 * by combining the estimated bare surface temperature for the day with the previous day's temperature in the second soil layer
 *  (the top 10 mm layer is considered too thin for this purpose).
 *
 * WIKI_END
 * \[
 * \begin{eqnarray}
 *     DST0&=&(1.-BCV) \cdot DST+BCV \cdot STMP(2))
 * \end{eqnarray}
 * \]
 * WIKI_START
 *
 * where
 * DST0 is the final estimate of soil surface temperature in °C and
 * BCV is a lagging factor for simulating residue and snow cover effects on surface temperature.
 *
 * This is done using the SnowCoverCalculator SimComponent that can therefore be linked
 * using the outputted SoilTemperature array and delivering the SoilSurfaceTemperature (DST0)
 * WIKI_END
 *
 * @author Andreas Enders
 * @author Gunther Krauss
 *
 */
public class STMPsimCalculator extends FWSimComponent
{
	private FWSimVariable<Double[]> SoilTempArray;
	private FWSimVariable<Double[]> cSoilLayerDepth;
	private FWSimVariable<Double> cFirstDayMeanTemp;
	private FWSimVariable<Double> cDampingDepth;
	private FWSimVariable<Double> cABD;
	private FWSimVariable<Double> cAVT;

	private FWSimVariable<Double[]> pSoilLayerDepth;
	private FWSimVariable<Double> iSoilWaterContent;
	private FWSimVariable<Double> iSoilSurfaceTemperature;
	private FWSimVariable<Boolean> iDoInitialize;

	/**
	 * Called by clone method only
	 * @param aName
	 * @param aFieldMap
	 * @param aInputMap
	 * @param aSimComponentElement
	 * @param aVarMap
	 */
	private STMPsimCalculator(String aName, HashMap<String, FWSimVariable<?>> aFieldMap,
			HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)
	{
		super(aName, aFieldMap, aInputMap, aSimComponentElement, aVarMap, aOrderNumber);
	}

	/**
	 * Empty constructor used by class.forName()
	 */
	public STMPsimCalculator()
	{
		super();
	}

	/**
	 * create the FWSimVariables as interface for this SimComponent
	 *
	 * @see net.simplace.sim.model.FWSimComponent#createVariables()
	 */
	@Override
	public HashMap<String, FWSimVariable<?>> createVariables()
	{
		addVariable(FWSimVariable.createSimVariable("cSoilLayerDepth", "Depth of soil layer", DATA_TYPE.DOUBLEARRAY,
				CONTENT_TYPE.constant, "http://www.wurvoc.org/vocabularies/om-1.8/metre", 0.03, 20d, null, this));
		addVariable(FWSimVariable.createSimVariable("cFirstDayMeanTemp", "Mean temperature on first day", DATA_TYPE.DOUBLE,
				CONTENT_TYPE.constant, "http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius", -40d, 50d, null, this));
		addVariable(FWSimVariable.createSimVariable("cAVT", "Constant Temperature of deepest soil layer", DATA_TYPE.DOUBLE,
				CONTENT_TYPE.constant, "http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius", -10d, 20d, null, this));
		addVariable(FWSimVariable.createSimVariable("cABD", "Mean bulk density", DATA_TYPE.DOUBLE,
				CONTENT_TYPE.constant, "http://www.wurvoc.org/vocabularies/om-1.8/tonne_per_cubic_metre", 1d, 4d, 2d, this));
		addVariable(FWSimVariable.createSimVariable("cDampingDepth", "Initial value for damping depth of soil", DATA_TYPE.DOUBLE,
				CONTENT_TYPE.constant, "http://www.wurvoc.org/vocabularies/om-1.8/metre", 1.5, 20d, 6d, this));
		
		//%%CyML Ignore Begin%%
		addVariable(FWSimVariable.createSimVariable("iDoInitialize", "Switch to re-initialize the model with initial values.",
				DATA_TYPE.BOOLEAN, CONTENT_TYPE.input, "http://www.wurvoc.org/vocabularies/om-1.8/one", null, null, false, this));
		//%%CyML Ignore End%%
		
		addVariable(FWSimVariable.createSimVariable("iSoilWaterContent", "Content of water in Soil", DATA_TYPE.DOUBLE,
				CONTENT_TYPE.input, "http://www.wurvoc.org/vocabularies/om-1.8/millimetre", 1.5, 20d, 5d, this));
		addVariable(FWSimVariable.createSimVariable("iSoilSurfaceTemperature", "Temperature at soil surface", DATA_TYPE.DOUBLE,
				CONTENT_TYPE.input, "http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius", 1.5, 20d, null, this));
		addVariable(FWSimVariable.createSimVariable("SoilTempArray", "Array of temperature ", DATA_TYPE.DOUBLEARRAY,
				CONTENT_TYPE.state, "http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius", -20, 40, null, this));

		addVariable(FWSimVariable.createSimVariable("pSoilLayerDepth", "Depth of soil layer plus additional depth", DATA_TYPE.DOUBLEARRAY,
				CONTENT_TYPE.privat, "http://www.wurvoc.org/vocabularies/om-1.8/metre", 0.03, 20d, null, this));
		return iFieldMap;
	}

	/**
	 * initializes the fields by getting input and output FWSimVariables from VarMap
	 *
	 * @see net.simplace.sim.model.FWSimComponent#init()

	 * Z(IndexOfSoilLayer) = Depth to the bottom of the soil layer L (m)
	 * ABD = Average bulk density over all layers in the soil profile (t m-3)
	 * AVT = Annual mean air temperature at 2 m (Â°C)
	 * STMP = SoilTemperature of layer (Â°C)
	 */
	@Override
	protected void init()
	{
    Double[] Z = cSoilLayerDepth.getValue();
    double tProfileDepth = Z[Z.length-1];
    Double firstDayMeanTemp = cFirstDayMeanTemp.getValue();
		Double additionalDepth = cDampingDepth.getValue() - tProfileDepth;
		Double firstAdditionalLayerHight = additionalDepth - floor(additionalDepth);
		Integer layers = (int)(abs(ceil(additionalDepth)))+Z.length;
		Double[] tStmp = new Double[layers];
		Double[] tz = new Double[layers];
		for (int i = 0; i < tStmp.length; i++)
		{
			double depth;
			if (i < Z.length)
			{
				depth = Z[i];
			}
			else //first additional layer might be smaller than 1 m
			{
				depth = tProfileDepth + firstAdditionalLayerHight + i - Z.length;
			}
			tz[i] = depth;
			tStmp[i] = (firstDayMeanTemp * (cDampingDepth.getValue() - depth) + cAVT.getValue() * depth) / cDampingDepth.getValue(); //set linear aproximation to the soil temperature as initial value
		}
		SoilTempArray.setValue( tStmp, this);
		pSoilLayerDepth.setValue(tz, this);
	}


	protected void reInitialize()
	{
	    init();
	}


	/**
	 *  process the algorithm and write the results back to VarMap
	 *
	 * TMX = Maximum air temperature at 2 m (Â°C)
	 * TMN = Minimum air temperature at 2 m (Â°C)
	 * RA = RA(t) = Mean daily solar radiation on day t (kJ/m2*d)
	 * PREC = Precipitation on day t (mm)
	 * CV = Crop residues plus above ground biomass (kg/ha)
	 * SNO = Water content in snow layer (mm)
	 * SW = ST(t) = Soil water stored in the soil profile at day t (mm)
	 * SLA = Leaf area index (m*m-1)
	 * PEVAP = Potential soil evaporation (mm)

	 * @see net.simplace.sim.model.FWSimComponent#process()
	 */
	@Override
	protected void process()
	{
		//%%CyML Ignore Begin%%
		if(iDoInitialize.getValue()) 
			reInitialize();
		//%%CyML Ignore End%%

		Double[] tZp = pSoilLayerDepth.getValue();
		Double[] tZc = cSoilLayerDepth.getValue();
		double XLAG =.8; //XLAG = LAG = Coefficient for weighting yesterday's soil temperature
		double XLG1 = 1 - XLAG; //XLG1 = Inverse of coefficient for weighting yesterday's soil temperature
		double DP = (1 + 2.5*cABD.getValue()/(cABD.getValue() + exp(6.53-5.63*cABD.getValue()))); //DP= Maximum damping depth (m)
		double WC = 0.001*iSoilWaterContent.getValue()/((.356 -.144*cABD.getValue())*tZc[tZc.length - 1]); //WC seems to be a water content related factor [cm3/g] to modify the damping depth ?
		double DD = exp(log(0.5/DP)*((1 - WC)/(1 + WC))*2)*DP; //DD(t)= Damping depth (m), multiplied by 2 (20110628 TG) to increase damping depth
		// DD could be also calculated from d = (2Dh /w )^0.5 (easy soilT, Nofziger et al.), where w = 2Pi/365 (d^-1)
		//and Dh is the thermal diffusivity (m^2 s^-l) with  ( Dh= K/Cs, Cs = volumetric heat capacity in J m^-3 K^-1, K=??)

		double Z1 = 0; //Z1=Depth of the bottom of the previous soil layer, initialized with 0 (m)
		for (int i = 0; i < SoilTempArray.getValue().length; i++)
		{
			double ZD = 0.5*(Z1 + tZp[i])/DD;
				//Factor of the depth in soil: Middle of depth of layer divided by damping depth
			double RATE = ZD / (ZD + exp(-.8669 - 2.0775 * ZD)) * (cAVT.getValue() - iSoilSurfaceTemperature.getValue());
				//RATE = Rate of change of STMP(ISL) (Â°C)
			SoilTempArray.setArrayValue(i, XLAG * SoilTempArray.getValue()[i] + XLG1 * (RATE + iSoilSurfaceTemperature.getValue()), this);
			Z1 = tZp[i];
		}


	}


	/**
	 * called for single component test to check the components algorithm. 
	 * 
	 * aParamIndex: Used to set up different test cases. Start with 0 - result check with 1 aso
	 *
	 * @see net.simplace.sim.util.FWSimFieldContainer#fillTestVariables(int aParamIndex, TEST_STATE aDefineOrCheck)
	 */
	public HashMap<String, FWSimVariable<?>> fillTestVariables(int aTestIndex, TEST_STATE aDefineOrCheck)
	{
		if(aTestIndex == 0 && aDefineOrCheck == TEST_STATE.DEFINE) //before process
		{
			FWSimVariable.setValue(new Double[]{0.1,0.5,1.5}, iFieldMap.get("STMPsimCalculator.cSoilLayerDepth"), this);
			FWSimVariable.setValue(15d, iFieldMap.get("STMPsimCalculator.cFirstDayMeanTemp"), this);
			FWSimVariable.setValue(9d, iFieldMap.get("STMPsimCalculator.cAVT"), this);
			FWSimVariable.setValue(1.4, iFieldMap.get("STMPsimCalculator.cABD"), this);
			FWSimVariable.setValue(6d, iFieldMap.get("STMPsimCalculator.cDampingDepth"), this);
			FWSimVariable.setValue(0.3, iFieldMap.get("STMPsimCalculator.iSoilWaterContent"), this);
			FWSimVariable.setValue(6d, iFieldMap.get("STMPsimCalculator.iSoilSurfaceTemperature"), this);
		}
		else if(aTestIndex == 0 && aDefineOrCheck == TEST_STATE.CHECK) //after process
		{
			FWSimVariable.setValue(new Double[]{13.624360856350041, 13.399968504634286, 12.599999999999845, 12.2, 11.4, 10.6, 9.799999999999999, 9.0}, iFieldMap.get("STMPsimCalculator.SoilTempArray"), this);
		}
		else return null;
		return iFieldMap;
	}
	
	/**
	 *
	 * @see net.simplace.sim.model.FWSimComponent#clone(net.simplace.sim.util.FWSimVarMap)
	 */
	@Override
	protected FWSimComponent clone(FWSimVarMap aVarMap)
	{
		return new STMPsimCalculator(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);
	}
}

