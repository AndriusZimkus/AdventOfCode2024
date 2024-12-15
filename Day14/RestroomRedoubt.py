import time
from PIL import Image, ImageDraw
def main():
    fileName = "input.txt"
    if fileName == "test.txt":
        r,c = 7, 11
    else:
        r,c = 103, 101
            
    path = "../../Advent Of Code Cases/Day14/" + fileName

    robots = []
    with open(path, 'r') as file:

        for line in file:
            #print(line)
            row = line.split()
            positionString = row[0]
            velocityString = row[1]

            pos = positionString.split("=")[1].split(",")
            vel = velocityString.split("=")[1].split(",")
            position = int(pos[0]),int(pos[1])
            velocity = int(vel[0]),int(vel[1])
            robot = {}
            robot['p'] = position
            robot['v'] = velocity

            robots.append(robot)

    #print (robots)

    robotCounts = [[0 for x in range(c)] for x in range(r)]
    initializeMatrix(robotCounts,robots)

    stepCount = 100
    i = 0

    while True:
        performStep(robotCounts,robots)
        i+=1

        #Part 1
        if i == 100:
            quadrants = parseQuadrants(robotCounts)
            print(quadrants)
            mult = 1
            for q in quadrants:
                mult *= q
            print("Safety factor:", mult)

        print("Step count:", i)

        #Part 2
        toPrint = False
        for row in robotCounts:
            inARow = 0
            for cell in row:
                if cell != 0:
                    inARow += 1
                else:
                    inARow = 0

                if inARow > 10:
                    toPrint = True
                    break

            if toPrint:
                break

        if toPrint:             
            # initializing delims
            in_del, out_del = "", "\n"
     
            # nested join using join()
            res = out_del.join([in_del.join([(" " if ele == 0 else "X" ) for ele in sub]) for sub in robotCounts])
     
            # printing result        
            img = Image.new('RGB', (750, 1600))
            d = ImageDraw.Draw(img)
            d.text((1,1), res, fill=(255,255,255))

            img.save('text'+str(i)+'.png')

def printMatrix(robotCounts):
    for row in robotCounts:
        for r in row:
            if r != 0:
                print(r, end = "")
            else:
                print(" ", end = "")
        print("")
def initializeMatrix(robotCounts, robots):
    for robot in robots:
        PX = robot['p'][0]
        PY = robot['p'][1]
        robotCounts[PY][PX]+=1

def performStep(robotCounts,robots):
    for robot in robots:
        PX = robot['p'][0]
        PY = robot['p'][1]
        VX = robot['v'][0]
        VY = robot['v'][1]
        
        robotCounts[PY][PX]-=1

        newPX,newPY = getNextCoords(robotCounts,PX,PY,VX,VY)
        robot['p'] = (newPX,newPY)
        robotCounts[newPY][newPX]+=1
        
def getNextCoords(robotCounts,PX,PY,VX,VY):
    newPX = PX + VX
    newPY = PY + VY

    if newPX < 0:
        newPX = len(robotCounts[0]) + newPX
    elif newPX >= len(robotCounts[0]):
        newPX -= len(robotCounts[0])

    if newPY < 0:
        newPY = len(robotCounts) + newPY
    elif newPY >= len(robotCounts):
        newPY -= len(robotCounts)

    return newPX,newPY
    
def parseQuadrants(robotCounts):
    quadrants = [0,0,0,0]
    rows = len(robotCounts)
    columns = len(robotCounts[0])
    medianX = columns // 2 
    medianY = rows // 2 
    #print(medianX)
    #print(medianY)
    
    for i in range(rows):
        for j in range(columns):
            if  j < medianX and i < medianY:
                quadrants[0] += robotCounts[i][j]
            elif j > medianX and i < medianY:
                    quadrants[1] += robotCounts[i][j]
            elif j < medianX and i > medianY:
                    quadrants[2] += robotCounts[i][j]
            elif j > medianX and i > medianY:
                quadrants[3] += robotCounts[i][j]
    return quadrants
            

if __name__ == "__main__":
    main()

