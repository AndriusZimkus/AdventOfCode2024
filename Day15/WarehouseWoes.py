
def main():
    fileName = "test2.txt"
            
    path = "../../Advent Of Code Cases/Day15/" + fileName

    warehouse = []
    
    with open(path, 'r') as file:
        instructions = ""
        isWarehouse = True
        for line in file:
            currentRow = []
            if line.strip() == "":
                isWarehouse = False
                continue

            if isWarehouse:
                for symbol in list(line.strip()):
                    currentRow.append(symbol)
                warehouse.append(currentRow)
            else:
                instructions = instructions + line.strip()
                                        

    newWarehouse = transformWarehouse(warehouse)
    for i in range(len(warehouse)):
        for j in range(len(warehouse[0])):
            if warehouse[i][j] == "@":
                rp = (j,i)
                        
    print(rp)

    i = 0
    for step in list(instructions):
        rp,isMoved = moveCell_Part1(warehouse,rp,step,rp)
        i += 1

    gpsSum = getGPSSum(warehouse)
    print("Part 1, GPS sum:", gpsSum)

    #Part 2
    for i in range(len(newWarehouse)):
        for j in range(len(newWarehouse[0])):
            if newWarehouse[i][j] == "@":
                rp = (j,i)
                
    for row in newWarehouse:
        print(*row)

    i = 0
    for step in list(instructions):
        #print("Step",i+1,step)
        rp = moveCell_Part2(newWarehouse,rp,step,rp)
        i += 1
        #if i > 155:
        #    for row in newWarehouse:
        #        print(*row)
        #if i > 5:
        #    break
    for row in newWarehouse:
        print(*row)


def moveCell_Part1(warehouse,cell,step,rp):
    cx = cell[0]
    cy = cell[1]

    if step == "<":
        vx = -1
        vy = 0
    elif step == "^":
        vx = 0
        vy = -1
    elif step == ">":
        vx = 1
        vy = 0
    elif step == "v":
        vx = 0
        vy = 1
    else:
        return rp,False

    symbol = warehouse[cy][cx]
    nextSymbol = warehouse[cy+vy][cx+vx]

    if nextSymbol == ".":
        warehouse[cy][cx],warehouse[cy+vy][cx+vx] = warehouse[cy+vy][cx+vx],warehouse[cy][cx]
        if symbol == "@":
            rp = (cx+vx,cy+vy)
        return rp, True
    
    elif nextSymbol == "#":
        return rp,False

    elif nextSymbol == "O":
        rp,nextMoved = moveCell_Part1(warehouse,(cx+vx,cy+vy),step,rp)
        if nextMoved:
            warehouse[cy][cx],warehouse[cy+vy][cx+vx] = warehouse[cy+vy][cx+vx],warehouse[cy][cx]
            if symbol == "@":
                rp = (cx+vx,cy+vy)
            return rp,True
        else:
            return rp,False
            
    else:
        return rp, False



def getGPSSum(warehouse):
    gpsSum = 0
    for i in range(len(warehouse)):
        for j in range(len(warehouse[0])):
            symbol = warehouse[i][j]
            if symbol == "O":
                gpsSum += i*100+j
    return gpsSum

def moveCell_Part2(warehouse,cell,step,rp):

    #print("Cell",cell)
    canMove = canCellMove(warehouse,cell,step)

    if canMove:
        rp = performMove(warehouse,cell,step,rp)

    return rp

def performMove(warehouse,cell,step,rp):
    cx = cell[0]
    cy = cell[1]

    if step == "<":
        vx = -1
        vy = 0
    elif step == "^":
        vx = 0
        vy = -1
    elif step == ">":
        vx = 1
        vy = 0
    elif step == "v":
        vx = 0
        vy = 1
    else:
        return rp
    
    symbol = warehouse[cy][cx]
    nextSymbol = warehouse[cy+vy][cx+vx]
    
    if nextSymbol == ".":
        warehouse[cy][cx],warehouse[cy+vy][cx+vx] = warehouse[cy+vy][cx+vx],warehouse[cy][cx]
        if symbol == "@":
            rp = (cx+vx,cy+vy)
        return rp
    
    elif nextSymbol == "#":
        return rp

    elif nextSymbol == "[" or nextSymbol == "]":
        rp = moveBox(warehouse,(cx+vx,cy+vy),step,rp)
        if symbol == "@":
            rp = performMove(warehouse,cell,step,rp)
        return rp
    else:
        return rp 

