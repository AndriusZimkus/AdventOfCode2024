import time

def main():
 
    fileName = "input.txt"
    path = "../../Advent Of Code Cases/Day24/" + fileName


    wires = {}
    connections = []
    relations = {}

    with open(path, 'r') as file:
        currentNumber = 0
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

                if first in relations:
                    relations[first].append(result)
                else:
                    relations[first] = [result]

                if second in relations:
                    relations[second].append(result)
                else:
                    relations[second] = [result]

                connections.append(Connection(first,second,result,logic))

    newWires = updateWires(wires,connections)

    zWGN = int(getWireGroupNumber(newWires,"z"),2)
    xWGN = int(getWireGroupNumber(newWires,"x"),2)
    yWGN = int(getWireGroupNumber(newWires,"y"),2)
    
    print("Part 1:", zWGN)
    #print("X", xWGN)
    #print("Y", yWGN)
    #print("Z", zWGN)
    #print("Part 2:",xWGN + yWGN == zWGN)
    
    print("Connection count", len(connections))

    
    i1 = 0
    i2 = 1
    #print(connections[i1])
    #print(connections[i2])
    connections[i1].result,connections[i2].result = connections[i2].result,connections[i1].result
    #print(connections[i1])
    #print(connections[i2])
    newWires2 = updateWires(wires,connections)
    
    zWGN = int(getWireGroupNumber(newWires2,"z"),2)
    xWGN = int(getWireGroupNumber(newWires2,"x"),2)
    yWGN = int(getWireGroupNumber(newWires2,"y"),2)
    
    print("X", xWGN)
    print("Y", yWGN)
    print("Z", zWGN)
    print("Part 2:",xWGN + yWGN == zWGN)


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
    def __init__(self,first,second,result,logic):
        self.first = first
        self.second = second
        self.result = result
        self.logic = logic

    def __str__(self):
        return (self.first + " " + self.logic + " " + self.second
                + " -> " + self.result)

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
        
        
        
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(round(end - start,4))
