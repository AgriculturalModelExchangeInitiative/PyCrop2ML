def test(int a):
    cdef int x=15, y=15
    cdef int i
    a=12
    for i in range(0,10,1):
        a=a+i 
    return a