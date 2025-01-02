import time

def main():
 
    fileName = "test.txt"
    path = "../../Advent Of Code Cases/Day23/" + fileName

    sets = set()
    connections = {}

    with open(path, 'r') as file:
        currentNumber = 0
        for line in file:
            line = line.strip()
            first = line.split("-")[0]
            second = line.split("-")[1]

            if first>second:
                first,second = second,first

            connections = addToConnections(connections,first,second)
            connections = addToConnections(connections,second,first)
            intersection = connections[first] & connections[second]
            
            for intsec in intersection:

                currentSet = [first,second,intsec]

                currentSet.sort()
                currentSet = (currentSet[0],currentSet[1],currentSet[2])

                sets.add(currentSet)


    setCount = 0
    for currentSet in sets:
        if (currentSet[0][0] == "t"
            or currentSet[1][0] == "t"
            or currentSet[2][0] == "t"):
            setCount += 1
            
    print("Total set count", len(sets))
    print("Part 1 set count:",setCount)

    print(sets)

    quadruplets = set()
    nextSets = {"A"}
    while len(nextSets) > 0:
        nextSets = getNextSets(connections,sets)

        if len(nextSets) == 0:
            break
        else:
            sets = nextSets

    print(sets)

def getNextSets(connections,sets):    
    for currentSet in sets:
        first = currentSet[0]
        second = currentSet[1]
        third = currentSet[2]
        firstCon = connections[first]
        secondCon = connections[second]
        thirdCon = connections[third]

        intersection = firstCon & secondCon & thirdCon

        for intsec in intersection:
            #print(intsec)
            
            
    return nextSets


def addToConnections(connections,first,second):
    if first in connections:
        connections[first].add(second)
    else:
        connections[first] = {second}
    return connections

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(round(end - start,4))
