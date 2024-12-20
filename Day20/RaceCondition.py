def main():
 
    fileName = "test.txt"
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

    global cheatsPossible
    global cheatsAdded
    cheatsPossible = []
    cheatsAdded = {}
    #initDistances = [[0 for x in range(len(raceTrack[0]))] for x in range(len(raceTrack))]    
    #for row in raceTrack:
    #    print(row)
    initDistances = traverseRaceTrack(raceTrack,sp)
    #print(ep)
    #print(sp)

    
    initialDistance = initDistances[ep[1]][ep[0]]
    print("Initial distance:",initialDistance)
    #for row in initDistances:
    #    print(row)

    #Determine cheats and traverse
    print(cheatsPossible)
        


def traverseRaceTrack(raceTrack,sp):
    distances = [
        [0 for x in range(len(raceTrack[0]))]
        for x in range(len(raceTrack))]

    steps = getSteps(sp,0)
    
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
                print("NC for cheat", nextCell)
                print("nY", nY)
                print("nX", nX)
                if nextCell == "." and nY >= 0 and nx >= 0:
                    print("CA",cheatsAdded)
                    if not nextCellPos in cheatsAdded:
                        cheatsAdded[nextCellPos] = True
                        cheatsPossible.append((startPos,pos))
            except:
                pass
                
            return []

        if distances[y][x] != 0 and currDist >= distances[y][x]:
            return []

        if distances[y][x] == 0 or currDist < distances[y][x]:
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
