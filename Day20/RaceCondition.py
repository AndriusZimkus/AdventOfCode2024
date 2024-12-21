def main():
 
    fileName = "input.txt"
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
    savesOver100 = {}
    savesOver50 = {}
    cheats2 = getCheats_Part2(raceTrack,sp,ep)
    #print("Printing cheats")
    for cheat in cheats2:
        #print(cheat)

        startPos = cheat[0]
        finishPositions = cheat[1]
        for fp in finishPositions:
            finPos = fp[0]
            saveValue = fp[1]
           

            
            saves[saveValue] = saves.get(saveValue, 0) + 1
            if saveValue >= 100:
                savesOver100[saveValue] = savesOver100.get(saveValue, 0) + 1

            if saveValue >= 50:
                savesOver50[saveValue] = savesOver50.get(saveValue, 0) + 1
            
                
    #print("Saves",saves)

    
    myKeys = list(savesOver50.keys())
    myKeys.sort()

    # Sorted Dictionary
    sd = {i: savesOver50[i] for i in myKeys}
    #print("Saves over 50 dict",sd)

    totalSavesOver100 = 0
    for save in savesOver100:
        totalSavesOver100+=savesOver100[save]
    print("Saves over 100",totalSavesOver100)

def getCheats_Part2(raceTrack,sp,ep):
    cheats = []

    nextCell = getMatrixCell(raceTrack,sp)
    currentPos = sp

    #Traverse track and determine all cheats for all cells
    while nextCell != "E":
        cheatsForCell = getCheatsForCell_3(raceTrack,currentPos)
        if len(cheatsForCell) > 0:
            #print(cheatsForCell)
            cheats.append((currentPos,cheatsForCell))
        
        nextTrackPos = getNextTrackPos(raceTrack,currentPos)

        nextCell = getMatrixCell(raceTrack,nextTrackPos)
        currentPos = nextTrackPos
        
        

    return cheats

def getCheatsForCell_3(raceTrack,pos):

    x = pos[0]
    y = pos[1]
    
    startDist = initDistances[y][x]

    cheats = []
    thisCell = raceTrack[y][x]

    
    for i in range(-20,21):
        newX = x + i

        for j in range (-20,21):
            #print(i,j)
            newY = y + j
            totalStep = abs(i)+abs(j)
            if totalStep < 2 or  totalStep>20:
                continue
            newPos = (newX,newY)

            if newX < 0 or newY <0:
                continue

            try:
                endDist = initDistances[newY][newX]
            except:
                continue

            if endDist == -1:
                continue


            save = endDist-startDist-totalStep
            if save > 0:
                #print(save)
                cheats.append((newPos,save))

    return cheats
    


def getCheatsForCell(raceTrack,pos,ep):
    #BFS - with queue - second attempt
    startDist = getMatrixCell(initDistances,pos)
    
    c = len(raceTrack[0])
    r = len(raceTrack)
    finPositionsWithStepCount = []
    finPositionsAdded = {}
    consideredPositions = []
    x = pos[0]
    y = pos[1]
    nextPositions = [((x+1,y),1,[pos]),((x-1,y),1,[pos]),((x,y+1),1,[pos]),((x,y-1),1,[pos])]
    #print(pos)
    validX1 = min(ep[0],x)
    validX2 = max(ep[0],x)
    
    validY1 = min(ep[1],y)
    validY2 = max(ep[1],y)

    while len(nextPositions) > 0:
        currentPosition = nextPositions.pop(0)
        cp = currentPosition[0]
        stepCount = currentPosition[1]
        #print(stepCount)
        #print("CurrentPosition object",currentPosition)
        visitedPositions = currentPosition[2]
        #print(visitedPositions)

        cX = cp[0]
        cY = cp[1]

        if stepCount > 20:
            continue
        
        if cp in visitedPositions:
            continue
        if cp in consideredPositions:
            continue

        if cX == 0 or cY == 0 or cX == c-1 or cY == r-1:
            continue

        if cX < validX1 or cY < validY1 or cX > validX2 or cY > validY2:
            continue

        cell = getMatrixCell(raceTrack,cp)
        
        if cell == "." or cell == "E":
            #End of cheat
            cellDist = getMatrixCell(initDistances,cp)
            for vp in visitedPositions:
                consideredPositions.append(vp)

            if (cellDist - startDist - (stepCount+1)) > 0:
                if not cp in finPositionsAdded:
                    finPositionsAdded[cp] = True
                    finPositionsWithStepCount.append((cp,stepCount))
                
        elif cell == "#":
            #Cheat continues:
            sc = stepCount+1

            nextPosForCell = [((cX+1,cY),sc,visitedPositions + [cp]),((cX-1,cY),sc,visitedPositions + [cp]),((cX,cY+1),sc,visitedPositions + [cp]),((cX,cY-1),sc,visitedPositions + [cp])]
            nextPositions.extend(nextPosForCell)
    

    return finPositionsWithStepCount   

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

    if step > 20:
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
