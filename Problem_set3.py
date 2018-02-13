
#Problem1
def isWordGuessed(word,letters):
    for letter in word:
        if letter not in letters:
            return False
    return True

#Problem2
def getGuessedWord(word,letters):
    string=""
    for letter in word:
        if letter not in letters:
            string=string+'_ '
        else:
            string=string+letter
    return string

#Problem3
def getAvailableLetters(letters):
    word="abcdefghijklmnopqrstuvwxyz"
    string=""
    for letter in word:
        if letter not in letters:
            string=string+letter
    return string

#Problem4
def hangman(secretWord):
    mistakes = 0
    lettersGuessed = []
    while 8-mistakes>0:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('you won')
            break
        else:
        	print('Guesses left now :' + str(8 - mistakes))
        	print('Available letters:', getAvailableLetters(lettersGuessed))
        	nguess = input('guess a letter:')
        	guess = nguess.lower()
        	if guess in secretWord and guess not in lettersGuessed:
        		lettersGuessed.append(guess)
        		print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
        	elif guess in lettersGuessed:
        		print("you have already guessed this letter", getGuessedWord(secretWord, lettersGuessed))
        	elif guess not in secretWord:
        		print("this letter is not in word", getGuessedWord(secretWord, lettersGuessed))
        		lettersGuessed.append(guess)
        		mistakes += 1
        if 8 - mistakes == 0:
        	print('your guesses are over and word is',secretWord)
        	break
