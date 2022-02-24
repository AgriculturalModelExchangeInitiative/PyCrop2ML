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
 * SnowCoverCalculator.java
 *
 * Responsible developers: Gunther Krauss, Crop Science Group, Katzenburgweg 5, 53115 Bonn, Germany
 *                         Andreas Enders, Crop Science Group, Katzenburgweg 5, 53115 Bonn, Germany
 * Contact Information:    lapit@uni-bonn.de
 * More information on <http://www.simplace.net>
 */

package net.simplace.sim.components.soil.temperature;

import static java.lang.StrictMath.*;

import net.simplace.sim.model.FWSimComponent;
import net.simplace.sim.util.FWSimVarMap;
import net.simplace.sim.util.FWSimVariable;
import net.simplace.sim.util.FWSimVariable.CONTENT_TYPE;
import net.simplace.sim.util.FWSimVariable.DATA_TYPE;

import java.util.HashMap;

import org.jdom.Element;


/**
 *
 * Calculates the snow cover, first soil layer temperature and biomass on ground factor depending on climate and soil conditions.
 *
 * WIKI_START
 *
 * === Snow Cover ===
 *
 * Snow Cover is calculated using the formula:
 *
 * WIKI_END
 * \[
 * \begin{eqnarray}
 *     DST0=(1.-BCV) \cdot  DST + BCV  \cdot STMP0
 * \end{eqnarray}
 * \]
 * WIKI_START
 *
 *  === Snow Cover calculation ===
 * If the soil surface is not bare, the surface temperature can be affected
 * considerably by the amount of cover (crop residue or snow).  This effect can be simulated
 * by combining the estimated bare surface temperature for the day with the previous day's temperature in the second soil layer
 *  (the top 10 mm layer is considered too thin for this purpose).
 *
 * where
 * DST0 is the final estimate of soil surface temperature in °C and
 * BCV is a lagging factor for simulating residue and snow cover effects on surface temperature.
 * The value of BCV is 0.0 for bare soil and approaches 1.0 as cover increases, as expressed in the equation
 * WIKI_END
 * \[
 * \begin{eqnarray}
 *    BCV &=& max(SNOF,BCV')  \\
 *    BCV' &=& \frac{CV}{CV+exp(5.34-2.40 \cdot CV)}	   \\
 *    SNOF &=& \frac{SNO}{SNO+exp(2.30-0.220 \cdot SNO)}
 * \end{eqnarray}
 * \]
 * WIKI_START
 * where
 * - CV is the sum of above ground biomass and crop residue in t ha-1 and
 * - SNO is the water content of the snow cover in mm.
 *
 * === Snow melt ===
 *
 * If snow is present, it may be melted on days when the second soil layer temperature exceeds 0 oC.
 * Snow is melted as a function of the snow pack temperature using the equation
 * WIKI_END
 *
 * \[
 * \begin{eqnarray}
 *      SML &=& max(0.,X1 \cdot (1.52+.54 \cdot F \cdot SNPKT)) \quad \text{for} \quad  0.0 \lt SML \lt SNO   \\
 *      SNPKT & =& .3333 \cdot (2. \cdot X2+TX)				                     \\
 *      X1 &=& \sqrt{TMX \cdot RA}					                           \\
 *      X2 &=& min(DST0,STMP(2))      			                    \\
 *      F &=& TSNO/(TSNO+exp(5.34-2.395 \cdot TSNO))
 * \end{eqnarray}
 * \]
 * WIKI_START
 * where
 *  - SML is the snowmelt rate in mm d-1,
 *  - SNO is the snow present in mm of water,
 *  - STMP is the temperature in oC of soil layer 2,
 *  - SNPKT is the snow pack temperature in oC,
 *  - DST0 is the soil surface temperature in oC, and
 *  - TSNO is the age of the snow pack in d.
 *
 * The equations for estimating STMP and DST0 are presented in the soil temperature section.
 * Melted snow is treated the same as rainfall for estimating runoff volume and percolation, but rainfall energy is set to 0.0 and peak runoff rate
 * is estimated by assuming uniformly distributed rainfall for a 24-h duration.
 *
 * === Snow evaporation ===
 *
 * EAJ is a soil cover index.  The value of EAJ ranges from 0 to 1.0 according to the equation
 * WIKI_END
 *
 * \[
 * \begin{eqnarray}
 *      EAJ & = & exp(-X1)    			                             \\
 *      X1 & = & max(0.4 \cdot SMLA,0.1 \cdot (CV+.1))
 * \end{eqnarray}
 * \]
 * WIKI_START
 * where
 *  - CV is the weight of all above ground plant material in t ha-1.
 *
 *  === Reference: ===
 *   Williams, J.R., Izaurralde, C.A., 2005.
 *   The APEX model, Blackland Research Center Reports, Vol. 2. Blackland Research Center, USDA, Temple, Texas, USA
 *
 * WIKI_END
 *
 * @author Andreas Enders
 * @author Gunther Krauss
 *
 */
