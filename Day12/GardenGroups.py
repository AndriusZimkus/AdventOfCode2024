def main(fileName):

    garden = []

    with open(fileName, 'r') as file:
        for line in file:
            currentRow = list(line.strip())
            garden.append(currentRow)

    #Determine regions
    regionMatrix = [[-1 for x in garden] for x in garden[0]]
    
    nextRegion = 1
    for i in range(len(garden)):
        for j in range(len(garden[i])):
            cell = garden[i][j]

            if regionMatrix[i][j] == -1:
                nextRegion = determineCellRegion(garden,regionMatrix,i,j,nextRegion,cell)

    regionAreas = {}
    regionPerimeters = {}
    regionSideCount = {}
    for i in range(len(regionMatrix)):
        for j in range(len(regionMatrix[i])):
            region = regionMatrix[i][j]

            cellPerimeterWeight = getCellPerimeterWeight(regionMatrix,i,j)

            if not region in regionAreas:
                regionAreas[region] = 1
                regionPerimeters[region] = cellPerimeterWeight
            else:
                regionAreas[region] += 1
                regionPerimeters[region] += cellPerimeterWeight


    regionSideCount = getRegionSideCount(regionMatrix)
    price = 0
    price2 = 0
    for region in regionAreas:
        regionPrice = regionAreas[region] * regionPerimeters[region]
        regionPrice2 = regionAreas[region] * regionSideCount[region]
        price += regionPrice
        price2 += regionPrice2

    print(f"{fileName} part 1 price: {price}")
    print(f"{fileName} part 2 price: {price2}")


def determineCellRegion(garden,regionMatrix,i,j,nextRegion,neededLetter):
    if i < 0 or j < 0:
        return nextRegion

    try:
        cell = garden[i][j]
    except:
        return nextRegion

    if regionMatrix[i][j] != -1:
        return nextRegion
    

    if cell == neededLetter:
        regionMatrix[i][j] = nextRegion
        determineCellRegion(garden,regionMatrix,i+1,j,nextRegion,neededLetter)
        determineCellRegion(garden,regionMatrix,i-1,j,nextRegion,neededLetter)
        determineCellRegion(garden,regionMatrix,i,j+1,nextRegion,neededLetter)
        determineCellRegion(garden,regionMatrix,i,j-1,nextRegion,neededLetter)
        return nextRegion + 1

    else:
        return nextRegion


def getCellPerimeterWeight(matrix,i,j):
    weigth = 0
    if getCell(matrix,i,j) != getCell(matrix,i+1,j):
        weigth += 1
    if getCell(matrix,i,j) != getCell(matrix,i-1,j):
        weigth += 1
    if getCell(matrix,i,j) != getCell(matrix,i,j+1):
        weigth += 1
    if getCell(matrix,i,j) != getCell(matrix,i,j-1):
        weigth += 1

    return weigth
   

def getCell(matrix,i,j):
    if i < 0 or j < 0:
        return -1
    try:
        return matrix[i][j]
    except:
        return -1

def getRegionSideCount(matrix):

    regionSideCount = {}

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            region = getCell(matrix,i,j)
            
            if hasDistinctTopEdge(matrix,i,j):
                addToDict(regionSideCount,region)

            if hasDistinctBottomEdge(matrix,i,j):
                addToDict(regionSideCount,region)

            if hasDistinctLeftEdge(matrix,i,j):
                addToDict(regionSideCount,region)

            if hasDistinctRightEdge(matrix,i,j):
                addToDict(regionSideCount,region)


    return regionSideCount

def hasDistinctTopEdge(matrix,i,j):
    if getCell(matrix,i,j) == getCell (matrix,i-1,j):
        return False

    if getCell(matrix,i,j) != getCell(matrix,i,j-1):
        return True

    #Corner
    if getCell(matrix,i,j-1) == getCell(matrix,i-1,j-1):
        return True

    return False

def hasDistinctBottomEdge(matrix,i,j):
    if getCell(matrix,i,j) == getCell (matrix,i+1,j):
        return False

    if getCell(matrix,i,j) != getCell(matrix,i,j-1):
        return True

    #Corner
    if getCell(matrix,i,j-1) == getCell(matrix,i+1,j-1):
        return True

    return False


def hasDistinctLeftEdge(matrix,i,j):
    if getCell(matrix,i,j) == getCell (matrix,i,j-1):
        return False

    if getCell(matrix,i,j) != getCell(matrix,i-1,j):
        return True

    #Corner
    if getCell(matrix,i-1,j) == getCell(matrix,i-1,j-1):
        return True

    return False

def hasDistinctRightEdge(matrix,i,j):
    if getCell(matrix,i,j) == getCell (matrix,i,j+1):
        return False

    if getCell(matrix,i,j) != getCell(matrix,i-1,j):
        return True

    #Corner
    if getCell(matrix,i-1,j) == getCell(matrix,i-1,j+1):
        return True

    return False
    
def addToDict(regionSideCount,region):
    if region in regionSideCount:
        regionSideCount[region] += 1
    else:
        regionSideCount[region] = 1

if __name__ == "__main__":

    fileNames = ["test.txt","test2.txt","test3.txt","test4.txt","test5.txt","input.txt"]

    for fileName in fileNames:
        main(fileName)
