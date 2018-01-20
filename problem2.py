s = input("Enter string: ")
count=0
bob=0
for letter in s:
   if letter=='b' and count==2:
       count=1 
       bob=bob+1
   if letter=='b':
       count=1
   if letter=='o' and count==2:
       count=0
   if letter=='o' and count==1:
       count=2
   elif letter!='o' and letter!='b':
       count=0
print("Number of times bob occurs is: " + str(bob))
