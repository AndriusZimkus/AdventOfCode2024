with open('input.txt', 'r') as file:
        text = file.read().strip()

numbers = []
for number in text:
    numbers.append(int(number))
#print (numbers)

disk = []

#Fill disk
isData = True
currentIndex = 0
for number in numbers:
    for i in range(number):
        if isData:
            disk.append(currentIndex)
        else:
            disk.append(".")

    if isData:
        currentIndex += 1
    isData = not isData

#print ("Unfragmented:",disk)

disk2 = disk.copy()

#Fragment disk
def fragmentDisk (disk):
    start = 0
    end = len(disk)-1

    while True:
        if start == end:
            break

        if disk[start] != ".":
            start+=1
            continue

        if disk[end] == ".":
            end-=1
            continue
        
        #swap
        disk[start],disk[end] = disk[end], disk[start]

fragmentDisk (disk)

def countDiskCheckSum(disk):
    checkSum = 0
    for i in range(len(disk)):
        try:
            checkSum += i*disk[i]
        except:
            pass
    return checkSum
    
print("checkSum:", countDiskCheckSum(disk))

#print(*disk2)

#Fragment disk
def fragmentDisk2 (disk):

    end = len(disk)-1
    currentID = -1
    i = end
    while currentID < 0:
        if disk[i] != ".":
            currentID = disk[i]
            break
        i-=1
    #print(currentID)
    previousStartOfID = end

    while True:
        #print("CurrentID:",currentID)
        if currentID < 0:
            break
        
        #Determine needed length
        i = previousStartOfID

        startOfID = -1
        endOfID = -1
        while i >=0:
            if disk[i] == currentID and endOfID == -1:
                endOfID = i
                startOfID = i
            elif disk[i] == currentID:
                startOfID = i
            elif startOfID != -1 and disk[i] != currentID:
                break
            i-=1

        previousStartOfID = startOfID

        #print("Start of ID",startOfID)
        #print("End of ID",endOfID)
        neededGap = endOfID - startOfID + 1
        #print("Needed gap:",neededGap)
        if startOfID == 0:
            break

        i = 0
        startOfGap = -1
        endOfGap = -1
        isGapFound = False
        #Search for gap
        while True:
            if disk[i] == "." and startOfGap == -1:
                startOfGap = i
                endOfGap = i
            elif disk[i] != "." and startOfGap != -1:
                #Reset gap
                startOfGap = -1
                endOfGap = -1
            elif disk[i] == ".":
                endOfGap = i

            if startOfGap != 1 and endOfGap != -1 and (endOfGap - startOfGap + 1 == neededGap):
                isGapFound = True
                break

            i+=1
            if i >= startOfID:
                break
            
        #print("Start of gap",startOfGap)
        #print("End of gap",endOfGap)
        #print(isGapFound)

        if isGapFound:
            #Transfer data
            for i in range(neededGap):
                #swap
                disk[startOfGap+i],disk[startOfID+i] = disk[startOfID+i], disk[startOfGap+i]

        currentID -= 1
        #print(*disk2)

fragmentDisk2(disk2)
print("checkSum:", countDiskCheckSum(disk2))
