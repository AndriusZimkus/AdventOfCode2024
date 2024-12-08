matrix = []
antennas = {}
with open('input.txt', 'r') as file:
        for line in file:
                currentRow = list(line.strip())
                matrix.append(currentRow)

rowCount = len(matrix)
columnCount = len(matrix[0])
hasAntinodeMatrix = [[False for x in range(rowCount)] for x in range(columnCount)]
for i in range(len(matrix)):
        for j in range(len(matrix[i])):
                cell = matrix[i][j]
                if cell != ".":
                        if not cell in antennas:
                                antennas[cell] = [(i,j)]
                        else:
                                antennas[cell].append((i,j))
                                
#print(antennas)

def markCell(x,y,matrix):
        if x >= 0 and y >=0:
                try:
                        matrix[y][x] = True
                except:
                        pass

for antenna in antennas:
        positions = antennas[antenna]
        #print(positions)

        for i in range(len(positions)):
                currentPosition = positions[i]
                cpY = currentPosition[0]
                cpX = currentPosition[1]
                for j in range(i+1,len(positions)):
                        otherPosition = positions[j]
                        opY = otherPosition[0]
                        opX = otherPosition[1]

                        diffY = (opY - cpY)
                        diffX = (opX - cpX)

                        a1X = cpX-diffX
                        a1Y = cpY-diffY
                        a2X = opX+diffX
                        a2Y = opY+diffY

                        #print("1st antinode:",cpY-diffY,cpX-diffX)
                        #print("2st antinode:",opY+diffY,opX+diffX)

                        markCell(a1X,a1Y,hasAntinodeMatrix)
                        markCell(a2X,a2Y,hasAntinodeMatrix)

antinodeCount = 0
for row in hasAntinodeMatrix:
        for cell in row:
                if cell:
                       antinodeCount += 1 

print("Antinode count:", antinodeCount) 

#Part 2
hasAntinodeMatrix = [[False for x in range(rowCount)] for x in range(columnCount)]

for antenna in antennas:
        positions = antennas[antenna]
        #print(positions)

        for i in range(len(positions)):
                currentPosition = positions[i]
                cpY = currentPosition[0]
                cpX = currentPosition[1]
                hasAntinodeMatrix[cpY][cpX] = True
                for j in range(i+1,len(positions)):
                        otherPosition = positions[j]
                        opY = otherPosition[0]
                        opX = otherPosition[1]

                        diffY = (opY - cpY)
                        diffX = (opX - cpX)
                        a1X = cpX
                        a1Y = cpY
                        a2X = opX
                        a2Y = opY

                        while True:
                                a1X = a1X-diffX
                                a1Y = a1Y-diffY
                                a2X = a2X+diffX
                                a2Y = a2Y+diffY

                                isA1Valid = a1X >= 0 and a1X < columnCount and a1Y >=0 and a1Y < rowCount
                                isA2Valid = a2X >= 0 and a2X < columnCount and a2Y >=0 and a2Y < rowCount

                                if not isA1Valid and not isA2Valid:
                                        break

                                #print("1st antinode:",cpY-diffY,cpX-diffX)
                                #print("2st antinode:",opY+diffY,opX+diffX)
                                markCell(a1X,a1Y,hasAntinodeMatrix)
                                markCell(a2X,a2Y,hasAntinodeMatrix)

antinodeCount = 0
for row in hasAntinodeMatrix:
        #print(row)
        for cell in row:
                if cell:
                       antinodeCount += 1 

print("Updated antinode count:", antinodeCount) 
