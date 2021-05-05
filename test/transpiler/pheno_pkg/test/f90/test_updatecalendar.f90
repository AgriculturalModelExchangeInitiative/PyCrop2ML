!Test generation'

PROGRAM test_test_wheat1_UpdateCalendar:
    REAL:: cumulTT

    CHARACTER, ALLOCATABLE, DIMENSION(:):: calendarMoments

    CHARACTER, ALLOCATABLE, DIMENSION(:):: calendarDates

    REAL, ALLOCATABLE, DIMENSION(:):: calendarCumuls

    CHARACTER:: currentdate

    REAL:: phase

    cumulTT =  112.330110409888

    calendarMoments = ["Sowing"]

    calendarDates = ["21/3/2007"]

    calendarCumuls = [0.0]

    phase = 1

    currentdate = 27/3/2007

    call updatecalendar_(cumulTT,calendarMoments,calendarDates,calendarCumuls,currentdate,phase)
    print *,calendarMoments,calendarDates,calendarCumuls
 END PROGRAM

