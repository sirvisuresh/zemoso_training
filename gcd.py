def gcdIter(a,b):
    while b!=0:
        c=b
        b=a%b
        a=c
    return a