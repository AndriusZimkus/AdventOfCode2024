def main():
    fileName = "input.txt"
            
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
                
    #for row in newWarehouse:
    #    print(*row)

    i = 0
    for step in list(instructions):
        #print("Step",i+1,step)
        rp,hasMoved = moveCell_Part2(newWarehouse,rp,step)
        i += 1


    #for row in newWarehouse:
    #    print(*row)

    gpsSum = getGPSSum(newWarehouse)
    print("Part 2, GPS sum:", gpsSum)



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
            if symbol == "O" or symbol == "[":
                gpsSum += i*100+j
    return gpsSum

#Part 2
def getNextCell(cell,step):
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

def moveCell_Part2(warehouse,cell,step):
    nextCell = getNextCell(cell,step)
    
    symbol = getCell(warehouse,cell)
    nextSymbol = getCell(warehouse,nextCell)
    isHorizontalStep = (step == ">" or step == "<")
    isNextBox = isBoxSymbol(nextSymbol)

    if nextSymbol == ".":
        swapCells(warehouse,cell,nextCell)
        if symbol == "@":
            cell = nextCell
        return cell, True
    elif nextSymbol == "#":
        return cell,False
    elif isNextBox and isHorizontalStep:
        #print("Cell",cell)
        otherCell, hasNextMoved = moveCell_Part2(warehouse,nextCell,step)
        hasMoved = False
        if hasNextMoved:
            cell, hasMoved = moveCell_Part2(warehouse,cell,step)
        return cell, hasMoved
    elif isNextBox and not isHorizontalStep:
        if nextSymbol == "[":
            box = nextCell
        else:
            box = (nextCell[0]-1,nextCell[1])
        boxes = [box]
        hasBoxMoved = moveBoxesVertically(warehouse,step,boxes)
        
        hasMoved = False
        if hasBoxMoved:
            cell, hasMoved = moveCell_Part2(warehouse,cell,step)
        return cell, hasMoved
    
    else:
        return cell,False
    
def moveBoxesVertically(warehouse,step,boxes):
    
    newBoxes = []
    #Check all beyond boxes
    for box in boxes:
        bx = box[0]
        by = box[1]
        boxRight = (bx+1,by)

        nextCell_1 = getNextCell(box,step)
        nextCell_2 = getNextCell(boxRight,step)
        nextSymbol_1 = getCell(warehouse,nextCell_1)
        nextSymbol_2 = getCell(warehouse,nextCell_2)

        if nextSymbol_1 == "#" or nextSymbol_2 == "#":
            return False

        if isBoxSymbol(nextSymbol_1):
            
            if nextSymbol_1 == "[":
                newBox = nextCell_1
            else:
                newBox = (nextCell_1[0]-1,nextCell_1[1])

            if not newBox in newBoxes:
                newBoxes.append(newBox)

        if isBoxSymbol(nextSymbol_2):
            if nextSymbol_2 == "[":
                newBox = nextCell_2
            else:
                newBox = (nextCell_2[0]-1,nextCell_2[1])

            if not newBox in newBoxes:
                newBoxes.append(newBox)

    if len(newBoxes) > 0:
        haveBoxesMoved = moveBoxesVertically(warehouse,step,newBoxes)
    else:
        haveBoxesMoved = True

    if not haveBoxesMoved:
        return False

    #Move boxes
    for box in boxes:
        bx = box[0]
        by = box[1]
        boxRight = (bx+1,by)
        nextCell_1 = getNextCell(box,step)
        nextCell_2 = getNextCell(boxRight,step)
        
        swapCells(warehouse,box,nextCell_1)
        swapCells(warehouse,boxRight,nextCell_2)

    return True


def getCell(warehouse,cell):
    x = cell[0]
    y = cell[1]
    return warehouse[y][x]
    
def swapCells(warehouse,cell,nextCell):
    x1 = cell[0]
    y1 = cell[1]
    x2 = nextCell[0]
    y2 = nextCell[1]

    warehouse[y1][x1], warehouse[y2][x2] = warehouse[y2][x2],warehouse[y1][x1]

def isBoxSymbol(symbol):
    return (symbol == "[" or symbol == "]")

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

