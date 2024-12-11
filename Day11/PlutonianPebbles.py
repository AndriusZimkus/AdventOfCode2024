def main():

    numbers = []
    numbersDict = {}
    with open('input.txt', 'r') as file:
        numbers = [int(i) for i in file.read().split()]
        

    for number in numbers:
        if number not in numbersDict:
           numbersDict[number] = 1
        else:
            numbersDict[number] += 1

    #Part 1 - brute force, parse every number every time
    blinkCount = 25

    for i in range(blinkCount):
        numbers = transformList_Part1(numbers)

    print(f"Part 1 - stone count after {blinkCount} blinks:", len(numbers))


    #Part 2 - dictionary solution, parse every distinct number once
    blinkCount = 75
    for i in range(blinkCount):
        numbersDict = transformList_Part2(numbersDict)

    stoneCount = 0
    for number in numbersDict:
        stoneCount+=numbersDict[number]
        
    print(f"Part 2 - stone count after {blinkCount} blinks:", stoneCount)
    
def transformList_Part1(numbers):

    newNumbers = []
    for number in numbers:
        newNumber_List = transformNumber_Part1(number)
        newNumbers.extend(newNumber_List)       
        
    return newNumbers

def transformNumber_Part1(number):
    if number == 0:
        return [1]
    elif hasEvenNumberOfDigits(number):
        nas = str(number)
        nasL = len(nas)


        firstNumber = int(nas[0:nasL//2])
        
        secondNumber = int(nas[nasL//2:nasL])

        return [firstNumber,secondNumber]
    else:
        return [number * 2024]

def hasEvenNumberOfDigits(number):
    return len(str(number)) % 2 == 0

    return newNumber


def transformList_Part2(numbersDict):

    newNumbersDict = {}

    for number in numbersDict:
        count = numbersDict[number]
        newNumber_List = transformNumber_Part1(number)

        for new in newNumber_List:
            if new in newNumbersDict:
                newNumbersDict[new] +=count
            else:
                newNumbersDict[new] = count

    return newNumbersDict
        

if __name__ == "__main__":
    main()
