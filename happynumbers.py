def getNextNumber(number):
    squareDigits=[int(digit) for digit in str(number)]
    squaredDigit=[digit**2 for digit in squareDigits]
    sumSquaredDigits=sum(squaredDigit)
    return sumSquaredDigits
def checkHappyNumber(number,checkedList):
    checkNumber=getNextNumber(number)
    alreadyChecked=list(checkedList)
    if checkNumber == 1:
        return True
    elif any(str(checkNumber) in str(oldNumbers) for oldNumbers in alreadyChecked):
        return False
    else:
        alreadyChecked.append(checkNumber)
        return(checkHappyNumber(checkNumber,alreadyChecked))  
def getHappyNumbers():
    for allNumbers in range (1,101,1):
        if checkHappyNumber(allNumbers,'') is True:
            yield (allNumbers)
        
happyNumber=list(getHappyNumbers())
print (happyNumber)