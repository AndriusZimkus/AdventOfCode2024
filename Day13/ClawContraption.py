import os
def main():
    path = "../../Advent Of Code Cases/Day13/input.txt"
    with open(path, 'r') as file:

        i = 0

        machines = []
        buttons = []
        for line in file:
            if line.strip() == "":
                continue
            currentRow = line.strip().split(":")[1].strip()

            if i < 2:
                currentRow = currentRow.split(", ")
                x = int(currentRow[0].split("+")[1])
                y = int(currentRow[1].split("+")[1])

                buttons.append((x,y))

            else:
                currentRow = currentRow.split(", ")
                x = int(currentRow[0].split("=")[1])
                y = int(currentRow[1].split("=")[1])

                target = (x,y)

            if i == 2:
                i = 0
                machine = {"buttons":buttons, "target":target}
                machines.append(machine)
                buttons = []
            else:
                i+=1


    minimumPrice = 0
    for machine in machines:

        currentPrice = bestMachinePrice(machine)
        #print(currentPrice)
        minimumPrice += currentPrice

    print ("Minimum price:",minimumPrice)

    #Part 2
    newMachines = []
    for machine in machines:
        buttons = machine['buttons']
        target = machine['target']
        newTargetX = 10000000000000 + target[0]
        newTargetY = 10000000000000 + target[1]
        newMachine = {"buttons":buttons, "target":(newTargetX,newTargetY)}
        newMachines.append(newMachine)


    newMinPrice = 0

    for machine in machines:
        newMinPrice += getMachinePrice_algebra(machine)

    print ("Minimum price, part 1, newMethod:",round(newMinPrice))

    newMinPrice = 0

    for machine in newMachines:
            newMinPrice += getMachinePrice_algebra(machine)
 
    print ("Minimum price, part 2, newMethod:",round(newMinPrice))
    
def getMachinePrice_algebra(machine):
    targetX = machine['target'][0]
    targetY = machine['target'][1]
    
    B1X = machine['buttons'][0][0]
    B1Y = machine['buttons'][0][1]
    B2X = machine['buttons'][1][0]
    B2Y = machine['buttons'][1][1]
    
    B2C = (B1X*targetY-B1Y*targetX) / ((B1X*B2Y)-(B1Y*B2X))

    B1C = ((targetY*B2X)-(targetX*B2Y)) / ((B2X*B1Y)-(B2Y*B1X))

    B2CA = (B1X*targetY-B1Y*targetX) // ((B1X*B2Y)-(B1Y*B2X))
    B1CA = ((targetY*B2X)-(targetX*B2Y)) // ((B2X*B1Y)-(B2Y*B1X))
    
    if B2C < 0 or B1C < 0 or B2CA != B2C or B1CA != B1C:
        price = 0
    else:
        price = B1C*3+B2C*1

    return price


def bestMachinePrice(machine):
    return getMachinePriceHelper(machine)

def getMachinePriceHelper(machine):
    bestPrice = 0
    TX = machine['target'][0]
    TY = machine['target'][1]
    B1X = machine['buttons'][0][0]
    B1Y = machine['buttons'][0][1]
    B2X = machine['buttons'][1][0]
    B2Y = machine['buttons'][1][1]

    isAttemptedMatrix = [[False for x in range(101)] for x in range(101)]

    def GMP(machine,TX,TY,buttonToPress,currentPrice,c1,c2):
        nonlocal bestPrice
        
        if buttonToPress == 1:
            TX = TX - B1X
            TY = TY - B1Y
            currentPrice += 3
            c1+=1
        else:
            TX = TX - B2X
            TY = TY - B2Y
            currentPrice += 1
            c2+=1
        
        if isAttemptedMatrix[c1][c2]:
            return 0
        
        isAttemptedMatrix[c1][c2] = True

        if TX == 0 and TY == 0 and (currentPrice < bestPrice or bestPrice == 0):
            bestPrice = currentPrice
            #print(bestPrice)
            return 0

        if TX < 0 or TY < 0:
            return 0

        if c1 < 100:
            GMP(machine,TX,TY,1,currentPrice,c1,c2)
        if c2 < 100:
            GMP(machine,TX,TY,2,currentPrice,c1,c2)

        return 0

    GMP(machine,TX,TY,1,0,0,0)
    GMP(machine,TX,TY,2,0,0,0)

    return bestPrice        
        

if __name__ == "__main__":
    main()

