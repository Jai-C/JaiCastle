
resistance_of_each = 12 #Ohms
required = 11
def parallel(resistance, number):
    effective_resistance = 1/(number/resistance)
    return effective_resistance

def series(resistance, number):
    effective_resistance = resistance * number
    return effective_resistance

def two_parallel(r1, r2):
    return (1/(1/r1 + 1/r2))
# Check for series only
for i in range (1000):
    if series(resistance_of_each, i) == required:
        print(i, " in a series")

# Check for parallel
for i in range (1000):
    if i > 0:
        if parallel(resistance_of_each, i) == required:
            print(i, " in parallel")

#Check for other
solutions = 0
for i in range(1000):
    for n in range(1000):
        if i != 0 and n != 0 :
            if series(parallel(resistance_of_each,n),i) == required:
                print("The following in a series: ",i, " lots of " ,n , " in parallel")
                solutions += 1
            if parallel(parallel(resistance_of_each,n),i) == required:
                print("The following in parallel: ",i, " lots of ", n ," in parallel")
            if two_parallel(parallel(resistance_of_each,i),parallel(resistance_of_each,n)) == required:
                print("DAM SON")


print(solutions)
print(1/((1/4)+1/12))
print(series(4,1) + series(4,3))

