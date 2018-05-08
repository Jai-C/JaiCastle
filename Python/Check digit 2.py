def get_data():
    Barcode = input("Enter your 13 digits of the barcode, no spaces: ")
    if len(Barcode) is not 13:
        print("Invalid number of digits!")
        return None
    data = []
    for item in Barcode:
        if ord(item) < ord('0') or ord(item) > ord('9'):
            print("{:s} isn't a digit!".format(item))
            return None
        data.append(ord(item)-ord('0'))
    return data


barcode = get_data()
while type(barcode) is not list:
    barcode = get_data()

secondSum = 0
for i in range(1,12,2):
    secondSum += barcode[i]*3

firstSum = 0
for j in range(0,12,2):
    firstSum += barcode[j]

overallSum = firstSum + secondSum

checkDigit = 10 - overallSum%10

if checkDigit == barcode[12]:
    print("Barcode has been read in correctly.")
else:
    print("Error. Barcode has not been read in correctly.")
