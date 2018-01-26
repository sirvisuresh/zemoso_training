print("Please think of a number between 0 and 100!")
start=50
low = 0
high=100
c='a'
while True:
 start = (low+high)//2
 print("Is your secret number " + str(start))
 c = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
 if c=='c':
    print("Game over. Your secret number was: " + str(start))
    break
 elif c=='h':
    high=start
 elif c=='l':
    low = start
 else:
    print("Sorry, I did not understand your input.") 

 
