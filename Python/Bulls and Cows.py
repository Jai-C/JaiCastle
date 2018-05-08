############################
##Bulls and Cows Program
##Computer Science 2017
##Jai Castle
##Program to play the game of "Moo" where the user tries to guess a number
##The computer returns the number of "bulls" (correctly placed digits) 
##and "cows" incorrectly placed digits that are still present in the answer.
##Created as a project
############################

import random, time #Importing of libraries for random number generating and time delays

#Constants for length of the number to be guessed
length = 4

#Testing/Assessment purposes
showAnswer = True  #Decide whether or not to tell the user what the answer is before playing

## Module definition ##
def generateRandom(length): #Module to generate a valid random number for the game
    if length not in range(0,11):
        return False
    #End if
    digits = [0,1,2,3,4,5,6,7,8,9]
    number = 0
    for i in range(0,length):
        start = 1 if i is 0 else 0 #Do not start the number with a 0
        digit = random.randint(start,len(digits)-1) #Choose a random position in the list (random digit generator)
        digit = digits[digit]
        digits.remove(digit)
        number = number*10 + digit #Add the next digit to the number
    #End if
    return str(number)
#End module

def getValidGuess(length): #Module to get a valid guess from the user (including no repeating digits)
    valid = False
    n = input("Please enter your guess (a {} digit valid number): ".format(length))
    while valid is False:
        valid = len(n) == length #Must be of the right length
        if valid is True:
            valid = checkNumeric(n) #Check numeric status
        else:
            print("Please enter a guess with {} digits and is numeric.".format(length))
        #End if
        if valid is True:
            charsCheck = [j for j in n] #Turn the string into an array
            for i in range(length):
                charsCheck.remove(n[i]) #Remove the digit being checked
                if n[i] in charsCheck and valid is True: #If there is a repeated digit
                    valid = False
                    print("Please do not enter a guess with repeated digits.")
                #End if
            #End for
        #End if 
        if valid is False:
            n = input("\nInvalid entry. Enter a valid {} digit guess please:  ".format(length))
        #End if
    return [j for j in n] #Return the array version of the guess (this method makes processing easier)
#End module

def checkNumeric(number):  #Module to check if a is numeric. The number could be a string or an integer, they both act the same in python
    returnVal = True
    if len(number) is 0: #If nothing is entered
        print("Please enter a number.")
        returnVal = False
    #End if
    for x in number: #For each character
        if not(ord(x)>=ord('0') and ord(x)<=ord('9')): #If the character being checked is numeric
            print("'{}' is not a digit! Please enter a valid number.".format(x)) #Tell the user which character is not numeric
            returnVal = False
        #End if
    #End for
    if number is '0': # Does not allow the user to enter zero
        print("Please enter a number that is not zero.")
        returnVal =  False
    #End if
    return returnVal
#End module

def convert(chars): #Function to convert a set of characters into their integer equivalent
    number = 0 #Initialised to 0
    for i in chars: #For each character in chars
        number = number*10 + (ord(i)-ord('0')) #multiply number by ten then add the new digit
    #End if
    return number
#End module

def bullsAndCows(currentGuess, answer): #Function to output and return number of bulls and cows
    bulls = 0 #Sum initialisation
    cows = 0
    for i in range(len(currentGuess)): #For each character of the guess
        if currentGuess[i] is answer[i]: #If the character is in the same spot as the answer
            bulls += 1 
        elif currentGuess[i] in answer: #If the character is in the answer but not in the same spot
            cows += 1
        #End if
    #End for
    print("Bulls: {:^5} Cows: {:^5}\n".format(bulls,cows)) #Output results
    return {"Guess":"".join(currentGuess), "Bulls":bulls, "Cows":cows} #Create a dictionary with the data about this guess
#End module

def manageCurrentGuess(answer, length): #Function to manage the current guess
    guess = getValidGuess(length) #Obtain a valid guess
    return bullsAndCows(guess, answer) #Get the results of the guess and return data about the guess
#End module

def getTotalGuesses(): #Function to ask the user for how many gusses to give themselves
    guesses = input("How many guesses would you like to give yourself?  ")
    valid = False
    while valid is False:
        valid = checkNumeric(guesses) #Make sure the input is numeric
        if valid is True:
            valid = convert(guesses)<=100 #Limit data validation, for sensibility
        if valid is False:
            guesses = input("\nPlease enter a valid number (maximum 100):  ")
        #End if
    #End while
    return convert(guesses) #Convert to a numeric value before returning
#End module

def checkPlayAgain(): #Function to ask the user if they would like to play again
    request = input("Would you like to play again? Enter yes or no:   ")
    while request.lower() not in ['y','n','yes','no']: #Is the response in the set of acceptible responses
        request = input("Please enter a valid yes/no response:   ")
    #End while
    return request.lower() == 'y' or request.lower() == 'yes' #Return a True /False
#End module

