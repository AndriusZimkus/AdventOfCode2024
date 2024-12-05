import copy
neededForNumbers = {}
neededNumbers = {}
updates = []
with open('input.txt', 'r') as file:
        readRules = True
        for line in file:
                currentRow = line.strip().split("|")
                if readRules and currentRow[0]:
                        
                        value = int(currentRow[0])
                        key = int(currentRow[1])
                        if key in neededNumbers:
                                currentArrayForKey = neededNumbers[key]
                        else:
                                currentArrayForKey = []
                                
                        currentArrayForKey.append(value)
                        neededNumbers[key] = currentArrayForKey

                        if value in neededForNumbers:
                                currentArrayForValue = neededForNumbers[value]
                        else:
                                currentArrayForValue = []

                        currentArrayForValue.append(key)
                        neededForNumbers[value] = currentArrayForValue     
                        
                elif not readRules:
                        currentRow = []
                        for x in line.strip().split(","):
                                currentRow.append(int(x))
                        updates.append(currentRow)
                        #print (currentRow)
                        
                if not currentRow[0] and readRules:
                        readRules = False

def filterNeededNumbers (update,neededForNumbers,neededNumbers):
        localNeededNumbers = {}
        localNeededForNumbers = {}
        for x in update:
                if x in neededNumbers:
                        unf = neededNumbers[x]
                        fil = list(filter(lambda x : x in update, unf))
                        localNeededNumbers[x] = fil

        for y in neededForNumbers:
                if y in update:
                        unf = neededForNumbers[y]
                        fil = list(filter(lambda x : x in update, unf))
                        localNeededForNumbers[y] = fil

                
        return localNeededNumbers, localNeededForNumbers

def isUpdateInRightOrder(update,neededForNumbers,neededNumbers):

        localNeededNumbers = copy.deepcopy(neededNumbers)
        localNeededForNumbers = copy.deepcopy(neededForNumbers)

        localNeededNumbers, localNeededForNumbers = filterNeededNumbers (update,localNeededForNumbers,localNeededNumbers)
        #print(update)
        #print(localNeededNumbers)
        #print(localNeededForNumbers)
        for x in update:
                if (x in localNeededNumbers) and len(localNeededNumbers[x]) > 0:
                        return False

                if (x in localNeededForNumbers):
                        for y in localNeededForNumbers[x]:
                                currentArray = localNeededNumbers[y]
                                try:
                                        currentArray.remove(x)
                                except:
                                        a=0
                                localNeededNumbers[y] = currentArray
        return True

middleValues = 0
for update in updates:
        if isUpdateInRightOrder(update,neededForNumbers,neededNumbers):
                length = len(update)
                middleValues += update[length // 2]
        
print("Correct middle values:", middleValues)

middleValues = 0
for update in updates:
        if not isUpdateInRightOrder(update,neededForNumbers,neededNumbers):
                #print(update)

                localNeededNumbers = copy.deepcopy(neededNumbers)
                localNeededForNumbers = copy.deepcopy(neededForNumbers)

                localNeededNumbers, localNeededForNumbers = filterNeededNumbers (update,localNeededForNumbers,localNeededNumbers)
                
                #print(localNeededNumbers)
                #print(localNeededForNumbers)
                #Determine if number is ok for order
                while True:
                        pred = []
                        for i in range(len(update)):
                                current = update[i]
                                if current in localNeededNumbers:
                                        neededForThis = localNeededNumbers[current]
                                else:
                                        neededForThis = []

                                #print("current:",current)
                                #print("NFT:",neededForThis)


                                fil = list(filter(lambda x : not (x in pred), neededForThis))
                                #print("fil:",fil)
                                pred.append(current)

                                if len(fil) > 0:
                                        #If not swap with first mistake
                                        for j in range(i+1,len(update)):
                                                if update[j] in neededForThis:
                                                        #print("update j in lnn:",update[j])
                                                        break
                                        update[i],update[j] = update[j],update[i]
                                        break
                                else:
                                        b=0
                                        #print("current is ok:", current)
                                        
                        #print("update:",update)
                        #print("pred:",pred)

                        if isUpdateInRightOrder(update,localNeededForNumbers,localNeededNumbers):
                                break
                        else:
                                continue
                        
                        

                
                #Check new update if correct
                length = len(update)
                middleValues += update[length // 2]


print("Incorrect middle values:", middleValues)    
