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

    global scoreMatrix 
    scoreMatrix = [[{} for x in range(len(maze[0]))] for x in range (len(maze))]

    #for row in scoreMatrix:
    #    print(row)

    #First attempt - recursively - fails because of recursion limit
    #traverseMaze(maze,cp,direction,0,scoreMatrix)

    #Second attempt - queue
    steps = getSteps(cp,direction,0,[cp])
    

    while True:
        if len(steps) == 0:
            break

        currentStep = steps.pop(0)
        cp = currentStep[0]
        cd = currentStep[1]
        cs = currentStep[2]
        stepsTaken = currentStep[3]
        steps.extend(performStep(maze,cp,cd,cs,stepsTaken))
        
    #for row in scoreMatrix:
    #    print(row)

    
    #print(scoreMatrix[ep[1]][ep[0]])

    finishScores = scoreMatrix[ep[1]][ep[0]]

    minScore = 0
    for score in finishScores:
        if score != "E" and score != "W" and score != "N" and score != "S":
            continue
        if minScore == 0 or finishScores[score] < minScore:
            minScore = finishScores[score]

    print("Minimum score:", minScore)

    print("Cell for minimum:", len(finishScores[minScore]))

    #for row in maze:
    #    print(row)

    newMaze = []
    for i in range(len(maze)):
        currentRow = []
        for j in range(len(maze[0])):
            if (j,i) in finishScores[minScore]:
                currentRow.append("O")
            else:
                currentRow.append(maze[i][j])
        newMaze.append(currentRow)
        

    #for row in newMaze:
    #    print(*row)
    
def traverseMaze(maze,cp,cd,cs,scoreMatrix):

    if maze[cp[1]][cp[0]] == "#":
        return
    
    isAdded = addScore(scoreMatrix,cp,cd,cs)

    if not isAdded:
        return

    if maze[cp[1]][cp[0]] == "E":
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
 
def getSteps(cp,cd,cs,stepsTaken):
    
    stepForward = (getNextCell(cp,cd),cd,cs+1,stepsTaken+[getNextCell(cp,cd)])

    newDirection = getNextDirection(cd,"Right")
    newCell = getNextCell(cp, newDirection)
    stepRight = (newCell,newDirection,cs+1001,stepsTaken+[newCell])

    newDirection = getNextDirection(cd,"Left")
    newCell = getNextCell(cp, newDirection)
    stepLeft = (newCell,newDirection,cs+1001,stepsTaken+[newCell])

    return [stepForward,stepRight,stepLeft]

def performStep(maze,cp,cd,cs,stepsTaken):
    global scoreMatrix
    
    if maze[cp[1]][cp[0]] == "#":
        return []
    
    isAdded = addScore(cp,cd,cs)  
    if not isAdded:
        return []

    if maze[cp[1]][cp[0]] == "E":
        #print(scoreMatrix)
        cellScores = scoreMatrix[cp[1]][cp[0]]
        #print("Cell scores",cellScores)
        if cs in cellScores:
            #print("CS already in", cs)
            stepsAlready = cellScores[cs]
            for step in stepsTaken:
                if not step in stepsAlready:
                    cellScores[cs].append(step)
        else:
            #print("CS",cs)
            #print("not in")
            #print (cellScores)
            cellScores[cs] = stepsTaken
        return []

    return getSteps(cp,cd,cs,stepsTaken)
    
def addScore(cp,cd,cs):
    global scoreMatrix
    cellScores = scoreMatrix[cp[1]][cp[0]]

    if (not cd in cellScores or cellScores[cd] >= cs):
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

    
if __name__ == "__main__":
    main()

