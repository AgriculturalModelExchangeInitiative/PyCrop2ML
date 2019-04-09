from math import *

from CumulTTFrom import *

def test_test_wheat1():
    params= cumulttfrom(
    calendarMoments = ["Sowing", "Emergence", "FloralInitiation", "FlagLeafLiguleJustVisible", "Heading", "Anthesis"],
    calendarCumuls = [0.0, 112.330110409888, 354.582294511779, 741.510096671757, 853.999637026622, 954.59002776961],
    cumulTT = 972.970888983105,
     )
    cumulTTFromZC_65_estimated = round(params[0], 2)
    cumulTTFromZC_65_computed = 18.38
    assert (cumulTTFromZC_65_estimated == cumulTTFromZC_65_computed)
    cumulTTFromZC_39_estimated = round(params[1], 2)
    cumulTTFromZC_39_computed = 231.46
    assert (cumulTTFromZC_39_estimated == cumulTTFromZC_39_computed)
    cumulTTFromZC_91_estimated = round(params[2], 2)
    cumulTTFromZC_91_computed = 0
    assert (cumulTTFromZC_91_estimated == cumulTTFromZC_91_computed)

from IsMomentRegistredZC_39 import *

def test_test_wheat1():
    params= ismomentregistredzc_39(
    calendarMoments = ["Sowing", "Emergence", "FloralInitiation", "FlagLeafLiguleJustVisible", "Heading", "Anthesis"],
     )
    isMomentRegistredZC_39_estimated = params
    isMomentRegistredZC_39_computed = 1
    assert (isMomentRegistredZC_39_estimated == isMomentRegistredZC_39_computed)

from LeafNumber import *

def test_test_wheat1():
    params= leafnumber(
    leafNumber = 5.147163833893262,
    phase = 3,
    phyllochron = 91.2,
     )
    leafNumber_estimated = round(params, 2)
    leafNumber_computed = 5.41
    assert (leafNumber_estimated == leafNumber_computed)

from Phyllochron import *

def test_test_wheat1():
    params= phyllochron(
    lincr = 8,
    ldecr = 3,
    pdecr = 0.4,
    pincr = 1.25,
    fixPhyll = 91.2,
    gai = 0.279874189539498,
     )
    phyllochron_estimated = round(params[0], 2)
    phyllochron_computed = 36.48
    assert (phyllochron_estimated == phyllochron_computed)
    pastMaxAI_estimated = round(params[1], 2)
    pastMaxAI_computed = 0
    assert (pastMaxAI_estimated == pastMaxAI_computed)

from PhylSowingDateCorrection import *

def test_test_wheat1():
    params= phylsowingdatecorrection(
    sowingDay = 80,
    latitude = 33.069,
    sDsa_sh = 151,
    rp = 0.003,
    sDws = 90,
    sDsa_nh = 200,
    p = 120,
     )
    fixPhyll_estimated = round(params, 2)
    fixPhyll_computed = 91.2
    assert (fixPhyll_estimated == fixPhyll_computed)

from RegisterZadok import *

def test_test_wheat1():
    params= registerzadok(
    slopeTSFLN = 0.9,
    intTSFLN = 2.6,
    calendarMoments = ["Sowing","Emergence","EndVernalisation","MainShootPlus1Tiller"],
    calendarDates = ["21/3/2007","27/3/2007","30/3/2007","5/4/2007"],
    calendarCumuls = [ 0.0, 112.330110409888,157.969706915664, 280.570678654207],
    phase = 2,
     )
    hasZadokStageChanged_estimated = params[0]
    hasZadokStageChanged_computed = 0
    assert (hasZadokStageChanged_estimated == hasZadokStageChanged_computed)
    currentZadokStage_estimated = params[1]
    currentZadokStage_computed = "MainShootPlus1Tiller"
    assert (currentZadokStage_estimated == currentZadokStage_computed)
    calendarMoments_estimated = params[2]
    calendarMoments_computed = ["Sowing","Emergence","EndVernalisation","MainShootPlus1Tiller"]
    assert np.all(calendarMoments_estimated == calendarMoments_computed)
    calendarDates_estimated = params[3]
    calendarDates_computed = ["21/3/2007", "27/3/2007", "30/3/2007", "5/4/2007"]
    assert np.all(calendarDates_estimated == calendarDates_computed)
    calendarCumuls_estimated = np.around(params[4], 2)
    calendarCumuls_computed = [ 0.0, 112.33,157.97, 280.57]
    assert np.all(calendarCumuls_estimated == calendarCumuls_computed)

from ShootNumber import *

def test_test_wheat1():
    params= shootnumber(
    targetFertileShoot = 600.0,
    sowingDensity = 288,
    canopyShootNumber = 288.0,
    leafNumber = 3.34348137255,
    leafTillerNumberArray = [1, 1, 1],
    tilleringProfile = [288.0],
     )
    averageShootNumberPerPlant_estimated = round(params[0], 2)
    averageShootNumberPerPlant_computed = 2
    assert (averageShootNumberPerPlant_estimated == averageShootNumberPerPlant_computed)
    canopyShootNumber_estimated = round(params[1], 1)
    canopyShootNumber_computed = 576
    assert (canopyShootNumber_estimated == canopyShootNumber_computed)
    leafTillerNumberArray_estimated = params[2]
    leafTillerNumberArray_computed = [1, 1, 1, 2]
    assert np.all(leafTillerNumberArray_estimated == leafTillerNumberArray_computed)
    tilleringProfile_estimated = np.around(params[3], 2)
    tilleringProfile_computed = [288.0, 288.0]
    assert np.all(tilleringProfile_estimated == tilleringProfile_computed)
    tillerNumber_estimated = params[4]
    tillerNumber_computed = 2
    assert (tillerNumber_estimated == tillerNumber_computed)

