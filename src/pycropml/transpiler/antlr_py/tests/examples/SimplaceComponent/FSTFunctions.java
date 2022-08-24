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
 * FSTFunctions.java
 *
 * Responsible developers: Gunther Krauss, Crop Science Group, Katzenburgweg 5, 53115 Bonn, Germany
 *                         Andreas Enders, Crop Science Group, Katzenburgweg 5, 53115 Bonn, Germany
 * Contact Information:    lapit@uni-bonn.de
 * More information on <http://www.simplace.net>
 */



import static java.lang.StrictMath.*;

import net.simplace.sim.util.FWSimVariable;


/**
 * Defines some helper functions similar to some FST functions (FortranSimulationTranslator)
 *
 * WIKI_START
 * Defines some of the FST-Functions (sometimes with different signatures than the original
 * FST ones).
 *
 * == References: ==
 * (FST) [https://www.wageningenur.nl/en/Publication-details.htm?publicationId=publication-way-333137323735 The Fortran simulation translator], Kraalingen, D.W.G. van; Rappoldt, C.; Laar, H.H. van, European Journal of Agronomy 18 (2003)
 * WIKI_END
 */
public class FSTFunctions
{



	/**
	 * Computes a linear interpolation for t from a table. The method returns the leftmost or rightmost value if t is out of range.
	 *
	 * Takes the table as a double array with x-values in the even and y-values in the odd entries
	 *
	 * @param xy interpolation table as double array with x and y values interleaved
	 * @param t point at which the value is computed
	 * @return the interpolated value
	 */
	public static double AFGEN(Double[] xy, double t)
	{
		double res = Double.NaN;
		int n = xy.length;
		if(n>1)
		{
			int i = 0;
			while (i < n-1 && t >= xy[i])
				i = i + 2;
			if(i==0)
			{
				res = xy[1];
			}
			else if (i>n-2)
			{
				res = xy[i-1];
			}
			else
			{
				double x1 = xy[i-2];
				double x2 = xy[i];
				double y1 = xy[i-1];
				double y2 = xy[i+1];
				res = (y2 - y1)/(x2 - x1) * (t-x1) + y1;
			}
		}
		return res;
	}


	/**
	 * Computes a linear interpolation for t from a table. The method returns the leftmost or rightmost value if t is out of range.
	 *
	 * Takes the table as two double array, first one with x-values, second one with y-values.
	 *
	 * @param x array with x values of the table
	 * @param y array with y values of the table
	 * @param t point at which the value is computed
	 * @return the interpolated value
	 */
	public static double AFGEN(Double[] x, Double[] y, double t)
	{
		double res = Double.NaN;
		int n = min(x.length,y.length);
		if(n>0)
		{
			int i = 0;
			while (i < n && t >= x[i])
				i++;
			if(i==0)
			{
				res = y[0];
			}
			else if (i==n)
			{
				res = y[n-1];
			}
			else
			{
				double x1 = x[i-1];
				double x2 = x[i];
				double y1 = y[i-1];
				double y2 = y[i];
				res = (y2 - y1)/(x2 - x1) * (t-x1) + y1;
			}
		}
		return res;
	}

	public static double AFGEN(FWSimVariable<Double[]> xy, double t)
	{
		return AFGEN(xy.getValue(),t);
	}


	/**
	 * Returns one value, if the test value is negative and another value, if the test value ist nonnegative
	 * @param testvalue
	 * @param X2 value returned if test value is negative
	 * @param X3 value returned if test value is positive or zero
	 * @return resulting value
	 */
	public static double INSW(double testvalue, double X2, double X3)
	{
		if (testvalue < 0)
		{
			return X2;
		}
		return X3;
	}

	/**
	 * Returns one value, if the test value is false and another value, if the test value ist nonnegative
	 * @param testvalue
	 * @param X2 value returned if test value is negative
	 * @param X3 value returned if test value is positive or zero
	 * @return resulting value
	 */
	public static double INSW(boolean testvalue, double X2, double X3)
	{
		if (!testvalue)
		{
			return X2;
		}
		return X3;
	}

	/**
	 * Tests whether two values are positive
	 * @param x1 first value
	 * @param x2 second value
	 * @return 1 if both are positive, 0 otherwise
	 */
	public static int REAAND(double x1, double x2)
	{
		if (x1 > 0 && x2 > 0)
		{
			return 1;
		}
		return 0;
	}

	/**
	 * Limits a value to a lower and upper bound
	 * @param XL lower bound
	 * @param XH upper bound
	 * @param X value
	 * @return the value or it's lower/upper bound if it exceeds the bounds
	 */
	public static double LIMIT(double XL, double XH, double X)
	{
		if (X > XH)
		{
			return XH;
		}
		if (X < XL)
		{
			return XL;
		}
		return X;
	}

	/**
	 * Returns 1 instead of 0 if the value is 0. Used to avoid division by 0
	 * @param x value
	 * @return value or 1
	 */
	public static double NOTNUL(double x)
	{
		if (x == 0.0)
		{
			return 1.0;
		}
		return x;
	}



	/**
	 * Returns 1 if two values are both zero or negative, returns 0 otherwise
	 * @param a first value
	 * @param b second value
	 * @return 1 or 0
	 */
	public static double REANOR(double a, double b) {
		if(a<=0 && b<=0)
			return 1.0;
		else
			return 0.0;
	}

}