testMatrix = []
with open('test.txt', 'r') as file:
        for line in file:
                currentRow = list(line.strip())
                testMatrix.append(currentRow)
test2Matrix = []
with open('test2.txt', 'r') as file:
        for line in file:
                currentRow = list(line.strip())
                test2Matrix.append(currentRow)

inputMatrix = []
with open('input.txt', 'r') as file:
        for line in file:
                currentRow = list(line.strip())
                inputMatrix.append(currentRow)

def getCell(matrix,y,x):
        if y < 0 or x < 0:
                return "O"
        try:
                return matrix[y][x]
        except:
                return "O"
def cellXMASCount(matrix, y, x):
        cell = matrix[y][x]
        if cell != 'X':
                return 0

        #print("Checking:",x,y)
        lettersToCheck = ['X','M','A','S']
        length = len(lettersToCheck)

        count = 0
        
        for i in range(length):
                if getCell(matrix,y,x+i) != lettersToCheck[i]:
                        break
                if i == length-1:
                        count+=1

        for i in range(length):
                if getCell(matrix,y+i,x+i) != lettersToCheck[i]:
                        break
                if i == length-1:
                        count+=1

        for i in range(length):
                if getCell(matrix,y-i,x+i) != lettersToCheck[i]:
                        break
                if i == length-1:
                        count+=1

        for i in range(length):
                if getCell(matrix,y,x-i) != lettersToCheck[i]:
                        break
                if i == length-1:
                        count+=1
                        
        for i in range(length):
                if getCell(matrix,y+i,x-i) != lettersToCheck[i]:
                        break
                if i == length-1:
                        count+=1

        for i in range(length):
                if getCell(matrix,y-i,x-i) != lettersToCheck[i]:
                        break
                if i == length-1:
                        count+=1

        for i in range(length):
                if getCell(matrix,y+i,x) != lettersToCheck[i]:
                        break
                if i == length-1:
                        count+=1

        for i in range(length):
                if getCell(matrix,y-i,x) != lettersToCheck[i]:
                        break
                if i == length-1:
                        count+=1

        horizontalRight = x <= len(matrix[y])-len(lettersToCheck)
        verticalDown = y <= len(matrix)-len(lettersToCheck)
        horizontalLeft = x >= len(lettersToCheck)-1
        verticalUp = y >= len(lettersToCheck)-1
        #print("horizontalRight:",horizontalRight)
        #print("verticalDown:",verticalDown)
        #print("horizontalLeft:",horizontalLeft)
        #print("verticalUp:",verticalUp)

        
##        if horizontalRight:
##                for i in range(length):
##                        if matrix[y][x+i] != lettersToCheck[i]:
##                                break
##                        if i == length-1:
##                                count+=1
##
##                if verticalDown:
##                        for i in range(length):
##                                if matrix[y+i][x+i] != lettersToCheck[i]:
##                                        break
##                                if i == length-1:
##                                        count+=1
##
##                if verticalUp:
##                        for i in range(length):
##                                if matrix[y-i][x+i] != lettersToCheck[i]:
##                                        break
##                        if i == length-1:
##                                count+=1
##                                
##        if horizontalLeft:
##                for i in range(length):
##                        if matrix[y][x-i] != lettersToCheck[i]:
##                                break
##                        if i == length-1:
##                                count+=1
##
##                if verticalDown:
##                        for i in range(length):
##                                if matrix[y+i][x-i] != lettersToCheck[i]:
##                                        break
##                                if i == length-1:
##                                        count+=1
##
##                if verticalUp:
##                        for i in range(length):
##                                if matrix[y-i][x-i] != lettersToCheck[i]:
##                                        break
##                        if i == length-1:
##                                count+=1     
##
##        if verticalDown:
##                for i in range(length):
##                        if matrix[y+i][x] != lettersToCheck[i]:
##                                break
##                        if i == length-1:
##                                count+=1
##                                
##        if verticalUp:
##                for i in range(length):
##                        if matrix[y-i][x] != lettersToCheck[i]:
##                                break
##                        if i == length-1:
##                                count+=1

        #print(count)
        return count

def totalCountOfMatrix(matrix):
        totalCount = 0
        for i in range(len(matrix)):
                row = matrix[i]
                for j in range(len(row)):
                        totalCount += cellXMASCount(matrix,i,j)

        return totalCount


print("Test XMAS count:", totalCountOfMatrix(testMatrix))
print("Test2 XMAS count:", totalCountOfMatrix(test2Matrix))
print("Input XMAS count:", totalCountOfMatrix(inputMatrix))

def isCellXMAS(matrix, y, x):
        cell = matrix[y][x]
        if cell != 'A':
                return False

        diagonalCount = 0

        # Left up
        if getCell(matrix,y+1,x+1) == 'M' and getCell(matrix,y-1,x-1) == 'S':
                diagonalCount +=1

        # Right down
        if getCell(matrix,y-1,x-1) == 'M' and getCell(matrix,y+1,x+1) == 'S':
                diagonalCount +=1

        # Left down
        if getCell(matrix,y-1,x+1) == 'M' and getCell(matrix,y+1,x-1) == 'S':
                diagonalCount +=1

        # Right up
        if getCell(matrix,y+1,x-1) == 'M' and getCell(matrix,y-1,x+1) == 'S':
                diagonalCount +=1

        return diagonalCount > 1
        
def totalXMASCountOfMatrix(matrix):
        totalCount = 0
        for i in range(len(matrix)):
                row = matrix[i]
                for j in range(len(row)):
                        if isCellXMAS(matrix,i,j):
                                totalCount += 1

        return totalCount


print("Test X-MAS count:", totalXMASCountOfMatrix(testMatrix))
print("Test2 X-MAS count:", totalXMASCountOfMatrix(test2Matrix))
print("Input X-MAS count:", totalXMASCountOfMatrix(inputMatrix))
