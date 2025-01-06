import time

def main():
 
    fileName = "input.txt"
    path = "../../Advent Of Code Cases/Day25/" + fileName


    keys = []
    locks = []

    with open(path, 'r') as file:


        isNewBlock = True

        while True:
            heights,isKey = readBlock(file)

            if isKey:
                keys.append(heights)
            else:
                locks.append(heights)

            if file.readline() == "":
                break


    fitCount = 0
    for key in keys:
        for lock in locks:
            if doesKeyFitLock(key,lock):
                fitCount += 1
    print("Part 1, fit count:", fitCount)

def doesKeyFitLock(key,lock):
    for i in range(len(key)):
        if key[i] + lock[i] > 5:
            return False
    return True
    
def readBlock(file):
    currentMatrix = []
    heights = []
    i = 0
    while i < 7:
        currentMatrix.append(list(file.readline().strip()))
        i+=1

    isKey = currentMatrix[0][0] == "."

    for x in range(len(currentMatrix[0])):
        currentHeight = 0
        for y in range(1,len(currentMatrix)-1):
            if currentMatrix[y][x] == "#":
                currentHeight+=1
        heights.append(currentHeight)    

    return heights,isKey
    

        
        
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(round(end - start,4))
