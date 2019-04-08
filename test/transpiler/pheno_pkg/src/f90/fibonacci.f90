MODULE Fibonacci_mod
    IMPLICIT NONE
CONTAINS
    SUBROUTINE fibonacci_(n, &
        result)
        INTEGER, INTENT(OUT) :: result
        INTEGER:: b
        INTEGER:: temp
        INTEGER:: i
        INTEGER, INTENT(IN) :: n
        !- Description:
    !            - Model Name: fibonacci function
    !            - Author: Pierre Martre
    !            - Reference:  to write in package
    !            - Institution: INRA Montpellier
    !            - Abstract: see documentation
        !- inputs:
    !            - name: n
    !                          - description : argument
    !                          - datatype : INT
    !                          - inputtype : variable
        !- outputs:
    !            - name: result
    !                          - description :  fibonacci number 
    !                          - datatype : INT
        result = 0
        b = 1
        DO i = 1 , n, 1
            temp = result
            result = b
            b = temp + b
        END DO
    END SUBROUTINE fibonacci_
END MODULE
