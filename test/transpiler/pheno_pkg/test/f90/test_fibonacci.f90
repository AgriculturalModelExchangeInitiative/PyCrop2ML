!Test generation'

PROGRAM test_test1_fibonacci:
    INTEGER:: n

    INTEGER:: result

    n = 6

    call fibonacci_(n,result)
    print *,result
 END PROGRAM

