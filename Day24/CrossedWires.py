import time

def main():
 
    fileName = "test.txt"
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

    for cxn in connections:
        print(cxn)
    print(wires)

            
class Connection:
    def __init__(self,first,second,result,logic):
        self.first = first
        self.second = second
        self.result = result
        self.logic = logic

    def __str__(self):
        return (self.first + " " + self.logic + " " + self.second
                + " -> " + self.result)

        
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(round(end - start,4))
