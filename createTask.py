# Transform parabola coordinate given the equation with the transformations, y =  a(x-h)^2+k
def identifyVariablesInEquation(equation : str) -> list:
    listValues = []
    equalSign = equation.find("=")
    bracketOpen = equation.find("(")
    bracketClose = equation.find(")")
    aValueSign = equalSign+1
    hValueSign = equation.find("x")+1
    kValueSign = equation.find("^")+2
    a = int(equation[aValueSign+1])
    if equation[aValueSign] == "-":
        a *= -1
    h = int(equation[hValueSign+1])
    if equation[hValueSign] == "+":
        h *= -1
    k = int(equation[kValueSign+1:])
    if equation[kValueSign] == "-":
        k *= -1
    listValues.append(a)
    listValues.append(h)
    listValues.append(k)
    return listValues

def printTransformationValueA(listOfValues : list):
    aValue = listOfValues[0]
    absoluteA = abs(aValue)
    hValue = listOfValues[1]
    absoluteH = abs(hValue)
    kValue = listOfValues[2]
    absoluteK = abs(kValue)
    if aValue < 0:
        print("Reflection in x axis")
    if aValue > 0 and aValue < 1:
        print("Vertical Compression by a factor of" , absoluteA)
    elif aValue > 1 or aValue < -1:
        print("Vertical Stretch by a factor of" , absoluteA)
    if hValue > 0:
        print("Translate right" , absoluteH , "units")
    elif hValue < 0:
        print("Translate left" , absoluteH , "units")
    if kValue > 0:
        print("Shift up" , absoluteK , "units")
    elif kValue < 0:
        print("Shift down" , absoluteK , "units")

def transformCoordinate(xVal : int, yVal : int, listValues : list) -> int:
    aVal = listValues[0]
    hVal = listValues[1]
    kVal = listValues[2]
    newX = xVal + hVal
    newY = yVal*aVal + kVal
    return (newX,newY)

xValue = int(input("Enter x value of coordinate: \n"))
yValue = int(input("Enter y value of coordinate: \n"))
transformedEquation = input("Enter equation in form y=a(x-h)^2+k with no spaces. All values must be whole numbers: \n")
allValues = identifyVariablesInEquation(transformedEquation)
printTransformationValueA(allValues)
transformedCoord = transformCoordinate(xValue,yValue, allValues)
print("The new coordinate after transformation is",transformedCoord)