public class SnowCoverCalculator extends FWSimComponent
{
	/*
	 * AGEOFSNOWC = Number of days since there is SNOWC > 5 mm (d)
	 * SNOWC = Snow cover water content (mm)
	 * ALB = AB(1) = Albedo index of radiation reflection of the first soil layer
	 */

	private FWSimVariable<Boolean> iDoInitialize;
	private FWSimVariable<Double> TMX;
	private FWSimVariable<Double> TMN;
	private FWSimVariable<Double> RA;
	private FWSimVariable<Double> PREC;
	private FWSimVariable<Double> CV;
	private FWSimVariable<Double> PEVAP;
	private FWSimVariable<Double> SLA;
	private FWSimVariable<Double[]> TSOIL;
	private FWSimVariable<Double> CARBON;

	private FWSimVariable<Double> SNOWC;
	private FWSimVariable<Double> SNOWC2;
	private FWSimVariable<Double> BCV;
	private FWSimVariable<Double> DST0;

	private FWSimVariable<Integer> AgeOfSnow;

	private FWSimVariable<Double> Albedo;

	/**
	 * called by clone method only
	 * @param aName
	 * @param aFieldMap
	 * @param aInputMap
	 * @param aSimComponentElement
	 * @param aVarMap
	 */
	private SnowCoverCalculator(String aName, HashMap<String, FWSimVariable<?>> aFieldMap,
			HashMap<String, String> aInputMap, Element aSimComponentElement, FWSimVarMap aVarMap, int aOrderNumber)
	{
		super(aName, aFieldMap, aInputMap, aSimComponentElement, aVarMap, aOrderNumber);
	}

