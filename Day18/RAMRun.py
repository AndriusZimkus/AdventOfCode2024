import copy
def main():
 
    fileName = "input.txt"
    path = "../../Advent Of Code Cases/Day18/" + fileName

    bytesArray = []
    with open(path, 'r') as file:
        for line in file:
            x = int(line.strip().split(",")[0])
            y = int(line.strip().split(",")[1])
            bytesArray.append((x,y))

    if fileName == "test.txt":
        size = 7
    else:
        size = 71

    global nodesMatrix
    initNodesMatrix = [[{} for x in range(size)] for x in range(size)]

    nodesMatrix = copy.deepcopy(initNodesMatrix)
    #for row in nodesMatrix:
    #    print(row)
    
    maze = [["." for x in range(size)] for x in range(size)]

    if fileName == "test.txt":
        bytesCount = 12
    else:
        bytesCount = 1024

    maze[size-1][size-1] = "E"
    lastByte = simulateBytesFalling(maze,bytesArray,bytesCount)

    cp = (0,0)
    steps = getSteps(maze,cp,0,bytesCount)
    
    while True:
        if len(steps) == 0:
            break
        currentStep = steps.pop(0)
        cp = currentStep[0]
        stepsCount = currentStep[1]
        steps.extend(getSteps(maze,cp,stepsCount,bytesCount))

    #Part 1
    br_sc =  nodesMatrix[size-1][size-1][bytesCount]["min"]
    print("Bottom right step count:", br_sc)

    #Part 2
    bytesCount += 1
    #for row in nodesMatrix:
    #    print(row)
        
    while bytesCount < len(bytesArray):
        #lastByte = simulateBytesFalling(maze,bytesArray,bytesCount)
        lastByte = bytesArray[bytesCount]
        x = lastByte[0]
        y = lastByte[1]
        maze[y][x] = "#"
        #nodesMatrix = [[{} for x in range(size)] for x in range(size)]
        #nodesMatrix = copy.deepcopy(initNodesMatrix)
        cp = (0,0)
        steps = getSteps(maze,cp,0,bytesCount)
        while True:
            if len(steps) == 0:
                break
            currentStep = steps.pop(0)
            cp = currentStep[0]
            stepsCount = currentStep[1]
            steps.extend(getSteps(maze,cp,stepsCount,bytesCount))

        if not bytesCount in nodesMatrix[size-1][size-1]:
            break
        
        bytesCount += 1
        
    print("Bytes count:",bytesCount)
    print("Blocking byte:", lastByte)
    
    
def getSteps(maze,cp,stepsCount,bytesCount):
    global nodesMatrix
    
    x = cp[0]
    y = cp[1]

    if x < 0 or y < 0:
        return []

    try:
        cell = maze[y][x]
    except:
        return []

    if cell == "#":
        return []

    node = nodesMatrix[y][x]
    if not bytesCount in node:
        node[bytesCount] = {}

  
    if not "min" in node[bytesCount]:
        node[bytesCount]["min"] = stepsCount
    else:
        minSteps = node[bytesCount]["min"]
        if stepsCount >= minSteps:
            return []
        else:
            node[bytesCount]["min"] = stepsCount

    if cell == "E":
        return []
        
    stepLeft = ((x-1,y),stepsCount + 1)
    stepRight = ((x+1,y),stepsCount + 1)
    stepUp = ((x,y-1),stepsCount + 1)
    stepDown = ((x,y+1),stepsCount + 1)

    return [stepLeft,stepRight,stepUp,stepDown]

def simulateBytesFalling(maze,bytesArray,bytesCount):
    for i in range(bytesCount):
        currentByte = bytesArray[i]
        x = currentByte[0]
        y = currentByte[1]
        maze[y][x] = "#"

    return (x,y)
        
if __name__ == "__main__":
    main()
