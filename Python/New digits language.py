operationsList = ['a','b']
equalsSign = 'c'
operations = ['+', '-']
digits = ['h','i','j','k']
actual_digits = [x for x in range(len(digits))]

#h= 3     i= 3   j= 2     k= 1      a= +    b= -
inputStrings = ['ibjck']
print(inputStrings)

def stringResults(string):
    String_Split = string.split(equalsSign)
    either_Side = []
    result = String_Split[1]
    for x in String_Split[0]:
        if x in operationsList:
            operationRecorded = x
        elif x in digits:
            either_Side.append(x)
    return either_Side, operationRecorded, result

valid_combos = []
for y in actual_digits:
    h = y
    Listh = [x for x in actual_digits]
    for z in Listh:
        i = z
        Listi = [x for x in actual_digits]
        for l in Listi:
            j = l
            Listl = [x for x in actual_digits]
            for m in Listl:
                k = m
                for op in operations:
                    operationNew = [i for i in operations]
                    operationNew.remove(op)
                    op2 = operationNew[0]
                    if len(set([h,i,j,k]))==len(actual_digits):
                        valid_combos.append({'h':h,'i':i, 'j':j,'k':k,'a':op,'b':op2})
                        #print([h,i,j,k, op,op2)
combinations = valid_combos

validAnswers = []
stringNo = 1
for abc in inputStrings:
    stringResult = stringResults(abc)
    either_Side = stringResult[0]
    operationRecorded = stringResult[1]
    result = stringResult[2]
    currentSolutions = []
    for x in combinations:
        exec("valid = {}{}{} == {}".format(x[either_Side[0]], x[operationRecorded], x[either_Side[1]], x[result]))
        #print("{}{}{} == {}".format(x[either_Side[0]], op, x[either_Side[1]], x[result]))# == x[result]
        if valid is True:
            if stringNo == 1:
                validAnswers.append(x)
                currentSolutions.append(x)
            else:
                currentSolutions.append(x)
    if stringNo != 1:
        newFinalAnswers = []
        for currentAnswer in currentSolutions:
            if currentAnswer in validAnswers:
                newFinalAnswers.append(currentAnswer)
        validAnswers = newFinalAnswers                                 
    stringNo += 1

for solution in validAnswers:
    print(solution)
    for x in inputStrings:
        string = ""
        for y in x:
            string += str(solution[y]) if y != 'c' else "="
        print(x, string)
