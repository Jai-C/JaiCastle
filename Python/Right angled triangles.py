import math
#Input
def DetermineWhichSides():
    hypo_known = input("Do you know the hypotenuese? (Type Y or N)     ")
    while not(hypo_known == 'Y' or hypo_known == 'N'):
        hypo_known = input("Do you know the hypotenuese? (Only type Y or N)     ")
    return hypo_known

#Processing
def DetermineAlgorithm(hypo_known):
    if hypo_known == 'Y':
        Algorithm = 1 # Algorithm 1 includes the hypotenuese
    elif hypo_known == 'N':
        Algorithm = 2 # Algorithm 2 calculates the hypotenuese
    return Algorithm

def Calculation(Algorithm_Number):
    if Algorithm_Number == 1: #Algorithm 1
        c = float(input("Enter the hypotenuese:     "))
        a = float(input("Enter the other known side:    "))
        b = math.sqrt(c**2 - a**2)
        return b
    elif Algorithm_Number == 2: #Algorithm 2
        a = float(input("Please enter the first side:    "))
        b = float(input("Please enter the second side:    "))
        c = math.sqrt(a**2 + b**2)
        return c

#Output
def Output(Result, Algorithm):
    if Algorithm == 1:
        filler = "side"
    elif Algorithm == 2:
        filler = "hypotenuese"
    print("The unknown", filler, " is ", Result)

#Code   
hypo_known = DetermineWhichSides()
Algorithm = DetermineAlgorithm(hypo_known)
Result = Calculation(Algorithm)
Output(Result, Algorithm)