	/**
	 * Empty constructor used by class.forName()
	 *
	 */
	public SnowCoverCalculator()
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
		addVariable(FWSimVariable.createSimVariable("cCarbonContent", "Carbon content of upper soil layer",
				DATA_TYPE.DOUBLE,
				CONTENT_TYPE.constant, "http://www.wurvoc.org/vocabularies/om-1.8/percent", 0d, 20d, 0.5, this));
		addVariable(FWSimVariable.createSimVariable("iDoInitialize", "Switch to re-initialize the model with initial values.",
				DATA_TYPE.BOOLEAN, CONTENT_TYPE.input, "http://www.wurvoc.org/vocabularies/om-1.8/one", null, null, false, this));
		addVariable(FWSimVariable.createSimVariable("iTempMax", "Daily maximum temperature", DATA_TYPE.DOUBLE,
				CONTENT_TYPE.input, "http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius", -40d, 50d, null, this));
		addVariable(FWSimVariable.createSimVariable("iTempMin", "Daily minimum temperature", DATA_TYPE.DOUBLE,
				CONTENT_TYPE.input, "http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius", -40d, 50d, null, this));
		addVariable(FWSimVariable.createSimVariable("iRadiation", "Solar radiation", DATA_TYPE.DOUBLE,
				CONTENT_TYPE.input, "http://www.wurvoc.org/vocabularies/om-1.8/megajoule_per_square_metre", 0d, 2000d, null, this));
		addVariable(FWSimVariable.createSimVariable("iRAIN", "Rain amount", DATA_TYPE.DOUBLE,
				CONTENT_TYPE.input, "http://www.wurvoc.org/vocabularies/om-1.8/millimetre", 0d, 60d, null, this));
		addVariable(FWSimVariable.createSimVariable("iCropResidues", "Crop residues plus above ground biomass", DATA_TYPE.DOUBLE,
				CONTENT_TYPE.input, "http://www.wurvoc.org/vocabularies/om-1.8/gram_per_square_metre", 0d, 20000d, null, this));
		addVariable(FWSimVariable.createSimVariable("iPotentialSoilEvaporation", "Potenial Evaporation", DATA_TYPE.DOUBLE,
				CONTENT_TYPE.input, "http://www.wurvoc.org/vocabularies/om-1.8/millimetre", 0d, 12d, null, this));
		addVariable(FWSimVariable.createSimVariable("iLeafAreaIndex", "Leaf area index", DATA_TYPE.DOUBLE,
				CONTENT_TYPE.input, "http://www.wurvoc.org/vocabularies/om-1.8/square_metre_per_square_metre", 0d, 10d, null, this));
		addVariable(FWSimVariable.createSimVariable("iSoilTempArray", "Soil Temp array of last day", DATA_TYPE.DOUBLEARRAY,
				CONTENT_TYPE.input, "http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius", -15d, 35d, null, this));
		addVariable(FWSimVariable.createSimVariable("Albedo", "Albedo", DATA_TYPE.DOUBLE,
				CONTENT_TYPE.out, "http://www.wurvoc.org/vocabularies/om-1.8/one", 0d, 1d, null, this));
		addVariable(FWSimVariable.createSimVariable("SnowWaterContent", "Snow water content", DATA_TYPE.DOUBLE,
				CONTENT_TYPE.out, "http://www.wurvoc.org/vocabularies/om-1.8/millimetre", 0d, 1500d, 0d, this));
		addVariable(FWSimVariable.createSimVariable("SnowIsolationIndex", "Snow isolation index", DATA_TYPE.DOUBLE,
				CONTENT_TYPE.out, "http://www.wurvoc.org/vocabularies/om-1.8/one", 0d, 1d, 0d, this));
		addVariable(FWSimVariable.createSimVariable("SoilSurfaceTemperature", "Soil surface temperature", DATA_TYPE.DOUBLE,
				CONTENT_TYPE.out, "http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius", -40d, 70d, 0d, this));
		addVariable(FWSimVariable.createSimVariable("AgeOfSnow", "Age of snow", DATA_TYPE.INT,
				CONTENT_TYPE.out, "http://www.wurvoc.org/vocabularies/om-1.8/one", 0, null, 0, this));
		return iFieldMap;
	}

	/**
	 * initializes the fields by getting input and output FWSimVariables from VarMap
	 *
	 * @see net.simplace.sim.model.FWSimComponent#init()
	 */
	@SuppressWarnings("unchecked")
	@Override
	protected void init()
	{
		TMX = (FWSimVariable<Double>) getVariable("iTempMax");
		TMN = (FWSimVariable<Double>) getVariable("iTempMin");
		RA = (FWSimVariable<Double>) getVariable("iRadiation");
		PREC = (FWSimVariable<Double>) getVariable("iRAIN");
		CV = (FWSimVariable<Double>) getVariable("iCropResidues");
		PEVAP = (FWSimVariable<Double>) getVariable("iPotentialSoilEvaporation");
		SLA = (FWSimVariable<Double>) getVariable("iLeafAreaIndex");
		TSOIL = (FWSimVariable<Double[]>) getVariable("iSoilTempArray");
		CARBON = (FWSimVariable<Double>) getVariable("cCarbonContent");
		SNOWC = (FWSimVariable<Double>) getVariable("SnowWaterContent");
		SNOWC.setDefaultValue();
		BCV = (FWSimVariable<Double>) getVariable("SnowIsolationIndex");
		BCV.setDefaultValue();
		DST0 = (FWSimVariable<Double>) getVariable("SoilSurfaceTemperature");
		DST0.setDefaultValue();
		AgeOfSnow.setDefaultValue();

		Albedo.setValue( 0.0226 * log10(CARBON.getValue()) + 0.1502, this); //taken from experimental fit from Thomas Gaiser, 2000, n=35, R2=0.97
	}


	protected void reInitialize()
	{
	    init();
	}



	/**
	 * process the algorithm and write the results back to VarMap
	 *
	 * @see net.simplace.sim.model.FWSimComponent#process()
	 */
	/*
	 * TMX = Maximum air temperature at 2 m (°C)
	 * TMN = Minimum air temperature at 2 m (°C)
	 * RA = RA(t) = Mean daily solar radiation on day t (kJ/m2*d)
	 * PREC = Precipitation on day t (mm)
	 * CV = crop residues plus above ground biomass (kg/ha)
	 * SNO = water content in snow layer (mm)
	 * SW = ST(t) = Soil water stored in the soil profile at day t (mm)
	 * SLA = leave area index (m*m-1)
	 * PEVAP = potential soil evaporation (mm)
	 * TSOIL = Soil temperature at topmost level (°C)
	 * PREC = Precipitation on day t (mm)
	 * SLA = leave area index (m*m-1)
	 * PEVAP = potential soil evaporation (mm)
	 */
	@Override
	protected void process()
	{

		if(iDoInitialize.getValue())
        {
            reInitialize();;
        }

		double tTMX = TMX.getValue();
		double tTMN = TMN.getValue();
		double tRA = RA.getValue();
		double tPREC = PREC.getValue();
		double tCV = CV.getValue()*10.0;  // convert from g/m^2 to kg/ha
		double tPEVAP = PEVAP.getValue();
		double tSLA = SLA.getValue();
		double tTSOIL = TSOIL.getValue()[0];

		double TMEAN = 0.5 * (tTMX + tTMN); //TMEAN = Mean daily air temperature at 2 m (°C)
		double TAMPL = 0.5 * (tTMX - tTMN); //TAMPL = Amplitude of daily air temperature at 2 m (°C)
		double DST = TMEAN + TAMPL * (tRA * (1 - Albedo.getValue()) - 14) / 20; //DST = Bare soil surface temperature (°C)

		double tDST0;
		double tBCV;
		double tSNOWC = SNOWC.getValue();
		int tAgeOfSnow = AgeOfSnow.getValue();
		double SNOWEVAPORATION;
		double SNOWMELT;

		if (tPREC > 0 && (tTSOIL < 1 || tSNOWC > 3 || DST0.getValue() < 0)) //adding new precipitation to snow cover
		{
			tSNOWC = tSNOWC + tPREC;
		}

		tBCV = 1d;
		if (tCV < 10)
		{
			tBCV = tCV / (tCV + exp(5.34 - 2.4 * tCV));
		}
		if (tSNOWC < 1E-10)
		{
			tBCV = tBCV * 0.85; //factor for no snow and crop cover
			tDST0 = 0.5 * (DST + (1 - tBCV) * DST + tBCV * tTSOIL); //DST0 = Actual soil surface temperature (°C), TSOIL = Yesterday's temperature in the first layer (°C)
		}
		else
		{
			tBCV = max(tSNOWC/(tSNOWC + exp(0.47 - 0.62*tSNOWC)), tBCV); //coefficients based on EPIC SCRP(17) values from PARM0509.file
			tDST0 = (1 - tBCV) * DST + tBCV * tTSOIL; //DST0 = Actual soil surface temperature (°C), TSOIL = Yesterday's temperature in the first layer (°C)
		}

		if (tSNOWC == 0 && !(tPREC > 0 && tTSOIL < 1))
		{
			tSNOWC = 0; // no snow cover possible}
		}

		else
		{
			double EAJ =.5; //EAJ = Soil cover index
			if (tSNOWC < 5) //Equation from EPIC documentation
			{
				EAJ = exp(-(max(0.4 * tSLA, 0.1 * (tCV + 0.1))));
			}
			SNOWEVAPORATION = tPEVAP*EAJ;

			double ageOfSnowFactor = tAgeOfSnow / (tAgeOfSnow + exp(5.34 - 2.395 * tAgeOfSnow));
			double SNPKT =.3333 * (2 * min(tDST0, tTSOIL) + tTMX); //SNPKT is the snow pack temperature (°C)
			if (TMEAN > 0)
			{
				SNOWMELT = max(0, sqrt(tTMX * tRA) * (1.52 +.54 * ageOfSnowFactor * SNPKT));
			}
			else
			{
				SNOWMELT = 0;
			}

			if (SNOWMELT + SNOWEVAPORATION > tSNOWC)
			{
				SNOWMELT = SNOWMELT / (SNOWMELT + SNOWEVAPORATION) * tSNOWC;
				SNOWEVAPORATION = SNOWEVAPORATION / (SNOWMELT + SNOWEVAPORATION) * tSNOWC;
			}
			tSNOWC = tSNOWC - (SNOWMELT + SNOWEVAPORATION);

			if (tSNOWC < 0) //no snow is minimum
			{
				tSNOWC = 0;
			}
			if (tSNOWC < 5)
			{
				tAgeOfSnow = 0;
			}
			else
			{
				tAgeOfSnow++;
				SNOWC2.setValue(tSNOWC,this);
			}
		}
		SNOWC.setValue(tSNOWC,this);
		BCV.setValue(tBCV, this);
		DST0.setValue(tDST0, this);
		AgeOfSnow.setValue(tAgeOfSnow, this);


	}

	/**
	 * creates a clone from this SimComponent for use in other threads
	 *
	 *
	 * @see net.simplace.sim.model.FWSimComponent#clone(net.simplace.sim.util.FWSimVarMap)
	 */
	@Override
	protected FWSimComponent clone(FWSimVarMap aVarMap)
	{
		return new SnowCoverCalculator(iName, iFieldMap, iInputMap, iSimComponentElement, aVarMap, iOrderNumber);
	}
}

