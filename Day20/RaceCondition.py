def main():
 
    fileName = "test2.txt"
    path = "../../Advent Of Code Cases/Day20/" + fileName

    raceTrack = []
    with open(path, 'r') as file:
        for line in file:
            line = list(line.strip())
            raceTrack.append(line)

    for i in range(len(raceTrack)):
        for j in range(len(raceTrack[i])):
            if raceTrack[i][j] == "E":
                ep = (j,i)
            if raceTrack[i][j] == "S":
                sp = (j,i)

    #Part 1
    global cheatsPossible
    global cheatsAdded
    global initDistances
    cheatsPossible = []
    cheatsAdded = {}
    
    initDistances = traverseRaceTrack(raceTrack,sp)
    initialDistance = initDistances[ep[1]][ep[0]]
    print("Initial distance:",initialDistance)
    
    saves = {}
    savesAtLeast100 = 0
    for cheat in cheatsPossible:
        startPos = cheat[0]
        cheatPos = cheat[1]
        direction = cheat[2]
        x = cheatPos[0]
        y = cheatPos[1]

        cheatFinishPos = getNextCellPos(raceTrack,x,y,direction)

        startPosValue = getMatrixCell(initDistances,startPos)
        finishPosValue = getMatrixCell(initDistances,cheatFinishPos)

        saveValue = finishPosValue - startPosValue - 2
        
        if saveValue >= 100:
            savesAtLeast100 += 1
        saves[saveValue] = saves.get(saveValue, 0) + 1
        

    print("Cheats possible:",len(cheatsPossible))
    print("Saves at least 100:",savesAtLeast100)

    #Part 2
    #Determine all possible cheats
    saves = {}
    cheats2 = getCheats_Part2(raceTrack,sp)
    #print("Printing cheats")
    for cheat in cheats2:
        print(cheat)
        finishPositionsConsidered = []
        startPos = cheat[0]
        startPosDist = getMatrixCell(initDistances,startPos)

        finishPositions = cheat[1]
        for fp in finishPositions:
            fpPos = fp[0]
            fpStepCount = fp[1]
            if fpPos in finishPositionsConsidered:
                continue
            finishPositionsConsidered.append(fpPos)
            finishPosDist = getMatrixCell(initDistances,fpPos)

            saveValue = finishPosDist-startPosDist - fpStepCount

            #if saveValue >= 50:
            saves[saveValue] = saves.get(saveValue, 0) + 1
                
    print(saves)


def getCheats_Part2(raceTrack,sp):
    steps = getSteps(sp,0)
    cheats = []

    nextCell = getMatrixCell(raceTrack,sp)
    currentPos = sp

    #Traverse track and determine all cheats for all cells
    while nextCell != "E":


        cheatsForCell = getCheatsForCell(raceTrack,currentPos)

        if len(cheatsForCell) > 0:
            cheats.append((currentPos,cheatsForCell))
        
        nextTrackPos = getNextTrackPos(raceTrack,currentPos)

        nextCell = getMatrixCell(raceTrack,nextTrackPos)
        currentPos = nextTrackPos
        
        #print(nextCell)

    return cheats

def getCheatsForCell(raceTrack,pos):
    #BFS - with queue - second attempt

    return []    

    #Recursively determine possible cheats - first attempt
##    global visitedCellsDists
##    visitedCellsDists = {}
##    finPosOfCheats = []
##    initialDistance = getMatrixCell(initDistances,pos)
##    initials = getInitials(raceTrack,pos)
##    for initial in initials:
##
##        finPosOfCheats.extend(getCheatsForCell_rec(raceTrack,initial,1,initialDistance,pos))
##
##    if len(finPosOfCheats)>0:
##        return finPosOfCheats
##    else:
##        return []

def getCheatsForCell_rec(raceTrack,pos,step,startDist,fromPos):
    global visitedCellsDists
    x = pos[0]
    y = pos[1]
    c = len(raceTrack[0])
    r = len(raceTrack)

    if x == 0 or y == 0 or x == c-1 or y == r-1:
        return []

    if step >= 20:
        return []

    if pos in visitedCellsDists and visitedCellsDists[pos] <= step:
        return []

    visitedCellsDists[pos] = step

    finPosOfCheats = []

    nextPositions = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
    nextPositions.remove(fromPos)

    #Check next positions - end of cheat or continue cheat
    for nextPos in nextPositions:
        nextCell = getMatrixCell(raceTrack,nextPos)
        
        if nextCell == "." or nextCell == "E":
            #End of cheat
            nextCellDist = getMatrixCell(initDistances,nextPos)

            if (nextCellDist - startDist - (step+1)) > 0:

                finPosOfCheats.append((nextPos,step+1))
        elif nextCell == "#":
            #Cheat continues:
            finPosOfCheats.extend(getCheatsForCell_rec(raceTrack,nextPos,step+1,startDist,pos))
            
    return finPosOfCheats

    

