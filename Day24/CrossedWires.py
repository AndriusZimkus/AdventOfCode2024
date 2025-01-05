import time

def main():
 
    fileName = "input.txt"
    path = "../../Advent Of Code Cases/Day24/" + fileName


    wires = {}
    connections = []
    relations = {}
    xConns = []
    with open(path, 'r') as file:
        cID = 0
        
        for line in file:
            line = line.strip().split(":")


            if len(line) == 2:
                wires[line[0]] = int(line[1])
            elif len(line) == 1 and line[0] != "":
                
                line = line[0]
                line = line.split("->")
                condition = line[0].split(" ")
                
                result = line[1].strip()
                first = condition[0]
                second = condition[2]
                logic = condition[1]

                if second < first:
                    first,second = second,first



                currConn = Connection(first,second,result,logic,cID)
                cID+=1
                connections.append(currConn)

                if first in relations:
                    relations[first].append(currConn)
                else:
                    relations[first] = [currConn]

                if second in relations:
                    relations[second].append(currConn)
                else:
                    relations[second] = [currConn]

                if first[0] == "x":
                    xConns.append(currConn)
                    

    
    newWires = updateWires(wires,connections)

    zWGN = int(getWireGroupNumber(newWires,"z"),2)
    xWGN = int(getWireGroupNumber(newWires,"x"),2)
    yWGN = int(getWireGroupNumber(newWires,"y"),2)
    
    print("Part 1:", zWGN)
    print("Unchanged wires, x",xWGN)
    print("Unchanged wires, y",yWGN)
    print("Unchanged wires, z",zWGN)
    print("Unchanged wires, result:", xWGN + yWGN == zWGN)

    #Finding erros in wiring by hand and looking, i.e. manually
    i1 = 7
    i2 = 154
    
    connections[i1].result,connections[i2].result \
    = connections[i2].result, connections[i1].result

    i3 = 33
    i4 = 75

    connections[i3].result,connections[i4].result \
    = connections[i4].result, connections[i3].result

    i5 = 68
    i6 = 79

    connections[i5].result,connections[i6].result \
    = connections[i6].result, connections[i5].result

    i7 = 114
    i8 = 136

    connections[i7].result,connections[i8].result \
    = connections[i8].result, connections[i7].result

    newWires = updateWires(wires,connections)

    zWGN = int(getWireGroupNumber(newWires,"z"),2)
    xWGN = int(getWireGroupNumber(newWires,"x"),2)
    yWGN = int(getWireGroupNumber(newWires,"y"),2)
    

    print("Changed wires, x",xWGN)
    print("Changed wires, y",yWGN)
    print("Changed wires, z",zWGN)
    print("Changed wires, result:", xWGN + yWGN == zWGN)
    print("Part 2:",xWGN + yWGN == zWGN)

    part2CXNS = [
        connections[i1].result,
        connections[i2].result,
        connections[i3].result,
        connections[i4].result,
        connections[i5].result,
        connections[i6].result,
        connections[i7].result,
        connections[i8].result,
        ]

    part2CXNS.sort()
    print(",".join(part2CXNS))
    
    #print(connections[i1].result)
    #print(connections[i2].result)
    #print(connections[i3].result)
    #print(connections[i4].result)
    
##    print("Connection count", len(connections))
##    xConns.sort()
##    for cxn in xConns:
##        print("------")
##        print(cxn)
##        
##        currResult = cxn.result
##        try:
##            currRelations = relations[currResult]
##            print("Related")
##            for cR in currRelations:
##                print(cR)
##        except:
##            pass



def updateWires(wires,connections):
    newCXNS = connections.copy()
    wrs = wires.copy()

    #print(wrs)

    while len(newCXNS) > 0:
        
        cxn = newCXNS.pop(0)

        cxnEvaluation = cxn.evaluate(wrs)
        if not cxn.first in wrs or not cxn.second in wrs:
            newCXNS.append(cxn)
            continue
            
        if cxnEvaluation == "":
            newCXNS.append(cxn)
            continue
            
        if not cxn.result in wrs:
            wrs[cxn.result] = cxnEvaluation

    return wrs

def getWireGroupNumber(wires,group):
    binaryNumber = ""
    
    binaryNumber = ""
    i = 0
    while True:
        if i < 10:
            cn = group + "0" + str(i)
        else:
            cn = group + str(i)

        try:
            currentResult = wires[cn]
            binaryNumber = str(currentResult) + binaryNumber

        except:
            break

        i+=1

    return binaryNumber
            
class Connection:
    def __init__(self,first,second,result,logic,cID):
        self.first = first
        self.second = second
        self.result = result
        self.logic = logic
        self.cID = cID

    def __str__(self):
        return (self.first + " " + self.logic + " " + self.second
                + " -> " + self.result + " " + str(self.cID))

    def evaluate(self,wires):

        if not self.first in wires or not self.second in wires:
            return ""

        
        if self.logic == "AND":
            if wires[self.first] == 1 and wires[self.second] == 1:
                return 1
            else:
                return 0
        elif self.logic == "OR":
            if wires[self.first] == 1 or wires[self.second] == 1:
                return 1
            else:
                return 0
        elif self.logic == "XOR":
            if wires[self.first] != wires[self.second]:
                return 1
            else:
                return 0
        else:
            assert False

    def __lt__(self, other):
         return (self.first < other.first
                 or (self.first == other.first and
                     self.logic > other.logic)
                     
                 )
        
        
        
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(round(end - start,4))
