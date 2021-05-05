!Test generation'

PROGRAM test_test1_Conductance:
    REAL:: vonKarman

    REAL:: heightWeatherMeasurements

    REAL:: zm

    REAL:: zh

    REAL:: d

    REAL:: plantHeight

    REAL:: wind

    REAL:: conductance

    d = 0.67

    zh = 0.013

    zm = 0.13

    wind = 124000

    plantHeight = 0

    vonKarman = 0.42

    heightWeatherMeasurements = 2

    call conductance_(vonKarman,heightWeatherMeasurements,zm,zh,d,plantHeight,wind,conductance)
    print *,conductance
 END PROGRAM

