import time

def main():
 
    fileName = "test2.txt"
    path = "../../Advent Of Code Cases/Day22/" + fileName

    initialNumbers = []
    
    with open(path, 'r') as file:
        for line in file:
            initialNumbers.append(int(line.strip()))

    results = []
    for init in initialNumbers:
        currentNumber = init
        for i in range(2000):
            currentNumber = getNextNumber(currentNumber)

        results.append(currentNumber)

    print("Part 1 sum:",sum(results))

    #initialNumbers = [123]

    priceMatrix = []
    
    for init in initialNumbers:
        currentNumber = init
        
        currentPrices = [getLastDigit(currentNumber)]
        for i in range(2000):
            currentNumber = getNextNumber(currentNumber)
            currentPrices.append(getLastDigit(currentNumber))




        priceMatrix.append(currentPrices)

    #print(priceMatrix)

    sequenceArrays = {}
    for prices in priceMatrix:
        sequences = {}
        
        for i in range(len(prices)):
            try:
                change1 = prices[i+1] - prices[i]
                change2 = prices[i+2] - prices[i+1]
                change3 = prices[i+3] - prices[i+2]
                change4 = prices[i+4] - prices[i+3]
                changeTuple = (change1,change2,change3,change4)
                
                lastPrice = prices[i+4]
                if not changeTuple in sequences:
                    sequences[changeTuple] = lastPrice
            except:
                break

        for sequence in sequences:
            currentPrice = sequences[sequence]
            if sequence in sequenceArrays:
                sequenceArrays[sequence].append(currentPrice)
            else:
                sequenceArrays[sequence] = [currentPrice]
    
    #print(sequenceArrays)
    maxSum = 0

    for sequence in sequenceArrays:
        currentSum = sum(sequenceArrays[sequence])
        if maxSum == 0 or currentSum > maxSum:
            maxSum = currentSum
            maxSequence = sequence

    print("Sequence",sequence,"Sum",maxSum)
                
        
def getLastDigit(number):
    return number % 10

def getNextNumber(secretNumber):
    value = secretNumber * 64

    secretNumber = secretNumber ^ value

    secretNumber %= 16777216

    value = secretNumber // 32

    secretNumber = secretNumber ^ value

    secretNumber %= 16777216

    value = secretNumber * 2048

    secretNumber = secretNumber ^ value

    secretNumber %= 16777216

    return secretNumber


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(round(end - start,4))
