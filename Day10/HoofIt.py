def main():

    topo = []
    with open('input.txt', 'r') as file:
            for line in file:
                line = [int(i) for i in line.strip()]
                topo.append(line)


    #print(topo)

    trailheadScore = 0
    trailheadRating = 0
    for i in range(len(topo)):
        for j in range(len(topo[i])):
            cell = topo[i][j]

            if cell == 0:
                #Traverse
                trailheadScore += traverse0Helper(topo,j,i,True)
                trailheadRating += traverse0Helper(topo,j,i,False)

    #Trailhead score - count of 9s reached
    print("Trailhead score:", trailheadScore)

    #Trailhead rating - number of distinct paths to 9s
    print("Trailhead rating:", trailheadRating)
                


def traverse0Helper(topo,x,y,toApplyVisits):
    rowCount = len(topo)
    columnCount = len(topo[0])
    isVisitedMatrix = [[False for x in range(rowCount)] for x in range(columnCount)]
    return traverseCell(topo,isVisitedMatrix,x,y,0,toApplyVisits)


def traverseCell(topo,isVisitedMatrix,x,y,neededValue,toApplyVisits):

    #print("At:",x,y)

    if x < 0 or y < 0:
        return 0
    
    try:
        cell = topo[y][x]
    except:
        return 0

    if cell != neededValue:
        return 0

    wasVisited = isVisitedMatrix[y][x]

    if wasVisited:
        return 0

    if toApplyVisits:
        isVisitedMatrix[y][x] = True

    if cell == 9:
        return 1

    #Traverse neighbours
    return (traverseCell(topo,isVisitedMatrix,x+1,y,neededValue+1,toApplyVisits)
            + traverseCell(topo,isVisitedMatrix,x-1,y,neededValue+1,toApplyVisits)
            + traverseCell(topo,isVisitedMatrix,x,y+1,neededValue+1,toApplyVisits)
            + traverseCell(topo,isVisitedMatrix,x,y-1,neededValue+1,toApplyVisits)
            )
  
if __name__ == "__main__":
    main()
