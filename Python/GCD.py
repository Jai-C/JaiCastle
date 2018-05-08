def GetData():
    string = input("Enter P and Q separated by spaces on one line:  ")
    data = string.split(' ')
    p = int(data[0])
    q = int(data[1])
    return p,q

def CalcGCD(data):
    p = data[0]
    q = data[1]
    rem = p%q
    while rem != 0:
        p = q
        q = rem
        rem = p % q
    return q

def ReportData(d,G):
    print("You entered: " + str(d[0]) + ", " + str(d[1]) )
    print("The GCD is : " + str(G))

data = GetData()
GCD = CalcGCD(data)
ReportData(data, GCD)