from UpdateCalendar import *

def test_test_wheat1():
    params= updatecalendar(
    cumulTT =  112.330110409888,
    calendarMoments = ["Sowing"],
    calendarDates = ["21/3/2007"],
    calendarCumuls = [0.0],
    phase = 1,
     )
    calendarMoments_estimated = params[0]
    calendarMoments_computed = ["Sowing", "Emergence"]
    assert np.all(calendarMoments_estimated == calendarMoments_computed)
    calendarDates_estimated = params[1]
    calendarDates_computed = ["21/3/2007", "27/3/2007"]
    assert np.all(calendarDates_estimated == calendarDates_computed)
    calendarCumuls_estimated = np.around(params[2], 2)
    calendarCumuls_computed = [ 0.0 ,112.33]
    assert np.all(calendarCumuls_estimated == calendarCumuls_computed)

from UpdateLeafFlag import *

def test_test_wheat1():
    params= updateleafflag(
    hasFlagLeafLiguleAppeared = 0,
    phase = 3,
    calendarMoments = ["Sowing", "Emergence", "EndVernalisation", "MainShootPlus1Tiller", "FloralInitiation", "MainShootPlus2Tiller", "TerminalSpikelet", "PseudoStemErection", "MainShootPlus3Tiller", "1stNodeDetectable", "2ndNodeDetectable", "FlagLeafJustVisible"],
    calendarDates = ["21/3/2007", "27/3/2007", "30/3/2007", "5/4/2007", "9/4/2007", "10/4/2007", "11/4/2007", "12/4/2007", "14/4/2007", "15/4/2007", "19/4/2007", "24/4/2007"],
    calendarCumuls = [0.0, 112.330110409888, 157.969706915664, 280.570678654207, 354.582294511779, 378.453152853726, 402.042720581446, 424.98704708663, 467.23305195298, 487.544313430698, 560.665248444002, 646.389617338974],
     )
    hasFlagLeafLiguleAppeared_estimated = params[0]
    hasFlagLeafLiguleAppeared_computed = 1
    assert (hasFlagLeafLiguleAppeared_estimated == hasFlagLeafLiguleAppeared_computed)
    calendarMoments_estimated = params[1]
    calendarMoments_computed = ["Sowing", "Emergence", "EndVernalisation", "MainShootPlus1Tiller", "FloralInitiation", "MainShootPlus2Tiller", "TerminalSpikelet", "PseudoStemErection", "MainShootPlus3Tiller", "1stNodeDetectable", "2ndNodeDetectable", "FlagLeafJustVisible", "FlagLeafLiguleJustVisible"]
    assert np.all(calendarMoments_estimated == calendarMoments_computed)
    calendarDates_estimated = params[2]
    calendarDates_computed = ["21/3/2007", "27/3/2007", "30/3/2007", "5/4/2007", "9/4/2007", "10/4/2007", "11/4/2007", "12/4/2007", "14/4/2007", "15/4/2007", "19/4/2007", "24/4/2007", "29/4/2007"]
    assert np.all(calendarDates_estimated == calendarDates_computed)
    calendarCumuls_estimated = np.around(params[3], 2)
    calendarCumuls_computed = [0.0, 112.33, 157.97, 280.57, 354.58, 378.45, 402.04, 424.99, 467.23, 487.54, 560.67, 646.39, 741.51]
    assert np.all(calendarCumuls_estimated == calendarCumuls_computed)

from UpdatePhase import *

def test_test_wheat1():
    params= updatephase(
    choosePhyllUse = "Default",
    phase = 1,
    hasLastPrimordiumAppeared = 0,
     )
    finalLeafNumber_estimated = round(params[0], 2)
    finalLeafNumber_computed = 8.80
    assert (finalLeafNumber_estimated == finalLeafNumber_computed)
    phase_estimated = round(params[1], 1)
    phase_computed = 2
    assert (phase_estimated == phase_computed)
    hasLastPrimordiumAppeared_estimated = params[2]
    hasLastPrimordiumAppeared_computed = 1
    assert (hasLastPrimordiumAppeared_estimated == hasLastPrimordiumAppeared_computed)

from VernalizationProgress import *

def test_test_wheat1():
    params= vernalizationprogress(
    isVernalizable = 1,
    cumulTT =  112.330110409888,
     )
    vernaprog_estimated = round(params[0], 2)
    vernaprog_computed = 0.64
    assert (vernaprog_estimated == vernaprog_computed)
    minFinalNumber_estimated = round(params[1], 2)
    minFinalNumber_computed = 5.5
    assert (minFinalNumber_estimated == minFinalNumber_computed)
    calendarMoments_estimated = params[2]
    calendarMoments_computed = ["Sowing"]
    assert np.all(calendarMoments_estimated == calendarMoments_computed)
    calendarDates_estimated = params[3]
    calendarDates_computed = ["21/3/2007"]
    assert np.all(calendarDates_estimated == calendarDates_computed)
    calendarCumuls_estimated = np.around(params[4], 2)
    calendarCumuls_computed = [0.0]
    assert np.all(calendarCumuls_estimated == calendarCumuls_computed)

from fibonacci import *

def test_test1():
    params= fibonacci(
    n = 6,
     )
    result_estimated = params
    result_computed = 8
    assert (result_estimated == result_computed)
