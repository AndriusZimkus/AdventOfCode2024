import numpy as np
import copy
matrix = []
with open('input.txt', 'r') as file:
        for line in file:
                currentRow = list(line.strip())
                matrix.append(currentRow)

#for row in matrix:
#        print(row)
initialMatrix = matrix.copy()

isVisitedMatrix = []
isTestedMatrix = []

#Get initial guard position
for i in range(len(matrix)):
        isVisitedMatrix.append([])
        isTestedMatrix.append([])
        for j in range(len(matrix[i])):
                cell = matrix[i][j]
                isVisitedMatrix[i].append(0)
                isTestedMatrix[i].append(False)
                if cell == "^":
                        gp = (i,j)
                        initialGP = (i,j)


print(gp)
isVisitedMatrix[gp[0]][gp[1]] = 1
isTestedMatrix[gp[0]][gp[1]] = True

currentDirection = "up"

def getNextDirection(currentDirection):
        if currentDirection == "up":
                nextDirection = "right"
        elif currentDirection == "right":
                nextDirection = "down"
        elif currentDirection == "down":
                nextDirection = "left"
        else:
                nextDirection = "up"
        return nextDirection

def getNextCell(currentDirection,gp):
        if currentDirection == "up":
                nextCell = (gp[0]-1,gp[1])
        elif currentDirection == "right":
                nextCell = (gp[0],gp[1]+1)
        elif currentDirection == "down":
                nextCell = (gp[0]+1,gp[1])
        elif currentDirection == "left":
                nextCell = (gp[0],gp[1]-1)
        return nextCell

def traverseMap (gp,currentDirection,matrix):
        visitedObstacles = {}
        while True:
                nextCell = getNextCell(currentDirection,gp)

                if (nextCell[0] == len(matrix) or nextCell[0] == -1
                or nextCell[1] == len(matrix[0]) or nextCell[1] == -1):
                        return True

                if matrix[nextCell[0]][nextCell[1]] == "#":
                        
                        if not nextCell in visitedObstacles:
                                visitedObstacles[nextCell] = [currentDirection]
                        else:
                                if currentDirection in visitedObstacles[nextCell]:
                                        #print (nextCell[0],nextCell[1])
                                        #Loop
                                        return False
                                visitedObstacles[nextCell].append(currentDirection)

                        #Change direction
                        currentDirection = getNextDirection(currentDirection)
                                
                else:
                        isVisitedMatrix[nextCell[0]][nextCell[1]] = 1
                        gp = nextCell

                #print(visitedObstacles)

print(traverseMap(gp, currentDirection, matrix))
visitedCount = 0
for row in isVisitedMatrix:
        #print(row)
        for cell in row:
                visitedCount += cell
print("Visited count:", visitedCount)

obstacleCount = 0
currentMatrix = initialMatrix.copy()
gp = copy.copy(initialGP)
currentDirection = "up"

while True:
        
        # Test all positions
        nextCell = getNextCell(currentDirection,gp)
        if (nextCell[0] == len(matrix) or nextCell[0] == -1
        or nextCell[1] == len(matrix[0]) or nextCell[1] == -1):
                        break
        #print(nextCell)
        isTested = isTestedMatrix[nextCell[0]][nextCell[1]]
        nextCellValue = currentMatrix[nextCell[0]][nextCell[1]]
        #print("isTested,nextCellValue",isTested,nextCellValue)

        if not isTested and nextCellValue == ".":
                #print("Testing:", nextCell)
                savedDirection = copy.copy(currentDirection)
                isTestedMatrix[nextCell[0]][nextCell[1]] = True
                currentMatrix[nextCell[0]][nextCell[1]] = "#"
                isTestALoop = not traverseMap (gp,currentDirection,currentMatrix)
                if isTestALoop:
                        #Stuck in loop
                        currentDirection = savedDirection
                        obstacleCount+=1
                        currentMatrix[nextCell[0]][nextCell[1]] = "."
                else:
                        currentMatrix[nextCell[0]][nextCell[1]] = "."
                        #Exited successfully
                        #Reset variables
                        currentMatrix = initialMatrix.copy()
                        gp = copy.copy(initialGP)
                        currentDirection = "up"
                        continue

        if currentMatrix[nextCell[0]][nextCell[1]] == "#":
                #Change direction
                currentDirection = getNextDirection(currentDirection)                        
        else:
                gp = nextCell
        
print("Obstacle count:", obstacleCount) 
        
