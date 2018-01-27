def iterPower(base,exp):
     if exp==1:
        return base
     else:
        return base*iterPower(base,exp-1)