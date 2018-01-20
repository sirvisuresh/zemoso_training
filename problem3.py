s = input("enter string: ")
l = len(s)
ans=1
count=1
j=1
start=0
while j<l:
   if s[j]<s[j-1]:
      if count>ans:
           ans=count
           string=s[start:start+ans]
      count=1
      start=j
   else:
     count=count+1
     if count>ans:
        ans=count
        string=s[start:start+ans]
   j=j+1
print("Longest substring in alphabetical order is: " + string)
      
   
