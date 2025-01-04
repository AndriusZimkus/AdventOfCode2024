import time

def main():
 
    fileName = "input.txt"
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
                currentSet = ",".join(currentSet)
                #currentSet = (currentSet[0],currentSet[1],currentSet[2])

                sets.add(currentSet)


    setCount = 0
    for itSet in sets:
        currentSet = itSet.split(",")
        if (currentSet[0][0] == "t"
            or currentSet[1][0] == "t"
            or currentSet[2][0] == "t"):
            setCount += 1
            
    print("Total set count", len(sets))
    print("Part 1 set count:",setCount)

    #print(sets)


    quadruplets = set()
    nextSets = {"A"}
    while len(nextSets) > 0:
        nextSets = getNextSets(connections,sets)
        #print(nextSets)

        if len(nextSets) == 0:
            break
        else:
            sets = nextSets

    for currentSet in sets:
        print("Part 2 password:",currentSet)


def getNextSets(connections,sets):
    currentLength = 0
    nextSets = set()
    for itSet in sets:
        currentSet = itSet.split(",")
        if currentLength == 0:
            currentLength = len(currentSet)
        #print(currentLength)
        currents = []
        conns = []

        for i in range(currentLength):
            current = currentSet[i]
            currents.append(current)
            conns.append(connections[current])

        #Get total intersection
        intersection = []
        for i in range(currentLength):
            try:
                if len(intersection) == 0:
                    intersection = conns[i] & conns[i+1]
                else:
                    intersection = intersection & conns[i]
            except:
                pass

        for intsec in intersection:
            currentExpanded = currents + [intsec]
            currentExpanded.sort()
            nextSets.add(",".join(currentExpanded))

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
