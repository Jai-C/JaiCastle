##Fibonacci Number Series Program
##Copyright © Jai Castle 2016
##This program either:
##      (i) Tests to see if an inputted number is prime; or
##      (ii)Generates a specified number of prime numbers
import time
List = ""

def takeInput(purpose):
    digits = ['1','2','3','4','5','6','7','8','9','0'] #The valid digits of a number to be entered
    valid = False
    n = ""
    while type(n) == str:
        while valid == False:
            n = input("Enter a number to " + purpose)
            valid = True
            for i in range(len(n)):
                if not(n[i] in digits):
                    valid = False
            if len(n) == 0:
                valid = False

            if valid is False:
                print("Invalid number!")          
        n = int(n)
        if decision == "P":
            if not(n > 2) or (n%2 == 0):
                n = str(n)
                valid = False
                print("Invalid number! Please enter a number that is greater than 2 and not even.")          
    return n

def isPrime(number):
    halfway = int(number**0.5)
    prime = True
    counter = 2
    while counter <= halfway and prime is True:
        if number % counter == 0:
                prime = False
        counter += 1
    if number == 1:
        prime = False
    elif number == 2:
        prime = True
    return prime

validDecision = False
while validDecision is False:
    decision = input('''If you would like to check if a number is prime, type P.
If you would like to generate a specified number of prime numbers, type L.
''')
    if decision == "P" or decision == "L":
        validDecision = True
    else:
        print("Invalid input. Please either type P or L.")

if decision == "P":
    checkPrime = True
else:
    checkPrime = False
    
print("-----------------------\nPlease enter a number that is an integer, greater than 2 and not even:")
if checkPrime is True:
    n = takeInput("test if the number is prime: ")
    stime = time.time()
    print(isPrime(n))
else:
    n = takeInput("print a list of a specified number of prime numbers:")
    counter = 1
    primes  = []
    numberChecking = 1
    stime = time.time()
    while counter <= n:
        halfway = int(numberChecking**0.5)
        prime = True
        counter2 = 2
        while counter2 <= halfway and prime is True:
            if numberChecking % counter2 == 0:
                    prime = False
            counter2 += 1
        if numberChecking == 1:
            prime = False
        elif numberChecking == 2:
            prime = True
        if prime:List = List + (str(numberChecking) + "\n"); counter += 1
 
        numberChecking += 2
timetime = time.time()
print(List)
print(timetime - stime)
