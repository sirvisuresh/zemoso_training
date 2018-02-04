def oddTuples(a):
   b=()
   i=0;
   for t in a:
      if i%2==0: 
        b = b + (t,)
      i=i+1
   return b