def getInitials(raceTrack,pos):
    x = pos[0]
    y = pos[1]
    initials = []

    #Up
    try:
        nextPosX = x
        nextPosY = y-1
        nextCell = raceTrack[nextPosY][nextPosX]
        if nextCell == "#":
            initials.append((nextPosX,nextPosY))
    except:
        pass

    #Down
    try:
        nextPosX = x
        nextPosY = y+1
        nextCell = raceTrack[nextPosY][nextPosX]
        if nextCell == "#":
            initials.append((nextPosX,nextPosY))
    except:
        pass

    #Left
    try:
        nextPosX = x-1
        nextPosY = y
        nextCell = raceTrack[nextPosY][nextPosX]
        if nextCell == "#":
            initials.append((nextPosX,nextPosY))
    except:
        pass

    #Right
    try:
        nextPosX = x+1
        nextPosY = y
        nextCell = raceTrack[nextPosY][nextPosX]
        if nextCell == "#":
            initials.append((nextPosX,nextPosY))
    except:
        pass

    return initials

def getNextTrackPos(raceTrack,pos):
    global initDistances
    x = pos[0]
    y = pos[1]
    posDist = initDistances[y][x]
    
    #Up
    try:
        nextPosX = x
        nextPosY = y-1
        nextCell = raceTrack[nextPosY][nextPosX]
        nextPosDist = initDistances[nextPosY][nextPosX]
        if (nextCell == "." or nextCell == "E") and nextPosDist > posDist:
            return (nextPosX,nextPosY)
    except:
        pass

    #Down
    try:
        nextPosX = x
        nextPosY = y+1
        nextCell = raceTrack[nextPosY][nextPosX]
        nextPosDist = initDistances[nextPosY][nextPosX]
        if (nextCell == "." or nextCell == "E") and nextPosDist > posDist:
            return (nextPosX,nextPosY)
    except:
        pass

    #Left
    try:
        nextPosX = x-1
        nextPosY = y
        nextCell = raceTrack[nextPosY][nextPosX]
        nextPosDist = initDistances[nextPosY][nextPosX]
        if (nextCell == "." or nextCell == "E") and nextPosDist > posDist:
            return (nextPosX,nextPosY)
    except:
        pass

    #Right
    try:
        nextPosX = x+1
        nextPosY = y
        nextCell = raceTrack[nextPosY][nextPosX]
        nextPosDist = initDistances[nextPosY][nextPosX]
        if (nextCell == "." or nextCell == "E") and nextPosDist > posDist:
            return (nextPosX,nextPosY)
    except:
        pass

    
    
def getMatrixCell(matrix,pos):
    x = pos[0]
    y = pos[1]
    cell = ""
    try:
        cell = matrix[y][x]
    except:
        pass
    
    return cell


def traverseRaceTrack(raceTrack,sp):
    distances = [
        [-1 for x in range(len(raceTrack[0]))]
        for x in range(len(raceTrack))]

    steps = getSteps(sp,0)
    distances[sp[1]][sp[0]] = 0
    
    def performStep(step):
        nonlocal distances
        nonlocal raceTrack
        global cheatsPossible
        global cheatsAdded
        
        startPos = step[0]
        pos = step[1]
        currDist = step[2]
        direction = step[3]
        
        x = pos[0]
        y = pos[1]
        try:
            cell = raceTrack[y][x]
        except:
            return []

        if x < 0 or y < 0:
            return []

        if cell == "#":
            #Check for cheats
            nextCellPos = getNextCellPos(raceTrack,x,y,direction)
            nX = nextCellPos[0]
            nY = nextCellPos[1]
            try:
                nextCell = raceTrack[nY][nX]

                if (nextCell == "." or nextCell == "E") and nY >= 0 and nX >= 0:
 
                    if not pos in cheatsAdded:
                        cheatsAdded[pos] = True
                        cheatsPossible.append((startPos,pos,direction))
            except:
                pass
                
            return []

        if distances[y][x] != -1 and currDist >= distances[y][x]:
            return []

        if distances[y][x] == -1 or currDist < distances[y][x]:
            distances[y][x] = currDist

        if cell == "E":
            return []
        
        steps = getSteps(pos,currDist)

        return steps    

    while len(steps) > 0:

        currentStep = steps.pop(0)
        steps.extend(performStep(currentStep))    
    
    return distances

def getNextCellPos(raceTrack,x,y,direction):
    if direction == "Up":
        return (x,y-1)
    elif direction == "Down":
        return (x,y+1)
    elif direction == "Left":
        return (x-1,y)
    elif direction == "Right":
        return (x+1,y)
    
def getSteps(pos,currDist):
    steps = []
    x = pos[0]
    y = pos[1]
    
    #Up
    steps.append((pos,(x,y-1),currDist+1,"Up"))
    #Down
    steps.append((pos,(x,y+1),currDist+1,"Down"))
    #Left
    steps.append((pos,(x-1,y),currDist+1,"Left"))
    #Right
    steps.append((pos,(x+1,y),currDist+1,"Right"))

    return steps
    
if __name__ == "__main__":
    main()