def setupGame(length): #Function for the initial output of graphics and instructions for the game
    print('''                
  ((__-^^-,-^^-__))\n   `-_---' `---_-'\n    <__|o` 'o|__>\n       \  `  /\n        ): :(\n        :o_o:\n         "-"   
--------------------------
Welcome to the game of Moo!
--------------------------
by Jai Castle
''')
    time.sleep(0.5) #Delay for graphic / visual effect
    print("This is a game where you have to try and guess the correct number,\na randomly generated {} digit number.".format(length))
    time.sleep(1.5) #Delay
    print('''
--------------------------

The computer will give you feedback on your guesses, by telling you
how many 'bulls' and how many 'cows' you have scored: 

    - A bull indicates one of the digits you have entered is in the
      correct answer and in the same spot!
    - A cow means that one of the digits you have entered is in the
      correct answer, but in a different spot!

You will have a maximum number of guesses that you can choose:
(5 is very hard, 10 is moderate and 20+ is easy).

Please note the following:
    - The correct answer will have no repeating digits and will always
      be between {} and {}.
    - The computer will not allow the user to guess a number that has
      repeating digits or is the wrong length.

Please consult the user manual if you require assistance.

Good luck!!

--------------------------
    '''.format(10**(length-1), 10**length - 1)) #Based on the length of the answer, change the bounds.
    time.sleep(1.5) #Delay
#End module

def generateGuessSummary(guessHistory): #Function to generate the table of past guesses. Parameter is a list of dictionaries
    guessesShown = len(guessHistory)
    print("--------------------------")
    print("Guess history for the past {} {}:".format(guessesShown, "guess" if guessesShown is 1 else "guesses")) #End if
    print("{:<10} {:^10} {:^10}".format("Guess","Bulls", "Cows")) #Header row
    for i in range(guessesShown):
        guesstoShow = guessesShown -1 - i #Display with the most recent guess at the top of the list
        print("{:<10} {:^10} {:^10}".format(guessHistory[guesstoShow]["Guess"], guessHistory[guesstoShow]["Bulls"], guessHistory[guesstoShow]["Cows"])) #Content row(s)
    #End for
    print("--------------------------\n")
#End module

def playGame(length, wins): #Function to manage the playing of a singular game
    totalGuesses = getTotalGuesses() #Obtain the number of total guesses
    print("\nOk, your game will allow {} total {}.\n".format(totalGuesses, "guess" if totalGuesses is 1 else "guesses")) #End if
    correct = generateRandom(length) #Generate the random number of the correct length
    print("The correct answer has been generated. Have fun guessing! "+ ("(For testing & \nassessment purposes, {} is the answer.)\n".format(correct) if showAnswer else "\n"))
    won = False
    guesses = 0
    pastGuesses = [] #List of dictionaries of past guesses' statistics
    while won is False and guesses < totalGuesses: #While the user has not yet won or lost
        print("You have {} {} remaining.".format(totalGuesses-guesses, "guess" if totalGuesses-guesses is 1 else "guesses")) #End if
        guessData = manageCurrentGuess(correct, length) #Returns a dictionary with guess statistics
        won = guessData["Bulls"] is length #E.g. 4 Bulls for a 4 digit target means the user has won
        if won is False:
            if len(pastGuesses) >= 5:#Code to remove the oldest guess (5th) and then add the newest
                newHistory = [] #Prepare a new list to hold the data
                for i in range(1,len(pastGuesses)):
                    newHistory.append(pastGuesses[i]) #Add the most recent 4 guesses
                #End for
                pastGuesses = newHistory #Reassign the variable to the new list
            #End if
            pastGuesses.append(guessData) #Add the most recent guess
            generateGuessSummary(pastGuesses) #Generate the summary table
        #End if
        guesses += 1 #The user has now completed their guess
    #End while
    if won is True: #Win output
        guessesRemaining = totalGuesses - guesses
        print("You won with {} {} to spare!".format(guessesRemaining, "guess" if guessesRemaining is 1 else "guesses"))
        wins += 1 #Change to the parameter passed in, to be returned later on
    else: #Lose output
        print("You lost! You are out of guesses! \nThe correct answer was {}.\n".format(correct))
    #End if
    return wins #Return the number of wins that have now been recorded
#End module
## End module definition ##

## MAIN LINE ##
setupGame(length) #Display initial information
finishedPlaying = False
wins = 0
games = 0

while finishedPlaying is False:
    games += 1
    wins = playGame(length, wins) #Play the game and record the number of wins
    print("\n--------------------------")
    finishedPlaying = not(checkPlayAgain()) #Check whether to run the game again
    print("--------------------------")
#End while

#Final output to conclude gameplay
print("You played {} {}. Wins: {}. Losses: {}.".format(games, "game" if games is 1 else "games", wins, games-wins)) #End if, Win/Lost statistics
print("\nThank you for playing!")
## End main line ##
## END PROGRAM ##
