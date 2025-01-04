import time

def main():
 
    fileName = "input.txt"
    path = "../../Advent Of Code Cases/Day24/" + fileName


    wires = {}
    connections = []

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

                connections.append(Connection(first,second,result,logic))

    while len(connections) > 0:
        
        cxn = connections.pop(0)
        #print(cxn)
        cxnEvaluation = cxn.evaluate(wires)
        if not cxn.first in wires or not cxn.second in wires:
            connections.append(cxn)
            continue
            
        if cxnEvaluation == "":
            #print(cxn.first)
            #print(wires[cxn.first])
            #print(cxn)
            connections.append(cxn)
            continue
            
        if not cxn.result in wires:
            wires[cxn.result] = cxnEvaluation

        
        #print(cxn.evaluate(wires))
    #print(wires)
    zNumbers = ""
    i = 0
    while True:


        if i < 10:
            cn = "z0" + str(i)
        else:
            cn = "z" + str(i)
        #print(cn)
        try:
            currentResult = wires[cn]
            zNumbers = str(currentResult) + zNumbers

        except:
            break

        i+=1

    print(zNumbers)
    print("Part 1:", int(zNumbers,2))

            
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
