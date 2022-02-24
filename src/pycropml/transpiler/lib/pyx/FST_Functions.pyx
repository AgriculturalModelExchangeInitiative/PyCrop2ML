# FSTFunctions
def AFGEN1(float xy[], float t):
    cdef float res;
    cdef float x1, x2, y1, y2
    cdef int i, n
    n = len(xy)
    res = float("nan")
    if(n>1):
        i = 0
        while (i < n-1 and t >= xy[i]):
            i = i + 2
        if(i==0):
            res = xy[1]
        elif (i>n-2):
            res = xy[i-1]
        else:
            x1 = xy[i-2]
            x2 = xy[i]
            y1 = xy[i-1]
            y2 = xy[i+1]
            res = (y2 - y1)/(x2 - x1) * (t-x1) + y1
    return res

def AFGEN2(int nx, int ny, float x[nx], float y[ny], float t):
    cdef float res, x1, x2, y1, y2 
    cdef int n, i
    n = min(len(x),len(y))
    res = float("nan")
    if(n>0):
        i = 0
        while (i < n and t >= x[i]):
            i = i+1
        if(i==0):
            res = y[0]
        elif (i==n):
            res = y[n-1]
        else:
            x1 = x[i-1]
            x2 = x[i]
            y1 = y[i-1]
            y2 = y[i]
            res = (y2 - y1)/(x2 - x1) * (t-x1) + y1
    return res

def AFGEN3(dict xy={0.0:0.0}, float t=1.5):
    cdef float x[len(xy)] 
    cdef float y[len(xy)]
    cdef int i=0
    cdef float tKey, res
    cdef int l
    l =len(xy)
    for tKey in xy.keys():
        x[i] = tKey;
        y[i] = xy.get(tKey)
        i = i+1
    res = AFGEN2(l,l,x,y,t)
    return res

	




