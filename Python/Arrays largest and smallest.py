size = int(input("Enter the length of the array:  "))
array = []
for i in range(0,size):
    array.append(int(input("Enter a number to be put into the array:  ")))

largestFound = False
smallestFound = False
smallCount = 0
largeCount = 0

for j in range(0,size):
    larger = 0
    for k in range(0,size):
        if array[j] > array[k]:
            larger +=1
    if larger == 0:
        smallestPos = j + 1
        smallestFound = True
        smallCount += 1
    if larger == size-1:
        largestPos = j + 1
        largestFound = True
        largeCount += 1
    
if largestFound is False or largeCount > 1:
    print("There is no single largest number." )
else:
    print("The largest number is: " + str(array[largestPos -1]) + " (position " + str(largestPos) + ")")
    
if smallestFound is False or smallCount > 1:
    print("There is no single smallest number.")
else:
    print("The smallest number is: " + str(array[smallestPos - 1]) + " (position " + str(smallestPos) + ")")