def moveBox(warehouse,cell,step,rp):
    if step == "<" or step == ">":
        cx = cell[0]
        cy = cell[1]
        nextCell = getNextCell(warehouse,cell,step)

        nextSymbol = warehouse[nextCell[1]][nextCell[0]]

        #Move other out of the way
        if nextSymbol == "[" or nextSymbol == "]":
            rp = moveBox(warehouse,nextCell,step,rp)
        else:
            rp = performMove(warehouse,nextCell,step,rp)

        #Move self
        return performMove(warehouse,cell,step,rp)
    else:
        #Up Down
        cx = cell[0]
        cy = cell[1]
        symbol = warehouse[cy][cx]
        #print("Symbol",symbol,"Cell",cell)
        
        nc1 = getNextCell(warehouse,cell,step)

        ns1 = warehouse[nc1[1]][nc1[0]]

        if symbol == "[":
            ox = cx + 1
        else:
            ox = cx - 1

        other = (ox,cy)
        nc2 = getNextCell(warehouse,other,step)

        #Move above/below boxes
        if symbol == ns1:
            rp = moveBox(warehouse,nc1,step,rp)
        elif (symbol == "[" and ns1 == "]") or (symbol == "]" and ns1 == "[") :
            #print("Two boxes")
            rp = moveBox(warehouse,nc1,step,rp)
            rp = moveBox(warehouse,nc2,step,rp)

        #Move oneself
        rp = performMove(warehouse,cell,step,rp)
        rp = performMove(warehouse,(ox,cy),step,rp)

        return rp

    
def canCellMove(warehouse,cell,step):
    cx = cell[0]
    cy = cell[1]

    if step == "<":
        vx = -1
        vy = 0
    elif step == "^":
        vx = 0
        vy = -1
    elif step == ">":
        vx = 1
        vy = 0
    elif step == "v":
        vx = 0
        vy = 1
    else:
        return False

    symbol = warehouse[cy][cx]
    nextSymbol = warehouse[cy+vy][cx+vx]

    if nextSymbol == ".":
        return True
    elif nextSymbol == "#":
        return False
    elif nextSymbol == "[" or nextSymbol == "]":
        return canBoxMove(warehouse,cell,step)   
    return False

def canBoxMove(warehouse,cell,step):
    if step == "<" or step == ">":
        return canCellMove(warehouse,getNextCell(warehouse,cell,step),step)
    else:
        cx = cell[0]
        cy = cell[1]
        symbol = warehouse[cy][cx]

        if symbol == "[":
            ox = cx+1
        else:
            ox = cx-1

        nc1 = getNextCell(warehouse,cell,step)
        nc2 = getNextCell(warehouse,(ox,cy),step)

        ns1 = warehouse[nc1[1]] [nc1[0]]
        ns2 = warehouse[nc2[1]] [nc2[0]]
        if ns1 == "." and ns2 == ".":
            return True
        elif ns1 == "#" or ns2 == "#":
            return False
        elif symbol == ns1:
            return canBoxMove(warehouse,nc1,step)
        else:
            return canBoxMove(warehouse,nc1,step) and canBoxMove(warehouse,nc2,step)


def getNextCell(warehouse,cell,step):
    cx = cell[0]
    cy = cell[1]
    if step == "<":
        vx = -1
        vy = 0
    elif step == "^":
        vx = 0
        vy = -1
    elif step == ">":
        vx = 1
        vy = 0
    elif step == "v":
        vx = 0
        vy = 1
    else:
        return cell

    return (cx+vx,cy+vy)

def transformWarehouse(warehouse):
    newWarehouse = []
    for row in warehouse:
        currentRow = []
        for symbol in row:
            if symbol == "@":
                currentRow.append(symbol)
                currentRow.append(".")
            elif symbol == "O":
                currentRow.append("[")
                currentRow.append("]")
            else:
                currentRow.append(symbol)
                currentRow.append(symbol)

        newWarehouse.append(currentRow)
    return newWarehouse

if __name__ == "__main__":
    main()

