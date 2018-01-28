def isIn(char, aStr):
    l=len(aStr)
    if l==0:
        return False
    mid=l//2
    if char>aStr[mid]:
        return isIn(char,aStr[mid+1:])
    elif char<aStr[mid]:
        return isIn(char,aStr[:mid])
    else: 
        return True