def main():
 
    fileName = "test.txt"
    path = "../../Advent Of Code Cases/Day19/" + fileName

    designs = []
    with open(path, 'r') as file:
        patterns = file.readline().strip().replace(" ", "").split(",")
        file.readline()
        for line in file:
            designs.append(line.strip())

    #print(patterns)
    #print(designs)
    print(len(patterns))
    print(len(designs))

    patternsGrouped = {}
    for pattern in patterns:
        firstLetter = pattern[:1]
        #print(pattern)
        #print(firstLetter)
        if firstLetter in patternsGrouped:
            patternsGrouped[firstLetter].append(pattern)
        else:
            patternsGrouped[firstLetter] = [pattern]

    designsPossible = 0
    possibleDesigns = {}
    i = 1
    for design in designs:
        #print(i)
        isCurrentPossible,possibleDesigns,ways = isDesignPossible(design,patternsGrouped,possibleDesigns)
        if isCurrentPossible:
            designsPossible+=1
            print(ways)
            #print(designsPossible)
        i+=1


    print("Designs possible:", designsPossible)

def isDesignPossible(design,patternsGrouped,possibleDesigns):
    designsToTry = [(design,[design])]
    #print("Design",design)
    ways = {}
    designsTried = {}
    while len(designsToTry) > 0:
        isPossible = False

        currentDesignObject = designsToTry.pop(0)
        currentDesign = currentDesignObject[0]
        designSequence = currentDesignObject[1]
        if currentDesign in possibleDesigns:
            for d in designSequence:
                possibleDesigns[d] = True
                #return True,possibleDesigns
        #print("Current design",currentDesign)

        designsTried[currentDesign] = "True"
        firstLetter = currentDesign[:1]
        try:

            for pattern in patternsGrouped[firstLetter]:
                #print("Pattern",pattern)
                if pattern == currentDesign:
                    isPossible = True
                    break
                #print("DLen",currentDesign[:len(pattern)])


                if currentDesign[:len(pattern)] == pattern:
                    leftoverDesign = currentDesign[len(pattern):]
                    #print("DLEFT",leftoverDesign)
                    if not leftoverDesign in designsTried:
                        designsToTry.append((leftoverDesign,designSequence + [leftoverDesign]))
                    #print("DTT",designsToTry)

            if isPossible:
                for d in designSequence:
                    possibleDesigns[d] = True
                ways.append(designSequence)
                #return True,possibleDesigns
        except:
            continue


    return isPossible,possibleDesigns,ways
        
if __name__ == "__main__":
    main()
