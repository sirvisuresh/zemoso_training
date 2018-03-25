def genPrime():
    k=2
    while True:
        i=2
        flag=0
        a=int(k**(.5))
        while i<=a:
            if k%i==0:
                flag=1
                break
            i=i+1
        if flag==0:
            yield k
        k=k+1
