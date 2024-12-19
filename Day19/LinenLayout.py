def main():
 
    fileName = "input.txt"
    path = "../../Advent Of Code Cases/Day19/" + fileName

    designs = []
    with open(path, 'r') as file:
        patterns = file.readline().strip().replace(" ", "").split(",")
        file.readline()
        for line in file:
            designs.append(line.strip())

    global possibleDesigns
    global designsTried
    possibleDesigns = {}
    designsTried = {}
    #designsPossible = countDesignsPossible_1_slow(patterns,designs)
    designsPossible = countDesignsPossible_1_rec(patterns,designs)
    print("Designs possible:", designsPossible)

    

def countDesignsPossible_1_rec(patterns,designs):
    global designsTried
    i = 1
    designsPossible = 0
    for design in designs:
        #print(i)
        #print(design)
        designsTried = {}
        isCurrentPossible = isDesignPossible_rec(design,patterns,[])
        #print(isCurrentPossible)
        if isCurrentPossible:
            designsPossible+=1
        i+=1
        
    return designsPossible

def isDesignPossible_rec(design,patterns,designSequence):
    global possibleDesigns
    global designsTried
    #print(designSequence)
    #print(designsTried)
    
    #print("D",design)
    designsToTry = []
    designsTried[design] = "True"
    for pattern in patterns:
        if design == pattern:
            for d in designSequence:
                possibleDesigns[d] = True
            return True
        elif design in possibleDesigns:
            return True
        elif design[:len(pattern)] == pattern:
            leftoverDesign = design[len(pattern):]
            if not leftoverDesign in designsTried:
                #print("adding",leftoverDesign)
                designsToTry.append((leftoverDesign,designSequence + [leftoverDesign]))
    #print(designsToTry)

    if len(designsToTry) == 0:
        return False
    else:
        for dtt in designsToTry:
            dtt_o = dtt[0]
            ds = dtt[1]
            inp = isDesignPossible_rec(dtt_o,patterns,ds)
            if inp:
                for d in ds:
                    possibleDesigns[d] = True
                return True

    return False
    
def countDesignsPossible_1_slow(patterns,designs):

    patternsGrouped = {}
    for pattern in patterns:
        firstLetter = pattern[:1]

        if firstLetter in patternsGrouped:
            patternsGrouped[firstLetter].append(pattern)
        else:
            patternsGrouped[firstLetter] = [pattern]
            
    designsPossible = 0
    possibleDesigns = {}
    i = 1
    for design in designs:
        print(i)
        isCurrentPossible,possibleDesigns = isDesignPossible(design,patternsGrouped,possibleDesigns)
        if isCurrentPossible:
            designsPossible+=1
        i+=1

    return designsPossible

def isDesignPossible(design,patternsGrouped,possibleDesigns):
    designsToTry = [(design,[design])]

    designsTried = {}
    isPossible = False
    while len(designsToTry) > 0:

        currentDesignObject = designsToTry.pop(0)
        currentDesign = currentDesignObject[0]
        designSequence = currentDesignObject[1]
        if currentDesign in possibleDesigns:
            for d in designSequence:
                possibleDesigns[d] = True
            return True,possibleDesigns

        designsTried[currentDesign] = "True"
        firstLetter = currentDesign[:1]
        try:

            for pattern in patternsGrouped[firstLetter]:
                if pattern == currentDesign:
                    isPossible = True
                    break

                if currentDesign[:len(pattern)] == pattern:
                    leftoverDesign = currentDesign[len(pattern):]
                    if not leftoverDesign in designsTried:
                        designsToTry.append((leftoverDesign,designSequence + [leftoverDesign]))

            if isPossible:
                for d in designSequence:
                    possibleDesigns[d] = True
                return True,possibleDesigns
        except:
            continue

    return isPossible,possibleDesigns
        
if __name__ == "__main__":
    main()
