
def main():
 
    fileName = "input.txt"
            
    path = "../../Advent Of Code Cases/Day16/" + fileName

    maze = []
    
    with open(path, 'r') as file:
        for line in file:
            maze.append(str(line.strip()))

    direction = "E"
    #for row in maze:
    #    print(row)

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "S":
                cp = (j,i)
            elif maze[i][j] == "E":
                ep = (j,i)

    print(cp)
    print(ep)

    scoreMatrix = [[{} for x in range(len(maze[0]))] for x in range (len(maze))]

    #for row in scoreMatrix:
    #    print(row)

    #First attempt - recursively
    #traverseMaze(maze,cp,direction,0,scoreMatrix)

    #Second attempt - queue
    steps = getSteps(cp,direction,0)

    while True:
        if len(steps) == 0:
            break

        currentStep = steps.pop(0)
        cp = currentStep[0]
        cd = currentStep[1]
        cs = currentStep[2]
        steps.extend(performStep(maze,cp,cd,cs,scoreMatrix))
        
    #for row in scoreMatrix:
    #    print(row)

    
    print(scoreMatrix[ep[1]][ep[0]])

    finishScores = scoreMatrix[ep[1]][ep[0]]

    minScore = 0
    for score in finishScores:
        if minScore == 0 or finishScores[score] < minScore:
            minScore = finishScores[score]

    print("Minimum score:", minScore)


def traverseMaze(maze,cp,cd,cs,scoreMatrix):

    if maze[cp[1]][cp[0]] == "#":
        return
    
    isAdded = addScore(scoreMatrix,cp,cd,cs)

    if not isAdded:
        return

    #Recursively go forward, go right, go left
    #Forward
    traverseMaze(maze,getNextCell(cp,cd),cd,cs+1,scoreMatrix)

    #Right
    newDirection = getNextDirection(cd,"Right")
    newCell = getNextCell(cp, newDirection)
    traverseMaze(maze,newCell,newDirection,cs+1001,scoreMatrix)

    #Left
    newDirection = getNextDirection(cd,"Left")
    newCell = getNextCell(cp, newDirection)
    traverseMaze(maze,newCell,newDirection,cs+1001,scoreMatrix)
 
def getSteps(cp,cd,cs):
    stepForward = (getNextCell(cp,cd),cd,cs+1)

    newDirection = getNextDirection(cd,"Right")
    newCell = getNextCell(cp, newDirection)
    stepRight = (newCell,newDirection,cs+1001)

    newDirection = getNextDirection(cd,"Left")
    newCell = getNextCell(cp, newDirection)
    stepLeft = (newCell,newDirection,cs+1001)

    return [stepForward,stepRight,stepLeft]

def performStep(maze,cp,cd,cs,scoreMatrix):
    if maze[cp[1]][cp[0]] == "#":
        return []
    
    isAdded = addScore(scoreMatrix,cp,cd,cs)  
    if not isAdded:
        return []

    return getSteps(cp,cd,cs)
    
def addScore(scoreMatrix,cp,cd,cs):
    cellScores = scoreMatrix[cp[1]][cp[0]]

    isOpp = isOppositeInScores(cd,cellScores)

    if (not cd in cellScores or cellScores[cd] > cs):
        cellScores[cd] = cs
        return True
    else:
        return False

def getNextCell(cp,cd):
    x = cp[0]
    y = cp[1]
    if cd == "E":
        return (x+1, y)
    elif cd == "W":
        return (x-1, y)
    elif cd == "N":
        return (x, y-1)
    elif cd == "S":
        return (x, y+1)

def getNextDirection(cd,turn):
    directions = ["E","S","W","N"]
    index = directions.index(cd)
    if turn == "Right":
        return directions[(index+1)%len(directions)]
    elif turn == "Left":
        return directions[index-1]

def isOppositeInScores(cd,cellScores):
    return (cd == "E" and "W" in cellScores
        or cd == "W" and "E" in cellScores
        or cd == "N" and "S" in cellScores
        or cd == "S" and "N" in cellScores)

    
if __name__ == "__main__":
    main()

