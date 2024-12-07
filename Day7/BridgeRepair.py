import numpy as np
import copy
data = []
with open('input.txt', 'r') as file:
        for line in file:
                currentRow = line.strip()
                splittedCR = currentRow.split(":")
                result = int(splittedCR[0])
                elements = list(map(int,splittedCR[1].strip().split()))
                data.append((result,elements))


def isResultPossible(row):
        result = row[0]
        elements = row[1]
        if len(elements) == 1 and elements[0] == result:
                return True
        elif len(elements) == 1:
                return False
                
        firstElement = elements[0]
        secondElement = elements[1]

        add = firstElement+secondElement
        multiply = firstElement*secondElement
        
        newAddElements = elements[2:]
        newAddElements.insert(0,add)
        newMultiplyElements = elements[2:]
        newMultiplyElements.insert(0,multiply)
        return isResultPossible((result,newAddElements)) or isResultPossible((result,newMultiplyElements))


calibrationResult = 0
for row in data:
        if isResultPossible(row):
             calibrationResult += row[0]   
    
print("Calibration result:", calibrationResult) 


#Part 2  
def isResultPossibleWithConcat(row):
        result = row[0]
        elements = row[1]
        if len(elements) == 1 and elements[0] == result:
                return True
        elif len(elements) == 1:
                return False

        firstElement = elements[0]
        secondElement = elements[1]
        concatResult = int(str(firstElement) + str(secondElement))

        if len(elements) == 2 and concatResult == result:
                return True

        add = firstElement+secondElement
        multiply = firstElement*secondElement
        newAddElements = elements[2:]
        newAddElements.insert(0,add)
        newMultiplyElements = elements[2:]
        newMultiplyElements.insert(0,multiply)
        newConcatElements = elements[2:]
        newConcatElements.insert(0,concatResult)       

        return (
                isResultPossibleWithConcat((result,newAddElements))
                or isResultPossibleWithConcat((result,newMultiplyElements))
                or isResultPossibleWithConcat((result,newConcatElements))
                )

calibrationWithConcatResult = 0
for row in data:
        if isResultPossibleWithConcat(row):
             calibrationWithConcatResult += row[0]   
             
print("Calibration with concatenation result:", calibrationWithConcatResult) 
